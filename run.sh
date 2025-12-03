#!/bin/bash

# Enhanced Agentic RAG System v4.0 - Startup Script

echo "=================================="
echo "🤖 Enhanced Agentic RAG System"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "📦 Checking dependencies..."
python3 -c "import langchain" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Dependencies not installed!"
    echo "Installing requirements..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
fi

echo "✅ Dependencies installed"
echo ""

# Create necessary directories
mkdir -p memory_store
mkdir -p faiss_index

echo "🚀 Starting Agentic RAG System..."
echo ""
echo "📱 The system will be available at:"
echo "   http://localhost:7860"
echo ""
echo "🔐 You will need to enter your API keys on first launch"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=================================="
echo ""

# Run the application
python3 gradio_ui.py

# Cleanup on exit
echo ""
echo "👋 Goodbye!"

