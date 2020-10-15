import random

print("----------------------------------------------------\n"
      "   ---------------------------------------------\n"
      "         -------------------------------\n"
      "                  ---------------\n"
      "                       -----\n"
      "\n"
      "             WELCOME ROCK PAPER SCISSOR\n"
      "\n"
      "                       -----\n"
      "                  ---------------\n"
      "         -------------------------------\n"
      "   ---------------------------------------------\n"
      "----------------------------------------------------\n")

print("------------------------->>> You have 3 choices: Scissors, Paper, Rock ! <<<-------------------------")

while(True):
    z = input("Enter your choice: ")
    choiceList = ["Rock", "Scissors", "Paper"]
    compChoice = random.choice(choiceList);
    if (z.lower() == "rock") & (compChoice == "Rock"):
        print("Computer's choice: " + compChoice)
        print("Tie\n")

    if (z.lower() == "rock") & (compChoice == "Scissors"):
        print("Computer's choice: " + compChoice)
        print("Conguratulations, You won the computer...\n")

    if (z.lower() == "rock") & (compChoice == "Paper"):
        print("Computer's choice: " + compChoice)
        print("Computer won! Try Again...\n")

    if (z.lower() == "scissors") & (compChoice == "Scissors"):
        print("Computer's choice: " + compChoice)
        print("Tie\n")

    if (z.lower() == "scissors") & (compChoice == "Rock"):
        print("Computer's choice: " + compChoice)
        print("Computer won! Try Again...\n")

    if (z.lower() == "scissors") & (compChoice == "Paper"):
        print("Computer's choice: " + compChoice)
        print("Conguratulations, You won the computer...\n")

    if (z.lower() == "paper") & (compChoice == "Paper"):
        print("Computer's choice: " + compChoice)
        print("Tie\n")

    if (z.lower() == "paper") & (compChoice == "Scissors"):
        print("Computer's choice: " + compChoice)
        print("Computer won! Try Again...\n")

    if (z.lower() == "paper") & (compChoice == "Rock"):
        print("Computer's choice: " + compChoice)
        print("Conguratulations, You won the computer...\n")

    if (z.lower() != "paper") | (z.lower() != "rock") | (z.lower() != "scissor"):
        print("Error... Input is wrong ! TRY AGAIN !!!\n")



