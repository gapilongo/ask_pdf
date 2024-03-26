# Talk to PDF using langchain

This project utilizes various libraries and tools to process, analyze, and extract information from the "Agile Practice Guide" PDF document. Here's how the process flows:

## Requirements

- `PyPDF2`: For reading PDF files.
- `langchain_openai`: For OpenAI embeddings and API interactions.
- `langchain.text_splitter`: To split text into manageable chunks.
- `langchain_community.vectorstores`: Utilizes FAISS for creating a vector store.
- `langchain.chains.question_answering`: For loading and utilizing the question-answering model.
- `os`: To access environment variables.

## Setup

1. Ensure you have an OpenAI API key set in your environment variables as `OPENAI_API_KEY`.
2. Install the required Python packages mentioned in the Requirements section.

## Workflow

1. **PDF Reading**: Use `PdfReader` from `PyPDF2` to open and read the PDF file.
2. **Text Extraction**: Loop through each page of the PDF, extracting text and appending it to a raw text variable.
3. **Text Splitting**: Utilize `CharacterTextSplitter` to split the raw text into smaller, manageable chunks.
4. **Embedding Initialization**: Initialize `OpenAIEmbeddings` for later processing.
5. **Vector Store Creation**: Create a FAISS vector store from the text chunks using the embeddings model.
6. **Question-Answering Model Loading**: Load a question-answering model chain from `langchain`.
7. **Query Processing**: Perform a similarity search in the document using a predefined query and then invoke the question-answering model with the relevant documents and query to get the answer.

## How to Use

- Run the provided Python script to process the 'agile-practice-guide-english.pdf'.
- The script will automatically handle text extraction, chunking, and querying based on the query provided.
- Results from the question-answering model will be displayed in the console.

## Note

Replace `'yourpdf.pdf'` with the path to your target PDF file and `query` with the specific question you want to ask about the document content.
