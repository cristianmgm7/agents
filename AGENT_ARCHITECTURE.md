# Agent Architecture Overview

## Multi-Agent System Structure

This project implements a hierarchical multi-agent system using Google Agent Development Kit (ADK):

### 1. Root Agent (Orchestrator)
**File:** `carbon_agent/agent.py`
- **Role:** Intelligent coordinator that uses LLM-driven delegation to route tasks to sub-agents
- **Capabilities:**
  - Analyzes user requests and breaks them down into components
  - Uses `transfer_to_agent()` calls to delegate to specialized sub-agents
  - Maintains conversation flow across agent transfers
  - Provides unified interface to multiple specialized agents
- **Sub-Agents:** market_analyzer (always available), github_agent (conditional on GITHUB_TOKEN)

### 2. GitHub Agent (Sub-Agent)
**File:** `carbon_agent/github_agent.py`
- **Role:** GitHub operations sub-agent
- **Capabilities:**
  - Repository management and code browsing
  - Issue and pull request management
  - Code security analysis and Dependabot alerts
  - Project board and organization management
- **Integration:** Full GitHub MCP Server with comprehensive toolsets
- **Requirements:** `GITHUB_TOKEN` environment variable

### 3. Market Analyzer (Sub-Agent)
**File:** `carbon_agent/search_agent.py`
- **Role:** Professional market analysis and financial research sub-agent
- **Capabilities:**
  - Stock market analysis and valuation
  - Financial research and company fundamentals
  - Industry trend analysis and competitive landscape
  - Economic indicator monitoring and investment insights
  - Risk assessment and portfolio strategy analysis
- **Tools:** GoogleSearchTool for comprehensive market data and financial information

## Architecture Benefits

1. **Modularity:** Each agent has a focused responsibility
2. **Scalability:** Easy to add new specialized agents
3. **Flexibility:** Root agent can coordinate complex workflows
4. **Graceful Degradation:** System works even if some agents are unavailable
5. **Error Handling:** Conditional imports prevent crashes from missing configurations

## How Delegation Works

### LLM-Driven Transfer Mechanism
1. **Root Agent Analysis:** Receives user request and analyzes it using LLM
2. **Decision Making:** Determines which sub-agent is best suited for the task
3. **Transfer Call:** Generates `transfer_to_agent('sub_agent_name')` function call
4. **Framework Routing:** ADK's AutoFlow intercepts the call and transfers execution
5. **Sub-Agent Execution:** Target sub-agent handles the specialized task
6. **Control Return:** Execution returns to root agent or completes the conversation

### Agent Hierarchy
```
root_agent (Orchestrator)
├── market_analyzer (Sub-Agent - always available)
└── github_agent (Sub-Agent - conditional on GITHUB_TOKEN)
```

## Usage Examples

### Simple Tasks
- *"Analyze Tesla's stock performance this quarter"* → `transfer_to_agent('market_analyzer')`
- *"Show me open issues in my repo"* → `transfer_to_agent('github_agent')`

### Complex Tasks
- *"Analyze the AI semiconductor market and create a GitHub issue with findings"*
  → Root agent coordinates: market_analyzer (research) → github_agent (create issue)

- *"Evaluate cybersecurity risks in my codebase and research market solutions"*
  → Root agent coordinates: github_agent (scan) → market_analyzer (market research)

## Configuration

### Required Environment Variables
- `GITHUB_TOKEN`: GitHub Personal Access Token (optional - system works without it)

### Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment: Create `.env` file with tokens
3. Run agents: Use ADK web interface or deploy to production

## Technical Implementation

- **ADK Framework:** Uses Google Agent Development Kit for agent management
- **MCP Integration:** GitHub agent uses Model Context Protocol for tool integration
- **Sub-Agent Pattern:** Root agent uses `sub_agents` parameter for proper hierarchical agent relationships
- **LLM-Driven Delegation:** Uses ADK's built-in `transfer_to_agent` mechanism for intelligent routing
- **Conditional Loading:** Graceful handling of optional sub-agents (GitHub token dependency)
- **Error Handling:** Comprehensive error handling for missing configurations
