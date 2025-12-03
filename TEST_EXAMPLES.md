# 🧪 Test Examples

Test your Enhanced Agentic RAG System with these examples.

---

## 📄 PDF Document Test

### Sample Questions
```
1. "What is the main topic of this document?"
2. "Summarize the key findings in the document"
3. "What methodology is described in the document?"
4. "List all the references mentioned"
5. "What are the conclusions?"
```

### Advanced Queries
```
1. "Compare the approaches mentioned in section 2 and section 3"
2. "What gaps in research are identified?"
3. "Calculate the percentage increase mentioned on page 5"
```

---

## 📝 Word Document (.docx) Test

### Sample Questions
```
1. "What are the action items in this document?"
2. "Who are the stakeholders mentioned?"
3. "Summarize the quarterly results"
4. "List all the deadlines"
5. "What budget is allocated?"
```

### Advanced Queries
```
1. "Format the action items as a bullet list"
2. "Calculate the total budget across all departments"
3. "What risks are identified and how are they mitigated?"
```

---

## 📃 Text File (.txt) Test

### For Code Files
```
1. "What functions are defined in this code?"
2. "Are there any TODO comments?"
3. "Analyze the code structure"
4. "What libraries are imported?"
5. "Are there any potential bugs?"
```

### For Log Files
```
1. "What errors appear in this log?"
2. "When did the system start?"
3. "What's the most common warning?"
4. "Analyze the timestamp patterns"
5. "How many unique error types are there?"
```

### For Plain Text
```
1. "Summarize this text"
2. "What are the main themes?"
3. "Extract all dates mentioned"
4. "Analyze the sentiment"
5. "Count the words and get keywords"
```

---

## 📡 PCAP File Test

### Network Analysis Questions
```
1. "What protocols are present in this capture?"
2. "How many packets were captured?"
3. "What are the top source IP addresses?"
4. "What are the most common destination ports?"
5. "Analyze the network traffic patterns"
```

### Security Analysis
```
1. "Are there any suspicious IP addresses?"
2. "What services are being accessed?"
3. "Identify any unusual port activity"
4. "Summarize the communication patterns"
```

---

## 🧮 Calculator Tool Test

Test the agent's ability to use the calculator:

```
1. "Calculate 15% of 2500"
   Expected: Agent uses Calculator tool
   Result: 375

2. "What is 45 multiplied by 67?"
   Expected: Agent uses Calculator
   Result: 3015

3. "Calculate the square root of 256"
   Expected: Agent uses Calculator with sqrt()
   Result: 16.0

4. "If the document mentions $10,000 and we add 25%, what's the total?"
   Expected: Agent uses DocumentSearch + Calculator
   Result: $12,500
```

---

## 📊 Data Formatter Tool Test

Test the agent's formatting capabilities:

```
1. "Format these items as bullets: Python, JavaScript, Java, C++"
   Expected: Agent uses DataFormatter
   Result: Bullet list

2. "List the following in a clean format: task1, task2, task3"
   Expected: Agent uses DataFormatter
   Result: Formatted list
```

---

## 📝 Text Analysis Tool Test

Test text analysis functionality:

```
1. "Analyze this paragraph: [paste long text]"
   Expected: Agent uses TextAnalysis
   Result: Word count, keywords, summary

2. "Count the words in the document"
   Expected: Agent uses TextAnalysis or DocumentSearch
   Result: Word count
```

---

## 🌐 Web Search Tool Test (Requires Tavily API Key)

Test real-time web search:

```
1. "What are the latest Python updates in 2024?"
   Expected: Agent uses WebSearch
   Result: Current information

2. "Search for current OpenAI pricing"
   Expected: Agent uses WebSearch
   Result: Latest pricing info

3. "What's the weather today?"
   Expected: Agent uses WebSearch
   Result: Current weather
```

---

## 📖 Wikipedia Tool Test

Test Wikipedia integration:

```
1. "Who is the current CEO of Microsoft?"
   Expected: Agent uses Wikipedia or WebSearch
   Result: Satya Nadella

2. "Tell me about the Python programming language from Wikipedia"
   Expected: Agent uses Wikipedia
   Result: Summary from Wikipedia

3. "What is machine learning?"
   Expected: Agent might use Wikipedia or direct knowledge
   Result: ML definition
```

---

## 🔄 Multi-Tool Queries

Test the agent's ability to chain multiple tools:

```
1. "Search the document for the budget, then calculate 20% of it"
   Expected: DocumentSearch → Calculator
   Result: Combined answer

2. "Find all names in the document and format them as a list"
   Expected: DocumentSearch → DataFormatter
   Result: Formatted name list

3. "Get the latest stock price for AAPL and calculate 15% gain"
   Expected: WebSearch → Calculator
   Result: Current price + calculated gain

4. "Analyze the abstract of the document and count its words"
   Expected: DocumentSearch → TextAnalysis
   Result: Analysis with word count
```

---

## 💭 Conversational Memory Test

Test that the agent remembers context:

```
Conversation 1:
You: "What databases are mentioned in the document?"
Agent: "Azure SQL Database and Cosmos DB"
You: "Compare them"  ← Agent should remember "them" = those 2 databases
Agent: [Comparison of the two]

Conversation 2:
You: "What's the capital of France?"
Agent: "Paris"
You: "What's its population?"  ← Agent should remember "its" = Paris
Agent: [Population of Paris]

Conversation 3:
You: "Upload document about cloud computing"
Agent: [Processes document]
You: "Summarize it"  ← Agent should know "it" = the document
Agent: [Summary]
```

---

