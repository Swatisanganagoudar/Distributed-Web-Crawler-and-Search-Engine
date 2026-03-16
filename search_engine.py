import json
import math
import re
from fastapi import FastAPI

app = FastAPI()

# ----------------------
# Load Index Files
# ----------------------

with open("inverted_index.json") as f:
    inverted_index = json.load(f)

with open("idf.json") as f:
    idf = json.load(f)

print("Index Loaded")


# ----------------------
# Tokenize Query
# ----------------------

def tokenize(text):

    text = text.lower()

    text = re.sub(r'[^a-z0-9\s]', '', text)

    tokens = text.split()

    return tokens


# ----------------------
# Search Function
# ----------------------

def search(query):

    tokens = tokenize(query)

    scores = {}

    for word in tokens:

        if word in inverted_index:

            postings = inverted_index[word]

            for doc, tf in postings:

                score = tf * idf[word]

                if doc not in scores:
                    scores[doc] = 0

                scores[doc] += score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:10]


# ----------------------
# API Endpoint
# ----------------------
@app.get("/")
def home():
    return {"message": "WebScour Search Engine Running"}

@app.get("/search")

def search_api(q: str):

    results = search(q)

    output = []

    for doc, score in results:


        output.append({
            "document": doc,
            "score": score
        })

    return output