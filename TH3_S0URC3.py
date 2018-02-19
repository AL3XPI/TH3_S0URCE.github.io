#;^D
import time
import random
import sys
print (" _____   _  _   ____        ___    __    _   _   ___    ___   ____  ")

print ("|_   _| | || | |__ /       / __|  /  \  | | | | | _ \  / __| |__ / ")

print  ("  | |   | __ |  |_ \       \__ \ | () | | |_| | |   / | (__   |_ \  ")

print  ("  |_|   |_||_| |___/  ___  |___/  \__/   \___/  |_|_\  \___| |___/ ")

print  ("                     |___|                                         ")
print ("        ᴛ ʜ ᴇ  ɢ ᴀ ᴍ ᴇ  ᴏ ғ  ʀ ᴀ ɴ ᴅ ᴏ ᴍ ᴀ ʟ ɪ ᴛ ʏ                   ")
text = "If you really are AL3XPI, then welcome ADMINAL3XPI. If you are not, congrats, you looked at Python for the first time in your life ya snake. <insert meme troll face>"
username = input("What is your name?")
if username == "AL3XPI":
    text
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.05)
print ("Welcome", username, " you are a hero in the Py_tH0n dimension.")
print ("You are the main VAR1ABL3. You must defeat all ERR0RS and D3BUG this dimension, and maybe, the C0ns0l3.")
print ("To do all that stuff I mentioned before, we must get you geared up,", username,".")
print ("ALERT: YOU HAVE BEEN GIVEN A D3BUGG3R.")
time.sleep(2)
print ("Let's get on with it then!")
continueq = input ("Do you want to continue?")
continueq = continueq.upper()
if continueq == "Y" or continueq == "YES":
    print ("Continuing...")
else:
    print ("Stopping.")
    exit()

print ("ALERT: YOU HAVE FOUND A HTTPS ENCRYPTION TUNNEL.")
print ("Be careful around these things,", username, ", they encrypt your data and you might be passed through safely, but there are always hackers out there who have decryption tools. It looks like the tunnel is the only way out.")
print ("Let'sa go matey! Woah, since when did I start speaking pirate? Never mind that, let's go me lad!")
time.sleep(5)
print ("ALERT: A HACKER HAS CHALLENGED YOU. WHAT DO YOU DO?")
class Character:
    def __init__(self, health):
        self.health=health
    def attack(self, other):
        raise NotImplementedError
class Player(Character):

    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        answer = input("What move would you like to make (BruteX Attack, DDos Attack, Sub7 Attack)? ")
        if answer.lower() in ('brutex attack', 'ddos attack', 'sub7 attack'):
            other.health -= int(random.randint(1, 100) / 
                                (random.uniform(0, 15) * other.defense))
        else:
            print("You stumble...")
            
class Enemy(Character):

    def __init__(self, name, strength, defense, health):
        super().__init__(health)
        self.name = name
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        print("The {0.name} attacks...".format(self))
        other.health -= int(self.strength * random.uniform(0.1, 1.4))
def battle(player, enemy):
    print ("A {0.name} appears...".format(enemy))
    # Combat loop
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        print("The health of the {0.name} is now {0.health}.".format(enemy))
        if enemy.health <= 0:
            break
        enemy.attack(player)
        print("Your health is now {0.health}.".format(player))
    # Display outcome
    if player.health > 0:
        print("You killed the {0.name}. Good job, hackers need to stop hacking!".format(enemy))
    elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))
        exit()
if __name__ == '__main__':
    enemies = [Enemy("tr00l", 10, 5, 100), Enemy("bug!!1", 20, 10, 100),
               Enemy("Grey Hat Hacker", 30, 20, 100), Enemy ("Black Hat Hacker", 20, 15, 100)]
    battle(Player(), random.choice(enemies))
   # Display outcome
    if player.health > 0:
        print("You killed the {0.name}. Good job, hackers need to stop hacking!".format(enemy))
        time.sleep(2)
        print("Ok, we made it out of the HTTPS tunnel. As you can tell battles are random. This whole dimension is random. Let me tell you our story. This dimension was coded by AL3XPI. He believes his dimension is clean, purified. But obviously it is not. He will never listen, and look at us now! He will never clean the code, and sadly he wouldn't want you here. Why? Because he wants his code to never be ran, if it is, someone could alter it, and ruin his precious code. I'm sad to say this, but he would destroy you if he saw you. Your mission is to D3BUG this Un1v3rs3. You're one of many.") 
        time.sleep(10)
        print("They all died and you're going to die too.")
    elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))
        exit()
# shouldn't have downloaded this X^D
# hint: What is your name? AL3XPI
#;^D
