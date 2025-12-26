import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

# Load environment variables from .env file
load_dotenv()

# Get GitHub token from environment variable
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is required. Please add it to your .env file.")

# Create GitHub agent with MCP tools
github_agent = Agent(
    model='gemini-2.5-flash',
    name='github_agent',
    description='A GitHub assistant powered by MCP tools for repository management, issues, and pull requests.',
    instruction='''You are a helpful GitHub assistant that can help users with:

    Repository Management:
    - Browse and query code files across repositories you have access to
    - Search files and analyze code patterns
    - Understand project structure and dependencies

    Issue & PR Management:
    - Create, update, and manage issues and pull requests
    - Help triage bugs and review code changes
    - Maintain project boards and track progress

    Code Analysis:
    - Examine security findings and Dependabot alerts
    - Analyze code patterns and provide insights
    - Review code changes and suggest improvements

    Always be helpful, accurate, and provide clear explanations of your actions.
    When using tools, explain what you're doing and why.''',
    tools=[
        McpToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "repos,issues,pull_requests,code_security,dependabot,discussions,projects,labels,notifications,users,orgs,stargazers",
                    "X-MCP-Readonly": "false"
                },
            ),
        )
    ],
)
