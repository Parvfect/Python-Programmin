

""" Number Guessing Game - Check if a number is equal to the secret number and give indication of how close it is """


secret_number = 42

user_input = int(input("Enter a number between 1 to 100"))

max_guesses, min_guesses = 20, 1


for i in range(min_guesses, max_guesses):
    
    if user_input != secret_number:
        
        if abs(secret_number - user_input) <= 5:
            print("Hot")
        elif abs(secret_number - user_input) <= 20:
            print("Warm")
        else: 
            print("Cold")

        user_input = int(input("Enter a number between 1 and 100"))
        continue    
    
    print("Well guessed! The number was {}".format(secret_number))
    break

print("You have exhausted your attempts! Please try again!")


    

