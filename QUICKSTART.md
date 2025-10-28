# 🚀 Quick Start Guide (For Beginners)

**Welcome!** This guide will help you get the Self-Auditing Prompt Generator running on your computer in 5 minutes.

## What You Need

- A computer (Mac, Windows, or Linux)
- An internet connection

---

## Step-by-Step Installation

### Step 1: Install Python

**If you don't have Python installed:**

- **Mac/Linux**: Python usually comes pre-installed. Check by opening Terminal and typing: `python3 --version`
- **Windows**: Download from [python.org](https://www.python.org/downloads/) (check "Add Python to PATH" during installation)

### Step 2: Download This Repository

Click the green "Code" button on GitHub and download as ZIP, or clone:

```bash
git clone https://github.com/yourusername/SACC.git
cd SACC
```

### Step 3: Install Dependencies

Open Terminal/Command Prompt in the SACC folder and run:

```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama (Free AI Model)

1. **Download Ollama**: Go to [ollama.ai](https://ollama.ai) and download for your computer
2. **Install it** (just follow the normal installation process)
3. **Pull the AI model**: Open Terminal/Command Prompt and run:
   ```bash
   ollama pull llama2
   ```
   This downloads the AI model (takes 5-10 minutes, ~4GB download)

### Step 5: Run the App!

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

---

## Using the App

1. **Sidebar (Left)**: Select "ollama" as provider
2. **Main Area**:
   - Either select an example from the dropdown OR
   - Type what you want (e.g., "Create a login page")
3. Click "🚀 Execute Self-Audit"
4. Wait 5-15 minutes (first time is slowest)
5. See your results in 4 tabs!

---

## Troubleshooting

**"python3: command not found"**

- Try `python` instead of `python3`

**"pip not found"**

- Try `pip3` instead of `pip`

**"ollama: command not found"**

- Restart your terminal after installing Ollama

**App running but nothing happens when I click Execute**

- Be patient! The first run can take 5-15 minutes
- You should see progress messages like "Phase 1/3: Generating Draft..."

---

## Alternative: Use OpenAI/Anthropic (Faster but Costs Money)

If you want faster results (or don't want to install Ollama):

1. Get an API key:

   - **OpenAI**: https://platform.openai.com/api-keys
   - **Anthropic**: https://console.anthropic.com/

2. Install the provider:

   ```bash
   pip install langchain-openai
   # OR
   pip install langchain-anthropic
   ```

3. Create a `.env` file in the SACC folder:

   ```
   OPENAI_API_KEY=your_key_here
   # OR
   ANTHROPIC_API_KEY=your_key_here
   ```

4. Run the app and select your provider in the sidebar

---

## Need Help?

- Check the full README.md for detailed information
- Open an issue on GitHub
- Make sure Python, Streamlit, and Ollama are all installed correctly

**Happy Self-Auditing! 🎉**
