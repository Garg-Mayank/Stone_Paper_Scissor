CONS = ["stone", "paper", "scissor"]

a = input("Enter name of Player 1 : ")
b = input("Enter name of Player 2 : ")
while True:
    print ("CHOICES AVAILABLE\n1 - stone\n2 - paper\n3 - scissor")
    a_answer = CONS[int(input("Enter choice for Player 1 :\n")) - 1]
    b_answer = CONS[int(input("Enter choice for Player 2 :\n")) - 1]
	
    if (a_answer == CONS[0] and b_answer == CONS[1]):
        print(b + " wins")

    elif (a_answer == CONS[1] and b_answer == CONS[0]):
        print(a + " wins")

    elif (a_answer == CONS[1] and b_answer == CONS[2]):
        print(b + " wins")

    elif (a_answer == CONS[2] and b_answer == CONS[1]):
        print(a + " wins")

    elif (a_answer == CONS[2] and b_answer == CONS[0]):
        print(b + " wins")

    elif (a_answer == CONS[0] and b_answer == CONS[2]):
        print(a + " wins")

    elif (a_answer == b_answer):
        print("Neither " + a + " nor " + b + " wins")

    else:
        print("Invalid Input")
	
    choice = input("Do you want to play the next round ? (y/n)\n")
    if choice == 'n':
        break

