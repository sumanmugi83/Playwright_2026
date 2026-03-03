# Project Constitution (gemini.md)

## 1. Data Schemas
## 1. Data Schemas

### Input Payload (Gherkin Source)
```json
{
  "project_name": "string (optional)",
  "gherkin_content": "string (The raw feature file content)",
  "language": "typescript" | "javascript",
  "browser_engine": "chromium" | "firefox" | "webkit"
}
```

### Output Payload (Playwright Test)
```json
{
  "files": [
    {
      "filename": "string (e.g., login.spec.ts)",
      "content": "string (The converted Playwright code)"
    }
  ],
  "logs": ["string (Execution logs or warnings)"],
  "status": "success" | "error"
}
```

## 2. Behavioral Rules
- **Protocol:** B.L.A.S.T. (Blueprint, Link, Architect, Stylize, Trigger)
- **Architecture:** A.N.T. (Architecture, Navigation, Tools)
- **Priority:** Reliability > Speed.
- **LLM:** Local (Ollama) with model `codellama`.
- **Data-First:** No coding until schema is defined.
- **SOPs:** Logic changes must update `architecture/` SOPs before code.
- **Self-Healing:** Analyze -> Patch -> Test -> Update Architecture.

## 3. Architectural Invariants
- **Layer 1:** Architecture (Markdown SOPs)
- **Layer 2:** Navigation (LLM Reasoning)
- **Layer 3:** Tools (Deterministic Python Scripts)
- **Environment:** Secrets in `.env`
- **Workspace:** Intermediate files in `.tmp/`

## 4. Maintenance Log
| Date | Action | Author |
|------|--------|--------|
|      |        |        |
