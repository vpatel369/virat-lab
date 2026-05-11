# Automation Guide

## Step 1: Pick A Repeated Task

Good automation candidates are tasks that are:

- Repeated often
- Rule-based enough to describe
- Time-consuming
- Low risk when tested with sample data
- Easy to review

## Step 2: Define Inputs And Outputs

Example:

| Item | Example |
| --- | --- |
| Trigger | New support ticket |
| Input | Ticket text and customer metadata |
| AI task | Classify urgency and summarize issue |
| Output | Ticket summary, priority, suggested owner |
| Review | Human support lead approves |

## Step 3: Add AI Carefully

Useful AI tasks:

- Summarization
- Classification
- Extraction
- Drafting
- Comparison
- Routing suggestions

Avoid fully autonomous decisions for high-impact tasks.

## Step 4: Add Safety

- Use sample data first.
- Remove secrets and sensitive data.
- Add human approval for important actions.
- Log inputs, outputs, and tool calls.
- Create a rollback plan.

## Step 5: Document The Workflow

Use [../templates/workflow-template.md](../templates/workflow-template.md).

