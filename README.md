# Create environment

python -m venv .venv
.venv\Scripts\activate

# Generate test

python cli.py gen "User transfers with missing account number"
python cli.py gen "User tries to pay bill with expired card" --retry 3 --temperature 0.9
python cli.py gen "User logs in with wrong password" --show_prompt True

# Mistral version - Download and keep it in the model

mistralai/Mistral-7B-Instruct-v0.1

# Script generator

python cli.py write outputs/user_logs_in_with_incorrect_password_20250418_XXXX/gen_1.txt --framework playwright
