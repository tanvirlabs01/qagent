import fire
from pathlib import Path
from datetime import datetime
from core.generator.generate import generate_test_scenario
from core.writer.playwright_writer import convert_to_playwright

class QAgentCLI:
    def gen(self, feature: str, template: str = "test_plain.txt", retry: int = 1, max_tokens: int = 1024, temperature: float = 0.7, show_prompt: bool = False):
        """
        Generate test scenarios from a user story.

        Args:
            feature: The user story or feature to test.
            template: Prompt template file to use (default: test_plain.txt)
            retry: Number of variations to generate (default: 1)
            max_tokens: Maximum number of tokens to generate
            temperature: Model creativity (0.1 = strict, 1.0 = creative)
            show_prompt: Print the full prompt used
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"{feature.lower().replace(' ', '_')}_{timestamp}"
        run_folder = Path("outputs") / folder_name
        run_folder.mkdir(parents=True, exist_ok=True)

        for i in range(retry):
            print(f"\n🔁 Generating variation {i+1}/{retry}...\n")

            result, full_prompt = generate_test_scenario(
                feature,
                template_name=template,
                max_tokens=max_tokens,
                temperature=temperature,
                return_prompt=True
            )

            out_path = run_folder / f"gen_{i+1}.txt"
            out_path.write_text(result, encoding="utf-8")

            print(result)
            print(f"\n💾 Saved to: {out_path}")

            if show_prompt:
                print("\n📤 Prompt used:\n")
                print(full_prompt)

    def write(self, input_file: str, framework: str = "playwright"):
        """
        Convert a plain text scenario into code for a specified test framework.

        Args:
            input_file: Path to .txt scenario file (from 'gen')
            framework: Target test framework (default: playwright)
        """
        input_path = Path(input_file)
        if not input_path.exists():
            print(f"❌ Input file not found: {input_file}")
            return

        scenario = input_path.read_text(encoding="utf-8")
        feature = input_path.stem.replace("_", " ")

        if framework.lower() == "playwright":
            code = convert_to_playwright(scenario, feature)

            output_dir = Path("outputs") / "scripts"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / (input_path.stem + ".spec.ts")
            output_file.write_text(code, encoding="utf-8")

            print(f"✅ Playwright test saved to: {output_file}")
            print("\n📄 Preview:\n")
            print(code)
        else:
            print(f"❌ Unsupported framework: {framework}")

if __name__ == "__main__":
    fire.Fire(QAgentCLI)
