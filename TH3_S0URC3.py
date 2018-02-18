username = input("What is your name?")
print ("Welcome", username, " you are a hero in the Py_tH0n dimension.")
print ("You are the main VAR1ABL3. You must defeat all ERR0RS and D3BUG this dimension, and maybe, the Un1v3rs3.")
print ("To do all that stuff I mentioned before, we must get you geared up,", username,".")

weapons = {'Axe': 5, 'Sword': 10, 'Brass Knuckles': 8 }
armor = {'Chain': 8, 'Diamond': 12, 'Gold': 10 }
User_stats = []
User_weapon = ""
User_armor = ""

print ("Ok, lets choose a weapon,(enter the name of weapon). The higher the number, the better.")
print(weapons)
User_weapon = input() 
User_stats.append(User_weapon)
print("Now, let's pick some armor (enter the name of the armor). The higher the number the better.")
print(armor)
User_armor = input ()
User_stats.append(User_armor)
print ("These are your user stats", (User_stats),".")
print ("Let's get on with it then!")
continueq = input ("Do you want to continue?")
continueq = continueq.upper()
if continueq == "Y" or continueq == "YES":
    print ("Continuing...")
else:
    print ("Stopping.")
    exit()

print ("ALERT: YOU HAVE FOUND A HTTPS ENCRYPTION TUNNEL.")
print ("Be careful around these things,", username, ", they encrypt your data and you might be passed through safely, but there are always hackers out there who have decryption tools.")
