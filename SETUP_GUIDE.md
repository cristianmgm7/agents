# Multi-Agent System Setup Guide

## Overview

This project implements a hierarchical multi-agent system with:
- **Root Agent**: Intelligent orchestrator that coordinates sub-agents
- **GitHub Agent**: Repository management and code analysis (optional)
- **Market Analyzer**: Professional financial market analysis

## Environment Setup

Create a `.env` file in the project root:

```bash
# GitHub Agent (Optional)
GITHUB_TOKEN=your_github_personal_access_token_here

# Carbon Voice Agent (Optional)
CARBON_VOICE_API_KEY=your_carbon_voice_api_key_here

# Google Search Tool (Optional - requires Google Cloud setup)
GOOGLE_CLOUD_API_KEY=your_google_cloud_api_key_here
```

## Agent Configuration Status

### ✅ Root Agent (Always Available)
- Intelligent orchestrator using `gemini-1.5-flash`
- Coordinates between sub-agents via `transfer_to_agent()` calls

### ⚠️ GitHub Agent (Optional)
**Setup Required:** Add `GITHUB_TOKEN` to `.env`

Features when enabled:
- Repository management and code browsing
- Issue and pull request operations
- Code security analysis and Dependabot alerts
- Project board management

### ⚠️ Carbon Voice Agent (Optional)
**Setup Required:** Add `CARBON_VOICE_API_KEY` to `.env`

Features when enabled:
- Message management (conversation, direct, voice memos)
- User directory and search operations
- Conversation thread management
- Folder organization and message archival
- Workspace statistics and AI actions
- Professional communication assistance

### ⚠️ Market Analyzer (Partially Available)
**Current Status:** Provides analysis based on knowledge (search tool disabled)

**Optional Enhancement:** Enable Google Search tool with `GOOGLE_CLOUD_API_KEY`

Features:
- Stock market trend analysis
- Company valuation assessment
- Industry competitive analysis
- Economic indicator evaluation
- Risk assessment and portfolio strategy

## Quick Start

1. **Basic Setup** (No external APIs required):
   ```bash
   # The system works immediately with knowledge-based analysis
   ```

2. **GitHub Integration**:
   ```bash
   # Add to .env file
   GITHUB_TOKEN=your_github_token_here
   ```

3. **Enhanced Market Analysis** (Advanced):
   ```bash
   # Requires Google Cloud setup
   GOOGLE_CLOUD_API_KEY=your_api_key_here
   ```

## Usage Examples

### Basic Usage (Always Works)
```python
# Root agent orchestration
"Analyze market trends and create a GitHub issue with findings"
"Research investment opportunities in renewable energy"
```

### Multi-Agent Coordination (When Multiple Agents Enabled)
```python
# Cross-platform workflows
"Analyze market data, create GitHub issues, and notify team via Carbon Voice"
"Review codebase, generate reports, and organize communications"
```

### With GitHub Token
```python
# GitHub operations
"Show me open issues in my repository"
"Create an issue about the market analysis findings"
```

### With Carbon Voice API Key
```python
# Messaging and communication
"Send a message to the team about the project update"
"Create a voice memo for the meeting notes"
"Organize my messages into project folders"
```

### With Google Search (Advanced)
```python
# Real-time market data
"Search for current Tesla stock performance"
"Find latest economic indicators"
```

## Troubleshooting

### 400 INVALID_ARGUMENT Error
- **Cause**: Model doesn't support function calling
- **Fixed**: Changed all models to `gemini-1.5-flash`

### Google Search Tool Issues
- **Cause**: Requires Google Cloud authentication
- **Solution**: Currently disabled - agent works with knowledge-based analysis
- **To Enable**: Set up Google Cloud API key and uncomment the tool

### GitHub Agent Not Available
- **Cause**: Missing `GITHUB_TOKEN`
- **Solution**: Add token to `.env` or use without GitHub features

## Security Notes

- Keep `.env` file secure and never commit to version control
- GitHub tokens provide repository access - treat as passwords
- Google Cloud API keys should be restricted to specific services

## Architecture

```
Root Agent (Orchestrator)
├── Market Analyzer (Financial Analysis)
├── GitHub Agent (Repository Management - optional)
└── Carbon Voice Agent (Communication Platform - optional)
```

The system gracefully degrades when optional components are unavailable, ensuring core functionality always works.
