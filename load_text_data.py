import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core import SimpleDirectoryReader
from ecommerce_prompts import QUERY_TEMPLATE
from llama_index.core.memory import ChatMemoryBuffer

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(
            data,
            show_progress=True,
        )
        
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

# Load text files from assessment_data folder
data_path = os.path.join("assessment_data")
text_documents = SimpleDirectoryReader(data_path).load_data()

# Create index for text documents
text_index = get_index(text_documents, "text_data")
# Create query engine with chat history support
text_engine = text_index.as_query_engine(
    text_qa_template=QUERY_TEMPLATE,
    similarity_top_k=3,
    streaming=True,  # Enable streaming for better chat experience
    memory=ChatMemoryBuffer.from_defaults(token_limit=2500)  # Add memory to query engine
)
