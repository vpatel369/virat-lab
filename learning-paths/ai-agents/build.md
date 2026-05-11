# Build

## Portfolio Project: Governed Research Agent

Build a research workflow that collects sources, summarizes them, creates a draft, and requires human approval before publishing.

## Required Artifacts

- Agent goal
- Tool list
- Permission matrix
- Prompt or workflow instructions
- Guardrail plan
- Trace/logging plan
- Risk review

## Architecture

```text
User Goal -> Planner -> Research Tool -> Summarizer -> Draft Generator -> Human Approval -> Publish
                              |              |                 |
                              -> Logs        -> Evaluation     -> Audit Trail
```

## Advanced Extension

Add a policy gate that blocks publishing if citations are missing or if the output contains sensitive data.

