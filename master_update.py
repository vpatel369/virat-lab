from pathlib import Path

base = Path(".")

files = {

    "README.md": """
# Virat Lab

## Open AI Learning & Workflow Hub

Virat Lab is an open-source AI learning ecosystem designed to help beginners, professionals, healthcare workers, cybersecurity engineers, and automation builders navigate the future of AI.

---

# Mission

Build a practical, beginner-friendly, future-ready AI knowledge platform that anyone can use to learn, build, automate, and grow in the AI era.

---

# Featured Learning Paths

## AI Security Roadmap

Future-ready AI security learning path covering:

- LLM security
- Prompt Injection
- Cloud + Identity Security
- AI Governance
- Agentic AI Risks
- AI Red Teaming

Open here:

[AI Security Roadmap](./ai-security/roadmap.md)

---

# Repository Structure

- beginner-path/
- ai-security/
- healthcare-ai/
- claude-skills/
- prompts/
- workflows/
- research/
- resources/
- templates/

---

# Quick Navigation

| Section | Link |
|---|---|
| Beginner Path | [Open](./beginner-path) |
| AI Security | [Open](./ai-security) |
| Healthcare AI | [Open](./healthcare-ai) |
| Claude Skills | [Open](./claude-skills) |
| Workflows | [Open](./workflows) |
| Research | [Open](./research) |
| Resources | [Open](./resources) |

---

# Future Vision

Virat Lab will evolve into:

- AI learning university
- Agentic workflow marketplace
- Security research hub
- Healthcare AI education platform
- Open-source automation ecosystem
""",

    "ai-security/README.md": """
# AI Security

## Overview

This section focuses on practical AI security for modern enterprises and future-ready professionals.

---

## Topics Covered

- LLM Security
- Prompt Injection
- AI Threat Modeling
- AI Governance
- AI Red Teaming
- Identity Security
- Cloud Security
- AI Supply Chain Risks
- Agentic AI Security

---

## Learning Goals

By completing this section, you will understand:

- How AI systems are attacked
- How to secure AI workflows
- AI risk management
- Enterprise AI governance
- Secure AI deployment strategies

---

## Recommended Projects

- Build prompt injection lab
- AI phishing detection workflow
- Secure chatbot architecture
- AI governance checklist
""",

    "ai-security/roadmap.md": """
# AI Security Roadmap

## Phase 1 — Foundations

- Python Basics
- APIs
- Cloud Basics
- Identity & Access Management
- Networking Fundamentals

---

## Phase 2 — AI Fundamentals

- LLM Basics
- Prompt Engineering
- RAG Systems
- AI Agents
- Open-source Models

---

## Phase 3 — AI Security

- Prompt Injection
- Jailbreak Attacks
- AI Data Poisoning
- Model Security
- AI Red Teaming

---

## Phase 4 — Enterprise AI

- AI Governance
- AI Compliance
- Secure AI Deployment
- Agentic Workflow Security

---

## Phase 5 — Future Skills

- Autonomous Agents
- AI SOC Analyst
- AI Security Automation
- Multi-Agent Systems
- Human + AI Collaboration
""",

    "beginner-path/README.md": """
# Beginner Path

## Start Here

This section is designed for people with zero technical background.

---

## Learn In Order

1. Computer Basics
2. Internet Fundamentals
3. Cloud Basics
4. AI Fundamentals
5. Prompt Engineering
6. Automation Basics
7. AI Tools

---

## Goal

Help anyone become AI-ready within 90 days using practical learning paths.
""",

    "claude-skills/README.md": """
# Claude Skills

## Overview

Collection of Claude Code skills, workflows, prompts, and AI engineering techniques.

---

## Includes

- AI coding workflows
- Agentic systems
- Prompt chains
- Automation templates
- Research agents
- AI copilots
""",

}

for file_path, content in files.items():
    path = base / file_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")

print("Virat Lab updated successfully.")