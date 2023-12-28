import random

def listing():
    list_length = random.randint(3, 10)
    random_list = [random.randint(0, 2) for _ in range(list_length)]
    return random_list


def printinfo(mylist, health, score, x):
    friend = list(filter(lambda x: x == 0, mylist))
    enemy = list(filter(lambda x: x == 1, mylist))
    button = list(filter(lambda x: x == 2, mylist))
    print("Game List:", mylist)
    print("There are", len(friend), "friends and", len(enemy), "enemies")
    print("Your health is", health)
    print("Your score is", score)
    print("-----------------------------------")

def interacting(health, score, mylist, index):
    if mylist[index] == 0:
        print("You see a friend")
        print("1 - Interact")
        print("2 - Ignore")
        interaction = input("What will you do? ")
        if interaction == "1":
            health += random.randint(1, 3)
            score -= 1

    elif mylist[index] == 1:
        print("You see an enemy")
        print("1 - Interact")
        print("2 - Ignore")
        interaction = input("What will you do? ")
        if interaction == "1":
            health -= random.randint(1, 3)
            score += 1

    elif mylist[index] == 2:
        print("You see a button")
        print("1 - Interact")
        print("2 - Ignore")
        interaction = input("What will you do? ")
        if interaction == "1":
            choice = random.choice([0, 1])
            mylist = list(map(lambda x: 1 - x if x == choice else x, mylist))

    return health, score, mylist

def game():
    health = 10
    score = 0
    mylist = listing()
    for x in mylist:
        if health <= 0:
            print("Game Over")
            break

        friend = list(filter(lambda x: x == 0, mylist))
        enemy = list(filter(lambda x: x == 1, mylist))
        button = list(filter(lambda x: x == 2, mylist))
        printinfo(mylist, health, score, x)

        health, score, mylist = interacting(health, score, mylist, mylist.index(x))

game()





