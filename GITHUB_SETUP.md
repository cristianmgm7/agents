# GitHub Agent Setup

## Prerequisites

1. **GitHub Personal Access Token**: Create a fine-grained personal access token at [https://github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new)

   Required permissions for full functionality:
   - **Repository permissions**:
     - Contents: Read and write
     - Issues: Read and write
     - Pull requests: Read and write
     - Metadata: Read
   - **Organization permissions** (if using org repos):
     - Members: Read
   - **Account permissions**:
     - Profile: Read

## Environment Setup

1. Create a `.env` file in the project root:
   ```
   GITHUB_TOKEN=your_github_personal_access_token_here
   ```

2. Replace `your_github_personal_access_token_here` with your actual GitHub token.

## Available GitHub MCP Tools

The GitHub agent includes the following toolsets:

- **repos**: Repository management and code browsing
- **issues**: Issue creation, updates, and management
- **pull_requests**: Pull request operations and reviews
- **code_security**: Security findings and Dependabot alerts
- **dependabot**: Dependency management
- **discussions**: GitHub Discussions
- **projects**: Project boards and organization
- **labels**: Issue and PR labels
- **notifications**: GitHub notifications
- **users**: User profile and information
- **orgs**: Organization management
- **stargazers**: Repository stargazers

## Usage Examples

Once set up, you can ask the GitHub agent to:

- "Show me the contents of the README.md file in repository owner/repo"
- "Create an issue in my-repo about fixing the login bug"
- "Review the pull request #123 in organization/repo"
- "List all open issues in my project"
- "Analyze the security vulnerabilities in repo-owner/repo"

## Security Note

Keep your `.env` file secure and never commit it to version control. The GitHub token provides access to your repositories, so treat it like a password.
