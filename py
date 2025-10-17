def guessing():
    list = []
    import random
    actual = random.randint(1, 10)
    guess = int(input("Guess a number between 1 to 10?"))
    while guess != actual:
        if guess > 10 or guess < 1:
            print ("You HAVE to guess a number between 1 to 10")
        elif 11 > guess > actual:
            print ("Your guess is too high")
        else:
            print ("Your guess is too low")
        print ("Guess again")
        list.append (guess)
        print (f"This is your history {list}")
        guess = int(input("What is your guess?"))
    if guess == actual:
        print ("Correct!")
guessing()