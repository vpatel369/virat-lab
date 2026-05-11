# Agentic AI Security

Agent security starts with one question: what can this system do without a human?

## Key Risks

- Excessive permissions
- Unsafe tool calls
- Secret exposure
- Prompt injection through files, webpages, or retrieved content
- Memory poisoning
- Unreviewed external actions
- Weak logging
- No rollback path

## Safer Design Pattern

1. Define the agent goal narrowly.
2. Give only the tools required.
3. Scope credentials and permissions.
4. Validate inputs and outputs.
5. Require approval for high-impact actions.
6. Log every tool call.
7. Test malicious and mistaken inputs.
8. Document failure and rollback procedures.

## Review Questions

- What tools can the agent call?
- What data can it read?
- What data can it modify?
- Can it send messages externally?
- Can it spend money or trigger production actions?
- Who reviews high-risk decisions?
- Where are logs stored?
- How do we disable it quickly?

