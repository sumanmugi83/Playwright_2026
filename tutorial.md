# 🚀 LIVE Session – Automating QA Workflow Using OpenCode
## Full Prompts, Commands & Configuration Cheat Sheet
### (QA + Selenium + Playwright + API Testing)

---

## 💡 What is OpenCode?

**OpenCode** is an **open-source AI coding agent** built for the terminal. Think of it as having a senior developer sitting right next to you — helping you write, debug, test, and automate code using natural language.

### Why OpenCode for QA?
- **100% Open Source** — MIT Licensed, no vendor lock-in
- **100K+ GitHub Stars** — Trusted by 2.5M+ developers monthly, 700+ contributors
- **Any Model, Any Provider** — Claude, GPT, Gemini, Groq, local models — your choice
- **Terminal-First TUI** — Beautiful interactive interface built for power users
- **MCP Support** — Plug in Playwright, Selenium, Appium MCP servers for browser/mobile automation
- **Multi-Agent Architecture** — Built-in `Build` (full access) and `Plan` (read-only) agents + custom agents
- **Privacy-First** — Your code stays on your machine. OpenCode does not store any code or context data
- **IDE + Desktop + Web** — Available as CLI, VS Code extension, desktop app, and web interface

### OpenCode vs Other Tools
| Feature | OpenCode | Claude Code | Cursor |
|---------|----------|-------------|--------|
| Open Source | ✅ Yes (MIT) | ❌ No | ❌ No |
| Cost | Free (bring your API key) | $20/mo subscription | $20/mo subscription |
| Model Flexibility | 75+ models, any provider | Claude only | Multiple (limited) |
| Terminal TUI | ✅ Full TUI | ✅ CLI | ❌ IDE only |
| MCP Servers | ✅ Local + Remote | ✅ Limited | ✅ Limited |
| Custom Agents | ✅ Fully customizable | ❌ No | ❌ No |
| GitHub Actions Agent | ✅ Built-in | ❌ No | ❌ No |

