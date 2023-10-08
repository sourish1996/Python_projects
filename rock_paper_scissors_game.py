import random
user_choice = int(input("Enter your choice :  Type 0 for Rock , 1 for Paper , 2 for scissors "))
computer_choice = random.choice([0, 1, 2])
print("computer_choice: ")
print(computer_choice)
if computer_choice == user_choice : 
    print ("It's a Draw ")
elif computer_choice > user_choice : 
    print ("You lose ")  
elif computer_choice < user_choice : 
    print ("You won ")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You won")    