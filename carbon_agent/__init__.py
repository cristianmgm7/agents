from . import agent
from . import search_agent

# Conditionally import github_agent if token is available
try:
    from . import github_agent
    github_agent_available = True
except ValueError as e:
    if "GITHUB_TOKEN" in str(e):
        github_agent_available = False
    else:
        raise

# Conditionally import carbon_voice_agent if API key is available
try:
    from . import carbon_voice_agent
    carbon_voice_agent_available = True
except ValueError as e:
    if "CARBON_VOICE_API_KEY" in str(e):
        carbon_voice_agent_available = False
    else:
        raise
