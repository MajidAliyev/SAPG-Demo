#!/usr/bin/env python3
"""
Quick test script to verify the app works
"""

import subprocess
import requests
import time

print("🧪 Testing Self-Auditing Prompt Generator...")

# Test 1: Check if app is running
print("\n1. Checking if app is running...")
try:
    response = requests.get("http://localhost:8501", timeout=5)
    if response.status_code == 200:
        print("✅ App is running at http://localhost:8501")
    else:
        print(f"❌ App returned status {response.status_code}")
except Exception as e:
    print(f"❌ App not responding: {e}")
    print("   Make sure to run: streamlit run app.py")

# Test 2: Check if Ollama is available
print("\n2. Checking Ollama...")
result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
if result.returncode == 0:
    models = result.stdout
    print("✅ Ollama is running")
    if 'llama2' in models:
        print("   ✓ llama2 model is installed")
    else:
        print("   ⚠️  llama2 not found. Run: ollama pull llama2")

    if 'mistral' in models:
        print("   ✓ mistral model is installed (fast option)")
    else:
        print("   💡 To install faster mistral: ollama pull mistral")
else:
    print("❌ Ollama not running")
    print("   Run: ollama serve")

# Test 3: Check Python imports
print("\n3. Checking Python dependencies...")
try:
    import streamlit
    print("✅ Streamlit installed")

    import langchain_core
    print("✅ LangChain installed")

    try:
        from langchain_ollama import ChatOllama
        print("✅ LangChain Ollama support installed")
    except ImportError:
        print("❌ langchain-ollama not installed")
        print("   Run: pip install langchain-ollama")

except ImportError as e:
    print(f"❌ Missing dependency: {e}")

print("\n" + "="*50)
print("🎯 READY TO TEST!")
print("\nTo test the app:")
print("1. Open: http://localhost:8501")
print("2. Select 'ollama' as provider")
print("3. For FASTER results, use 'mistral' model:")
print("   - Type 'mistral' in 'Model Name' field")
print("   - Or run: ollama pull mistral")
print("4. Enter: 'build me a to do app'")
print("5. Click 'Execute Self-Audit'")
print("6. Wait 1-5 minutes (depends on model)")
print("\nFor INSTANT results, use OpenAI API instead!")
print("="*50)
