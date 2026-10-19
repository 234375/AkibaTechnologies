secret_number = 5
attempt = 0

while attempt < 5:
    guess = int(input("Guess the secret number from 1 UpTo 10: ")) #we put the input part inside the loop because we want to iterate it if the guess is wrong.
    attempt += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break

    else:
        if attempt==5:
            print ("Game Over.")
        else:
            print("Not correct .Try again.")