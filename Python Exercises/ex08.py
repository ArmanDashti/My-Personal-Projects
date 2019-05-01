while True:
    p1 = input("Rock, Paper, Scissor? ")
    p2 = input("Rock, Paper, Scissor? ")
    if p1 == "quit" or p2 == "quit":
        print("Game Has Ended.")
        break
    if p1 == "Rock" and p2 == "Rock":
        print("No Winner.")
        continue
    elif p1 == "Rock" and p2 == "Paper":
        print("Player 2 Wins.")
        continue
    elif p1 == "Rock" and p2 == "Scissor":
        print("Player 1 Wins.")
        continue
    elif p1 == "Paper" and p2 == "Rock":
        print("Player 1 Wins.")
        continue
    elif p1 == "Paper" and p2 == "Paper":
        print("No Winner.")
        continue
    elif p1 == "Paper" and p2 == "Scissor":
        print("Player 2 Wins.")
        continue
    elif p1 == "Scissor" and p2 == "Rock":
        print("Player 2 Wins.")
        continue
    elif p1 == "Scissor" and p2 == "Paper":
        print("Player 1 Wins.")
        continue
    elif p1 == "Scissor" and p2 == "Scissor":
        print("No Winner.")
        continue