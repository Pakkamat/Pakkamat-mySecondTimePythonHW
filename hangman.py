word = "hangman"
y = ''
turns = 8
while turns > 0:
    failed = 0
    # Print the words that contain in word put in y
    for i in word:
        if i in y:
            print(i, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    # If u have all word == Win
    if failed == 0:
        print(">> You survived !")
        break
    x = input("Input a letter: > ")
    # put x in y
    y += x
    # x not in word turns or times -1
    if x not in word:
        turns -= 1
        print("No such letter in the word")
    #print("You have", + turns, 'lives')
    # if turn = 0 >>> lose
    if turns == 0:
        print("You hanged")