### Key Links
| Resource | URL |
|----------|-----|
| 🌐 Website | [opencode.ai](https://opencode.ai) |
| 📖 Docs | [opencode.ai/docs](https://opencode.ai/docs) |
| 💻 GitHub | [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) |
| 🔑 Zen (Managed Models) | [opencode.ai/auth](https://opencode.ai/auth) |
| 💬 Discord | [opencode.ai/discord](https://opencode.ai/discord) |
| 📦 Download Desktop | [opencode.ai/download](https://opencode.ai/download) |

---

## 🔧 PART 1: Installation & Setup

### Install OpenCode
```bash
# Quick install (Linux/macOS)
curl -fsSL https://opencode.ai/install | bash

# Via npm
npm i -g opencode-ai@latest

# Via Homebrew (macOS/Linux - recommended, always up to date)
brew install anomalyco/tap/opencode

# Windows (Scoop)
scoop install opencode

# Windows (Chocolatey)
choco install opencode

# Arch Linux
sudo pacman -S opencode

# Verify installation
opencode --version

# Upgrade to latest
opencode upgrade

# Upgrade to specific version
opencode upgrade v0.1.48
```

---

## 🔑 PART 2: Credentials & Authentication

### Method 1: Using `/connect` (Inside TUI – Recommended)
```bash
# Launch OpenCode first
opencode

# Then inside the TUI, type:
/connect
# → Select your provider (Anthropic, OpenAI, Google, OpenCode Zen, etc.)
# → Follow the browser-based auth flow or paste your API key
```

### Method 2: Using CLI `auth login`
```bash
# Interactive login (prompts you to select provider)
opencode auth login

# This stores credentials in:
# ~/.local/share/opencode/auth.json
```

### Method 3: Environment Variables (.env or shell)
```bash
# Anthropic
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"

# OpenAI
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"

# Google Gemini
export GOOGLE_API_KEY="xxxxxxxxxxxxx"

# Groq
export GROQ_API_KEY="gsk_xxxxxxxxxxxxx"

# OpenRouter
export OPENROUTER_API_KEY="sk-or-xxxxxxxxxxxxx"

# xAI (Grok)
export XAI_API_KEY="xxxxxxxxxxxxx"

# You can also put these in a .env file in your project root
```

### Method 4: OpenCode Config File (opencode.json)
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "apiKey": "sk-ant-xxxxxxxxxxxxx"
    },
    "openai": {
      "apiKey": "sk-xxxxxxxxxxxxx"
    },
    "google": {
      "apiKey": "xxxxxxxxxxxxx"
    }
  }
}
```

### Method 5: OpenCode Zen (Easiest for Beginners)
```bash
# Inside TUI:
/connect
# → Select "opencode" (Zen)
# → Go to opencode.ai/auth in browser
# → Sign in, add billing, copy API key
# → Paste the key in terminal

# Zen gives you curated, tested models optimized for coding
```

### Manage Credentials
```bash
# List all authenticated providers
opencode auth list
opencode auth ls          # short version

# Logout from a provider
opencode auth logout
```

---

## 🤖 PART 3: Models & Providers

### Supported Providers
| Provider | Env Variable | Model Format |
|----------|-------------|--------------|
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic/claude-sonnet-4-5` |
| OpenAI | `OPENAI_API_KEY` | `openai/gpt-5` |
| Google Gemini | `GOOGLE_API_KEY` | `google/gemini-2.5-pro` |
| OpenCode Zen | Via `/connect` | `opencode/...` |
| Groq | `GROQ_API_KEY` | `groq/...` |
| OpenRouter | `OPENROUTER_API_KEY` | `openrouter/...` |
| AWS Bedrock | AWS credentials | `bedrock/...` |
| Azure OpenAI | Azure config | `azure/...` |
| xAI | `XAI_API_KEY` | `xai/grok-beta` |
| Z.AI (GLM) | `ZAI_API_KEY` | `zai/glm-4.7` |
| Cloudflare AI | Cloudflare config | Via gateway |
| Vercel AI Gateway | Vercel key | Via gateway |
| Local (Ollama/LM Studio) | `LOCAL_ENDPOINT` | `local/model-name` |

### Popular Models for QA Work
```
# Anthropic (Best for code quality)
anthropic/claude-sonnet-4-5          # Fast, great for daily QA tasks
anthropic/claude-opus-4-6            # Most capable, complex test architecture

# OpenAI
openai/gpt-5                        # Strong all-rounder
openai/gpt-5-mini                   # Faster, lighter tasks

# Google
google/gemini-2.5-pro               # Excellent for large context
google/gemini-2.5-flash             # Fast iterations
```

### Model Commands
```bash
# List all available models from CLI
opencode models

# List models for a specific provider
opencode models anthropic
opencode models openai
opencode models google

# Refresh models cache (when new models are released)
opencode models --refresh

# Verbose output with costs
opencode models --verbose

# Inside TUI:
/models                              # Opens model selector
```

### Configure Models in opencode.json
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "openai/gpt-5-mini"
}
```

### Pro Tip: Switching Models in TUI
```
/models → Select model from list
Ctrl+T  → Cycle through model variants (e.g., thinking mode)
Tab     → Switch between Build and Plan agents
```

---

## 🎨 PART 4: Themes

### Built-in Themes
```
opencode        → Default OpenCode theme
system          → Adapts to your terminal's colors (supports transparency)
catppuccin      → Popular pastel theme
dracula         → Dark theme with vibrant colors
+ many more built-in themes
```

### Theme Commands
```bash
# Inside TUI:
/theme                               # Opens theme picker (preview before selecting)

# In opencode.json:
{
  "$schema": "https://opencode.ai/config.json",
  "theme": "catppuccin"
}
```

### Install Community Themes
```bash
# Install 200+ base16/base24 themes
mkdir -p ~/.config/opencode
cd ~/.config/opencode
git clone https://github.com/scaryrawr/base16-opencode .

# Or symlink just the themes
git clone https://github.com/scaryrawr/base16-opencode
ln -s $PWD/base16-opencode/themes ~/.config/opencode/themes

# Dracula theme
# Download from draculatheme.com/opencode and place in themes/

# After adding themes, use /theme in TUI to select
```

### Custom Theme (Create Your Own)
```bash
# Create theme file
mkdir -p ~/.config/opencode/themes/
```

```json
// ~/.config/opencode/themes/qa-dark.json
{
  "name": "QA Dark",
  "defs": {
    "primary": "#61AFEF",
    "success": "#98C379",
    "error": "#E06C75",
    "warning": "#E5C07B"
  },
  "colors": {
    "background": "#1E1E2E",
    "foreground": "#CDD6F4",
    "primary": "$primary",
    "secondary": "#89B4FA"
  }
}
```

### Theme Directories (Priority Order)
```
1. ./.opencode/themes/          → Project-specific (highest priority)
2. ~/.config/opencode/themes/   → User-wide themes
3. Built-in themes              → Embedded in binary (lowest priority)
```

---

## 🔌 PART 5: MCP Servers for QA

### What is MCP?
MCP (Model Context Protocol) lets you add external tools to OpenCode. For QA, this means browser automation, code search, accessibility testing, and more — all controllable by the AI agent.

### 🎭 Playwright MCP (Official by Microsoft – MUST HAVE)
```json
// opencode.json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@anthropic-ai/mcp-server-playwright"],
      "enabled": true
    }
  }
}
```
**What it does:** Browser automation via accessibility tree (not screenshots). Navigate, click, fill forms, take screenshots, generate tests — all through natural language.

**Usage prompt:** `use the playwright tool to navigate to https://demo.site.com and test the login flow`

