import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
DOCS_PATH = os.getenv("DOCS_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")