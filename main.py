import inquirer
import os

python_files = [file for file in os.listdir('.') if file.endswith('.py')]

if not python_files:
    print("No Python files found in the current directory.")
    exit()

choices = [f"{index + 1}. {file}" for index, file in enumerate(python_files)]

questions = [
    inquirer.List(
        'choice',
        message="Which file do you want to open and run?",
        choices=choices,  
    ),
]


answers = inquirer.prompt(questions)

selected_index = int(answers['choice'].split('.')[0]) - 1
selected_file = python_files[selected_index]


print(f"You selected: {selected_file}")

try:
    exec(open(selected_file).read())
except Exception as e:
    print(f"An error occurred: {e}")
    