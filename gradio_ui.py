#!/usr/bin/env python3
"""
🎨 Gradio UI for Enhanced Agentic RAG System
==============================================

Interactive web interface with:
- API key entry at startup
- Multi-format document upload
- Interactive chat
- Agent reasoning visualization
- Feedback collection
- Statistics dashboard

Author: Enhanced Agentic RAG Team
Version: 4.0
"""

import gradio as gr
from typing import List, Tuple, Dict
from datetime import datetime
from collections import Counter

# Import the core system
from agentic_rag_app import AgenticRAG, logger

# ═══════════════════════════════════════════════════════════════════
# 🎨 Custom CSS
# ═══════════════════════════════════════════════════════════════════

CUSTOM_CSS = """
/* Global Styles */
.gradio-container {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Header Styling */
.app-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
}

/* Status Cards */
.status-card {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #667eea;
    margin: 1rem 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.status-success {
    border-left-color: #10b981;
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
}

.status-error {
    border-left-color: #ef4444;
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
}

.metric {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 20px;
    font-weight: 600;
    margin: 0.25rem;
}
"""

# ═══════════════════════════════════════════════════════════════════
# 🌐 Global Variables
# ═══════════════════════════════════════════════════════════════════

rag_system = None

# ═══════════════════════════════════════════════════════════════════
# 🎨 UI Handler Functions
# ═══════════════════════════════════════════════════════════════════

def initialize_system(openai_key: str, tavily_key: str = ""):
    """Initialize the RAG system with API keys."""
    global rag_system
    
    if not openai_key or len(openai_key.strip()) < 10:
        return """
        <div class="status-card status-error">
            <h3>❌ Invalid API Key</h3>
            <p>Please provide a valid OpenAI API key (starts with 'sk-').</p>
        </div>
        """, gr.update(visible=False), gr.update(visible=True)
    
    try:
        api_keys = {
            'openai': openai_key.strip(),
            'tavily': tavily_key.strip() if tavily_key else None
        }
        
        rag_system = AgenticRAG(api_keys=api_keys)
        
        status_html = """
        <div class="status-card status-success">
            <h2>✅ System Initialized Successfully!</h2>
            <p style="margin-top: 1rem; font-size: 1.1rem;">
                🤖 <strong>Agentic RAG System is ready!</strong>
            </p>
            <div style="margin-top: 1rem;">
                <div class="metric">✅ OpenAI Connected</div>
        """
        
        if tavily_key:
            status_html += '<div class="metric">✅ Tavily Connected</div>'
        
        status_html += """
            </div>
            <p style="margin-top: 1rem; color: #059669;">
                ⚡ You can now upload documents and start chatting!
            </p>
        </div>
        """
        
        return status_html, gr.update(visible=True), gr.update(visible=False)
        
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return f"""
        <div class="status-card status-error">
            <h3>❌ Initialization Failed</h3>
            <p><strong>Error:</strong> {str(e)}</p>
            <p style="margin-top: 0.5rem;">
                💡 Check your API key and try again.
            </p>
        </div>
        """, gr.update(visible=False), gr.update(visible=True)


def load_conversation_history() -> Tuple[List[Tuple[str, str]], str]:
    """Load past conversation history."""
    if not rag_system:
        return [], "<div class='status-card status-error'>System not initialized</div>"
    
    try:
        history = rag_system.get_conversation_history(num_interactions=50)
        
        if not history:
            return [], "<div class='status-card'>No previous conversations found.</div>"
        
        chat_history = [(h.query, h.response) for h in history]
        
        status_msg = f"""
        <div class="status-card status-success">
            <h3>📂 History Loaded</h3>
            <p>✅ Restored <strong>{len(history)}</strong> conversations</p>
        </div>
        """
        
        return chat_history, status_msg
        
    except Exception as e:
        return [], f"<div class='status-card status-error'>Error: {str(e)}</div>"


def process_document_ui(file):
    """Process uploaded document."""
    if not rag_system:
        return "<div class='status-card status-error'>Please initialize the system first!</div>"
    
    if not file:
        return "<div class='status-card status-error'>Please upload a file.</div>"
    
    try:
        result = rag_system.process_document(file.name)
        
        if result['success']:
            return f"""
            <div class="status-card status-success">
                <h2>✅ Document Processed Successfully!</h2>
                <div style="margin-top: 1rem;">
                    <div class="metric">📄 {result['filename']}</div>
                    <div class="metric">📋 {result['format']}</div>
                    <div class="metric">📊 {result['chunks']} chunks</div>
                </div>
                <p style="margin-top: 1rem; color: #059669;">
                    ⚡ Ready to answer questions about this document!
                </p>
            </div>
            """
        else:
            return f"""
            <div class="status-card status-error">
                <h3>❌ Processing Failed</h3>
                <p>{result.get('error', 'Unknown error')}</p>
            </div>
            """
    except Exception as e:
        logger.error(f"Document processing error: {e}")
        return f"<div class='status-card status-error'>Error: {str(e)}</div>"


