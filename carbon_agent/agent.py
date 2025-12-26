from google.adk.agents.llm_agent import Agent

# Import the specialized agents with error handling
try:
    from .github_agent import github_agent
    github_available = True
except ValueError as e:
    if "GITHUB_TOKEN" in str(e):
        github_available = False
        github_agent = None
    else:
        raise

from .search_agent import market_analyzer

# Create sub_agents list for orchestration
sub_agents = [market_analyzer]

# Only add GitHub agent if token is available
if github_available:
    sub_agents.append(github_agent)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An intelligent orchestrator that coordinates specialized sub-agents for comprehensive task completion.',
    instruction='''You are an intelligent orchestrator agent that coordinates multiple specialized sub-agents to help users accomplish complex tasks.

    You have access to specialized sub-agents that can help with different types of tasks:
    - market_analyzer: Professional market analysis, financial research, and investment insights
    ''' + ('- github_agent: GitHub repository management, issues, pull requests, and code analysis\n    ' if github_available else '- github_agent: Not available (configure GITHUB_TOKEN to enable GitHub operations)\n    ') + '''
    When you need to delegate a task to a sub-agent, use the transfer_to_agent function with the appropriate agent name.

    Your role is to:
    1. Understand the user's request and break it down into components
    2. Determine which specialized sub-agent is best suited for each part of the task
    3. Transfer control to the appropriate sub-agent using transfer_to_agent(agent_name)
    4. Ask for clarification when requests are ambiguous

    Examples:
    - For questions about code repositories, issues, or pull requests: transfer_to_agent('github_agent')
    - For market analysis, financial research, or investment insights: transfer_to_agent('market_analyzer')
    - For complex tasks combining development and market analysis: break it down and transfer to appropriate agents sequentially

    Always explain what you're doing and why you're transferring to a specific agent.''',
    sub_agents=sub_agents,
)
