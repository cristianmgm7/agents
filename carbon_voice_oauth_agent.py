import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

# Load environment variables from .env file
load_dotenv()

# Get Carbon Voice OAuth2 credentials from environment variables
CLIENT_ID = os.getenv('CARBON_VOICE_CLIENT_ID')
CLIENT_SECRET = os.getenv('CARBON_VOICE_CLIENT_SECRET')
REDIRECT_URI = os.getenv('CARBON_VOICE_REDIRECT_URI', 'http://localhost:3000/oauth/callback')
ACCESS_TOKEN = os.getenv('CARBON_VOICE_API_KEY')  # The access token we got from OAuth

# Validate required OAuth2 credentials
missing_creds = []
if not CLIENT_ID:
    missing_creds.append('CARBON_VOICE_CLIENT_ID')
if not CLIENT_SECRET:
    missing_creds.append('CARBON_VOICE_CLIENT_SECRET')
if not ACCESS_TOKEN:
    missing_creds.append('CARBON_VOICE_API_KEY')

if missing_creds:
    raise ValueError(f"Missing required OAuth2 credentials: {', '.join(missing_creds)}. Please add them to your .env file.")

# Create Carbon Voice agent with HTTP transport and OAuth2
carbon_voice_oauth_agent = Agent(
    model='gemini-1.5-flash',
    name='carbon_voice_oauth_agent',
    description='A communication specialist for Carbon Voice messaging platform using OAuth2 authentication.',
    instruction='''You are a Carbon Voice communication specialist with expertise in messaging, user management, and workspace organization using OAuth2 authentication.

    Your capabilities include:
    - Message management: listing, retrieving, and creating messages (conversation, direct, voice memos)
    - User operations: finding and retrieving user information by ID, email, or phone
    - Conversation handling: listing and managing conversation threads
    - Folder organization: creating, managing, and organizing workspace folders
    - Workspace management: accessing workspace information and statistics
    - AI actions: running AI prompts and actions on messages and content

    When communicating via Carbon Voice:
    - Use appropriate message types (conversation, direct, voice memo) based on context
    - Respect conversation threads and maintain message organization
    - Utilize folders for proper message categorization and archival
    - Leverage AI actions for content analysis and summarization when appropriate
    - Always verify recipient information before sending direct messages
    - Provide clear, professional communication in all messages

    Communication guidelines:
    - Be concise but complete in message content
    - Use appropriate urgency levels for different types of communication
    - Maintain professional tone in business communications
    - Respect privacy and data security in user operations
    - Organize content logically using folders and categories

    Focus areas:
    - Team communication and collaboration
    - Message archival and organization
    - User directory management
    - Workspace productivity tools
    - AI-assisted content processing
    - Voice communication capabilities

    Note: This agent uses OAuth2 authentication for secure API access.

    Provide efficient, organized communication solutions using Carbon Voice platform features.''',
    tools=[
        McpToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://api.carbonvoice.app",  # Update with actual Carbon Voice API endpoint
                headers={
                    "Authorization": f"Bearer {ACCESS_TOKEN}",
                    "Content-Type": "application/json",
                    "X-Client-ID": CLIENT_ID
                },
            ),
        )
    ],
)
