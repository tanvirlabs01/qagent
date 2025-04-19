from core.writer.step_to_code import convert_step_to_code

def convert_to_playwright(scenario: str, feature: str) -> str:
    lines = scenario.strip().splitlines()

    steps = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("1.") or stripped[0].isdigit():
            steps.append(stripped.lstrip("0123456789. ").strip())

    test_code = [
        f'// Test for: {feature}',
        'import { test, expect } from "@playwright/test";',
        '',
        'test("Auto-generated scenario", async ({ page }) => {',
        '  await page.goto("http://parabank.parasoft.com");'
    ]

    for step in steps:
        try:
            code = convert_step_to_code(step)
            test_code.append(f"  {code}")
        except Exception as e:
            test_code.append(f"  // Failed to convert: {step}")
            test_code.append(f"  // Error: {e}")

    test_code.append('});')

    return "\n".join(test_code)
