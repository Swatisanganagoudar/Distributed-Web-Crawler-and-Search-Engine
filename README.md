

Mini Search Engine using Python, FastAPI and TF-IDF

Project Overview

This project implements a simple Search Engine using Python. The system crawls web pages, processes text data, builds an inverted index, and allows users to search documents using a TF-IDF ranking algorithm. The project is divided into multiple milestones, each focusing on an important part of a search engine pipeline.

Technologies Used

Python
FastAPI
HTML (Simple UI)
JSON for data storage
TF-IDF ranking algorithm
Project Structure

mini-search-engine/ │ ├── docs/ │ ├── doc1.txt │ ├── doc2.txt │ ├── doc3.txt │ ├── doc4.txt │ └── doc5.txt │ ├── indexer.py ├── main.py ├── index.html ├── inverted_index.json └── idf.json

Milestone 1 – Web Crawling

Crawled sample web pages from a demo website.
Saved the HTML content of pages locally.
Milestone 2 – Data Processing

Extracted visible text from HTML pages.
Removed unnecessary tags and scripts.
Converted the content into clean text documents.
Milestone 3 – Indexing

Tokenized text into words.
Computed Term Frequency (TF) for each word.
Built an Inverted Index mapping words to documents.
Calculated Inverse Document Frequency (IDF).
Stored the index and IDF values in JSON files.
Milestone 4 – Search Engine Implementation

Implemented query processing and tokenization.
Used the inverted index to retrieve relevant documents.
Applied TF-IDF ranking to score documents.
Built a FastAPI backend to handle search queries.
Developed a simple HTML interface to allow users to search.
How to Run the Project

Install dependencies
pip install fastapi uvicorn

Start the server
python -m uvicorn main:app --reload

Open the API documentation
http://127.0.0.1:8000/docs

Open the search interface
index.html

Example Search

Users can search queries like:

life
history
science
The system retrieves documents and ranks them based on TF-IDF relevance scores.

Learning Outcome

This project demonstrates the fundamental components of a search engine including:

Web crawling
Text processing
Inverted index creation
TF-IDF ranking
API-based search system
Simple user interface for querying
Author

Student Project – Information Retrieval / Search Engine Implementation