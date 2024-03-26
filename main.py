# Importing necessary libraries and modules
from PyPDF2 import PdfReader  # For reading PDF files
from langchain_openai import OpenAIEmbeddings, OpenAI  # For working with OpenAI embeddings and API
from langchain.text_splitter import CharacterTextSplitter  # For splitting text into manageable chunks
from langchain_community.vectorstores import FAISS  # For creating a vector store using FAISS
from langchain.chains.question_answering import load_qa_chain  # For loading a question-answering model
import os  # For accessing environment variables

# Retrieving the OpenAI API key from the environment variables
open_key = os.environ["OPENAI_API_KEY"]

# Opening the PDF file to be processed
pdf_file = PdfReader('your.pdf')

# Initializing a variable to store the extracted text
raw_text = ''

# Looping through each page in the PDF to extract text
for i, page in enumerate(pdf_file.pages):
    content = page.extract_text()  # Extracting text from the current page
    if content:
        raw_text += content  # Appending the extracted text to the raw_text variable

# Setting up a text splitter to break the raw text into smaller chunks
text_splitter = CharacterTextSplitter(
    separator='\n',  # Using newline character as separator between chunks
    chunk_size=800,  # Maximum number of characters in a chunk
    chunk_overlap=200,  # Number of characters to overlap between chunks
    length_function=len  # Function to calculate the length of text
)

# Splitting the raw text into manageable chunks
texts = text_splitter.split_text(raw_text)

# Initializing the embeddings model using OpenAI
embeddings = OpenAIEmbeddings()

# Creating a FAISS vector store from the text chunks using the embeddings
document_search = FAISS.from_texts(texts, embeddings)

# Loading a question-answering model chain with OpenAI
chain = load_qa_chain(OpenAI(), chain_type='stuff')

# Defining the query for the question-answering model
query = 'What is the agile method'

# Performing a similarity search in the document using the query
docs = document_search.similarity_search(query)

# Invoking the question-answering chain with the relevant documents and query
# then printing the answer
print(chain.invoke(input={'input_documents': docs, 'question': query})['output_text'])
