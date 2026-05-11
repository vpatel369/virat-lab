# Prompt Engineering Guide

## Simple Prompt Formula

```text
Role: Who should the AI act as?
Task: What should it do?
Context: What information does it need?
Constraints: What rules should it follow?
Output: What format should the answer use?
```

## Example

```text
Role: You are an AI security analyst.
Task: Review this chatbot design for risks.
Context: The chatbot answers HR policy questions using internal documents.
Constraints: Focus on prompt injection, sensitive data, and excessive permissions.
Output: Return a table with risk, impact, likelihood, and mitigation.
```

## Better Prompting Habits

- Be specific about the goal.
- Provide enough context.
- Ask for a structured output.
- Include examples when possible.
- Ask the model to state assumptions.
- Ask for uncertainty when accuracy matters.
- Review and revise the output.

## Prompt Patterns

### Explain Simply

```text
Explain [topic] to a beginner using plain language, one example, and a short checklist.
```

### Compare Options

```text
Compare [option A] and [option B] for [use case]. Use a table with pros, cons, risks, and recommendation.
```

### Create A Workflow

```text
Turn this repeated task into a step-by-step workflow. Include inputs, outputs, tools, risks, and review points.
```

### Improve A Draft

```text
Improve this draft for clarity, structure, and professionalism. Preserve the original meaning.
```

