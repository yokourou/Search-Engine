
# Woogle: Mini wiki search engine

## Project overview

Woogle is a basic search engine designed to mine and rank Wikipedia documents based on user queries. It involves crawling Wikipedia data, processing and parsing the content, and ranking the documents using standard Information Retrieval techniques, such as PageRank and vector space models. The project aims to provide hands-on experience in building a search engine, while implementing essential algorithms and techniques in the field of Information Retrieval.
[['webcrawler.png']]

## Installation

To set up the project, clone the Git repository:

```bash
git clone https://gitlab.ensimag.fr/galiezc/wikisearchengineproject.git
```

Once you have cloned the repository, navigate to the project directory and make sure the dependencies are installed. You may need to install the following Python modules:

```bash
pip3 install --user numpy httplib2
```

## Files and directories

The project directory contains several files and subdirectories, each serving a specific purpose:

- **capture/**: Contains logs and other output generated during crawling.
- **crawl.py**: Script that collects Wikipedia pages from a given category.
- **dw.sh**: Bash script used to download pages listed in `wiki.lst`.
- **dws/**: Directory where downloaded Wikipedia pages are stored.
- **search.py**: Main script for querying the Wikipedia dataset and ranking pages.
- **parsexml.py**: Python script that parses downloaded Wikipedia XML data and creates document-term matrices.
- **pageRank.py**: Script implementing the PageRank algorithm for ranking the Wikipedia pages.
- **wiki.lst**: List of pages to be downloaded from Wikipedia.
- **tfidf.dict, links.dict, tokInfo.dict, pageRank.dict**: Files storing pre-processed data related to term frequency, document links, and PageRank.
- **tpWikiSearchEngine.pdf**: PDF document providing project details and instructions.

## Project objective

The goal of this project is to build a basic search engine that mines and ranks Wikipedia documents based on their relevance to user queries. The main objectives are:

1. **Crawling Wikipedia Data**: Use the Wikipedia API to collect pages from a specified category.
2. **Parsing and Processing**: Parse raw data, clean it, and create a term-document matrix for text analysis.
3. **Ranking Pages**: Implement algorithms like PageRank and the vector space model to rank Wikipedia pages based on query relevance.
4. **Search Interface**: Develop a search function that allows users to query the dataset and return ranked results.

## How to run

Follow these steps to run the project:

1. Clone the repository and install the required dependencies.
2. Use the provided scripts to crawl Wikipedia data:
   - Run `python3 crawl.py` to collect the list of pages.
   - Execute the `dw.sh` script to download the data in batches.
3. Parse the downloaded data with `python3 parsexml.py`.
4. Run the search engine with `python3 search.py` to test queries.
