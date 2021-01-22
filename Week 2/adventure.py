print("Welcome to this quick choose-your-own-adventure text game!!")
name = input("what is your name?  ")
inventory = {"Truck Keys": 0}
print("okay " + name + ", you find yourself in the middle of a zombie apocalypse in a room with a door, a chest, and a window.")
choice = input("do you choose 1) look through the window 2) open the door  3) open the chest  ")

if choice is '1':
    print("There are zombies outside")
elif choice is '2':
    if inventory.get("Truck Keys") is 0:
        print("you open the door and don't have the keys to get into your truck. You sadly get eaten :/")
        print("Game over")
        exit(0)
    else:
        print("You unlock the truck and drive into the sunset")
        print("you win")
        exit(0)
elif choice is '3':
    print("You look inside the chest and pull out keys to a Ford Truck")
    inventory["Truck Keys"] = inventory.get("Truck Keys") + 1


if choice == '1':
    choice2 = input("do you 1) open the door 2) open the chest  ")
    if choice2 is '1':
        print("you open the door and don't have the keys to get into your truck. You sadly get eaten :/")
        print("Game over")
        exit(0)
    elif choice2 is '2':
        print("You look inside the chest and pull out keys to a Ford Truck")
    inventory["Truck Keys"] = inventory.get("Truck Keys") + 1
choice2 = input("do you 1) open the door  ")
if choice2 is '1':
    if inventory.get("Truck Keys") is 0:
        print("you open the door and don't have the keys to get into your truck. You sadly get eaten :/")
        print("Game over")
        exit(0)
    else:
        print("You unlock the truck and drive into the sunset")
        print("you win")
        exit(0)


    #make code more modular, like check if keys exist or not before they die etc.
