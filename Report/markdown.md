### First attempt

### _Info_:

- Used supreme court judgements from 1975 year.
- For initial testing around 80 pdfs loaded and it generated around 920 documents

### Tools
- **AI model:** Groq provider (qwen 32b)
- **Embed model:** Hugging face (sentence-transformers/all-MiniLM-L6-v2)
- **Data Extraction tool:** Pymupdf
- **Dataset**: Kaggle (Supreme court judgements)
- **vectorDb:** ChromaDb
### Time taken

- **Loading PDF**: 1s (faster than normal pdf loading)
- **Indexing and embedding:** 17m 5s
- **Index querying:** 2s thinking and answering 
