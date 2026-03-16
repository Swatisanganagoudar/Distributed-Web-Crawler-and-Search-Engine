import os
import json
import math
import re
from bs4 import BeautifulSoup
from collections import defaultdict, Counter

PAGES_FOLDER = "pages"

documents = {}

# ---------------------------
# Load HTML Files
# ---------------------------
for file in os.listdir(PAGES_FOLDER):
    if file.endswith(".html"):
        path = os.path.join(PAGES_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            documents[file] = f.read()

total_docs = len(documents)

print("Documents Loaded:", total_docs)


# ---------------------------
# Extract Text
# ---------------------------
def extract_text(html):

    soup = BeautifulSoup(html, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    return text


# ---------------------------
# Tokenization
# ---------------------------
def tokenize(text):

    text = text.lower()

    text = re.sub(r'[^a-z0-9\s]', '', text)

    tokens = text.split()

    return tokens


# ---------------------------
# Build Inverted Index
# ---------------------------
inverted_index = defaultdict(list)

for doc_id, html in documents.items():

    text = extract_text(html)

    tokens = tokenize(text)

    tf = Counter(tokens)

    for word, freq in tf.items():
        inverted_index[word].append((doc_id, freq))


# ---------------------------
# Save Inverted Index
# ---------------------------
with open("inverted_index.json", "w") as f:
    json.dump(inverted_index, f, indent=4)

print("Inverted Index Saved")


# ---------------------------
# Compute IDF
# ---------------------------
idf = {}

for word, postings in inverted_index.items():

    docs_with_word = len(postings)

    idf[word] = math.log(total_docs / docs_with_word)


# ---------------------------
# Save IDF
# ---------------------------
with open("idf.json", "w") as f:
    json.dump(idf, f, indent=4)

print("IDF Saved")


print("Unique Words:", len(inverted_index))

print("\nSample Index Entries:")

for word in list(inverted_index.keys())[:5]:
    print(word, "->", inverted_index[word])