### 🌐 Selenium MCP
```json
{
  "mcp": {
    "selenium": {
      "type": "local",
      "command": ["npx", "-y", "mcp-selenium"],
      "enabled": true
    }
  }
}
```
**What it does:** Browser automation through Selenium WebDriver via MCP. Supports Chrome and Firefox.

### 📖 Context7 (Documentation Lookup)
```json
{
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "enabled": true
    }
  }
}
```
**What it does:** Fetches up-to-date, version-specific docs for libraries (Playwright, Selenium, TestNG, Jest, etc.) directly into your prompt.

**Usage prompt:** `use context7 to look up Playwright's page.route() API for request interception`

### 🔍 Grep by Vercel (GitHub Code Search)
```json
{
  "mcp": {
    "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app",
      "enabled": true
    }
  }
}
```
**What it does:** Searches public GitHub repos for code patterns. Great for finding test examples, framework patterns, or real-world implementations.

**Usage prompt:** `use the gh_grep tool to find Playwright Page Object Model examples in TypeScript`

### ♿ Accessibility MCP Scanner
```json
{
  "mcp": {
    "a11y_scanner": {
      "type": "local",
      "command": ["npx", "-y", "mcp-accessibility-scanner"],
      "enabled": true
    }
  }
}
```
**What it does:** AI-powered accessibility testing using Playwright + axe-core. Run WCAG compliance checks via natural language.

### 📱 Appium MCP (Mobile Testing)
```json
{
  "mcp": {
    "appium_gestures": {
      "type": "local",
      "command": ["npx", "-y", "mcp-appium-gestures"],
      "enabled": true
    }
  }
}
```
**What it does:** Automates complex mobile gestures (swipe, pinch, scroll) through MCP for Appium-based mobile testing.

### 🧪 UI Test Generator MCP
```json
{
  "mcp": {
    "test_generator": {
      "type": "local",
      "command": ["node", "/path/to/playwright-test-generator/cli.js"],
      "env": {
        "NODE_ENV": "production",
        "BROWSER_TYPE": "chromium",
        "HEADLESS": "true"
      },
      "enabled": true
    }
  }
}
```
**What it does:** Analyzes web apps and auto-generates test scripts for Playwright, Cypress, or Selenium. Supports test healing and manual-to-automated test conversion.

### MCP Management Commands
```bash
# CLI commands
opencode mcp add              # Interactive MCP server setup
opencode mcp list             # List configured MCP servers
opencode mcp ls               # Short version
opencode mcp auth <name>      # Authenticate OAuth MCP server
opencode mcp auth list        # List OAuth status
opencode mcp logout <name>    # Remove OAuth credentials
opencode mcp debug <name>     # Debug connection issues

# Inside TUI:
/mcp                          # View MCP server status
```

