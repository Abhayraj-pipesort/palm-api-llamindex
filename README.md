# palm-api-llamindex
This project demonstrates how to customize llm and embeddings in Llamaindex

## Project Overview
his is a simple Python application that allows you to add a document and ask questions about its content. The application utilizes Google's PaLM API for question answering and embedding.

## Getting Started

Before running the application, make sure you have the necessary dependencies installed and set up your environment.

### Prerequisites

You'll need the following Python libraries installed:

- `dotenv`: For loading environment variables.
- `google-generativeai`: The Google API for using llm.
- `llama_index`: LlamaIndex is a data framework for LLM applications to ingest, structure, and access data.

You can install these libraries using `pip`:

```bash
pip install python-dotenv google-generativeai llama_index
```

## Project Structure
The project consists of a single Python script (`app.py`) that performs the following tasks:

1. Imports necessary libraries and modules.
2. Loads environment variables using `dotenv` for configuration.
3. Sets up the PaLM model and Google PALM embeddings.
4. Reads a collection of text documents from a specified directory.
5. Creates a text vector index using the `llama_index` library and the loaded documents.
6. Performs a sample query using the index and prints the response.

## Usage
To use this project, follow these steps:

1. Make sure you have the required dependencies and the Google PALM API key.

2. Place your text documents in a directory (default: "data") where the project can access them.

3. Create a `.env` file in the project directory and set the `PALM_API_KEY` environment variable to your Google PALM API key.

4. Execute the `main.py` script:

   ```bash
   python app.py
   ```
   
   This will run a sample query on the indexed documents and print the response.

## Note

This is a example of customizing llm and embedding model in llama-index. it can also be extended and customized further according to your needs.
