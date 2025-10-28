# Quick Setup Guide

## Installation Steps

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Choose ONE of the following LLM options:**

   ### Option A: Ollama (FREE - Runs Locally)

   ```bash
   # Install Ollama from https://ollama.ai
   # Then download a model:
   ollama pull llama2
   ```

   ### Option B: OpenAI (Requires API Key)

   ```bash
   # Create .env file with your API key:
   echo "OPENAI_API_KEY=your_key_here" > .env
   pip install langchain-openai
   ```

   ### Option C: Anthropic (Requires API Key)

   ```bash
   # Create .env file with your API key:
   echo "ANTHROPIC_API_KEY=your_key_here" > .env
   pip install langchain-anthropic
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## What You Get

✅ **Draft Agent**: Generates initial execution plans  
✅ **Critique Agent**: Systematically audits for errors  
✅ **Revision Agent**: Produces corrected, auditable output  
✅ **Beautiful UI**: Tabbed interface to review all phases  
✅ **Multi-LLM Support**: Works with Ollama, OpenAI, Anthropic

## Try These Examples

1. "Create a Python script that processes user uploads with validation"
2. "Design a database migration with rollback safety"
3. "Build a secure API endpoint with rate limiting"
4. "Write an ETL pipeline with error handling and logging"
