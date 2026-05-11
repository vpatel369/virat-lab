# Build

## Portfolio Project: AI Security Lab

Build a GitHub repo that demonstrates AI security thinking using safe, synthetic examples.

## Required Artifacts

- Threat model
- Prompt injection lab report
- RAG security checklist
- Agent permission matrix
- Governance checklist
- Observability plan
- Incident response notes

## Architecture Diagram

```text
User -> App -> Prompt Layer -> Model -> Tool Gateway -> External Systems
             |                |       |
             |                |       -> Audit Logs
             |                -> Output Validation
             -> Input Review / Data Classification
```

## Advanced Extension

Prototype a policy gate that blocks risky tool calls, such as sending email, running shell commands, or accessing sensitive files without approval.