### Complete QA MCP Config (Copy-Paste Ready)
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "theme": "catppuccin",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@anthropic-ai/mcp-server-playwright"],
      "enabled": true
    },
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "enabled": true
    },
    "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app",
      "enabled": true
    }
  }
}
```

> ⚠️ **Note:** MCP servers add to your context window. Don't enable too many at once — keep only what you need for the current task. The GitHub MCP server in particular uses a lot of tokens.

---

## ⌨️ PART 6: All OpenCode Commands

### TUI Slash Commands (Inside OpenCode TUI)
| Command | Alias | Description |
|---------|-------|-------------|
| `/connect` | — | Add/manage provider credentials |
| `/models` | — | List and switch AI models |
| `/theme` | — | List and switch themes |
| `/new` | `/clear` | Start a new session |
| `/session` | `/resume`, `/continue` | List and switch between sessions |
| `/undo` | — | Undo last message + revert file changes |
| `/redo` | — | Redo previously undone message |
| `/compact` | — | Compact conversation history (save tokens) |
| `/share` | — | Share current session (generates link) |
| `/init` | — | Create/update AGENTS.md for current project |
| `/editor` | — | Export conversation to markdown, open in `$EDITOR` |
| `/mcp` | — | View MCP server status |
| `/thinking` | — | Toggle visibility of thinking/reasoning blocks |
| `/help` | — | Show help dialog |
| `/exit` | `/quit`, `/q` | Exit OpenCode |
| `/commands` | — | List all available commands |
| `/status` | — | Show current session status |
| `@filename` | — | Reference a file in your prompt |
| `@agent` | — | Invoke a subagent |

### TUI Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Tab` | Switch between Build ↔ Plan agents |
| `Ctrl+T` | Cycle through model variants (thinking mode) |
| `Ctrl+P` | Open command palette (searchable) |
| `Ctrl+X H` | Open help |
| `Ctrl+C` | Cancel current generation |
| `Ctrl+L` | Clear screen |
| `Enter` | Submit prompt |
| `Shift+Enter` | New line in prompt |
| Drag & Drop | Drop images into terminal for vision |

### CLI Commands (From Terminal)
```bash
# Core
opencode                              # Launch TUI
opencode [project-path]               # Launch in specific project
opencode -c                           # Continue last session
opencode -s <session-id>              # Continue specific session
opencode -m <provider/model>          # Start with specific model
opencode --agent <agent-name>         # Start with specific agent

# Non-Interactive Mode (Great for CI/CD)
opencode run "your prompt here"
opencode run "Run all tests" --model anthropic/claude-sonnet-4-5
opencode run -f test-report.html "Analyze this test report"
opencode run -c "Now fix the failing tests"    # Continue last session
opencode run --share "Generate test plan"       # Auto-share result

# Attach to Running Server (Avoids MCP cold boot)
opencode serve                         # Start headless server
opencode run --attach http://localhost:4096 "Run tests"

# Auth
opencode auth login                    # Interactive login
opencode auth list                     # List providers
opencode auth ls                       # Short version
opencode auth logout                   # Remove credentials

# Models
opencode models                        # List all models
opencode models anthropic              # Filter by provider
opencode models --refresh              # Refresh model cache
opencode models --verbose              # Show costs

# MCP Servers
opencode mcp add                       # Add MCP server (interactive)
opencode mcp list                      # List MCP servers
opencode mcp ls                        # Short version
opencode mcp auth <name>               # Authenticate OAuth server
opencode mcp auth list                 # List OAuth status
opencode mcp logout <name>             # Remove OAuth credentials
opencode mcp debug <name>              # Debug connection issues

# Agents
opencode agent create                  # Create custom agent
opencode agent list                    # List all agents

# Sessions
opencode session list                  # List all sessions
opencode session list -n 10            # Last 10 sessions
opencode session list --format json    # JSON output

# Statistics
opencode stats                         # All-time stats
opencode stats --days 7                # Last 7 days
opencode stats --models 5              # Top 5 models used
opencode stats --tools 10              # Top 10 tools used

# Import/Export
opencode export <session-id>           # Export session as JSON
opencode import session.json           # Import from file
opencode import https://opncd.ai/s/abc123  # Import from shared URL

# Server
opencode serve                         # Start headless API server
opencode serve --port 4096             # Custom port
opencode web                           # Start server + open web UI
opencode acp                           # Start ACP server (for IDEs)

# GitHub Agent
opencode github install                # Install GitHub Actions agent
opencode github run                    # Run GitHub agent

# Attach to Remote Server
opencode attach http://10.20.30.40:4096

# Maintenance
opencode upgrade                       # Update to latest
opencode upgrade v0.1.48               # Specific version
opencode uninstall                     # Full uninstall
opencode uninstall --dry-run           # Preview what would be removed
opencode uninstall --keep-config       # Keep config files

# Global Flags
opencode --version                     # Print version
opencode --help                        # Show help
opencode --print-logs                  # Print logs to stderr
opencode --log-level DEBUG             # Set log level
```

