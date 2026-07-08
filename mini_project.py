#Name:
#Mini-Project - Build Your Own Game!
'''
This is YOUR game. You are the designer. There are only two requirements:

  1. Your game must use USER INPUT — typed answers, key strokes, mouse clicks, etc.
  2. Your game must keep track of and DISPLAY A SCORE.

You have everything you need from Modules 1-6: variables, input(), if/elif/else,
while loops, for loops, lists, random, and turtle graphics.

======================= NEED AN IDEA? PICK ONE OF THESE =======================

  TERMINAL GAMES (use input(), great with while loops + random):
    - Number guessing: score points for guessing in fewer tries, play 5 rounds
    - Math quiz: random questions, +1 per right answer, show the final score
    - Rock, paper, scissors: first to 3 wins, show the running score
    - Trivia: store questions and answers in lists, loop through them

  TURTLE GAMES (use the mouse or keyboard, see the reminder below):
    - Click the turtle: it jumps to a random spot every time you click it
    - Turtle race: press a key to make your turtle dash to the finish line
    - Falling catch: move a paddle with the arrow keys to catch a falling dot

  ...or invent something completely new. Weird ideas are welcome.

============================ HELPFUL SNIPPETS ================================

  Typed input:
      guess = int(input("Your guess: "))

  Turtle keyboard input:
      screen = turtle.Screen()
      screen.onkey(move_left, "Left")     # calls move_left() on the left arrow
      screen.listen()

  Turtle mouse input:
      screen.onclick(jump)                # calls jump(x, y) on every click
      my_turtle.onclick(caught)           # only when the turtle itself is clicked

  Keeping and showing a score:
      score = 0
      score = score + 1                   # when the player earns a point
      print("Score:", score)              # terminal
      pen.write("Score: " + str(score))   # turtle (use a separate pen turtle)

  REMINDER for turtle games — to see your game in Codespaces: run it, open the
  PORTS tab, click port 6080 ("Turtle Desktop"), Connect, password: vscode

========================== LEVEL-UP IDEAS (optional) ==========================

  - Add lives: the game ends after 3 misses
  - Add difficulty: harder questions or a faster game as the score goes up
  - Add a high score: remember the best score across rounds with a variable
  - Add sound-off flair: ASCII art title screens, victory messages, emoji

==============================================================================
Build your game below. Delete this line and start coding!
'''


import random
level = 1
damage = 1
mons_dmg = 2
health_choices = [1]
monster_healths = {}
health = 5


def winner_RPS(attack):
   global health
   while True:
       computer_choices = ["rock", "paper", "scissor"]
       computer_choice = random.choice(computer_choices)
       player_input = input("Type rock, paper, or scissor to fight monster: ")
       player_choice = player_input.lower()
       if player_choice == computer_choice:
           print(f"Computer choice: {computer_choice}")
           print("""You deal half your damage to the monster but take some damage yourself.
           """)
           monster_healths[attack] -= damage/2
           health -= mons_dmg / 2
           if health <= 0:
               break
           print(f"Remaining Health: {health}")
           if monster_healths[attack] <= 0:
               monster_death()
               break
       elif (player_choice == "rock" and computer_choice == "scissor") or (player_choice == "paper" and computer_choice == "rock") or (player_choice== "scissor" and computer_choice =="paper"):
           monster_healths[attack] -= damage
           print(f"Computer choice: {computer_choice}")
           if monster_healths[attack] <= 0:
               monster_death()
               break
           else:
               print("""You dealt damage to the monster but didn't kill it
               """)
       elif (computer_choice == "rock" and player_choice == "scissor") or (computer_choice == "paper" and player_choice == "rock") or (computer_choice == "scissor" and player_choice == "paper"):
           print(f"Computer choice: {computer_choice}")
           print("""The monster blocked your attack and dealt damage to you
           """)
           health -= mons_dmg
           if health <= 0:
               break
           print(f"Remaining Health: {health}")
       else:
           print("that isn't a valid option")


def monster_spawn():
   for i in range(1, level + 1):
       monster_health = random.choice(health_choices)
       monster_healths[i] = 0
       monster_healths[i] += monster_health
       print(f"""
       ---Monster {i}(Health {monster_health})---
       """)
def monster_death():
   print("You killed the monster")
   del monster_healths[attack]
   for i in monster_healths:
       print(f"""
       ---Monster {i}(Health {monster_healths[i]})---
       """)




print("""
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)


   _______
---'   ____)____
         ______)
         _______)
        _______)
---.__________)


   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)""")       
      
player_name = input("What is your name?")


instructions = input(f"Welcome {player_name}. You awaken in a dark dungeon. You see a monster and you must fight it using rock-paper-scissors. Type anything to continue: ")


while True:
   monster_spawn()
   while len(monster_healths) > 0:
       try:
           attack = int(input("What monster do you want to attack: "))
           if attack not in monster_healths:
               print("Type in a monster number that exist")
               continue
           winner_RPS(attack)
           if health <= 0:
               break
           item = random.randint(1, 6)
           if item == 1:
               print()
               print("The monster dropped a health potion healing you.")
               health += 2
               print(f"New Health: {health}")
           elif item == 2:
               print()
               print("The monster dropped a potion to increase your damage.")
               damage += 1
               print(f"New damage: {damage}")
       except:
           print("Type a number")
   if health <= 0:
       print(f"You died. Final level reached was level {level}.")
       break
   upgrade = input("You killed all the monsters do you want to upgrade your health or damage. Type h to upgrade health and anything else to upgrade damage: ")
   if upgrade == "h":
       health += 4
       print()
       print(f"New Health: {health}")
   else:
       damage += 1
       print()
       print(f"New damage: {damage}")
   level += 1
   print(f"Level increased to level {level}.")
   health_choices.append(level)
   print(f"Monster health choices: {health_choices}")






