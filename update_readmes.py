files_content = {
    "beginner-path/README.md": """
# Beginner AI Path

This section is designed for people completely new to AI.

## Topics
- AI basics
- Prompt engineering
- AI tools
- AI productivity
- Automation basics

No advanced coding knowledge required.
""",

    "ai-security/README.md": """
# AI Security

This section covers:
- LLM Security
- AI Threat Modeling
- AI Governance
- AI Red Teaming
- Identity Security
- Cloud Security
""",

    "healthcare-ai/README.md": """
# Healthcare AI

This section covers:
- AI for clinicians
- AI research workflows
- Healthcare automation
- Compliance awareness
""",

    "claude-skills/README.md": """
# Claude Skills

This section includes:
- Reusable AI workflows
- Prompt systems
- Automation templates
- AI workflow libraries
""",

    "prompts/README.md": """
# Prompts

This section provides:
- Beginner prompts
- Research prompts
- Automation prompts
- Security prompts
""",

    "workflows/README.md": """
# Workflows

This section covers:
- AI agents
- GitHub workflows
- n8n automation
- AI automation systems
""",

    "research/README.md": """
# Research

This section includes:
- Weekly AI updates
- AI tools
- AI papers
- Startups
- Industry trends
""",

    "resources/README.md": """
# Resources

This section provides:
- Videos
- Newsletters
- Certifications
- Useful websites
- Learning links
""",

    "templates/README.md": """
# Templates

This section includes:
- Skill templates
- Prompt templates
- Workflow templates
- Research templates
"""
}

for file_path, content in files_content.items():
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content.strip())

print("README files updated successfully!")