### Environment Variables
| Variable | Description |
|----------|-------------|
| `OPENCODE_AUTO_SHARE` | Auto-share sessions |
| `OPENCODE_CONFIG` | Custom config file path |
| `OPENCODE_CONFIG_DIR` | Custom config directory |
| `OPENCODE_CONFIG_CONTENT` | Inline JSON config |
| `OPENCODE_DISABLE_AUTOUPDATE` | Disable auto-updates |
| `OPENCODE_DISABLE_AUTOCOMPACT` | Disable auto context compaction |
| `OPENCODE_ENABLE_EXPERIMENTAL_MODELS` | Enable experimental models |
| `OPENCODE_ENABLE_EXA` | Enable Exa web search tools |
| `OPENCODE_SERVER_PASSWORD` | Enable basic auth for serve/web |
| `OPENCODE_PERMISSION` | Inline JSON permissions config |
| `OPENCODE_CLIENT` | Client identifier (default: `cli`) |

---

## 🧪 PART 7: Selenium Test Automation Prompts

### Prompt 1 – Scaffold a Selenium Project from Scratch
```
Create a complete Selenium Java TestNG project with the following:
- Maven pom.xml with Selenium 4, TestNG, WebDriverManager, ExtentReports dependencies
- Page Object Model (POM) design pattern
- Base test class with WebDriver setup/teardown using WebDriverManager
- A config.properties file for browser, baseURL, and timeout settings
- A utility class for common actions (click, sendKeys, waitForElement, screenshot)
- Folder structure: src/main/java (pages, utils) and src/test/java (tests)
- testng.xml with parallel execution support
- .gitignore for Java/Maven projects
```

### Prompt 2 – Generate Page Objects for a Login Page
```
Create a LoginPage class using Page Object Model for a login page with:
- URL: https://demo.example.com/login
- Elements: username field (id="username"), password field (id="password"), 
  login button (id="loginBtn"), error message (class="error-msg"), 
  remember me checkbox (id="rememberMe")
- Methods: enterUsername(), enterPassword(), clickLogin(), 
  loginWith(username, password), getErrorMessage(), isErrorDisplayed()
- Use explicit waits (WebDriverWait) for all element interactions
- Add proper logging with Log4j2
```

### Prompt 3 – Generate Selenium Test Cases
```
Write TestNG test class LoginTest with these test cases for the LoginPage:
1. testValidLogin - login with valid credentials and verify dashboard page loads
2. testInvalidPassword - verify error message for wrong password
3. testEmptyCredentials - verify validation for empty fields
4. testRememberMe - verify remember me checkbox functionality
5. testLoginLogout - full login-logout cycle

Use @BeforeMethod, @AfterMethod, @DataProvider for data-driven tests.
Add soft assertions where appropriate. Include ExtentReports logging for each step.
Read test data from a testdata.json file.
```

### Prompt 4 – Fix Flaky Selenium Tests
```
My Selenium tests are flaky. Analyze the test files in src/test/java/ and:
1. Replace Thread.sleep() with explicit waits
2. Add retry logic using TestNG IRetryAnalyzer
3. Fix any stale element reference issues
4. Add proper synchronization for AJAX calls
5. Implement fluent waits where needed
6. Add screenshot capture on test failure using TestNG listeners

Show me a before/after comparison of what you changed and why.
```

### Prompt 5 – Add Cross-Browser Testing
```
Update the framework to support cross-browser testing:
- Chrome, Firefox, Edge support via WebDriverManager
- Browser selection through testng.xml parameters and config.properties
- Headless mode option for CI/CD
- Create a testng-crossbrowser.xml that runs tests in parallel across all 3 browsers
- Add browser-specific capabilities (Chrome options, Firefox profile)
```

---

## 🎭 PART 8: Playwright Test Automation Prompts

