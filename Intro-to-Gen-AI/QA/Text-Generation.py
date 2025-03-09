#use case 1
#Text Generation
from transformers import pipeline


#Why to use pipeline
generator = pipeline("text-generation",model="gpt-3.5-turbo")

topic = "Future of AI in Telecommunication"

prompt = f"Write an engaging blog introduction about {topic}"

result = generator(prompt, max_length=250, temperature=0.9)#temperature is used for randomness


#max_new_token 

#top_k - limits the token selection - higher probability , lower probability 
#by default its 0
#top_0
#repetition_penalty 
print(result[0]['generated_text'])