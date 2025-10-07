# Semantic Search Engine with LangChain

A semantic search engine built using LangChain that enables intelligent document retrieval from PDF files using vector embeddings and similarity search.

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment & Extension](#deployment--extension)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

This Jupyter Notebook implements a semantic search engine that processes PDF documents, converts text into vector embeddings, and enables intelligent query-based retrieval. The system uses LangChain's document processing pipeline combined with Hugging Face embeddings and Chroma vector storage to provide contextually relevant search results.

## Motivation

Traditional keyword-based search engines often fail to capture the semantic meaning behind user queries. This project addresses that limitation by:
- Enabling semantic understanding of document content
- Providing more accurate and contextually relevant search results
- Demonstrating practical applications of retrieval-augmented generation (RAG) systems
- Serving as a foundation for building intelligent document management systems

## Features

- **PDF Document Processing**: Load and process multi-page PDF documents
- **Intelligent Text Splitting**: Recursive text splitting with overlap for optimal chunking
- **Semantic Embeddings**: Uses state-of-the-art sentence transformers for text representation
- **Vector Storage**: ChromaDB integration for efficient similarity search
- **Multiple Search Methods**: 
  - Similarity search
  - Maximum marginal relevance (MMR)
  - Score-threshold filtering
- **Async Support**: Asynchronous query processing capabilities
- **Metadata Preservation**: Maintains document source and positional information

## Dataset

The project uses Nike's 2023 Form 10-K filing as a sample dataset:

- **Source**: Nike 2023 Annual Report (Form 10-K)
- **Description**: 106-page PDF containing financial reports, business operations, and corporate information
- **Usage**: Demonstrates the search engine's capability to retrieve specific information from complex corporate documents
- **Format**: PDF with structured financial data and textual content

## Installation

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Git

### Required Libraries

Install the necessary dependencies:

```bash
pip install langchain-community pypdf
pip install langchain-huggingface
pip install sentence-transformers
pip install langchain-chroma
```

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/semantic-search-engine.git
cd semantic-search-engine
```

2. Set up LangSmith for tracing (optional but recommended):
```python
import getpass
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

## Usage

1. **Load Documents**: Use PyPDFLoader to process PDF files
2. **Split Text**: Configure chunk size and overlap for optimal processing
3. **Generate Embeddings**: Use Hugging Face sentence transformers
4. **Create Vector Store**: Initialize ChromaDB with document embeddings
5. **Query the System**: Ask natural language questions and get relevant document excerpts

Example queries:
- "How many distribution centers does Nike have in the US?"
- "What was Nike's revenue in 2023?"
- "When was Nike incorporated?"

## Deployment & Extension

This notebook can be extended into a full application by:

### Web Application
- Convert to Flask/FastAPI backend
- Add React/Vue.js frontend
- Implement user authentication
- Add document upload functionality

### Enhanced Features
- Multi-document support
- User query history
- Search result ranking improvements
- Integration with cloud storage (AWS S3, Google Drive)
- Real-time collaborative filtering

### Production Considerations
- Scale vector database (Pinecone, Weaviate)
- Implement caching mechanisms
- Add monitoring and logging
- Containerize with Docker

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Set up development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **LangChain**: For providing the core framework and abstractions
- **Hugging Face**: For the sentence-transformers and embedding models
- **ChromaDB**: For the efficient vector storage solution
- **Nike Inc.**: For the sample dataset (2023 Form 10-K)
- **Sentence Transformers**: All-mpnet-base-v2 model for embeddings

### References
- [LangChain Documentation](https://python.langchain.com/)
- [Hugging Face Transformers](https://huggingface.co/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers Paper](https://arxiv.org/abs/1908.10084)

---

**Note**: This project is for educational and demonstration purposes. Always ensure compliance with data usage rights and licensing when working with external documents.