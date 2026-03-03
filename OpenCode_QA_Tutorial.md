# AI Meets QA: Master OpenCode for Test Automation

### The Open-Source AI Coding Agent That Works with Any LLM — Built for QA Engineers

**Covering:** STLC · Selenium Automation · Playwright Automation · API Testing · CI/CD  
**Every Command, Shortcut & QA-Specific Use Case Included**

---

**Created by: Pramod Dutta**  
SDET Manager at Tekion | Ex BrowserStack | CSM® Certified Scrum Master  
10+ Years in Software Testing & Test Automation | Mentored 10,000+ Students  
Founder — [TheTestingAcademy.com](https://thetestingacademy.com)  
LinkedIn — [linkedin.com/in/pramoddutta](https://www.linkedin.com/in/pramoddutta/)  
YouTube — 150K+ Subscribers | Instagram — 100K+ Followers

---

## Table of Contents

1. [Module 1: Introduction — Why OpenCode for QA?](#module-1-introduction--why-opencode-for-qa)
2. [Module 2: Installation & First Session](#module-2-installation--first-session)
3. [Module 3: Every OpenCode Command & Shortcut for QA](#module-3-every-opencode-command--shortcut-for-qa)
4. [Module 4: Built-in Tools Deep Dive for QA](#module-4-built-in-tools-deep-dive-for-qa)
5. [Module 5: Agents — Build, Plan, Research & Custom QA Agents](#module-5-agents--build-plan-research--custom-qa-agents)
6. [Module 6: AGENTS.md — Your QA Playbook](#module-6-agentsmd--your-qa-playbook)
7. [Module 7: STLC Implementation with OpenCode](#module-7-stlc-implementation-with-opencode)
8. [Module 8: Selenium Automation with OpenCode](#module-8-selenium-automation-with-opencode)
9. [Module 9: Playwright Automation with OpenCode](#module-9-playwright-automation-with-opencode)
10. [Module 10: API Testing with OpenCode](#module-10-api-testing-with-opencode)
11. [Module 11: CI/CD Pipeline Integration](#module-11-cicd-pipeline-integration)
12. [Module 12: Advanced QA Workflows](#module-12-advanced-qa-workflows)
13. [Module 13: Quick Reference — Cheat Sheet](#module-13-quick-reference--cheat-sheet)

---

## Module 1: Introduction — Why OpenCode for QA?

### 1.1 What is OpenCode?

OpenCode is an **open-source AI coding agent** built for the terminal. Unlike proprietary tools, OpenCode supports **75+ models** across every major LLM provider — OpenAI, Anthropic Claude, Google Gemini, AWS Bedrock, Groq, Azure OpenAI, OpenRouter, and even local models via Ollama and LM Studio.

- **Open source** under MIT License — fully transparent, no vendor lock-in
- **Terminal-native TUI** built with Bubble Tea for a beautiful, responsive interface
- **Multi-provider freedom** — use Claude for planning, Gemini for bulk generation, local models for private code
- **95K+ GitHub stars** — one of the most popular AI coding tools in the open-source ecosystem

### 1.2 Why OpenCode for QA Engineers?

For QA Engineers, OpenCode offers unique advantages over closed tools:

- **Model Flexibility:** Use a cheaper model for test planning conversations, then switch to an expensive model for actual test generation. No single-vendor dependency.
- **Privacy First:** Your code never leaves your machine if you use local models. Critical for enterprise QA teams working with sensitive test data.
- **Git-Based Undo/Redo:** Every file change is tracked via Git. Undo a botched test refactor instantly with `/undo`. No guessing what changed.
- **Built-in Agents:** Switch between Build (full access), Plan (read-only analysis), and custom QA-specific agents with a single Tab press.

### 1.3 OpenCode vs Claude Code — Key Differences for QA

| Feature | OpenCode | Claude Code |
|---------|----------|-------------|
| LLM Providers | 75+ models, any provider | Anthropic Claude only |
| License | MIT (open source) | Proprietary |
| Undo/Redo | Git-based `/undo` `/redo` | Double-Escape rewind |
| Agent System | Build, Plan, Research + custom | Plan mode toggle |
| Project Context | AGENTS.md | CLAUDE.md |
| Custom Commands | Markdown files in `commands/` | `.claude/commands/` |
| Permissions | Granular per-tool, per-command | `--dangerously-skip-permissions` |
| Session Sharing | `/share` generates public URL | Not built-in |
| IDE Integration | VS Code, Cursor, any terminal | Terminal only |
| Cost | Free (bring your own API key) | Claude subscription required |

---

## Module 2: Installation & First Session

### 2.1 Installation Methods

**Method 1 — Install Script (Recommended):**
```bash
curl -fsSL https://opencode.ai/install | bash
```

- Fastest method, works on Mac and Linux
- Automatically adds `opencode` to your PATH

**Method 2 — npm:**
```bash
npm install -g opencode-ai
```

- Works on any platform with Node.js installed
- Good for Windows users

**Method 3 — Windows (WSL Recommended):**
```bash
# Inside WSL
curl -fsSL https://opencode.ai/install | bash
```

- OpenCode recommends WSL for the best Windows experience
- Full compatibility with all features

### 2.2 First-Time Setup

**Step 1: Configure your LLM provider**

Option A — OpenCode Zen (easiest, curated models):
```
# Inside OpenCode TUI
/connect
# Select "opencode", go to opencode.ai/auth
# Sign in, add billing, copy API key
```

Option B — Bring your own API key:
```bash
opencode auth login
# Select provider (OpenAI, Anthropic, Google, etc.)
# Paste your API key
```

**Step 2: Navigate to your QA project and launch:**
```bash
cd ~/projects/my-qa-framework
opencode
```

**Step 3: Initialize project context:**
```
/init
```

- This analyzes your project structure and creates an `AGENTS.md` file
- Commit `AGENTS.md` to Git so the whole QA team benefits
- OpenCode now understands your test framework, folder structure, and conventions

### 2.3 Verify Installation

```bash
opencode --version          # Check version
opencode models             # List available models
opencode auth list          # Show configured providers
opencode --help             # Full CLI reference
```

---

## Module 3: Every OpenCode Command & Shortcut for QA

### 3.1 TUI Slash Commands (Complete Reference)

These are all commands available inside the OpenCode interactive TUI.

| Command | Aliases | QA Use Case |
|---------|---------|-------------|
| `/init` | — | Analyze project and create/update AGENTS.md. Run this first on any QA project. Generates project context that helps the AI understand your test framework. |
| `/new` | `/clear` | Start a fresh session. Use between different testing activities — don't carry Selenium context into API test work. |
| `/undo` | — | Undo last message AND all file changes. Git-based, so it reverts actual code. Essential when AI-generated tests break your suite. Can be called multiple times. |
| `/redo` | — | Redo a previously undone message. Only available after `/undo`. Restores both the message and file changes. |
| `/sessions` | `/resume`, `/continue` | List and switch between sessions. Resume yesterday's test writing session exactly where you stopped. |
| `/compact` | `/summarize` | Compact the session to reduce token usage. Use during long test generation sessions before context gets too large. |
| `/share` | — | Share current session via public URL. Perfect for sharing a QA debugging session with teammates or in code reviews. |
| `/models` | — | List available models. Switch between cheap models for planning and expensive ones for test generation. |
| `/details` | — | Toggle tool execution details. See exactly what commands OpenCode ran, which files it read — great for debugging test failures. |
| `/editor` | — | Open external editor ($EDITOR) for composing long prompts. Use for writing detailed test requirements that need precise formatting. |
| `/export` | — | Export conversation to Markdown. Save your entire QA session as documentation — test decisions, rationale, and generated code. |
| `/themes` | — | List available themes. Customize your terminal appearance. |
| `/help` | — | Show help dialog with all commands, keybinds, and loaded skills. |
| `/exit` | `/quit`, `/q` | Exit OpenCode cleanly. |

### 3.2 Vim-Style Keybinds (Complete Reference)

OpenCode uses a `<leader>` key (default: Space) for Vim-style keybinds.

| Keybind | Action | QA Context |
|---------|--------|-----------|
| `Tab` | **Switch between agents** (Build ↔ Plan) | Most critical QA keybind. Switch to Plan for test strategy, switch to Build for test execution. |
| `Escape` | Interrupt current generation | Stop a runaway test generation or command execution immediately. |
| `<leader>u` | Undo message | Quick undo — same as `/undo` but faster. Revert bad test changes instantly. |
| `<leader>r` | Redo message | Quick redo — same as `/redo`. |
| `<leader>m` | Model list | Quickly switch models mid-session. Use Opus for complex test design, Sonnet for bulk generation. |
| `<leader>c` | Compact session | Quick compact when context is getting large during long test generation. |
| `<leader>y` | Copy message | Copy generated test code to clipboard for pasting into other files. |
| `<leader>h` | Toggle conceal (tool details) | Show/hide tool execution details. Useful when debugging why a test command failed. |
| `<leader>a` | Agent list | Quick switch between Build, Plan, Research, and custom QA agents. |
| `<leader>→` | Cycle child sessions | Navigate between sub-sessions spawned by subagents. |
| `<leader>←` | Cycle child (reverse) | Navigate back through sub-sessions. |
| `<leader>↑` | Go to parent session | Return to main session from a subagent session. |
| `F2` | Cycle recent model | Quickly toggle between your two most recently used models. |
| `Shift+F2` | Cycle recent model (reverse) | Reverse toggle models. |
| `Ctrl+T` | Cycle variants | Switch between response variants. |
| `Ctrl+P` | Command palette | Open command list — all slash commands searchable. |
| `PageUp` / `Ctrl+Alt+B` | Scroll up messages | Scroll through long test outputs and reports. |
| `PageDown` / `Ctrl+Alt+F` | Scroll down messages | Scroll down through messages. |
| `Ctrl+Alt+U` | Half page up | Quick scroll in long test results. |
| `Ctrl+Alt+D` | Half page down | Quick scroll down. |
| `Ctrl+G` / `Home` | Jump to first message | Go to start of session — useful for reviewing initial test plan. |
| `Ctrl+Alt+G` / `End` | Jump to last message | Jump to most recent output. |

### 3.3 CLI Commands (Outside TUI)

These commands run directly in your terminal without launching the full TUI.

| Command | QA Use Case |
|---------|-------------|
| `opencode` | Start interactive TUI in current directory |
| `opencode -p "prompt"` | **Print mode** — execute a single prompt and exit. Essential for CI/CD scripts and automated test generation. |
| `opencode -p "prompt" -f json` | Print mode with JSON output. Parse AI responses programmatically in test pipelines. |
| `opencode -p "prompt" -q` | Quiet mode — no spinner. Best for scripting and automation where clean output matters. |
| `opencode -m "provider/model"` | Start with a specific model. E.g., `opencode -m "anthropic/claude-sonnet-4-20250514"` |
| `opencode --continue` | Continue most recent conversation |
| `opencode --session <id>` | Resume a specific session by ID |
| `opencode auth login` | Configure LLM provider credentials |
| `opencode auth list` | List authenticated providers |
| `opencode auth logout` | Remove provider credentials |
| `opencode models` | List all available models across providers |
| `opencode models --refresh` | Refresh cached model list |
| `opencode agent create` | Create a new custom agent (interactive wizard) |
| `opencode agent list` | List all available agents |
| `opencode mcp add` | Add an MCP server (Playwright, etc.) |
| `opencode mcp list` | List configured MCP servers |
| `opencode mcp auth` | Authenticate with OAuth-enabled MCP server |
| `opencode github install` | Install GitHub agent for repo automation |
| `opencode github run` | Run GitHub agent (for GitHub Actions) |
| `opencode web` | Start headless server with web interface |
| `opencode serve` | Start headless server for remote access |
| `opencode attach` | Connect TUI to a running headless server |
| `opencode import <file/url>` | Import session from JSON file or share URL |
| `opencode update` | Update to latest version |
| `opencode update <version>` | Update to specific version |
| `opencode uninstall` | Uninstall OpenCode and remove all files |

### 3.4 In-Session Features

| Feature | How to Use | QA Context |
|---------|-----------|-----------|
| File reference | Type `@` then filename | Reference test files: `How is auth handled in @tests/login.spec.ts?` |
| Shell command | Start message with `!` | Run commands inline: `!mvn test -Dtest=LoginTest` — output goes into conversation. |
| Fuzzy file search | Type `@` and start typing | Quickly find test files across your project without knowing exact paths. |
| Custom commands | Type `/` + command name | Run your custom `/run-smoke`, `/generate-tests` commands. |

---

## Module 4: Built-in Tools Deep Dive for QA

### 4.1 What Are Tools?

Tools are capabilities the AI uses to interact with your codebase. OpenCode comes with 15 built-in tools. Each can be independently allowed, denied, or set to require approval.

- **Tools are the hands of the AI** — they let it read, write, search, and execute
- **Permissions give you control** — deny destructive tools in Plan mode, allow everything in Build mode
- **For QA, tools enable autonomous testing** — the AI can write tests, run them, read failures, and self-correct

### 4.2 Complete Built-in Tools Reference

| Tool | What It Does | QA Use Case | Default |
|------|-------------|-------------|---------|
| `bash` | Execute shell commands | Run `mvn test`, `npx playwright test`, `pytest`, `npm run lint`. The most critical tool for QA — enables the validation loop. | allow |
| `edit` | Modify existing files via exact string replacement | Fix failing test locators, update assertions, refactor page objects. Precise edits, not full file rewrites. | allow |
| `write` | Create new files or overwrite existing | Generate new test files, create page objects, write config files. Controlled by `edit` permission. | allow |
| `read` | Read file contents | Read test files, configs, page objects, test data. Supports reading specific line ranges for large files. | allow |
| `grep` | Search file contents with regex | Find all `@Test` annotations, locate flaky test patterns like `Thread.sleep()`, search for hardcoded test data. | allow |
| `glob` | Find files by pattern | `**/*.spec.ts` to find all Playwright tests, `**/Test*.java` for all TestNG classes. Results sorted by modification time. | allow |
| `list` | List directory contents | Explore test folder structure, find reports directory, list screenshots. | allow |
| `patch` | Apply patch/diff to files | Apply diffs from code reviews, batch-update test files. Controlled by `edit` permission. | allow |
| `skill` | Load a SKILL.md file | Load QA-specific skills: test generation patterns, framework conventions, reporting templates. | allow |
| `todowrite` | Create/update todo lists | Track multi-step QA tasks: "1. Create page objects ✓ 2. Write tests ⬜ 3. Run suite ⬜ 4. Generate report ⬜" | allow |
| `todoread` | Read current todo list | Check task progress during complex QA workflows. | allow |
| `webfetch` | Fetch web page content | Read API documentation, fetch Swagger/OpenAPI specs from URLs, check deployment status. | allow |
| `websearch` | Search the web via Exa AI | Research testing best practices, find framework documentation, look up error messages. Requires OpenCode provider or `OPENCODE_ENABLE_EXA=1`. | allow |
| `question` | Ask user a question | "Which browser should I target: Chrome only or cross-browser?" Gathers preferences mid-task. | allow |
| `lsp` | Language Server Protocol integration | Go-to-definition, find references, hover info. Understands your code structure for smarter test generation. Experimental: set `OPENCODE_EXPERIMENTAL_LSP_TOOL=true`. | allow |

### 4.3 Permission Configuration for QA

Create `opencode.json` at your project root:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": {
      "mvn test*": "allow",
      "npx playwright*": "allow",
      "npm test*": "allow",
      "pytest*": "allow",
      "git push": "ask",
      "rm -rf *": "deny",
      "docker rm*": "deny",
      "*": "ask"
    },
    "edit": "allow",
    "read": "allow",
    "grep": "allow",
    "glob": "allow",
    "webfetch": "allow"
  }
}
```

- **allow** test execution commands automatically
- **ask** before git push or unknown commands
- **deny** destructive commands completely
- Wildcards (`*`) let you create powerful patterns

---

## Module 5: Agents — Build, Plan, Research & Custom QA Agents

### 5.1 Understanding Agents

Agents are specialized AI assistants with different capabilities and restrictions. OpenCode comes with built-in agents and lets you create custom ones.

- **Primary agents** are what you interact with directly — switch with `Tab`
- **Subagents** run in parallel, spawned by primary agents for isolated tasks
- **Mode determines usage**: `primary` (direct interaction), `subagent` (spawned), or `all` (both)

### 5.2 Built-in Agents

| Agent | Mode | Tools | QA Role |
|-------|------|-------|---------|
| **Build** | Primary | All tools enabled | Default agent. Full access to read, write, execute. Use for actual test creation, framework setup, and test execution. |
| **Plan** | Primary | Read-only (edit/write/bash = ask) | Analysis and strategy. Use for test planning, reviewing coverage, designing test architecture — without accidentally changing anything. |
| **Research** | Subagent | All except todo | Researches complex questions. Spawn to investigate a testing pattern, framework docs, or error while main session continues. |
| **Explore** | Subagent | Read-only (no write/edit/bash) | Fast codebase exploration. Spawn to search for test patterns, find file structures, answer "where is X?" questions. |

### 5.3 Creating Custom QA Agents

**Method 1 — Interactive wizard:**
```bash
opencode agent create
```
This walks you through name, description, system prompt, and tool selection.

**Method 2 — Markdown file:**

Create `.opencode/agents/qa-analyst.md`:
```markdown
---
id: qa-analyst
description: Analyzes features and generates test strategies
model: anthropic/claude-sonnet-4-20250514
mode: primary
tools:
  write: false
  edit: false
  bash: false
  read: true
  grep: true
  glob: true
---

You are a Senior QA Analyst with 15 years of experience. When given a feature or requirement:

1. Identify ALL testable requirements (functional, non-functional, edge cases)
2. Create test cases in BDD format (Given/When/Then)
3. Categorize each: Smoke, Regression, Edge Case, Security, Performance
4. Estimate test effort (hours) and automation feasibility
5. Identify risks and suggest mitigation strategies
6. Generate a Requirements Traceability Matrix (RTM)

Always consider: boundary values, equivalence partitioning, state transitions, error guessing.
Never modify any files. Analysis only.
```

Create `.opencode/agents/qa-builder.md`:
```markdown
---
id: qa-builder
description: Builds test automation frameworks and writes tests
model: anthropic/claude-sonnet-4-20250514
mode: primary
---

You are a Senior SDET specializing in test automation. When building tests:

1. Always use Page Object Model (POM) for UI tests
2. Never hardcode test data — use data providers or fixtures
3. Every test MUST have at least one assertion
4. Include proper setup/teardown in every test class
5. Add meaningful test names that describe the scenario
6. After writing tests, ALWAYS run them to verify they pass
7. If tests fail, analyze the error and fix immediately

Validation commands:
- Java/Maven: mvn clean test
- Playwright: npx playwright test
- Python: pytest -v
- Node: npm test
```

### 5.4 Agent Permissions

Override permissions per agent:
```json
{
  "agent": {
    "qa-analyst": {
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    },
    "qa-builder": {
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    }
  }
}
```

---

## Module 6: AGENTS.md — Your QA Playbook

### 6.1 What is AGENTS.md?

AGENTS.md is OpenCode's project context file — equivalent to Claude Code's CLAUDE.md. It tells the AI everything about your project structure, conventions, and rules.

- **Generated by `/init`** which analyzes your project automatically
- **Commit to Git** so the entire QA team shares the same AI-powered workflow
- **Hierarchical**: global `~/.config/opencode/AGENTS.md` + project-level `AGENTS.md`

### 6.2 Sample AGENTS.md for a QA Project

```markdown
# QA Automation Framework

## Project Overview
This is a test automation framework for an e-commerce application using
Selenium (Java) and Playwright (TypeScript) for UI tests, REST Assured
for API tests, and GitHub Actions for CI/CD.

## Tech Stack
- Java 17 + Maven + Selenium 4 + TestNG
- TypeScript + Playwright
- REST Assured for API testing
- Allure for reporting
- Docker Compose for Selenium Grid

## Project Structure
- src/main/java/pages/        → Page Object classes
- src/main/java/utils/        → Utility/helper classes
- src/test/java/tests/        → Selenium test classes
- playwright/tests/            → Playwright test specs
- playwright/pages/            → Playwright page objects
- api-tests/                   → REST Assured API tests
- .github/workflows/           → CI/CD pipelines
- docker-compose.yml           → Selenium Grid setup

## Critical Rules
- ALWAYS use Page Object Model for UI tests
- NEVER hardcode test data — use @DataProvider or fixtures
- NEVER use Thread.sleep() — use explicit waits only
- ALL tests MUST have meaningful assertions
- ALL test methods MUST have descriptive names
- Screenshot on EVERY failure (configured in TestBase)

## Validation Commands
- Build: mvn clean compile
- Run all Selenium tests: mvn test
- Run smoke suite: mvn test -DsuiteXmlFile=smoke-testng.xml
- Run specific test: mvn test -Dtest=LoginTest
- Run Playwright: npx playwright test
- Run Playwright headed: npx playwright test --headed
- Run API tests: mvn test -pl api-tests
- Generate Allure report: allure serve target/allure-results

## Coding Conventions
- Page Object file: {PageName}Page.java
- Test file: {Feature}Test.java
- Playwright spec: {feature}.spec.ts
- API test: {Endpoint}ApiTest.java
- Use camelCase for methods, PascalCase for classes
```

### 6.3 Why Validation Commands Are the #1 Most Important Thing

The AGENTS.md validation commands create a **self-correcting feedback loop**:

1. AI writes tests
2. AI runs `mvn test` (from validation commands)
3. Tests fail with specific errors
4. AI reads the error output
5. AI fixes the tests
6. Repeat until all tests pass

**Without validation commands:** You're hoping the AI gets it right on the first try.  
**With validation commands:** You get an autonomous testing loop that self-improves.

---

## Module 7: STLC Implementation with OpenCode

### 7.1 Phase 1 — Requirement Analysis (Plan Agent)

Press `Tab` to switch to **Plan** agent, then:

```
Analyze the requirements at @docs/requirements.md and create:
1. List of all testable requirements (functional + non-functional)
2. Requirements Traceability Matrix (RTM)
3. Risk assessment for each requirement
4. Test estimation (effort in hours)
```

- Plan agent reads files but won't modify anything — safe for analysis
- Use `@` file references to point at specific documents
- Export the analysis with `/export` for team review

### 7.2 Phase 2 — Test Planning

```
Create a comprehensive test plan for the checkout module:
- Scope: what's in and out of testing
- Test strategy: risk-based, browser matrix, mobile coverage
- Entry/exit criteria for each test phase
- Resource requirements and timeline
- Risk mitigation strategies
```

### 7.3 Phase 3 — Test Case Design

```
Generate BDD test cases for user authentication:
Given/When/Then format for: valid login, invalid password (3 attempts → lock),
forgot password flow, SSO login, session timeout (30 min), concurrent sessions
(max 3), remember me (14 days), CAPTCHA after 5 failed attempts.
```

### 7.4 Phase 4 — Test Environment Setup

Switch to **Build** agent (`Tab`), then:

```
Set up the complete test automation framework:
- Selenium 4 + TestNG + Maven project with POM structure
- WebDriverManager for browser driver management
- ExtentReports for HTML reporting
- TestBase with Chrome/Firefox setup and screenshot on failure
- Sample LoginPage and LoginTest to verify setup
- testng.xml with smoke and regression suites
```

### 7.5 Phase 5 — Test Execution

```
Run the smoke test suite and analyze results. If any test fails:
1. Read the error message and stack trace
2. Check if it's a test issue or app bug
3. Fix test issues automatically
4. Re-run to confirm the fix
Report final pass/fail status.
```

### 7.6 Phase 6 — Test Reporting

```
Analyze test results in target/surefire-reports/ and generate:
- Executive summary: total, passed, failed, skipped
- Failure analysis with root causes
- Defect density and coverage percentage
- Recommendations for next sprint
- Top 5 flaky tests to investigate
```

---

## Module 8: Selenium Automation with OpenCode

### 8.1 Project Setup

```
Create a Selenium Java automation project with Maven. Include:
- pom.xml with Selenium 4, TestNG, WebDriverManager, ExtentReports, Apache POI
- Page Object Model base class with WebDriverWait and fluent waits
- TestBase class with @BeforeMethod/@AfterMethod for Chrome and Firefox
- ConfigReader for properties file (base URL, timeout, browser)
- Sample LoginPage with locators and action methods
- Sample LoginTest with @DataProvider for valid/invalid credentials
- testng.xml with smoke and regression suites
- .gitignore for Java/Maven projects
```

### 8.2 Key Prompts

**Page Objects:**
```
Create Page Object for ProductSearchPage with: search input, search button,
result count label, first result link, price filter slider, sort dropdown,
category checkboxes. Use explicit waits. Include method chaining (return this).
```

**Data-Driven Tests:**
```
Create data-driven test using Apache POI to read from Excel:
- ExcelReader utility class
- Test data in testdata/login-data.xlsx
- LoginTest with @DataProvider reading from Excel
- Columns: username, password, expectedResult, testDescription
```

**Cross-Browser Parallel:**
```
Configure testng.xml for parallel cross-browser testing:
- 3 threads: Chrome, Firefox, Edge
- Separate suites for smoke (5 min) and regression (30 min)
- Retry analyzer for flaky tests (max 2 retries)
```

### 8.3 AGENTS.md Validation Block for Selenium

```markdown
## Selenium Validation Commands
- Build: mvn clean compile
- Run all: mvn test
- Run smoke: mvn test -DsuiteXmlFile=smoke-testng.xml
- Run specific: mvn test -Dtest=LoginTest
- Run with retries: mvn test -DsuiteXmlFile=retry-testng.xml
- Report: mvn surefire-report:report
```

### 8.4 Debugging Workflow

```
LoginTest.testInvalidPassword fails with NoSuchElementException on error message.
Analyze: check LoginPage locators, look for dynamic elements, check if there's
a loading spinner blocking the element. Fix and re-run.
```

Use `!mvn test -Dtest=LoginTest` (inline shell with `!`) to run the failing test directly from the conversation.

---

## Module 9: Playwright Automation with OpenCode

### 9.1 Project Setup

```
Initialize a Playwright TypeScript project with:
- playwright.config.ts with Chrome, Firefox, WebKit + mobile viewports
- Base test fixture with shared authentication state
- Page Object Model pattern with TypeScript classes
- Visual regression with toMatchSnapshot()
- CI-ready headless config + local headed config
- Sample login.spec.ts with multiple test cases
```

### 9.2 MCP Integration — Playwright Browser Control

```bash
opencode mcp add playwright-mcp
```

Once configured, OpenCode can directly control a browser — navigate pages, fill forms, click buttons, and verify behavior autonomously.

### 9.3 Key Prompts

**E2E Checkout Flow:**
```
Write Playwright E2E test for checkout:
add item → update quantity → apply coupon (valid + invalid) → shipping form
→ payment (card + PayPal) → order confirmation → verify email sent.
Screenshot every step. Trace on failure.
```

**Visual Regression:**
```
Set up visual regression testing:
- Baseline screenshots for homepage, product page, cart, checkout
- Per-browser baselines (Chrome vs Firefox render differently)
- 0.1% pixel threshold for acceptable diff
- Automatic diff images on failure
```

**Accessibility Testing:**
```
Add @axe-core/playwright accessibility tests:
- WCAG 2.1 AA compliance for all main pages
- Custom rules for our design system components
- Generate detailed a11y report with violation counts and fixes
```

**Mobile Testing:**
```
Configure Playwright for: iPhone 14, Pixel 7, iPad Pro viewports.
Write responsive tests: hamburger menu, touch gestures, viewport breakpoints.
```

### 9.4 AGENTS.md Validation Block for Playwright

```markdown
## Playwright Validation Commands
- Run all: npx playwright test
- Run headed: npx playwright test --headed
- Run specific: npx playwright test tests/login.spec.ts
- Show report: npx playwright show-report
- Update snapshots: npx playwright test --update-snapshots
- Debug: npx playwright test --debug
- Trace viewer: npx playwright show-trace trace.zip
```

---

## Module 10: API Testing with OpenCode

### 10.1 Framework Setup

```
Create an API testing framework with REST Assured (Java):
- Request/response logging with filters
- JSON Schema validation using json-schema-validator
- Environment configs: dev.properties, staging.properties, prod.properties
- Auth helpers: OAuth2 token manager, JWT decoder, API key rotator
- Allure reporting integration
- Base request specification with common headers
```

### 10.2 CRUD Test Generation

```
Generate comprehensive API tests for /api/users endpoint:
POST: valid user, missing required fields, duplicate email, invalid email format,
      exceeds field length, SQL injection in name, XSS in bio
GET /users: pagination (?page=1&limit=10), filtering (?role=admin),
            sorting (?sort=created_at&order=desc), empty results
GET /users/:id: valid ID, invalid ID (999999), deleted user (410 Gone), UUID format
PUT: full update, partial update, unauthorized (no token), forbidden (wrong role)
DELETE: valid, already deleted (idempotent), cascade check (user with orders)
Validate: status codes, response headers, body schema, response time < 200ms.
```

### 10.3 API Chaining Workflow

```
Create API workflow test chain:
1. POST /auth/register → extract userId
2. POST /auth/login → extract JWT token
3. GET /users/:userId → verify profile with token
4. POST /products → create product with token → extract productId
5. GET /products/:productId → verify product exists
6. PUT /products/:productId → update price
7. DELETE /products/:productId → remove product
8. GET /products/:productId → verify 404
Cleanup: DELETE /users/:userId in afterAll.
Pass data between steps using shared context.
```

### 10.4 Contract Testing

```
Set up Pact contract testing:
- Consumer tests for frontend → backend API
- Provider verification tests
- Pact Broker integration for contract sharing
- Versioned contracts aligned with Git branches
```

---

## Module 11: CI/CD Pipeline Integration

### 11.1 GitHub Actions Pipeline

```
Create a GitHub Actions CI/CD pipeline:
Trigger: push to main/develop, PR to main, manual dispatch
Jobs (in order):
  1. lint-and-compile (fast feedback, fail early)
  2. unit-tests (parallel with api-tests)
  3. api-tests (REST Assured suite)
  4. selenium-tests (cross-browser via Selenium Grid)
  5. playwright-tests (Chrome + Firefox + WebKit, with trace)
  6. report (aggregate all results, Allure report)
  7. notify (Slack on failure, PR comment with results)
Artifacts: test reports, screenshots, Playwright traces.
```

### 11.2 OpenCode in CI/CD (Print Mode)

Use OpenCode's non-interactive print mode for automation:

```bash
# In GitHub Actions step:
opencode -p "Analyze the test failures in target/surefire-reports/ and suggest fixes" -q

# Generate tests for changed files:
opencode -p "Generate tests for the files changed in this PR: $(git diff --name-only main)" -q

# JSON output for parsing:
opencode -p "List all test files missing assertions" -f json -q
```

- `-p` = print mode (execute and exit)
- `-q` = quiet (no spinner, clean output)
- `-f json` = JSON format for programmatic parsing

### 11.3 GitHub Agent Integration

```bash
# Install the GitHub agent in your repo
opencode github install
```

Then in PR comments, mention `/opencode` or `/oc`:
- "Review this PR for test coverage gaps"
- "Generate tests for the changed files"
- "Analyze if these changes could break existing tests"

OpenCode runs inside your GitHub Actions runner — secure, no code leaves your infrastructure.

### 11.4 Docker Compose for Selenium Grid

```
Create Docker Compose for QA:
- App container (our web application)
- Selenium Grid hub + Chrome node + Firefox node + Edge node
- PostgreSQL with test data seeding script
- Mock API server (WireMock)
- Health checks and depends_on for proper startup order
- Network isolation between test and app containers
```

---

## Module 12: Advanced QA Workflows

### 12.1 Custom QA Commands

Create reusable commands as Markdown files in `.opencode/commands/`:

**`.opencode/commands/run-smoke.md`:**
```markdown
---
description: Run smoke test suite and report results
agent: build
---
Run the smoke test suite using the validation commands in AGENTS.md.
After execution, summarize: total tests, passed, failed, duration.
If any test failed, analyze the failure and suggest a fix.
```

**`.opencode/commands/generate-tests.md`:**
```markdown
---
description: Generate comprehensive tests for a file
agent: build
---
Analyze the file at $ARGUMENTS and generate comprehensive tests:
1. Happy path tests (valid inputs, expected flows)
2. Negative tests (invalid inputs, error conditions)
3. Boundary value tests (min, max, off-by-one)
4. Security tests (injection, XSS, auth bypass)
5. Performance considerations (response time assertions)

Use the project's existing test patterns and framework.
Always run tests after generating to verify they pass.
```

**Usage:** `/run-smoke` or `/generate-tests src/pages/CheckoutPage.ts`

### 12.2 Skills for QA

Create `.opencode/skills/qa-testing/SKILL.md`:
```markdown
---
name: qa-testing
description: QA testing best practices and patterns
---

## Test Design Principles
- Equivalence Partitioning: divide inputs into classes
- Boundary Value Analysis: test at edges
- State Transition: test valid and invalid transitions
- Error Guessing: use experience to predict failures

## Automation Patterns
- Page Object Model for all UI tests
- Builder pattern for test data
- Factory pattern for page object creation
- Strategy pattern for different test environments
```

### 12.3 Parallel Workflows with Subagents

OpenCode's subagents let you run multiple QA tasks in parallel:

```
Spawn a Research subagent to investigate the flaky test in LoginTest while
I continue working on the checkout flow tests here.
```

The Research subagent works independently — reading files, searching — while your main Build agent keeps writing tests.

### 12.4 Flaky Test Detection

```
Use grep to find all tests in our suite that have any of these flaky patterns:
- Thread.sleep() or hardcoded waits
- Tests that depend on execution order
- Shared mutable state between test methods
- Network calls without retry logic
- Time-dependent assertions (checking exact timestamps)
- Random data without seeding
List each file, line number, and pattern found. Suggest fixes for each.
```

### 12.5 Session Sharing for QA Reviews

After a complex debugging session:
```
/share
```
This generates a public URL. Share it in:
- PR comments: "Here's how I debugged and fixed the auth test failure"
- Team Slack: "Here's the session where I set up the new Playwright framework"
- Documentation: Export with `/export` for permanent records

---

## Module 13: Quick Reference — Cheat Sheet

### 13.1 Complete Command Quick Reference

**TUI Slash Commands:**

| Command | What It Does |
|---------|-------------|
| `/init` | Create/update AGENTS.md |
| `/new` `/clear` | Fresh session |
| `/undo` | Undo last + revert files |
| `/redo` | Redo after undo |
| `/sessions` `/resume` | Switch sessions |
| `/compact` `/summarize` | Reduce context |
| `/share` | Public share URL |
| `/models` | List/switch models |
| `/details` | Toggle tool details |
| `/editor` | External editor |
| `/export` | Export to Markdown |
| `/themes` | Change theme |
| `/help` | Show all commands |
| `/exit` `/quit` `/q` | Exit |

**Critical Keybinds:**

| Key | Action |
|-----|--------|
| `Tab` | Switch Build ↔ Plan agent |
| `Escape` | Stop generation |
| `<leader>u` | Undo |
| `<leader>r` | Redo |
| `<leader>m` | Model list |
| `<leader>c` | Compact |
| `<leader>a` | Agent list |
| `F2` | Cycle recent model |
| `Ctrl+P` | Command palette |

**CLI Commands:**

| Command | What It Does |
|---------|-------------|
| `opencode` | Start TUI |
| `opencode -p "..."` | Print mode (CI/CD) |
| `opencode -p "..." -q` | Quiet print mode |
| `opencode -p "..." -f json` | JSON output |
| `opencode auth login` | Add provider |
| `opencode models` | List models |
| `opencode agent create` | Create agent |
| `opencode mcp add` | Add MCP server |
| `opencode github install` | GitHub integration |
| `opencode update` | Update OpenCode |

### 13.2 Top 20 QA Prompts for OpenCode

1. *"Analyze this codebase and identify areas with zero test coverage."*
2. *"Generate unit tests for all public methods in @src/services/"*
3. *"Create E2E Playwright tests for the user registration flow."*
4. *"Write API tests from the Swagger spec at @docs/api-spec.yaml"*
5. *"Find all flaky test patterns using grep: Thread.sleep, hardcoded waits, shared state."*
6. *"Set up Page Object Model for our Selenium project."*
7. *"Create a GitHub Actions pipeline with parallel Selenium and Playwright."*
8. *"Generate 100 user test records with realistic fake data."*
9. *"Set up visual regression with Playwright snapshots."*
10. *"Aggregate JUnit, Allure, and Playwright reports into one summary."*
11. *"Write OWASP Top 10 security tests for our login endpoint."*
12. *"Create Docker Compose for Selenium Grid with 3 browser nodes."*
13. *"Add WCAG 2.1 AA accessibility tests with axe-core."*
14. *"Generate a Requirements Traceability Matrix from our test suite."*
15. *"Set up k6 performance tests: load (100 VUs), stress (500 VUs), spike (1000 VUs)."*
16. *"Create WireMock stubs for all external API dependencies."*
17. *"Identify which tests should be in the smoke suite based on risk and execution time."*
18. *"Configure Playwright traces on failure for CI debugging."*
19. *"Create database fixtures with setup/teardown for integration tests."*
20. *"Build a test metrics dashboard showing 30-day pass/fail trends."*

---

**Created by [Pramod Dutta](https://www.linkedin.com/in/pramoddutta/) | [TheTestingAcademy](https://thetestingacademy.com) | [YouTube](https://www.youtube.com/@TheTestingAcademy)**

*— End of OpenCode QA Tutorial —*