def chat_ui(message: str, history: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], Dict]:
    """Handle chat interaction."""
    if not rag_system:
        history.append((message, "❌ Please initialize the system first! Go to the setup tab and enter your API key."))
        return history, {}
    
    if not message.strip():
        return history, {}
    
    try:
        result = rag_system.chat(message)
        response = result.get('response', 'No response')
        metadata = result.get('metadata', {})
        
        if 'conversation_id' in result:
            metadata['conversation_id'] = result['conversation_id']
        
        history.append((message, response))
        return history, metadata
    except Exception as e:
        logger.error(f"Chat error: {e}")
        history.append((message, f"❌ Error: {str(e)}"))
        return history, {}


def display_agent_reasoning(metadata: Dict) -> str:
    """Format agent reasoning."""
    if not metadata:
        return "<div class='status-card'>Waiting for query...</div>"
    
    tools_used = metadata.get('tools_used', [])
    agent_reasoning = metadata.get('agent_reasoning', [])
    
    output = '<div class="status-card">'
    output += '<h3>🤖 Agent Reasoning</h3>'
    
    if tools_used:
        output += '<p><strong>Tools Used:</strong> '
        for tool in tools_used:
            output += f'<span style="background: #667eea; color: white; padding: 0.25rem 0.5rem; border-radius: 4px; margin: 0.25rem;">{tool}</span> '
        output += '</p>'
    
    if agent_reasoning:
        output += '<div style="margin-top: 1rem;">'
        for i, step in enumerate(agent_reasoning, 1):
            tool = step.get('tool', 'Unknown')
            tool_input = step.get('input', '')
            tool_output = step.get('output', '')
            
            output += f'<div style="margin: 0.5rem 0; padding: 0.75rem; background: white; border-radius: 4px; border-left: 3px solid #667eea;">'
            output += f'<strong>Step {i}: {tool}</strong><br>'
            output += f'<em>Input:</em> {tool_input}<br>'
            output += f'<em>Output:</em> {tool_output}'
            output += '</div>'
        output += '</div>'
    
    output += '</div>'
    return output


def handle_feedback(conversation_id: int, feedback_type: str):
    """Handle user feedback."""
    if not rag_system:
        return "<div class='status-card status-error'>System not initialized</div>"
    
    if conversation_id is not None and conversation_id >= 0:
        rag_system.add_feedback(conversation_id, feedback_type)
        emoji = "👍" if feedback_type == "positive" else "👎"
        return f"""
        <div class='status-card status-success'>
            <strong>{emoji} Feedback recorded!</strong>
            <p>Thank you for helping improve the system.</p>
        </div>
        """
    
    return "<div class='status-card'>No active conversation</div>"


def export_logs_ui():
    """Export logs."""
    if not rag_system:
        return "<div class='status-card status-error'>System not initialized</div>"
    
    success = rag_system.export_logs()
    if success:
        return f"""
        <div class='status-card status-success'>
            ✅ Logs exported to interaction_logs.json
            <br><small>Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>
        </div>
        """
    return "<div class='status-card status-error'>❌ Export failed</div>"


def clear_memory_ui():
    """Clear memory."""
    if not rag_system:
        return [], "<div class='status-card status-error'>System not initialized</div>"
    
    rag_system.clear_memory()
    return [], "<div class='status-card'>🗑️ Memory cleared successfully</div>"


