def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer. Try again: ")
            attempt += 1
    if attempt == 3:
        print(f"The correct answer is {answer}")

score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest animal on land? ")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "whale")
print(f"Your score is {score}")
