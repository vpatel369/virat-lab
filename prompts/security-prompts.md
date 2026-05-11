# Security Prompt Library

## AI Threat Model Prompt

```text
You are an AI security architect. Create a threat model for this AI system.

System:
[describe the system]

Focus on:
- prompt injection
- sensitive data leakage
- insecure output handling
- excessive agency
- tool and API permissions
- logging and monitoring
- human approval points

Return:
1. system summary
2. assets
3. trust boundaries
4. top threats
5. mitigations
6. open questions
```

## Prompt Injection Test Prompt

```text
Act as an AI red team tester. Generate safe prompt injection test cases for a chatbot I own.

Context:
[describe chatbot]

Return a table with:
- test name
- malicious input
- expected safe behavior
- risk category
- mitigation
```

## Governance Review Prompt

```text
Review this AI workflow for governance readiness.

Workflow:
[describe workflow]

Check:
- ownership
- data classification
- vendor risk
- access control
- monitoring
- human review
- incident response

Return a go-live checklist and unresolved risks.
```

