import inquirer
questions = [
  inquirer.List('size',
                message="which file do you what to open?",
                choices=[''],
            ),
]
answers = inquirer.prompt(questions)