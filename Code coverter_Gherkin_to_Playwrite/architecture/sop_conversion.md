# SOP: Gherkin to Playwright Typescript Conversion

## Goal
Convert valid Gherkin `.feature` content into Playwright `spec.ts` files using `codellama`.

## Architecture
1. **Input:** Raw Gherkin text.
2. **Process:**
   - **Step 1: Structural Parsing** - Extract Feature Name, Scenarios, and Steps.
   - **Step 2: LLM Generation** - Send Gherkin snippet to `codellama` to generate valid Playwright code.
   - **Step 3: Validation** - Ensure output contains proper `test()`, `test.describe()`, and `await test.step()`.

## Prompt Strategy
We will use a specialized system prompt for CodeLlama to enforce the Playwright syntax.

**System Prompt Template:**
```text
You are an expert Playwright automation engineer. Convert the following Gherkin Scenario into a Playwright TypeScript test.
- Use `test('Scenario Name', async ({ page }) => { ... })`
- Map Gherkin steps to `await test.step('Step Name', async () => { ... })`
- Do NOT implement logic inside steps, just add comments like `// Implement logic here`
- Output ONLY the code, no markdown.
```

## Data Mapping
| Gherkin | Playwright |
|---------|------------|
| Feature: X | `test.describe('X', () => { ... })` |
| Scenario: Y | `test('Y', async ({ page }) => { ... })` |
| Given A | `await test.step('Given A', async () => { ... })` |

## Error Handling
- If LLM fails, generate a fallback deterministic skeleton using regex.
