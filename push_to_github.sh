#!/bin/bash

# Script to push Agentic RAG Chatbot to GitHub
# Repository: https://github.com/sjuan/Agentic_RAG_Chatbot

echo "=================================================="
echo "📤 Pushing Agentic RAG Chatbot to GitHub"
echo "=================================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed!"
    echo "Install it with: sudo apt-get install git"
    exit 1
fi

echo "✅ Git found: $(git --version)"
echo ""

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already initialized"
fi

echo ""

# Configure git (update these with your info if needed)
echo "🔧 Configuring git..."
read -p "Enter your GitHub username (default: sjuan): " username
username=${username:-sjuan}

read -p "Enter your email: " email

git config user.name "$username"
git config user.email "$email"

echo "✅ Git configured"
echo ""

# Add all files
echo "📁 Adding files to git..."
git add .
echo "✅ Files added"
echo ""

# Show status
echo "📊 Git status:"
git status
echo ""

# Commit
read -p "Enter commit message (default: 'Initial commit - Enhanced Agentic RAG System v4.0'): " commit_msg
commit_msg=${commit_msg:-"Initial commit - Enhanced Agentic RAG System v4.0"}

echo "💾 Committing changes..."
git commit -m "$commit_msg"
echo "✅ Changes committed"
echo ""

# Add remote if not exists
if ! git remote | grep -q origin; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/sjuan/Agentic_RAG_Chatbot.git
    echo "✅ Remote added"
else
    echo "✅ Remote already exists"
fi

echo ""
echo "🌿 Setting main branch..."
git branch -M main
echo ""

# Push to GitHub
echo "🚀 Pushing to GitHub..."
echo "⚠️  You may be asked for your GitHub credentials"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "✅ SUCCESS! Project pushed to GitHub!"
    echo "=================================================="
    echo ""
    echo "🌐 View your repository at:"
    echo "   https://github.com/sjuan/Agentic_RAG_Chatbot"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Go to your repository on GitHub"
    echo "   2. Add a description and topics"
    echo "   3. Check that all files are there"
    echo "   4. Share your project!"
    echo ""
else
    echo ""
    echo "=================================================="
    echo "❌ Push failed!"
    echo "=================================================="
    echo ""
    echo "Common issues:"
    echo "1. Authentication failed"
    echo "   - Use a Personal Access Token instead of password"
    echo "   - Create one at: https://github.com/settings/tokens"
    echo ""
    echo "2. Repository doesn't exist"
    echo "   - Make sure the repo exists on GitHub"
    echo "   - URL: https://github.com/sjuan/Agentic_RAG_Chatbot"
    echo ""
    echo "3. Permission denied"
    echo "   - Make sure you have write access to the repository"
    echo ""
fi

