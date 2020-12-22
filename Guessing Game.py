secret_word = "Lion"
guess = input("Enter a guess: ")
guesses = []
total = 0

print(guess)
print("You guessed " + guess)

while guess != secret_word:
    guesses.append(guess)
    total = total+1
    print("Not quite. Try again!")
    guess = input("Enter a guess: ")

guesses.append(guess)
total = total+1
print("Correct! You guessed the word!")


print(guesses)
print("It took you " + str(total) + " guesses to guess the correct word")
