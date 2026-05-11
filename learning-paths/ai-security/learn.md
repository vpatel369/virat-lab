# Learn

## Core Concepts

| Concept | Practical Meaning |
| --- | --- |
| Prompt injection | Untrusted input attempts to override trusted instructions |
| Insecure output handling | Downstream systems trust generated output without validation |
| Excessive agency | An AI system can take actions beyond safe limits |
| RAG poisoning | Retrieved content includes malicious, false, or unsafe instructions |
| MCP security | Model Context Protocol servers and tools must be treated as privileged integration surfaces |
| AI observability | Logs, traces, evaluations, and tool-call records that help teams detect failures |
| AI governance | Ownership, policy, risk review, monitoring, and accountability |

## Reading Path

1. [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
2. [OWASP GenAI Security Project](https://genai.owasp.org/)
3. [Microsoft Security for AI](https://learn.microsoft.com/security/ai/)
4. [Microsoft Entra security for AI](https://learn.microsoft.com/en-us/entra/agent-id/identity-professional/security-for-ai)
5. [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
6. [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
7. [MITRE ATLAS](https://atlas.mitre.org/)

## Beginner

Learn the difference between model behavior risk, application risk, data risk, and tool/action risk.

## Intermediate

Map an AI app into components: model, prompt, memory, retrieval, tools, identity, logs, and users.

## Advanced

Study runtime governance patterns: deterministic policy checks, least-privilege tool access, agent identity, audit trails, and kill switches.

