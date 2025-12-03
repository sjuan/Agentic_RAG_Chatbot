# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Install Dependencies (2 min)

```bash
cd "/home/unit-s/Documents/Agentic RAG Chatbot"
pip install -r requirements.txt
```

## Step 2: Get Your OpenAI API Key (1 min)

1. Visit: https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

## Step 3: Start the Application (30 sec)

```bash
python gradio_ui.py
```

Or use the startup script:
```bash
./run.sh
```

## Step 4: Initialize System (30 sec)

1. Open browser to: **http://localhost:7860**
2. Paste your OpenAI API key
3. Click "🚀 Initialize System"

## Step 5: Upload & Chat (1 min)

### Upload a Document
1. Click "Document Upload" tab
2. Click "Select File"
3. Choose any PDF, DOCX, TXT, or PCAP file
4. Click "🔄 Process Document"
5. Wait for "✅ Document Processed Successfully!"

### Start Chatting
1. Click "Interactive Chat" tab
2. Type a question in the text box
3. Click "📤 Send" or press Enter
4. Watch the agent reason through its response!

---

## 🎯 Try These Examples

### For a Research Paper (PDF)
```
"What is the main thesis of this paper?"
"Summarize the methodology"
"What are the key findings?"
```

### For a Business Document (DOCX)
```
"What are the action items?"
"Summarize the quarterly results"
"Who are the stakeholders mentioned?"
```

### For Code or Logs (TXT)
```
"What errors are in this log file?"
"Analyze the function definitions"
"Find all TODO comments"
```

### For Network Traffic (PCAP)
```
"What protocols are present?"
"What are the most common destination IPs?"
"Summarize the network activity"
```

---

## 💡 Pro Tips

1. **Be Specific**: "What does the document say about X?" works better than "Tell me about X"

2. **Follow Up**: The agent remembers context
   ```
   You: "What databases are mentioned in the document?"
   Agent: "Azure SQL Database and Cosmos DB"
   You: "Compare them"  ← Agent remembers what "them" means
   ```

3. **Use Feedback**: Rate responses with 👍/👎 to help improve the system

4. **Check Reasoning**: Look at the "Agent Reasoning" panel to see which tools were used

5. **Save Your Work**: Use "📥 Export Logs" to save all conversations

---

## 🐛 Common Issues

### "System not initialized"
→ You forgot to enter your API key. Go back to the setup screen.

### "No document uploaded"
→ Upload a document in the "Document Upload" tab first.

### "Connection error"
→ Check your internet connection and API key validity.

### "Port already in use"
→ Change the port in `gradio_ui.py`:
```python
demo.launch(server_port=7861)  # Use a different port
```

---

## 🔐 Optional: Add Web Search

Want to search the internet in addition to documents?

1. Get Tavily API key: https://tavily.com
2. When initializing, enter it in the "Tavily API Key" field
3. Now ask: "What are the latest Python trends in 2024?"

---

## 📱 Access URLs

- **Local**: http://localhost:7860
- **Network** (if others on your network want to access):
  - Find your IP: `ip addr show` or `ifconfig`
  - Share: http://YOUR_IP:7860

---

## 🎉 You're All Set!

The system is now ready. Some things to explore:

- **Statistics Tab**: See usage analytics
- **Help Tab**: Detailed documentation
- **Agent Reasoning**: Watch how the AI thinks
- **Feedback System**: Rate responses to improve quality

---

## 📚 Next Steps

- Read the full [README.md](README.md) for advanced features
- Check [CHANGES.md](CHANGES.md) to see what's new in v4.0
- Review `agentic_rag.log` for detailed system logs
- Export conversation logs for analysis

---

**Happy Chatting! 🤖**

