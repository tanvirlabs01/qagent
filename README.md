# Create environment

python -m venv .venv
.venv\Scripts\activate

# Generate test

python cli.py gen "User transfers with missing account number"
python cli.py gen "User tries to pay bill with expired card" --retry 3 --temperature 0.9
python cli.py gen "User logs in with wrong password" --show_prompt True
