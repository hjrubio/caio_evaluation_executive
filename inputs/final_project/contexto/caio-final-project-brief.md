# CAIO Certification — Final Project Brief (TP · Plan Maestro del CAIO)

**Issuer:** UTN.BA (Universidad Tecnológica Nacional, Buenos Aires)
**Status:** Official guideline for the final project. Evaluator personas must assess against this brief first, and use the CAIO evaluation lens (`caio-synthesis-and-evaluation-lens.md`) to judge depth and quality.
**Recorded:** 26 October 2026 (transcribed from the course's brief infographic)

---

## 1. The brief, as given

| Element | Requirement (original Spanish → meaning) |
|---|---|
| **Format** | *Entrega en equipo* → team submission |
| **Horizon** | *12 meses* → the plan covers a 12-month period |
| **Scope** | *Elegí un alcance* → choose one: **whole organization**, **one area**, or **one team** |
| **Integrate what was learned** | *Integrá lo aprendido* — the plan must cover the five blocks below |
| **Deliverable** | *Máximo 10 slides* → at most 10 slides containing **what the board has to decide** |
| **Annexes** | *Anexos* → what supports the plan: **analysis, numbers, assumptions, evidence** |

### The five content blocks
1. **Estrategia integral (comprehensive strategy):** architecture, governance, security, people, finance.
2. **Roadmap:** three tracks (technical, financial, cultural), with **milestones and success criteria**.
3. **Convencé al CFO (convince the CFO):** numbers plus a credible story.
4. **Ajustá por riesgo (risk-adjust the plan):** scenarios, contingencies, and a distinction between **reversible and irreversible decisions**.
5. **Prepará la defensa (prepare the defense):** a clear story, anticipated objections, and evidence.

---

## 2. What the brief implies

- **The audience is a board.** The slides exist to get a decision, not to explain the work. Analysis belongs in the annexes.
- **The CFO is the named skeptic.** Financial credibility is a primary test, not a supporting section.
- **The plan must be operational.** A 12-month horizon with milestones and success criteria means the CAIO 2.0 orientation (production, metrics, guardrails). A plan that stops at pilots does not meet the brief.
- **Scope is a choice.** Expectations should scale with the scope chosen. A plan for one team should go deeper; a plan for the whole organization should go wider. Every scope still needs all five blocks.
- **There is an oral defense.** Personas should be able to ask questions, not only score the documents.

---

## 3. Mapping the brief to the competency framework (D1–D7)

| Brief block | Dimensions | What evaluators check |
|---|---|---|
| Estrategia integral: architecture | D3 | Target architecture and platforms; path to production; shared standards |
| Estrategia integral: governance | D2, D4 | Decision rights; responsible-AI policy; interfaces with CIO/CTO/CDO/CISO/COO |
| Estrategia integral: security | D4 | Data protection, privacy, model and vendor risk, compliance |
| Estrategia integral: people | D6 | Team, talent, upskilling, change management |
| Estrategia integral: finance | D5 | Investment, run costs (including usage-based pricing), ROI |
| Roadmap: technical / financial / cultural | D3, D5, D6 | All three tracks present and sequenced; milestones and measurable success criteria |
| Convencé al CFO | D5, D7 | Numbers that hold together; explicit assumptions; a credible value story |
| Ajustá por riesgo | D4, D2 | Scenarios; triggers and contingencies; reversible vs irreversible decisions identified and treated differently |
| Prepará la defensa | D7 | Clear narrative; objections anticipated and answered; claims backed by evidence |
| Scope + strategic fit | D1 | Use cases tied to business goals of the chosen scope; ideally shows how AI changes the strategy, not only efficiency |

---

## 4. Reference structure: 10 slides + annexes

This is a suggested structure that satisfies the brief. Teams don't have to follow it, but evaluators can use it to check coverage.

| # | Slide | Brief block | Annex support |
|---|---|---|---|
| 1 | **The decision we ask for** (executive summary: ask, investment, expected return) | Defensa, CFO | — |
| 2 | **Scope and context** (chosen scope, problem or opportunity, current AI maturity) | Scope | Diagnosis, maturity assessment |
| 3 | **AI strategy and prioritized use cases** | Estrategia (D1) | Use-case scoring, business cases |
| 4 | **Operating model and governance** (decision rights, roles, C-suite interfaces) | Estrategia: governance | RACI, policies |
| 5 | **Architecture and security** | Estrategia: architecture, security | Architecture diagrams, security and compliance analysis |
| 6 | **People and culture** | Estrategia: people | Skills gap, training plan, change plan |
| 7 | **12-month roadmap** (technical, financial and cultural tracks; milestones; success criteria) | Roadmap | Detailed plan, KPI definitions |
| 8 | **Financial case** (investment, run costs, ROI or payback) | CFO, Estrategia: finance | Financial model, assumptions, sensitivity |
| 9 | **Risk-adjusted plan** (scenarios, contingencies, reversible vs irreversible decisions) | Riesgo | Risk register, scenario analysis |
| 10 | **Board decisions and next steps** (what is approved now; gates for later decisions) | Defensa | Anticipated objections and answers, evidence |

### Annex checklist
- [ ] **Analysis:** diagnosis, use-case prioritization, stakeholder map
- [ ] **Numbers:** financial model, costs (build and run), benefits, sensitivity
- [ ] **Assumptions:** listed explicitly and tied to the numbers that depend on them
- [ ] **Evidence:** benchmarks, pilot results, references, data that supports the claims
- [ ] (Recommended) Objection log with answers, for the defense

---

## 5. Brief-specific red flags

- More than 10 slides, or slides carrying analysis instead of decisions.
- No explicit board ask: the deck informs but doesn't request a decision.
- Numbers without assumptions in the annex, or assumptions that don't trace to the model.
- No run costs (only build costs), or no ROI or payback.
- A roadmap with only a technical track (missing the financial and cultural tracks), or milestones without success criteria.
- Risk treated as a list, with no scenarios, no contingencies, and no reversible/irreversible distinction.
- No anticipated objections, especially from the CFO.
- A scope that doesn't match the content (for example, "one team" in the title but an enterprise-wide plan in the slides).
- A plan that stays in exploration for 12 months (pilots only; CAIO 1.0).

---

## 6. Implications for evaluator personas

- **Board member and CFO are mandatory personas.** The brief names them as the decision-maker and the person to convince.
- The **CTO/CIO** (architecture), **CISO** (security) and **CHRO** (people/culture) cover the components of the comprehensive strategy.
- An **experienced CAIO** persona judges overall coherence and maturity (1.0 vs 2.0) and leads the defense questioning.
- Each persona should produce:
  1. a score on its dimensions
  2. a check against the brief's requirements
  3. two or three hard questions for the oral defense