### Prompt 6 – Scaffold a Playwright Project
```
Create a complete Playwright TypeScript test project with:
- package.json with @playwright/test and required dev dependencies
- playwright.config.ts with multi-browser setup (chromium, firefox, webkit)
- Base URL configuration for https://demo.example.com
- Screenshot on failure, video recording on retry, trace on first retry
- Custom fixtures for authenticated state
- Folder structure: tests/, pages/, utils/, test-data/, fixtures/
- Global setup for authentication state storage
- Reporter config: HTML reporter + JUnit for CI
```

### Prompt 7 – Migrate Selenium Tests to Playwright
```
I have Selenium Java Page Object tests in src/. Convert them to Playwright TypeScript:
- Convert all Page Objects to Playwright page classes with locators
- Replace WebDriverWait with Playwright's built-in auto-waiting
- Convert TestNG assertions to Playwright expect assertions
- Replace @DataProvider with Playwright's test.describe + parameterized tests
- Convert XPath/CSS selectors to Playwright's recommended locators 
  (getByRole, getByText, getByTestId, getByLabel)
- Maintain the same test coverage and test case structure

Show me the mapping of what changed between Selenium and Playwright approaches.
```

### Prompt 8 – E2E Checkout Flow with Playwright
```
Create a complete E2E test for an ecommerce checkout flow in Playwright:
- Test flow: Search product → Add to cart → View cart → Checkout → 
  Fill shipping → Fill payment → Place order → Verify confirmation
- Use Page Object Model with these pages: SearchPage, ProductPage, 
  CartPage, CheckoutPage, ConfirmationPage
- Include API mocking for payment gateway using page.route()
- Add visual regression test using toHaveScreenshot()
- Include accessibility checks using @axe-core/playwright
- Network request interception to validate API calls
- Test data from JSON fixtures
```

### Prompt 9 – Playwright API + UI Hybrid Tests
```
Create hybrid tests that combine Playwright API and UI testing:
1. Test 1: Create user via API → Login via UI → Verify profile displayed
2. Test 2: Create product via API → Search via UI → Verify product details
3. Test 3: Place order via UI → Verify order status via API
4. Test 4: Update settings via API → Refresh UI → Verify changes reflected

Use Playwright's request context for API calls.
Store auth tokens from API and inject into browser context.
Add proper setup/teardown to clean test data.
```

### Prompt 10 – Generate Playwright Test from User Story
```
Here is a user story. Generate complete Playwright tests for it:

"As a registered user, I want to reset my password so that I can regain 
access to my account if I forget it."

Acceptance Criteria:
- User clicks 'Forgot Password' on login page
- User enters registered email
- System sends reset link (mock the email API)
- User clicks reset link and lands on reset page
- User enters new password (min 8 chars, 1 uppercase, 1 number)
- Password validation errors shown for weak passwords
- Success message displayed after reset
- User can login with new password

Generate: Page objects, test file with positive + negative cases, 
test data, and any required fixtures.
```

---

## 🔌 PART 9: API Test Automation Prompts

### Prompt 11 – API Testing Framework Setup
```
Create a REST API testing framework using:
- TypeScript with Playwright's APIRequestContext
- OR Java with RestAssured (ask me which one to use)
- Base configuration for multiple environments (dev, staging, prod)
- Authentication helper (Bearer token, OAuth2, API key)
- Request/Response logging interceptor
- JSON schema validation using ajv (TS) or json-schema-validator (Java)
- Custom assertions for status codes, headers, response time
- Test data builder pattern for request payloads
- Environment-specific .env files
- Allure reporting integration
```

### Prompt 12 – CRUD API Test Suite
```
Generate a complete API test suite for a User Management API:

Endpoints:
- POST /api/users - Create user
- GET /api/users/{id} - Get user by ID
- GET /api/users?page=1&limit=10 - List users with pagination
- PUT /api/users/{id} - Update user
- PATCH /api/users/{id} - Partial update
- DELETE /api/users/{id} - Delete user

For each endpoint, write tests for:
- Happy path (200/201 responses)
- Validation errors (400 - missing/invalid fields)
- Authentication errors (401 - no token, expired token)
- Authorization errors (403 - insufficient permissions)
- Not found (404)
- Duplicate resource (409)
- Response schema validation
- Response time assertions (< 500ms)
- Chained tests: Create → Read → Update → Delete lifecycle
```

