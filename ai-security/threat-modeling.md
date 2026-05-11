# AI Threat Modeling Guide

Threat modeling helps you understand what can go wrong before an AI system is deployed.

## Step 1: Describe The System

Document:

- Users
- Business goal
- Model or provider
- Data sources
- Tools and APIs
- Permissions
- Storage
- Logs
- Human approval points

## Step 2: Map Trust Boundaries

Ask:

- Where does user input enter?
- Where does external content enter?
- What systems can the model access?
- What actions can the agent perform?
- What sensitive data is available?
- What decisions require a human?

## Step 3: Identify AI-Specific Threats

| Threat | Example | Mitigation |
| --- | --- | --- |
| Prompt injection | Malicious text tells the model to ignore rules | Input isolation, instruction hierarchy, output validation |
| Data leakage | Model reveals private context | Data minimization, access controls, redaction |
| Excessive agency | Agent sends email or deletes data without approval | Least privilege, approval gates, scoped tools |
| RAG poisoning | Retrieved document contains malicious instructions | Source trust, content scanning, retrieval filtering |
| Insecure output | Model generates unsafe code or commands | Validation, sandboxing, human review |
| Secret exposure | API key appears in prompt or logs | Secret scanning, vaults, log filtering |

## Step 4: Rate Risk

Use a simple scale:

- Impact: Low, Medium, High
- Likelihood: Low, Medium, High
- Control strength: Weak, Moderate, Strong

## Step 5: Define Controls

Useful controls include:

- Least privilege
- Data classification
- Prompt and context separation
- Output validation
- Tool allowlists
- Human approval gates
- Sandboxed execution
- Audit logs
- Monitoring alerts
- Incident response plan

## Threat Model Template

```markdown
# AI Threat Model

## System

## Users

## Data Sources

## Model And Tools

## Permissions

## Trust Boundaries

## Key Threats

## Risk Ratings

## Required Controls

## Open Questions
```

