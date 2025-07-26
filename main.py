import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

# Load the files
qna_df = pd.read_excel('D:/RAG-LLM/Pre-processed data-stage2/QnA_data.xlsx')
word_df = pd.read_excel('D:/RAG-LLM/Pre-processed data-stage2/word_meaning_data.xlsx')

# Format them for embedding
qna_data = [f"প্রশ্ন: {row['QUESTIONS']} উত্তর: {row['ANSWERS']}" for _, row in qna_df.iterrows()]
word_data = [f"শব্দ: {row['WORD']} অর্থ: {row['MEANING']}" for _, row in word_df.iterrows()]

documents = qna_data + word_data

model = SentenceTransformer('intfloat/multilingual-e5-small')  # Supports Bengali
embeddings = model.encode(documents, show_progress_bar=True)

# Store in FAISS
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

def retrieve_answer(user_query, top_k=1):
    query_embedding = model.encode([user_query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [documents[i] for i in I[0]]


# Load Bengali LLM (offline or online depending on your setup)
llm = pipeline("text2text-generation", model="csebuetnlp/banglat5")

# Example query
query = "মামাকে ভাগ্য দেবতার প্রধান এজেন্ট বলা হয়েছে কেন?"
results = retrieve_answer(query)
context = results[0]

# Construct the final prompt
prompt = f"প্রশ্ন: {query}\nতথ্য: {context}\nউত্তর:"
response = llm(prompt, max_length=100, do_sample=True)
print(response[0]['generated_text'])
