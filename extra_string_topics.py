# operations with strings and values

character_class = "wizard"
character_race = "gnome"
character_mana = 50

# I want to print the string "Your character is a wizard gnome with 50 mana"

# by joining strings and values with addition (concatenation)
#print("Your character is a" + character_class + " " character_race + " with# " + str(character_mana) + " Mana")

#use str() to typecast a value to a string type
print("Your character is a",character_class,character_race,"with",character_mana,"mana")
# by joining strings and values with commas


# multiplication

print("There is an","echo "*5)
# print the following
# ask the user how many times they want to cast their spell if each cast is 10 mana
cast_num = int(input("How many times should you cast your fire spell (10 mana per cast)?"))
# if they use more than 50 mana, just default to 10


# print the following (if n were )
#print(f"The {character_class} {character_race} cast a fire spell {cast_num} times")
fire_spell = (" ~~ x x x ~~   " )

if cast_num > 5:
    print(f"The {character_class} {character_race} cast a fire spell 5 times")
    print(f"|===o {fire_spell*5}")
    print("Too many casts. You only have 50 mana")
else:
    print(f"The {character_class} {character_race} cast a fire spell {cast_num} times")
    print(f"|===o {fire_spell * cast_num}")
# "The {class} {race} cast a fire spell {n} times" (use any method you want)
# |===o  ~~ x x x ~~    ~~ x x x ~~    ~~ x x x ~~ (use multiplication)


