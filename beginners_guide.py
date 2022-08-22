#This part of the code prints out the name of the game, as well as the options for each story they may delve into
print("Welcome to Beginner's Guide, a game that introduces you to the concept of creative narrative, as well as interactive-story based games!")
print("Choose your adventure:")
print("1- The Office")
print("2- The Wizard's Tower")
print("3- The Cave")
print("4- Leave game")
chooseAdventure = int(input("Type a number: "))

while chooseAdventure != 0:
    if chooseAdventure == 1: #The Office storyline
        print("Imagine you are in an office...")
        print("You are the new employee, just starting out with little experience, a fresh mind, and a motivation to do your job right.")
        print("You are sitting at your wooden, somewhat worn out desk, inputting data in the ancient computer the company has provided you. The cool breeze of an air vent blows gently onto your forehead.")
        print("The atmosphere is busy. You hear multiple co-workers talking unintelligibly throughout the department.")
        print("Suddenly, your computer makes a bell sound. It's your boss, and he wants to see you in his office immediately!")
        print("Feeling the urge to not disappoint him, you get up from your four-wheel chair, and rush to his office.")
        print("")
        print("On your way to your boss's office, you come across a tall staircase. You realise that you don't remember where your boss's office actually is.")
        print("You may go upstairs or downstairs. Which do you choose?")
        print("1- Upstairs")
        print("2- Downstairs")
        theOfficeChoice1 = int(input("Make your choice: ")) #The first major choice the user has to make.
        while theOfficeChoice1 >= 1 or theOfficeChoice1 <= 2:
            if theOfficeChoice1 == 1:
                print("You chose to go upstairs...")
                print("...and by sheer luck, you chose correctly! The entire floor was sublime. It had that scent of printer paper and old leather. You stand still for a moment, breathing it all in.")
                print("Eagerly, you start fast-walking towards your boss's office. You reach the giant mahogany door, and knock. 'Come in.', your boss says.")
                print("You walk into the office. It looks very fancy, as if the boss had spent more money on making his office as lavish as possible. There is a portrait of him on the wall, and on his sleek wooden desk, there is a golden plaque which reads 'Mr. Stuzo'.")
                print("You ask Mr. Stuzo politely why he'd asked you to come. 'Make me a coffee!', he yells. 'Just a regular black coffee'.")
                print("")
                print("You look around the office...")
                print("1- Mr. Stuzo")
                print("2- Portrait")
                print("3- Coffee machine")
                print("4- Piece of paper")
                theOfficeChoice2 = int(input("Choose or be fired: ")) #The second choice. Here the user is able to interact with different items inside the room.
                while theOfficeChoice2 >=1 or theOfficeChoice2 <=4:
                    if theOfficeChoice2 == 1:
                        print("Mr Stuzo: Well what are you waiting for, winter? Get me my coffee!")
                        theOfficeChoice2 = int(input("Choose or be fired: "))

                    elif theOfficeChoice2 == 2:
                        print("You take a closer look at Mr. Stuzo's portrait. He's wearing a suit and red tie, and has a shiny bald head and bushy moustache.")
                        theOfficeChoice2 = int(input("Choose or be fired: "))

                    elif theOfficeChoice2 == 3:
                        print("You walk towards the coffee machine. However, you notice that it is unplugged from its socket.")
                        print("You see two sockets in the wall. The left socket looks fine, but the right socket clearly has a big, red sign over it that says 'DO NOT USE'.")
                        print("1- Plug the machine into the left socket")
                        print("2- Plug the machine into the right socket")
                        theOfficeChoice3 = int(input("Surely you wouldn't...: ")) #The third choice. This will lead to two of three endings that the user can get for this storyline
                        while theOfficeChoice3 >=1 or theOfficeChoice3 <=2:
                            if theOfficeChoice3 == 1:
                                print("Phew! That could have been disastrous. Thankfully you managed to plug the coffee machine into the correct socket.")
                                print("You successfully make the coffee, based of course on your years of experience making it beforehand.")
                                print("Mr. Stuzo takes a sip from his #1 Boss mug. 'Oh my...', he exclaims. 'That is the best coffee I've ever had!'. You feel a warm sense of accomplishment. You stand still for a moment, drinking in the moment.")
                                print("Mr. Stuzo stares at you. 'What are you waiting for, a raise? Get back to work!'. You walk happily back to your office, and feel a bright future ahead of you.")
                                print("")
                                print("Ending 3: Employee of the Month")
                                break
                            elif theOfficeChoice3 == 2:
                                print("Oh no! You've plugged the coffee machine into the wrong socket. That socket happened to be connected to the main generator in the building, which ultimately cause the coffee machine to explode.")
                                print("And as if things couldn't get any worse, the coffee that flew out of the machine splashed onto the exposed wiring, causing massive circuit failure in your entire building.")
                                print("Darkness. You've caused a blackout. 'PLAYEEEEER!!!', Mr Stuzo shouted at the top of his voice. He was fuming and sounded ready to strangle someone, but at least he can't see you.")
                                print("")
                                print("Ending 2: Blackout")
                                break
                            else:
                                print("Invalid option.")
                                theOfficeChoice3 = int(input("Surely you wouldn't...: "))
                        break
                    
                    elif theOfficeChoice2 == 4:
                        print("You notice a piece of paper on Mr. Stuzo's desk. It is in fact a receipt from your favourite fast-food place, Pepe's. Seems like he eats there a lot.")
                        theOfficeChoice2 = int(input("Choose or be fired: "))

                    else:
                        print("Invalid option.")
                        theOfficeChoice2 = int(input("Choose or be fired: "))
                break
            elif theOfficeChoice1 == 2:
                print("You chose to go downstairs...")
                print("...but unfortunately, your boss's office wasn't down here. There was a strong smell of... sandwiches? You realise that you are inside a giant food pantry. And it's the one with all the good food, that you've heard the boss keeps to himself.")
                print("You try to restrain yourself, but the aroma of freshly baked donuts and sandwiches overtakes you. You end up eating the entire stash of food, leaving you lying on the ground surrounded by crumbs.")
                print("Oh, and you were immediately fired after you were found. Way to go.")
                print("")
                print("Ending 1: Foodie")
                break
            else:
                print("Invalid option.")
                theOfficeChoice1 = int(input("Make your choice: "))
        break

    elif chooseAdventure == 2:
        print("This adventure is still being created. Check back again soon!")
        chooseAdventure = int(input("Type a number: "))

    elif chooseAdventure == 3:
        print("This adventure is still being created. Check back again soon!")
        chooseAdventure = int(input("Type a number: "))

    elif chooseAdventure == 4:
        print("See you soon!")
        break

    else:
        print("That adventure doesn't exist (yet!)")
        chooseAdventure = int(input("Type a number: "))