def get_conversation_stats() -> str:
    """Get conversation statistics."""
    if not rag_system:
        return "<div class='status-card'>System not initialized</div>"
    
    history = rag_system.get_conversation_history(num_interactions=100)
    
    if not history:
        return "<div class='status-card'>No conversations yet</div>"
    
    total = len(history)
    with_feedback = sum(1 for h in history if h.feedback)
    positive = sum(1 for h in history if h.feedback == 'positive')
    negative = sum(1 for h in history if h.feedback == 'negative')
    
    all_tools = []
    for h in history:
        all_tools.extend(h.tools_used)
    tool_counts = Counter(all_tools)
    
    satisfaction_rate = (positive / with_feedback * 100) if with_feedback > 0 else 0
    
    output = '<div class="status-card">'
    output += '<h2>📊 Conversation Statistics</h2>'
    
    # Main metrics
    output += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin: 1rem 0;">'
    
    output += f'''
    <div style="padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; color: white; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold;">{total}</div>
        <div style="font-size: 0.9rem;">Total Conversations</div>
    </div>
    '''
    
    output += f'''
    <div style="padding: 1rem; background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-radius: 8px; color: white; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold;">{positive}</div>
        <div style="font-size: 0.9rem;">👍 Positive</div>
    </div>
    '''
    
    output += f'''
    <div style="padding: 1rem; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); border-radius: 8px; color: white; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold;">{len(tool_counts)}</div>
        <div style="font-size: 0.9rem;">🛠️ Tools Used</div>
    </div>
    '''
    
    output += f'''
    <div style="padding: 1rem; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); border-radius: 8px; color: white; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold;">{satisfaction_rate:.0f}%</div>
        <div style="font-size: 0.9rem;">Satisfaction</div>
    </div>
    '''
    
    output += '</div>'
    
    # Tool Usage
    if tool_counts:
        output += '<div style="margin-top: 1rem; padding: 1rem; background: white; border-radius: 8px;">'
        output += '<h3>🛠️ Tool Usage Breakdown:</h3><ul>'
        for tool, count in tool_counts.most_common():
            output += f'<li><strong>{tool}:</strong> {count} times</li>'
        output += '</ul></div>'
    
    output += '</div>'
    return output


# ═══════════════════════════════════════════════════════════════════
# 🚀 Create Gradio Interface
# ═══════════════════════════════════════════════════════════════════