### Prompt 13 – Contract Testing
```
Create API contract tests for our microservices:
1. Read the OpenAPI/Swagger spec from docs/api-spec.yaml
2. Auto-generate contract tests that validate:
   - All response schemas match the spec
   - Required fields are always present
   - Enum values match allowed values from spec
   - Response status codes match documented codes
   - Content-Type headers are correct
3. Generate a report showing coverage: 
   which endpoints and status codes are tested vs documented
4. Flag any undocumented endpoints found during testing
```

### Prompt 14 – Performance API Tests
```
Add performance/load testing capabilities:
- Use k6 (JavaScript) for load testing our API
- Scenarios: 
  1. Smoke test: 1 VU, 1 minute
  2. Load test: 50 VUs ramping up over 5 mins, sustain for 10 mins
  3. Stress test: ramp to 200 VUs over 10 mins
  4. Spike test: sudden jump to 100 VUs
- Thresholds: p95 < 500ms, error rate < 1%, throughput > 100 rps
- Test endpoints: GET /api/users, POST /api/orders, GET /api/products/search
- Custom metrics for business transactions
- HTML report generation
- CI integration script
```

---

## 🤖 PART 10: AI-Powered QA Workflows

### Prompt 15 – Auto-Generate Tests from Source Code
```
Analyze the source code in src/main/java/com/app/services/ and:
1. Identify all public methods and their business logic
2. Generate unit tests with edge cases I might have missed
3. Generate integration tests for service-to-service interactions
4. Calculate current code coverage and suggest tests to improve it
5. Focus especially on: null handling, boundary values, 
   exception scenarios, and concurrent access patterns
6. Use JUnit 5 with Mockito for mocking dependencies
```

### Prompt 16 – Bug Analysis and Test Gap Detection
```
I have a bug report log in bugs.csv. Analyze it and:
1. Identify the most bug-prone modules/features
2. Map each bug to existing test cases in tests/ directory
3. Find gaps: which bugs had no corresponding test?
4. Generate NEW test cases to cover those gaps
5. Prioritize tests by bug severity and frequency
6. Create a test gap analysis report in markdown

Also suggest what types of tests are missing (unit/integration/e2e/performance).
```

### Prompt 17 – Generate Test Plan from PRD
```
Read the requirements document requirements.md and generate:
1. A comprehensive test plan with:
   - Test strategy (what levels of testing needed)
   - In-scope and out-of-scope items
   - Entry/exit criteria
   - Risk analysis with mitigation
   - Test environment requirements
   - Test data requirements
2. Test scenarios mapped to each requirement (traceability matrix)
3. Detailed test cases in a structured format:
   TC_ID | Priority | Precondition | Steps | Expected Result | Type
4. Automation candidates marked (which tests to automate first)
5. Export as a formatted markdown document
```

### Prompt 18 – CI/CD Pipeline for Tests
```
Create a complete CI/CD pipeline configuration:

For GitHub Actions:
1. .github/workflows/qa-pipeline.yml that:
   - Triggers on PR and push to main
   - Runs unit tests first (fast feedback)
   - Runs API tests in parallel
   - Runs Playwright E2E tests with sharding (4 shards)
   - Runs Selenium cross-browser tests
   - Generates consolidated test report
   - Uploads Allure/HTML reports as artifacts
   - Posts test summary as PR comment
   - Fails PR if any critical tests fail
   - Runs performance tests on main branch only (nightly)

2. Docker setup for test execution
3. Slack notification on failures
```

### Prompt 19 – Smart Test Selection
```
Analyze the git diff of the current PR and:
1. Identify which source files changed
2. Map changed files to dependent test files
3. Determine which tests are affected by the changes
4. Create a filtered test suite that runs ONLY affected tests
5. Generate the command to run just those tests
6. Estimate time saved vs running the full suite
7. Flag if changes affect shared utilities that need full regression
```

---

## ⚡ PART 11: Quick Utility Prompts (One-Liners)

```
# Generate test data
Create a test data generator that creates 100 realistic user profiles 
with: name, email, phone, address, DOB. Export to JSON and CSV.
```

```
# Fix all test compilation errors
Scan all test files, fix compilation errors, update deprecated methods, 
and ensure all tests pass. Show me a summary of changes.
```

```
# Add logging to all tests
Add structured logging (Log4j2/Winston) to all test files. Log test start, 
each major step, assertions, and test end with PASS/FAIL status.
```

