# 📚 Bengali RAG-based Question Answering System

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline in Bengali, capable of answering:
- General questions from a Bengali Q&A Excel file
- Word meanings from a Bengali vocabulary Excel file

It uses **FAISS for dense retrieval** and a **pretrained Bengali LLM** (`csebuetnlp/banglat5`) from Hugging Face to generate intelligent answers grounded in context.

---

## 🚀 Features

- ✅ Accepts queries in Bengali
- ✅ Answers from two sources:
  - Bengali Questions & Answers (`QnA_data.xlsx`)
  - Bengali Word Meanings (`word_meaning_data.xlsx`)
- ✅ Embedding-based semantic search using `sentence-transformers`
- ✅ Bengali LLM generation using HuggingFace Transformers
- ✅ Runs fully offline after first-time model downloads

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/RistianRidoy/Bengali-RAG-LLM.git
cd Bengali-RAG-LLM

### 2. Create environment

python -m venv bengali_rag_env
bengali_rag_env\Scripts\activate   # Windows
# or
source bengali_rag_env/bin/activate  # macOS/Linux

### 3. Install dependencies

pip install -r requirements.txt
