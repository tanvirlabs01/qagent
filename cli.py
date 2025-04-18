import fire
from core.generator.generate import generate_test_scenario
from pathlib import Path
from datetime import datetime

class QAgentCLI:
    def gen(self, feature: str, template: str = "test_plain.txt", retry: int = 1, max_tokens: int = 1024, temperature: float = 0.7, show_prompt: bool = False):
        """
        Generate test scenarios from a user story.

        Args:
            feature: The user story (e.g., "User resets password")
            template: Prompt template to use (default: test_plain.txt)
            retry: Number of different generations to produce (default: 1)
            max_tokens: Maximum number of tokens to generate
            temperature: Model creativity (higher = more diverse)
            show_prompt: Print the full prompt for debugging
        """
        # Create a unique folder name
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

            # Save output
            out_path = run_folder / f"gen_{i+1}.txt"
            out_path.write_text(result, encoding="utf-8")

            # Display output
            print(result)
            print(f"\n💾 Saved to: {out_path}")

            # Optionally show the prompt used
            if show_prompt:
                print("\n📤 Prompt used:\n")
                print(full_prompt)

    def save_output(self, feature: str, content: str) -> str:
        filename = (
            "test_" +
            feature.lower().replace(" ", "_").replace(".", "") +
            "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        )
        path = Path("outputs") / filename
        path.write_text(content, encoding="utf-8")
        return str(path)

if __name__ == "__main__":
    fire.Fire(QAgentCLI)