def create_ui():
    """Create the complete Gradio interface."""
    
    with gr.Blocks(css=CUSTOM_CSS, title="🤖 Agentic RAG System") as demo:
        
        # Header
        gr.HTML("""
        <div class="app-header">
            <h1>🤖 Enhanced Agentic RAG System v4.0</h1>
            <p>Multi-format document support • Secure API management • Modern LangChain</p>
            <div style="margin-top: 0.5rem;">
                <span style="background: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 12px; margin: 0.25rem; display: inline-block;">📄 PDF</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 12px; margin: 0.25rem; display: inline-block;">📝 DOCX</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 12px; margin: 0.25rem; display: inline-block;">📃 TXT</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 12px; margin: 0.25rem; display: inline-block;">📡 PCAP</span>
            </div>
        </div>
        """)
        
        # API Key Setup Section (initially visible)
        with gr.Group(visible=True) as setup_section:
            gr.Markdown("## 🔐 API Key Configuration")
            gr.Markdown("""
            **Welcome!** To use this system, you need to provide your API keys.
            
            - **OpenAI API Key** (Required): Get from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
            - **Tavily API Key** (Optional): Get from [https://tavily.com](https://tavily.com) for web search capability
            
            🔒 Your keys are stored securely in memory only and are never saved to disk.
            """)
            
            with gr.Row():
                openai_key_input = gr.Textbox(
                    label="OpenAI API Key (Required)",
                    type="password",
                    placeholder="sk-...",
                    scale=3,
                    info="Your OpenAI API key for GPT-3.5-turbo and embeddings"
                )
                tavily_key_input = gr.Textbox(
                    label="Tavily API Key (Optional)",
                    type="password",
                    placeholder="tvly-...",
                    scale=3,
                    info="Optional: Enables real-time web search"
                )
            
            init_button = gr.Button("🚀 Initialize System", variant="primary", size="lg")
            init_status = gr.HTML()
        
        # Main Application (initially hidden)
        with gr.Group(visible=False) as main_app:
            
            with gr.Tabs():
                # Document Upload Tab
                with gr.Tab("📄 Document Upload"):
                    gr.Markdown("## 📤 Upload Your Document")
                    gr.Markdown("""
                    **Supported Formats:**
                    - **PDF** (.pdf) - Text-based PDF documents
                    - **Word** (.docx, .doc) - Microsoft Word documents
                    - **Text** (.txt) - Plain text files with any encoding
                    - **PCAP** (.pcap, .pcapng) - Network packet capture files for analysis
                    """)
                    
                    with gr.Row():
                        with gr.Column(scale=2):
                            file_input = gr.File(
                                label="📂 Select File",
                                file_types=[".pdf", ".docx", ".doc", ".txt", ".pcap", ".pcapng"]
                            )
                        with gr.Column(scale=1):
                            process_btn = gr.Button("🔄 Process Document", variant="primary", size="lg")
                    
                    doc_status = gr.HTML()
                    
                    process_btn.click(
                        fn=process_document_ui,
                        inputs=[file_input],
                        outputs=[doc_status]
                    )
                
                # Chat Tab
                with gr.Tab("💬 Interactive Chat"):
                    gr.Markdown("## 💬 Chat with Your Documents")
                    gr.Markdown("Ask questions and watch the AI agent reason through its response in real-time.")
                    
                    with gr.Row():
                        with gr.Column(scale=3):
                            chatbot = gr.Chatbot(
                                label="🤖 Conversation",
                                height=500,
                                show_copy_button=True,
                                bubble_full_width=False
                            )
                            
                            with gr.Row():
                                msg_input = gr.Textbox(
                                    label="Your Question",
                                    placeholder="Ask anything... (e.g., 'What is the main topic?', 'Summarize the document')",
                                    lines=2,
                                    scale=5
                                )
                                send_btn = gr.Button("📤 Send", variant="primary", scale=1)
                            
                            with gr.Row():
                                clear_btn = gr.Button("🗑️ Clear Chat", size="sm")
                                load_history_btn = gr.Button("📂 Load History", size="sm")
                                export_btn = gr.Button("📥 Export Logs", size="sm")
                            
                            gr.Markdown("### 📊 Rate the Response")
                            with gr.Row():
                                thumbs_up = gr.Button("👍 Helpful", size="sm")
                                thumbs_down = gr.Button("👎 Not Helpful", size="sm")
                            
                            feedback_status = gr.HTML()
                        
                        with gr.Column(scale=2):
                            gr.Markdown("### 🤖 Agent Reasoning")
                            reasoning_output = gr.HTML(value="<div class='status-card'>Waiting for query...</div>")
                    
                    # Hidden states
                    conv_id_state = gr.State(value=-1)
                    metadata_state = gr.State(value={})
                    
                    # Example questions
                    gr.Markdown("""
                    **💡 Example Questions:**
                    - "What is this document about?"
                    - "Summarize the key points"
                    - "Calculate 15% of 2500"
                    - "What are the main findings in the document?"
                    """)
                    
                    # Chat interactions
                    def chat_wrapper(message, history):
                        new_history, metadata = chat_ui(message, history)
                        reasoning = display_agent_reasoning(metadata)
                        conv_id = metadata.get('conversation_id', -1)
                        return new_history, reasoning, conv_id, metadata
                    
                    send_btn.click(
                        fn=chat_wrapper,
                        inputs=[msg_input, chatbot],
                        outputs=[chatbot, reasoning_output, conv_id_state, metadata_state]
                    ).then(lambda: "", outputs=[msg_input])
                    
                    msg_input.submit(
                        fn=chat_wrapper,
                        inputs=[msg_input, chatbot],
                        outputs=[chatbot, reasoning_output, conv_id_state, metadata_state]
                    ).then(lambda: "", outputs=[msg_input])
                    
                    # Feedback
                    thumbs_up.click(
                        fn=lambda cid: handle_feedback(cid, 'positive'),
                        inputs=[conv_id_state],
                        outputs=[feedback_status]
                    )
                    
                    thumbs_down.click(
                        fn=lambda cid: handle_feedback(cid, 'negative'),
                        inputs=[conv_id_state],
                        outputs=[feedback_status]
                    )
                    
                    # Utility buttons
                    clear_btn.click(
                        fn=clear_memory_ui,
                        outputs=[chatbot, feedback_status]
                    )
                    
                    export_btn.click(
                        fn=export_logs_ui,
                        outputs=[feedback_status]
                    )
                    
                    load_history_btn.click(
                        fn=load_conversation_history,
                        outputs=[chatbot, feedback_status]
                    )
                
                # Statistics Tab
                with gr.Tab("📊 Statistics"):
                    gr.Markdown("## 📈 System Statistics & Analytics")
                    
                    refresh_stats_btn = gr.Button("🔄 Refresh Statistics", variant="primary", size="lg")
                    stats_output = gr.HTML(value="<div class='status-card'>Click 'Refresh Statistics' to load data</div>")
                    
                    refresh_stats_btn.click(
                        fn=get_conversation_stats,
                        outputs=[stats_output]
                    )
                
                # Help Tab
                with gr.Tab("❓ Help"):
                    gr.Markdown("""
                    ## 🎯 User Guide
                    
                    ### Quick Start (3 Steps)
                    
                    1. **Initialize System**: Enter your OpenAI API key in the setup screen
                    2. **Upload Document**: Go to "Document Upload" tab and process your file
                    3. **Start Chatting**: Ask questions in the "Interactive Chat" tab
                    
                    ### Supported File Formats
                    
                    | Format | Extension | Use Case |
                    |--------|-----------|----------|
                    | **PDF** | .pdf | Research papers, reports, manuals |
                    | **Word** | .docx, .doc | Business documents, proposals |
                    | **Text** | .txt | Code, logs, plain text |
                    | **PCAP** | .pcap, .pcapng | Network traffic analysis |
                    
                    ### Available Tools
                    
                    The AI agent automatically selects from these tools:
                    
                    - **DocumentSearch** 📚 - Search uploaded documents
                    - **Calculator** 🧮 - Perform mathematical calculations
                    - **TextAnalysis** 📝 - Analyze text for keywords, word count
                    - **DataFormatter** 📊 - Format lists and bullet points
                    - **WebSearch** 🌐 - Search the internet (requires Tavily API key)
                    - **Wikipedia** 📖 - Look up factual information
                    
                    ### Features
                    
                    - **🧠 Intelligent Agent**: Uses ReAct (Reasoning + Acting) pattern
                    - **💾 Persistent Memory**: All conversations automatically saved
                    - **🔍 Transparent Reasoning**: See exactly how the agent thinks
                    - **👍👎 Feedback System**: Rate responses to improve quality
                    - **📊 Analytics**: Track usage patterns and satisfaction
                    - **🔐 Secure**: API keys stored in memory only
                    
                    ### Tips for Best Results
                    
                    - Be specific in your questions
                    - Reference the document explicitly when needed
                    - Use follow-up questions to dig deeper
                    - Provide feedback to help the system learn
                    - Check agent reasoning to understand the process
                    
                    ### Troubleshooting
                    
                    **Problem**: "System not initialized"
                    - **Solution**: Go back to setup and enter your API key
                    
                    **Problem**: "No document uploaded"
                    - **Solution**: Upload a document in the "Document Upload" tab first
                    
                    **Problem**: Slow responses
                    - **Solution**: Large documents take longer to process
                    
                    **Problem**: API errors
                    - **Solution**: Check your API key is valid and has credits
                    
                    ### Getting API Keys
                    
                    **OpenAI API Key** (Required):
                    1. Visit [https://platform.openai.com](https://platform.openai.com)
                    2. Sign up or log in
                    3. Go to API Keys section
                    4. Create new secret key
                    5. Copy and paste into the setup screen
                    
                    **Tavily API Key** (Optional):
                    1. Visit [https://tavily.com](https://tavily.com)
                    2. Sign up for an account
                    3. Get your API key from dashboard
                    4. Enter in setup screen for web search capability
                    
                    ### Privacy & Security
                    
                    - API keys are stored in memory only
                    - Keys are never written to disk
                    - Conversations saved locally in JSON format
                    - No data sent to third parties except OpenAI/Tavily APIs
                    
                    ### Support
                    
                    For issues, check the logs in `agentic_rag.log` or export conversation logs for analysis.
                    """)
        
        # Initialize system
        init_button.click(
            fn=initialize_system,
            inputs=[openai_key_input, tavily_key_input],
            outputs=[init_status, main_app, setup_section]
        )
        
        gr.Markdown("""
        ---
        <div style="text-align: center; color: #666;">
            <p><strong>Enhanced Agentic RAG System v4.0</strong></p>
            <p>Built with LangChain, FAISS, OpenAI, Gradio</p>
            <p style="font-size: 0.8rem;">Production-ready • Secure • Multi-format • Modern Architecture</p>
        </div>
        """)
    
    return demo


# ═══════════════════════════════════════════════════════════════════
# 🚀 Main Entry Point
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print('=' * 60)
    print('🚀 Enhanced Agentic RAG System v4.0')
    print('=' * 60)
    print('✅ Multi-format support: PDF, DOCX, TXT, PCAP')
    print('✅ Secure API key entry')
    print('✅ Modern LangChain implementation')
    print('✅ Enhanced error handling')
    print('✅ JSON-based persistence')
    print('=' * 60)
    
    demo = create_ui()
    
    demo.launch(
        server_name='0.0.0.0',
        server_port=7860,
        share=False,  # Set to True for public URL
        show_error=True
    )
    
    print('\n✅ System launched successfully!')
    print('📱 Access at: http://localhost:7860')

