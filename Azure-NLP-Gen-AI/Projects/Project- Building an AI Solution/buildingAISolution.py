import os
import asyncio
from azure.ai.studio import AIClient
from azure.ai.studio.models import DeploymentConfiguration, ModelConfiguration
from azure.identity import DefaultAzureCredential

# Azure AI Studio configuration
AZURE_AI_STUDIO_ENDPOINT = "https://your-azure-ai-studio-endpoint.com"
DEPLOYMENT_NAME = "customer-service-chatbot"
MODEL_NAME = "llama-2-70b-chat"

# Initialize Azure AI Studio client
credential = DefaultAzureCredential()
ai_client = AIClient(endpoint=AZURE_AI_STUDIO_ENDPOINT, credential=credential)

async def deploy_model():
    """Deploy the Llama-2-70b-chat model."""
    model_config = ModelConfiguration(name=MODEL_NAME)
    deployment_config = DeploymentConfiguration(
        name=DEPLOYMENT_NAME,
        model=model_config,
        sku="Standard_NC24s_v3",  # Adjust based on your requirements
        scale_settings={"scale_type": "Standard"}
    )
    
    deployment = await ai_client.deployments.begin_create_or_update(deployment_config)
    return deployment

async def generate_response(prompt):
    """Generate a response using the deployed model."""
    deployment = await ai_client.deployments.get(DEPLOYMENT_NAME)
    response = await deployment.generate(prompt=prompt)
    return response.choices[0].text

async def chat_loop():
    """Main chat loop for the customer service chatbot."""
    print("Customer Service Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Customer Service Chatbot: Thank you for using our service. Goodbye!")
            break
        
        prompt = f"Customer: {user_input}\nChatbot:"
        response = await generate_response(prompt)
        print(f"Customer Service Chatbot: {response.strip()}")

async def main():
    """Main function to set up and run the chatbot."""
    try:
        # Deploy the model (uncomment if needed)
        # await deploy_model()
        
        # Run the chat loop
        await chat_loop()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
