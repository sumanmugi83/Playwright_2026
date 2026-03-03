import re
import traceback
from llm_client import generate_text

def clean_code_block(text):
    """
    Extracts code from markdown code blocks if present.
    """
    if "```typescript" in text:
        return text.split("```typescript")[1].split("```")[0].strip()
    if "```javascript" in text:
        return text.split("```javascript")[1].split("```")[0].strip()
    if "```" in text:
        return text.split("```")[1].split("```")[0].strip()
    return text.strip()

def convert_gherkin_to_playwright(gherkin_content):
    """
    Converts gherkin content to Playwright Playwright code.
    Uses regex for structure parsing and LLM for step generation.
    """
    try:
        # Extract Feature Name
        feature_match = re.search(r'Feature:\s*(.*)', gherkin_content)
        feature_name = feature_match.group(1).strip() if feature_match else "Gherkin Feature"

        # Split into Scenarios (Basic regex split)
        scenarios_raw = re.split(r'Scenario:\s*', gherkin_content)
        
        output_code = f"import {{ test, expect }} from '@playwright/test';\n\n"
        output_code += f"test.describe('{feature_name}', () => {{\n\n"

        for i, raw in enumerate(scenarios_raw):
            if i == 0 and "Feature:" in raw:
                # The first chunk usually contains the Feature description, skip or parse background
                continue
            
            lines = raw.strip().split('\n')
            scenario_name = lines[0].strip()
            steps = "\n".join(lines[1:]).strip()
            
            # Use LLM to generate the test body for this scenario
            prompt = f"""
            You are a code generator. Write the body of a Playwright test for these steps.
            
            Scenario: {scenario_name}
            Steps:
            {steps}
            
            Rules:
            1. Output ONLY the code inside the test function.
            2. Use `await page.click(...)`, `await expect(...)` etc.
            3. Do NOT wrap it in `test(...)`.
            4. Do NOT include imports.
            5. Do NOT use markdown backticks.
            """
            
            generated_steps = generate_text(prompt)
            if generated_steps:
                generated_steps = clean_code_block(generated_steps)
            else:
                generated_steps = f"// Failed to generate steps via LLM for: {scenario_name}"

            output_code += f"  test('{scenario_name}', async ({{ page }}) => {{\n"
            output_code += "    // Generated steps\n"
            # Indent generated steps
            indented_steps = "\n".join([f"    {line}" for line in generated_steps.split('\n')])
            output_code += indented_steps
            output_code += "\n  });\n\n"

        output_code += "});"
        
        return {
            "status": "success",
            "files": [
                {
                    "filename": f"{feature_name.lower().replace(' ', '_')}.spec.ts",
                    "content": output_code
                }
            ]
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "status": "error",
            "logs": [str(e)]
        }

if __name__ == "__main__":
    # Test
    sample_gherkin = """
    Feature: Login
    
    Scenario: Successful Login
        Given I am on the login page
        When I enter valid credentials
        Then I should see the dashboard
    """
    print(convert_gherkin_to_playwright(sample_gherkin))