## 🎯 Edge Cases & Error Handling

Test error handling:

```
1. Ask question without uploading document
   Expected: "No document has been uploaded yet"

2. Upload corrupted file
   Expected: Error message with details

3. Ask extremely vague question: "Tell me"
   Expected: Request for clarification

4. Try to divide by zero: "Calculate 100/0"
   Expected: Error message from Calculator

5. Upload very large file (>100MB)
   Expected: Processing status or size warning
```

---

## 📊 Feedback System Test

Test the feedback mechanism:

```
1. Ask a question
2. Click 👍 (Thumbs up)
   Expected: "Feedback recorded!"

3. Ask another question
4. Click 👎 (Thumbs down)
   Expected: "Feedback recorded!"

5. Go to Statistics tab
   Expected: See feedback counts
```

---

## 💾 Memory Persistence Test

Test that conversations are saved:

```
1. Ask several questions
2. Close the browser
3. Restart the application (python gradio_ui.py)
4. Click "📂 Load History"
   Expected: Previous conversations appear

5. Check memory_store/interaction_history.json
   Expected: JSON file with all conversations
```

---

## 📤 Export Test

Test log export functionality:

```
1. Have a few conversations
2. Click "📥 Export Logs"
   Expected: "Logs exported to interaction_logs.json"

3. Check the file
   Expected: JSON file with all interactions
```

---

## 🗑️ Clear Memory Test

Test memory clearing:

```
1. Have several conversations
2. Click "🗑️ Clear Chat"
   Expected: Chat history disappears
   
3. Check Statistics tab
   Expected: Conversation count resets to 0
```

---

## 📈 Statistics Test

Test analytics dashboard:

```
1. Have multiple conversations
2. Give some 👍 and 👎 feedback
3. Use different tools (Calculator, DocumentSearch, etc.)
4. Go to Statistics tab
5. Click "🔄 Refresh Statistics"
   Expected:
   - Total conversations count
   - Feedback breakdown
   - Tool usage statistics
   - Satisfaction rate
```

---

## 🔒 Security Test

Test API key security:

```
1. Enter API keys
2. Initialize system
3. Check browser inspector (F12)
   Expected: Keys NOT visible in source code

4. Check agentic_rag.log
   Expected: Keys NOT logged

5. Check all .py files
   Expected: No hardcoded keys
```

---

## 🌍 Multi-Format Test

Test all formats in one session:

```
1. Upload PDF → Ask questions → Success ✅
2. Upload DOCX → Ask questions → Success ✅
3. Upload TXT → Ask questions → Success ✅
4. Upload PCAP → Ask questions → Success ✅

All should work without restarting!
```

---

## 📱 User Interface Test

Test all UI elements:

```
✅ API key entry screen
✅ Initialize button
✅ Document upload
✅ Process button
✅ Chat interface
✅ Send button
✅ Agent reasoning panel
✅ Feedback buttons
✅ Clear chat button
✅ Load history button
✅ Export logs button
✅ Statistics tab
✅ Refresh statistics button
✅ Help tab
✅ All tabs accessible
```

---

## 🎓 Learning Test

Test progressive learning:

```
Session 1:
1. Upload research paper
2. Ask basic questions
3. Rate responses with 👍

Session 2 (after restart):
1. Load history
2. Continue conversation
   Expected: Agent remembers previous context
```

---

## 🚀 Performance Test

Test with different file sizes:

```
1. Small file (<1MB)
   Expected: Fast processing (<10 seconds)

2. Medium file (1-10MB)
   Expected: Moderate processing (10-30 seconds)

3. Large file (>10MB)
   Expected: Longer processing (30+ seconds)
   Status updates should show progress
```

---

## ✅ Checklist for Complete Testing

Before considering the system fully tested:

- [ ] PDF upload and query
- [ ] DOCX upload and query
- [ ] TXT upload and query
- [ ] PCAP upload and query (if scapy installed)
- [ ] Calculator tool usage
- [ ] DocumentSearch tool usage
- [ ] TextAnalysis tool usage
- [ ] DataFormatter tool usage
- [ ] Wikipedia tool usage
- [ ] WebSearch tool usage (if Tavily configured)
- [ ] Multi-tool queries
- [ ] Conversational memory
- [ ] Feedback system
- [ ] Export logs
- [ ] Clear memory
- [ ] Load history
- [ ] Statistics dashboard
- [ ] Error handling
- [ ] API key security
- [ ] Memory persistence across restarts

---

## 🐛 Known Limitations

Things that might not work as expected:

1. **Scanned PDFs**: Text-based PDFs only, no OCR
2. **Very Large Files**: May take time to process
3. **Complex PCAP**: Only analyzes first 1000 packets
4. **Old .doc Files**: May need conversion to .docx
5. **Binary Files**: Not supported (only text-based formats)

---

## 💡 Tips for Best Results

1. **Be Specific**: "What does the document say about X?" vs "Tell me about X"
2. **Use Context**: Agent remembers recent conversation
3. **Check Reasoning**: Look at tool selection in reasoning panel
4. **Provide Feedback**: Helps improve the system
5. **Start Simple**: Test with simple queries first
6. **Read Logs**: Check `agentic_rag.log` for details

---

## 🎉 Success Criteria

Your system is working correctly if:

✅ All file formats process successfully
✅ Agent selects appropriate tools
✅ Responses are relevant and accurate
✅ Memory persists across restarts
✅ No errors in logs (except expected ones)
✅ UI is responsive
✅ Feedback system works
✅ Statistics update correctly

---

**Happy Testing! 🧪**

