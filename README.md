# Communication Value Delivery

## Overview

This skill helps an agent communicate value clearly, create practical demos and use cases, explain ROI responsibly, gather feedback, and drive adoption through trust-building communication.

Use it when a user needs to turn a capability, product, feature, automation, workflow change, or initiative into a stakeholder-ready value story, demo, use-case plan, ROI narrative, feedback loop, or adoption plan.

## What this skill produces

- Value propositions and benefit maps.
- Demo agendas, scripts, storyboards, and talk tracks.
- Use-case libraries and prioritized proof-of-value plans.
- ROI narratives, assumption tables, simple formulas, and confidence notes.
- Adoption plans, stakeholder FAQs, objection handling, and enablement checklists.
- Feedback surveys, interview guides, synthesis summaries, and iteration plans.

## When to use

Use this skill when the user asks for help with communication and value delivery, including phrases such as:

- "Create a demo for this feature."
- "Explain the ROI of this automation."
- "Turn this technical capability into a business value story."
- "Create use cases for adoption."
- "Help me gather feedback and iterate."
- "Build a stakeholder walkthrough."
- "Make this more trustworthy for users."

## How it works

The skill follows a repeatable value-delivery workflow:

1. Define the communication goal and desired adoption behavior.
2. Segment the audience and identify trust concerns.
3. Translate features into benefits, outcomes, and proof points.
4. Create clear demos and use cases with realistic before/after examples.
5. Explain ROI using assumptions, formulas, confidence levels, and caveats.
6. Plan adoption through champions, enablement, governance, and measurement.
7. Gather feedback, synthesize themes, prioritize improvements, and iterate.

## Contents

- `SKILL.md`: agent-facing instructions, boundaries, workflow, output formats, and safety rules.
- `README.md`: this human-readable package overview.
- `agents/openai.yaml`: display metadata and invocation policy.
- `references/style-guide.md`: templates, examples, writing rules, feedback prompts, and edge cases.
- `assets/demo-plan-template.md`: reusable demo planning template.
- `assets/roi-assumptions-template.csv`: lightweight ROI input template.
- `scripts/example_helper.py`: deterministic helper for simple ROI and feedback-priority calculations.

## Package structure

```text
communication-value-delivery/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   |-- demo-plan-template.md
|   `-- roi-assumptions-template.csv
|-- references/
|   `-- style-guide.md
`-- scripts/
    `-- example_helper.py
```

## Safety notes

This skill must not fabricate ROI, testimonials, user evidence, or adoption results. It should label assumptions, disclose limitations, protect confidential data, and avoid manipulative persuasion.
