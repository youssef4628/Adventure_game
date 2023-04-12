import time
import random
import sys

# this function that write the text with a good way
def write_function(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(.085)


# this the function that control in taking input from user
def choosing_function():
    while True:
        ch = input("choose(1 or 2):")
        if ch == "1" or ch == "2":
            return ch
            break
        else:
            continue


# this function that ask the user if he want to play again
def play_again():
    while True:
        again = input("Do you want play again? (yes or no)")
        if again == "yes" or again == "no":
            break
        else:
            continue
    if again == "yes":
        game()
    else:
        sys.exit()


# check the weapon for the player if it can damage the evil.
def fight(weapon, evil):
    win = "The Victory.\n Yes, I did it! I have surpassed the wizard and achieved freedom.\n Congratulations to you. You were smart enough to win this challenge."
    lose = "You have tried your utmost to defeat him,\nand the battle lasted for a long time,\nbut unfortunately, you were not well-prepared,\nand he outperformed you and killed you.\nyou have lost this time, better luck next time."
    if weapon == "old-sword":
        write_function(lose)
        play_again()
    elif weapon == "magic-wand":
        if evil == "wizard":
            write_function(lose)
            play_again()
        elif evil == "dragon":
            write_function(win)
            play_again()
    elif weapon == "Zosar-sword":
        if evil == "d":
            write_function(lose)
            play_again()
        elif evil == "wizard":
            write_function(win)
            play_again()


# that makes the player choose the first or second door when he go again to the room.
def go_room(weapon,evil):
    senario_back = "you have now returned to the room and there are two choices in front of you: \n1-Going to the first door \n2-Going to the second door."    
    write_function(senario_back)
    ch2 = choosing_function()
    if ch2 == "1":
        the_first(weapon,evil)
    elif ch2 == "2":
        the_second(weapon,evil)


# this controls in the first stage of the game and moving from and to it 
def the_first(weapon,evil):
    senario1 = "You went to the first door and opened it,\nonly to discover that it was the door of salvation, but in front of you,\nthere is a " + \
        evil+" that you have to kill to get out safely or escape from it.\nThe decision is yours.\n1-fight the " + \
        evil+"\n2-run away to the room\n"
    write_function(senario1)
    ch1 = choosing_function()
    if ch1 == "1":
        fight(weapon, evil)
    elif ch1 == "2":
        go_room(weapon,evil)


# this controls in puzlle and check the answer and the weapon that the user will take if he answered corectly 
def check_puzzle(evil):
    puzzle= "The puzzle is 1+1 = 1 \nSo if 1+0 = ? \nA simple hint, this puzzle depends on your skills in communicating with the computer.\nWhat is your solution? "
    right_answer= "In fact, you are a genius person, as you were able to solve this puzzle. Luckily,\nthere was a good wizard behind the puzzle, \nwho congratulates you on your intelligence \nand offers you to take either (a powerful magic wand or a Zosar-sw.)\n You need to think properly in order to make use of one of these weapons.\n What do you choose? \n1-Zosar-sword \n2-magic-wand"
    wrong_answer= "Unfortunately, you didn't think well about the riddle. \nWhat do you want?\n1-Do you want to try again?\n2-Do you want to go back to the room?"
    write_function(puzzle)
    answer_puzzle=input("")
    if answer_puzzle == "0":
        write_function(right_answer)
        ch5=choosing_function()
        if ch5=="1":
            weapon = "Zosar-sword"
        elif ch5 =="2":
            weapon="magic-wand"
        take_weapon= "And now that you have obtained "+weapon+", you must return to the room."
        write_function(take_weapon)
        go_room(weapon,evil)
    else:
        write_function(wrong_answer)
        ch6=choosing_function()
        if ch6==1:
            check_puzzle()
        else:
            go_room(weapon,evil)
        

# This controls in the second door and moving from or to it
def the_second(weapon,evil):
    senario2 = "You went to the second door and found a difficult puzzle \nthat you have to solve in order to reach what's behind it. \nWhat do you choose: \n1-Solve the puzzle.\n2-Go back to the room "
    write_function(senario2)
    ch4=choosing_function()
    if ch4 == "1":
        check_puzzle(evil)
    elif ch4 == "2":
        go_room(weapon,evil)


# excute the game
def game():
    weapon = "old-sword"
    evil = random.choice(["wizard", "dragon"])
    intro = "You wake up in a dark room, with no memory of how you got there. As you look around,\nyou notice the room has only two doors.\nSuddenly, you hear a strange voice coming from the room. Welcome to the strength test,\nthe voice says, All you have in this test is an old sword,\nthere are two doors but you know nothing about them.\nYou have to choose whether to go through the first door or the second door.\nThings start to crowd your mind and you realize that you have to make a quick decision:\n1-I go to the first door.\n2-I go to the second door\ntake a long breath and go.\n"
    write_function(intro)
    ch = choosing_function()
    if ch == "1":
        the_first(weapon,evil)
    else:
        the_second(weapon,evil)


game()
