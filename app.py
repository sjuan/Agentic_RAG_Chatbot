#!/usr/bin/env python3
"""
🤖 Enhanced Agentic RAG System - Hugging Face Spaces Deployment
================================================================

This is the main entry point for Hugging Face Spaces.
The app uses Gradio for the web interface and supports multiple document formats.

Author: Enhanced Agentic RAG Team
Version: 4.0
Deployed on: Hugging Face Spaces
"""

import os
import sys

# Set up logging before other imports
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info("🚀 Starting Enhanced Agentic RAG System on Hugging Face Spaces...")

# Import the UI
try:
    from gradio_ui import create_ui
    logger.info("✅ Successfully imported UI components")
except ImportError as e:
    logger.error(f"❌ Failed to import UI: {e}")
    raise

# Create the Gradio interface
try:
    demo = create_ui()
    logger.info("✅ Gradio interface created successfully")
except Exception as e:
    logger.error(f"❌ Failed to create UI: {e}")
    raise

# Launch the app
if __name__ == "__main__":
    logger.info("🌐 Launching Gradio app on Hugging Face Spaces...")
    
    # Hugging Face Spaces configuration - minimal parameters for compatibility
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
    
    logger.info("✅ App launched successfully!")

