---
title: Enhanced Agentic RAG Chatbot
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
tags:
  - langchain
  - rag
  - chatbot
  - openai
  - document-qa
  - ai
  - nlp
  - faiss
  - gradio
  - multi-format
short_description: Intelligent RAG system with multi-format support (PDF, DOCX, TXT, PCAP)
---

# 🤖 Enhanced Agentic RAG System v4.0

An intelligent document question-answering system powered by LangChain and OpenAI with multi-format support and modern architecture.

## ✨ Features

- 📄 **Multi-Format Support**: PDF, DOCX, TXT, PCAP files
- 🤖 **Intelligent Agent**: ReAct (Reasoning + Acting) pattern
- 🔐 **Secure**: API keys entered via UI (not hardcoded)
- 🛠️ **Multiple Tools**: Calculator, Text Analysis, Web Search, Wikipedia
- 💾 **Persistent Memory**: Conversation history saved automatically
- 📊 **Analytics**: Statistics and feedback system
- 🎨 **Beautiful UI**: Modern Gradio interface

## 🚀 How to Use

### 1. Get Your API Keys

**Required:**
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

**Optional:**
- **Tavily API Key**: Get from [Tavily](https://tavily.com) for web search

### 2. Initialize the System

1. Enter your OpenAI API key in the setup screen
2. Optionally add Tavily API key for web search capability
3. Click "🚀 Initialize System"

### 3. Upload a Document

**Supported Formats:**
- **PDF** (.pdf) - Research papers, reports
- **Word** (.docx, .doc) - Business documents
- **Text** (.txt) - Code files, logs, notes
- **PCAP** (.pcap, .pcapng) - Network packet captures

### 4. Start Chatting!

Ask questions like:
- "What is the main topic of this document?"
- "Summarize the key findings"
- "Calculate 15% of the budget mentioned"
- "What protocols are in this network capture?"

## 🛠️ Available Tools

The AI agent automatically selects from:

- **📚 DocumentSearch** - Semantic search in uploaded documents
- **🧮 Calculator** - Mathematical calculations
- **📝 TextAnalysis** - Word count, keywords, summaries
- **📊 DataFormatter** - Format lists and bullet points
- **🌐 WebSearch** - Real-time internet search (Tavily)
- **📖 Wikipedia** - Factual information lookup

## 🔒 Privacy & Security

- ✅ API keys stored in memory only (never on disk)
- ✅ Your documents are processed privately
- ✅ Conversations saved locally in your session
- ✅ No data shared with third parties (except OpenAI/Tavily APIs)

## 💡 Example Queries

### For Research Papers:
```
"What methodology was used in this study?"
"Summarize the abstract"
"What are the limitations mentioned?"
```

### For Business Documents:
```
"List all action items"
"What's the quarterly revenue?"
"Who are the key stakeholders?"
```

### For Code Files:
```
"What functions are defined?"
"Are there any security issues?"
"Count the lines of code"
```

### For Network Captures:
```
"What protocols are present?"
"What are the top destination IPs?"
"Analyze the traffic patterns"
```

### Multi-Tool Queries:
```
"Find the budget in the document and calculate 20% of it"
"Search for latest Azure pricing and compare to the document"
```

## 🏗️ Architecture

- **Framework**: LangChain (modern create_react_agent API)
- **LLM**: OpenAI GPT-3.5-turbo
- **Vector Store**: FAISS
- **UI**: Gradio 4.x
- **Agent Pattern**: ReAct (Reasoning + Acting)

## 📊 Technical Details

- Multi-format document loader with fallback support
- Recursive text splitting with 1000-char chunks
- 200-char overlap for context preservation
- Semantic similarity search with FAISS
- JSON-based conversation persistence
- Comprehensive error handling

## 🔧 Configuration

This Space uses the following secrets (set in Space settings):
- `OPENAI_API_KEY` (optional - can be entered via UI)
- `TAVILY_API_KEY` (optional - for web search)

## 📝 Notes

- Processing large documents may take a few seconds
- PCAP support requires scapy (included in requirements)
- Web search requires Tavily API key
- System memory persists during your session

## 🌟 Credits

Built with:
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Gradio](https://gradio.app)
- [Hugging Face Spaces](https://huggingface.co/spaces)

## 📄 License

MIT License - Free to use and modify

## 🔗 Links

- **GitHub**: [Source Code](https://github.com/sjuan/Agentic_RAG_Chatbot)
- **Documentation**: See GitHub repository for detailed docs

---

**Made with ❤️ for the AI community**

*Enhanced Agentic RAG System v4.0*