```
# Generate Allure annotations
Add Allure reporting annotations to all existing test methods:
@Epic, @Feature, @Story, @Step, @Description, @Severity
Map them logically based on test file location and test names.
```

```
# Create test documentation
Read all test files and generate:
1. Test inventory spreadsheet (test name, type, module, priority, status)
2. README.md for the test framework with setup instructions
3. Architecture diagram using Mermaid
```

```
# Database test cleanup script
Create a database cleanup utility that:
- Identifies test data by prefix/pattern (test_, auto_)
- Safely removes it in correct order (respecting foreign keys)  
- Runs before and after test suites
- Logs what was cleaned
```

---

## 🛠️ PART 12: Custom QA Commands for OpenCode

Create these as markdown files in `.opencode/commands/` for your QA projects:

### /test command
```markdown
<!-- .opencode/commands/test.md -->
---
description: Run the full test suite with coverage
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

### /flaky command
```markdown
<!-- .opencode/commands/flaky.md -->
---
description: Find and fix flaky tests
---

Analyze test results for flaky patterns. Look for:
- Tests that pass/fail inconsistently
- Race conditions or timing issues
- Missing waits or synchronization
- Environment-dependent behavior
Fix them and explain each change.
```

### /testplan command
```markdown
<!-- .opencode/commands/testplan.md -->
---
description: Generate test plan from requirements
---

Read all requirement documents in the project and generate a comprehensive
test plan with test cases, traceability matrix, and automation candidates.
Export as markdown.
```

### /coverage command
```markdown
<!-- .opencode/commands/coverage.md -->
---
description: Analyze and improve test coverage
---

Run coverage analysis and identify gaps. Generate new tests for 
uncovered critical paths. Focus on business logic and edge cases.
```

---

## 🎯 PART 13: Pro Tips & Session Flow

### OpenCode Power User Tips
```bash
# Run in non-interactive mode (great for CI/CD)
opencode run "Run all tests and fix any failures"

# Use Plan mode first, then Build mode
# Tab → Switch to Plan agent (read-only analysis)
# Get the plan, then Tab back to Build to execute

# Multi-session parallel work
# Open multiple terminals, each with its own OpenCode session
# Session 1: API tests | Session 2: UI tests | Session 3: Bug fixes

# Start server once, reuse for multiple runs (no MCP cold boot)
opencode serve --port 4096
opencode run --attach http://localhost:4096 "Fix the login test"
opencode run --attach http://localhost:4096 "Add new API tests"

# Check your spend
opencode stats --days 7 --models 5

# Reference specific files in prompts
# Type @ then filename to include it in context
```

### Suggested 60-Min Live Session Flow
```
Step 1:  [5 min]  → Install OpenCode + Auth Setup + Theme
Step 2:  [5 min]  → Walk through all commands + MCP config
Step 3:  [10 min] → Scaffold Selenium framework (Prompt 1-2)
Step 4:  [10 min] → Generate + run tests (Prompt 3)
Step 5:  [10 min] → Create Playwright project (Prompt 6)
Step 6:  [5 min]  → Migrate Selenium → Playwright (Prompt 7)
Step 7:  [5 min]  → API testing framework (Prompt 11-12)
Step 8:  [5 min]  → AI test generation from code (Prompt 15)
Step 9:  [3 min]  → CI/CD pipeline (Prompt 18)
Step 10: [2 min]  → Q&A + Wrap up
```

---

## 📌 YouTube Title & Description

### Title Options
```
1. 🚀 I Automated My ENTIRE QA Workflow Using AI | OpenCode Full Tutorial
2. AI Writes ALL My Tests Now — Selenium + Playwright + API | OpenCode 2026
3. QA Engineers: This AI Tool Just Changed EVERYTHING | OpenCode Tutorial
```

### Description Keywords
```
opencode qa automation, ai testing tutorial, selenium playwright ai, 
automated testing with ai, opencode tutorial 2026, qa workflow automation,
ai test generation, playwright typescript testing, selenium java ai,
api testing automation, ai powered qa, the testing academy, opencode mcp,
playwright mcp server, opencode commands, opencode themes
```

---

> **💡 Reminder:** Always review AI-generated tests before pushing to CI. 
> Validate selectors, assertions, and test data for your actual application.
> OpenCode is a tool to 10x your speed — not replace your QA brain! 🧠
