# Agentic Workflow Documentation

Use this guide when designing AI systems that can call tools or complete multi-step tasks.

## Minimum Documentation

Every agentic workflow should document:

- Goal
- User group
- Tools available
- Data available
- Permissions
- Actions the agent can take
- Actions requiring approval
- Logs and monitoring
- Failure modes
- Rollback plan

## Example Workflow

```markdown
# Research Agent Workflow

## Goal
Find, summarize, and compare AI security resources.

## Tools
- Web search
- Document reader
- Markdown writer

## Human Approval Required For
- Publishing results
- Sending emails
- Updating shared documents

## Risks
- Inaccurate summaries
- Source quality problems
- Prompt injection in webpages

## Controls
- Cite sources
- Prefer primary sources
- Human review before publishing
```

