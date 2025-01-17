***Mini Wiki Search Engine***

**Overview**

Woogle is a mini search engine developed as part of a hands-on session for the Information Retrieval lecture. This project aims to implement a search engine using standard Information Retrieval techniques on a dataset mined from Wikimedia sources. The following README provides detailed instructions to set up, run, and explore the functionalities of Woogle.

1. Setting Up Your Environment

Prerequisites

Before starting, ensure the following dependencies are installed:

Python 3.x

Required Python modules: httplib2, numpy

Installation Steps

Clone the Git repository:

git clone https://gitlab.ensimag.fr/galiezc/wikisearchengineproject.git

Install the required Python modules:

pip3 install --user numpy httplib2

2. Crawling the Data

The script crawl.py is used to query the Wikipedia API to retrieve pages under a specified category.

Usage

Run the script with:

python3 crawl.py

This will generate a file wiki.lst containing a list of pages.

Notes

The script uses the categorymembers action of the Wikipedia API.

To adjust the depth of subcategories, modify the crawlingDepth parameter in the script.

3. Downloading the Data

The script dw.sh downloads Wikipedia pages listed in wiki.lst in batches to avoid API rate limits.

Usage

bash dw.sh wiki.lst

Notes

Pages are downloaded in batches of a fixed size (as specified in dw.sh).

The downloaded pages are stored in the dws folder.

The pages are encoded in JSON format.

4. Parsing the Data

The script parsexml.py processes the downloaded Wikipedia pages to create two matrices:

A doc-token matrix for term-document relationships.

A jump matrix for the random surfer model.

Tasks to Complete

Implement a regular expression to extract links and remove noisy data (e.g., external links, info boxes).

Transpose the doc-token matrix to create a token-doc index for optimized searches.

Questions to Explore

How are the matrices encoded?

Measure the performance improvements of a direct token-doc index.

5. PageRank Computation

The script pageRank.py implements the PageRank algorithm to rank documents based on the random surfer model.

Usage

Run the script in interactive mode:

python3 -i pageRank.py

Tasks to Complete

Implement the random surfer probability.

Calculate the convergence factor (δ).

Analyze convergence behavior and rank key pages such as “DNA”.

6. Search Engine Implementation

The script search.py implements a search engine using a vector space model.

Usage

Run the script in interactive mode:

python3 -i search.py

Example Query

Retrieve the top 15 results for the query:

search("evolution of bacteria", top_n=15)

Improvements to Implement

Address the “classical cheating” issue where overly generic terms dominate results.

Experiment with ranking by PageRank and combining content scores with rankings.

7. Extras and Advanced Features

Stemming

Implement simple grammar rules for stemming (e.g., “bacteria” vs “bacterial”).

Latent Semantics

Use scipy's sparse SVD to implement latent semantic analysis.

Embeddings

Replace TF-IDF embeddings with pre-trained models (e.g., word2vec, fasttext).

Custom Scoring

Detect and emphasize key parts of documents (titles, bold text).

Combine content scores with ranking algorithms.

Project Files

crawl.py: Crawls Wikipedia categories and generates a list of pages.

dw.sh: Downloads pages from Wikipedia.

parsexml.py: Parses downloaded pages and creates data structures for indexing.

pageRank.py: Computes PageRank for the documents.

search.py: Implements the search engine.

wiki.lst: List of Wikipedia pages to process.

Running the Project

Set up the environment and install dependencies.

Crawl and download Wikipedia data using crawl.py and dw.sh.

Parse the data with parsexml.py.

Compute PageRank scores with pageRank.py.

Run the search engine using search.py.

For any issues, consult the documentation in the respective scripts or reach out to the course instructor.
