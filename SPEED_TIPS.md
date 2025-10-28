# ⚡ Speed Tips for Faster Results

## The Problem

The default `llama2` model is HUGE (3.8GB) and SLOW (5-15 minutes per request).

## The Solution: Use Faster Models

### Option 1: Mistral (Recommended - 5x Faster!)

```bash
ollama pull mistral
```

Then in the app, change "Model Name" to: `mistral`

### Option 2: Smaller Llama2

```bash
ollama pull llama2:7b
```

Then in the app, change "Model Name" to: `llama2:7b`

### Option 3: Even Smaller Models

```bash
ollama pull phi  # Super fast, smaller
ollama pull gemma:2b  # Very fast
```

## Speed Comparison

| Model            | Size  | Speed                             | Quality    |
| ---------------- | ----- | --------------------------------- | ---------- |
| llama2 (default) | 3.8GB | ⏱️ Slow (5-15 min)                | ⭐⭐⭐⭐⭐ |
| llama2:7b        | 3.8GB | ⚡ Medium (2-5 min)               | ⭐⭐⭐⭐⭐ |
| mistral          | 4.1GB | ⚡⚡ Fast (1-3 min)               | ⭐⭐⭐⭐⭐ |
| phi              | 1.6GB | ⚡⚡⚡ Very Fast (30 sec - 1 min) | ⭐⭐⭐     |
| gemma:2b         | 0.5GB | ⚡⚡⚡⚡⚡ Ultra Fast (10-30 sec) | ⭐⭐       |

## Recommended Workflow

1. **For Testing**: Use `mistral` or `phi` - fast iteration
2. **For Production**: Use `llama2` or `mistral` - better quality
3. **For Instant Results**: Use OpenAI/Anthropic APIs

## Using the App

1. Download a faster model: `ollama pull mistral`
2. In the app sidebar, select "ollama"
3. Change "Model Name" from "llama2" to "mistral"
4. Enter your request and click Execute
5. Results in 1-3 minutes instead of 5-15!

## OpenAI/Anthropic (Fastest Option)

If you want INSTANT results (no waiting):

1. Get API key from OpenAI or Anthropic
2. Create `.env` file in project folder:
   ```
   OPENAI_API_KEY=your_key_here
   ```
3. In app, select "openai" or "anthropic" as provider
4. Results in 10-60 seconds!

## Troubleshooting

**"Connection timeout"**

- Ollama is too slow with large models
- Solution: Use smaller model or API

**"Model not found"**

- Run: `ollama list` to see installed models
- Download: `ollama pull mistral`

**Still too slow?**

- Use OpenAI API (fastest)
- Or use `phi` model (super fast, decent quality)

## Pro Tips

- **Batch testing**: Use `phi` or `gemma:2b`
- **Final output**: Use `mistral` or OpenAI
- **Production**: Use `llama2` with patience

Happy (faster) self-auditing! ⚡
