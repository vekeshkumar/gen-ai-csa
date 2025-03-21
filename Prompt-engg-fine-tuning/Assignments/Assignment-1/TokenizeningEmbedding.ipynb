import nltk
from nltk.tokenize import word_tokenize
from transformers import BertTokenizer, BertModel
import torch
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Download necessary NLTK data
nltk.download('punkt')

#Text from How to not stop worry and start living
text = """
When I was a little boy, I was playing with some of my friends in the attic of an old,
abandoned log house in north-west Missouri. As I climbed down out of the attic, I rested
my feet on a window-sill for a moment-and then jumped. I had a ring on my left
forefinger; and as I jumped, the ring caught on a nailhead and tore off my finger.
I screamed. I was terrified. I was positive I was going to die. But after the hand healed, I
never worried about it for one split second. What would have been the use? ... I
accepted the inevitable.
Now I often go for a month at a time without even thinking about the fact that I have only
three fingers and a thumb on my left hand.
A few years ago, I met a man who was running a freight elevator in one of the downtown
office buildings in New York. I noticed that his left hand had been cut off at the wrist. I
asked him if the loss of that hand bothered him. He said: "Oh, no, I hardly ever think
about it. I am not married; and the only time I ever think about it is when I try to thread a
needle."
It is astonishing how quickly we can accept almost any situation-if we have to-and adjust
ourselves to it and forget about it.
I often think of an inscription on the ruins of a fifteenth-century cathedral in Amsterdam,
Holland. This inscription says in Flemish: "It is so. It cannot be otherwise."
As you and I march across the decades of time, we are going to meet a lot of
unpleasant situations that are so. They cannot be otherwise. We have our choice. We
can either accept them as inevitable and adjust ourselves to them, or we can ruin our
lives with rebellion and maybe end up with a nervous breakdown.
Here is a bit of sage advice from one of my favourite philosophers, William James. "Be
willing to have it so," he said. "Acceptance of what has happened is the first step to
overcoming the consequence of any misfortune." Elizabeth Connley, of 2840 NE 49th
Avenue, Portland, Oregon, had to find that out the hard way. Here is a letter that she
wrote me recently: "On the very day that America was celebrating the victory of our
armed forces in North Africa," the letter says, "I received a telegram from the War
Department: my nephew- the person I loved most-was missing in action. A short time
later, another telegram arrived saying he was dead. """

# Tokenization
tokens = word_tokenize(text)
print(f"Number of tokens: {len(tokens)}")

# Check for subword splits
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
subwords = tokenizer.tokenize(text)
split_words = [word for word in subwords if word.startswith('##')]
print(f"Words split into subwords: {split_words}")

# Extract embeddings
model = BertModel.from_pretrained('bert-base-uncased')
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
embeddings = outputs.last_hidden_state.squeeze().numpy()

# Reduce dimensionality with t-SNE
tsne = TSNE(n_components=2, random_state=42)
reduced_embeddings = tsne.fit_transform(embeddings)

# Plot embeddings
plt.figure(figsize=(10, 8))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
for i, token in enumerate(subwords):
    plt.annotate(token, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]))
plt.title("Token Embeddings Visualization")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.show()
