from requests import get

sentences = ""
while not sentences.isdigit():
    sentences = input("Number of sentences: ")
url = 'https://baconipsum.com/api/?type=all-meat&sentences=' + sentences
response = get(url)
paragraphs = response.json()
paragraph = paragraphs[0]
print(paragraph)
