# AI Governance Checklist

Use this checklist before approving an AI tool, model, workflow, or agent for real use.

## Ownership

- [ ] Business owner is identified
- [ ] Technical owner is identified
- [ ] Security reviewer is identified
- [ ] Human escalation path exists

## Data

- [ ] Data sources are documented
- [ ] Sensitive data is classified
- [ ] PHI, PII, secrets, and regulated data are handled correctly
- [ ] Data retention is understood
- [ ] Logs do not expose sensitive data

## Model And Vendor

- [ ] Model provider is documented
- [ ] Terms of service are reviewed
- [ ] Training and data usage policy is understood
- [ ] Model limitations are documented
- [ ] Vendor risk is reviewed if needed

## Security

- [ ] Authentication is required
- [ ] Authorization uses least privilege
- [ ] Tool permissions are scoped
- [ ] Secrets are stored securely
- [ ] Prompt injection risk is reviewed
- [ ] Output validation exists for high-risk use cases
- [ ] Audit logs are available

## Agentic Workflows

- [ ] Agent actions are documented
- [ ] High-impact actions require human approval
- [ ] Rollback process exists
- [ ] External tool access is restricted
- [ ] Memory use is documented

## Monitoring

- [ ] Usage is logged
- [ ] Errors and refusals are monitored
- [ ] Security events are reviewed
- [ ] Incident response process includes AI-specific issues

## Go-Live Decision

- [ ] Risks are accepted by the owner
- [ ] Required controls are implemented
- [ ] Users know limitations
- [ ] Review date is scheduled

