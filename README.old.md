# 🤖 Enhanced Agentic RAG System v4.0

A production-ready, intelligent document Q&A system powered by LangChain and OpenAI.

## ✨ Features

### Core Capabilities
- ✅ **Multi-Format Support**: PDF, DOCX, TXT, PCAP files
- ✅ **Intelligent Agent**: ReAct (Reasoning + Acting) pattern
- ✅ **Secure API Management**: Keys stored in memory only
- ✅ **Modern LangChain**: Uses latest `create_react_agent` API
- ✅ **Persistent Memory**: JSON-based conversation storage
- ✅ **Transparent Reasoning**: See how the agent thinks
- ✅ **Feedback System**: Rate responses for continuous improvement

### What's Fixed from v3.0
- ✅ No hardcoded API keys
- ✅ Replaced deprecated `initialize_agent` with `create_react_agent`
- ✅ JSON instead of pickle for security
- ✅ Better error handling throughout
- ✅ Multi-format document support (not just PDF)
- ✅ Proper API key entry at startup
- ✅ Configurable ports to avoid conflicts
- ✅ Enhanced validation and type checking

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get API Keys

**Required:**
- **OpenAI API Key**: Get from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

**Optional:**
- **Tavily API Key**: Get from [https://tavily.com](https://tavily.com) (for web search)

### 3. Run the Application

```bash
python gradio_ui.py
```

Or use the startup script:
```bash
chmod +x run.sh
./run.sh
```

### 4. Access the UI

Open your browser to: **http://localhost:7860**

### 5. Initialize System

1. Enter your OpenAI API key in the setup screen
2. Optionally add Tavily API key for web search
3. Click "🚀 Initialize System"

### 6. Upload & Chat

1. Go to "Document Upload" tab
2. Upload a PDF, DOCX, TXT, or PCAP file
3. Go to "Interactive Chat" tab
4. Ask questions!

## 📚 Supported File Formats

| Format | Extension | Use Case | Features |
|--------|-----------|----------|----------|
| **PDF** | `.pdf` | Research papers, reports | Page-aware chunking |
| **Word** | `.docx`, `.doc` | Business documents | Structure preservation |
| **Text** | `.txt` | Code, logs, notes | Multi-encoding support |
| **PCAP** | `.pcap`, `.pcapng` | Network analysis | Protocol statistics, IP/port extraction |

## 🛠️ Available Tools

The AI agent automatically selects from these tools based on your query:

### 1. DocumentSearch 📚
Searches uploaded documents using semantic similarity.

**Example:** "What does the document say about Azure?"

### 2. Calculator 🧮
Performs mathematical calculations safely.

**Example:** "Calculate 15% of 2500"

### 3. TextAnalysis 📝
Analyzes text for word count, keywords, and summary.

**Example:** "Analyze this paragraph for keywords"

### 4. DataFormatter 📊
Formats data as bullet points or lists.

**Example:** "Format these items: A, B, C"

### 5. WebSearch 🌐
Searches the internet for current information (requires Tavily API key).

**Example:** "What are the latest Azure pricing updates?"

### 6. Wikipedia 📖
Looks up factual information from Wikipedia.

**Example:** "Who is the CEO of Microsoft?"

## 💡 Usage Examples

### Upload a Research Paper
```
1. Upload PDF → Process
2. Ask: "What is the main thesis of this paper?"
3. Follow up: "What methodology did they use?"
```

### Analyze Network Traffic
```
1. Upload PCAP file → Process
2. Ask: "What protocols are present in this capture?"
3. Ask: "What are the most common destination ports?"
```

### Multi-Step Reasoning
```
User: "Based on the document, calculate the total cost if we increase the budget by 15%"

Agent:
- Step 1: DocumentSearch for budget information
- Step 2: Calculator to compute 15% increase
- Step 3: Synthesize final answer
```

## 📊 Architecture

```
┌─────────────────┐
│   Gradio UI     │  ← User Interface
└────────┬────────┘
         │
┌────────▼────────┐
│  AgenticRAG     │  ← Core System
│  System         │
└────────┬────────┘
         │
    ┌────┴────┬──────────┬───────────┬──────────┐
    │         │          │           │          │
┌───▼──┐ ┌───▼──┐  ┌───▼────┐ ┌────▼────┐ ┌──▼───┐
│ FAISS│ │Tools │  │ Memory │ │ OpenAI  │ │Tavily│
│Vector│ │Chain │  │Manager │ │   API   │ │ API  │
└──────┘ └──────┘  └────────┘ └─────────┘ └──────┘
```

## 🔐 Security & Privacy

### API Key Security
- ✅ Keys never stored on disk
- ✅ Keys only in memory during session
- ✅ Password-masked input fields
- ✅ No logging of sensitive data

### Data Privacy
- ✅ All processing done locally (except API calls)
- ✅ Conversations saved locally in JSON
- ✅ No third-party data sharing
- ✅ You control all data retention

## 📝 File Structure

```
Agentic RAG Chatbot/
├── agentic_rag_app.py      # Core RAG system
├── gradio_ui.py            # Web interface
├── requirements.txt        # Dependencies
├── README.md              # This file
├── run.sh                 # Startup script
├── memory_store/          # Conversation history (auto-created)
│   └── interaction_history.json
├── faiss_index/           # Vector database (auto-created)
└── agentic_rag.log       # System logs (auto-created)
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'X'"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### "Invalid API Key"
**Solution:** 
- Check your API key is correct
- Ensure it starts with `sk-`
- Verify you have credits in your OpenAI account

### "Port 7860 already in use"
**Solution:** Edit `gradio_ui.py` and change the port:
```python
demo.launch(server_port=7861)  # Change to any available port
```

### "Scapy not available"
**Solution:** Only needed for PCAP files
```bash
pip install scapy
# On Linux, may need: sudo apt-get install tcpdump
```

### Agent not using tools correctly
**Solution:**
- Be explicit in your questions
- Use trigger phrases like "in the document", "calculate", "search for"
- Check agent reasoning panel to see tool selection

## 🆚 Version Comparison

| Feature | v3.0 (Old) | v4.0 (New) |
|---------|------------|------------|
| API Keys | Hardcoded ❌ | Secure entry ✅ |
| LangChain | Deprecated methods ⚠️ | Modern API ✅ |
| File Formats | PDF only | PDF, DOCX, TXT, PCAP ✅ |
| Persistence | Pickle | JSON ✅ |
| Error Handling | Basic | Comprehensive ✅ |
| Port Config | Fixed 7110 | Configurable 7860 ✅ |

## 🔧 Configuration

### Change LLM Model
Edit `agentic_rag_app.py`:
```python
self.llm = ChatOpenAI(model="gpt-4", temperature=0)  # Use GPT-4
```

### Adjust Chunk Size
Edit `agentic_rag_app.py`:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,     # Larger chunks
    chunk_overlap=300    # More overlap
)
```

### Change Memory Path
Edit `gradio_ui.py`:
```python
rag_system = AgenticRAG(api_keys=api_keys, memory_path="custom_path")
```

## 📈 Performance Tips

1. **Large Documents**: Processing time scales with document size
2. **Chunk Size**: Smaller chunks = more precise but slower
3. **API Costs**: GPT-4 is more expensive than GPT-3.5-turbo
4. **Vector Store**: Save FAISS index to avoid reprocessing

## 🤝 Contributing

Found a bug or have a suggestion? Please create an issue with:
- System information
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs from `agentic_rag.log`

## 📄 License

MIT License - feel free to use, modify, and distribute.

## 🙏 Acknowledgments

Built with:
- [LangChain](https://github.com/langchain-ai/langchain) - Agent framework
- [OpenAI](https://openai.com) - Language models
- [FAISS](https://github.com/facebookresearch/faiss) - Vector search
- [Gradio](https://gradio.app) - Web interface
- [Scapy](https://scapy.net) - PCAP analysis

## 📞 Support

- Check `agentic_rag.log` for errors
- Export conversation logs for debugging
- Review agent reasoning panel for tool usage

---

**Made with ❤️ by the Enhanced Agentic RAG Team**

*Version 4.0 - Production Ready*

