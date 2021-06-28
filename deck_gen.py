## Deck Generator by Amos Nimos 2021
## For Yu Gi Oh Gx Duel Academy on the GBA

#Imports
from random import randrange as random


##(Other forbidden/Limited card might still be found, if so place them here.)

Limited = True
Frobidden_spell = ["Change fo Hearth", "Dark Hole", "Monster Reborn",]
Limited_spell = ["Sword of Revealing Light","Premature Burial","Snatch Steal"]
Limited_trap = ["Call of the haunted","Magic Cylinder","Mirror Force","Torrential tribute"]
Limited_monster = ["Reflect Bounder","Sagan","Tribe-Infection Virus"]
Limited_rate = 2

Must_monster = ["Nimble Momonga","Nimble Momonga","Nimble Momonga","Cyber Stein","Jinzo"]
Must_trap = ["Draining Shield"]
Must_spell = ["Wave Motion Cannon"]
Deck_Extra = ["Cyber End Dragon","Master Of Dragon Soldier"]

Monster = [
"Marshmallon",
"Penguin Soldier",
"Kuriboh",
"Goblin Attack Force",
"Goblin elite attack force",
"Jinzo #7",
"Slate Warrior",
"Skull Mark Ladybug",
"Des Kangaroo",
"Des Koala",
"Giant Rat",
"Cybernetic Cyblopean",
"Cyber Dragon",
"Trap Master",
"Ancient Gear Beast",
"Ancient Gear Soldier",
"Blade Rabbit",
"Bowganian",
"Chaos Necomancer",
"Magician of Faith",
"Swam of Scarabs",
"Man-eater Bug",
"Moai Interceptor Cannons",
"Theban Nightmare",
"Yomi Ship",
"Gear Golem the moving fortress",
"Luster Dragon",
"Arsenal Bug",
"Witch of the black forest",
"The Fiend Megacyber",
"Shadow Ghoul",
"Shadowslayer",
"Kiseitai",
"Gyaku-gire Panda",
"Copycat",
"Cobra Jar",
"Creeping Doom",
"Cure Mermaid"
]

Monster_copy = []
#addapt list size
while len(Monster_copy) < len(Monster):
	Monster_copy.append(0)

Trap = [
"D.D. Trap Hole",
"Threatening Roar",
"Spirit Barrier"
"Trap Jammer",
"Compulsory Evacuation Device",
"Raigeki Break",
"Sakuretsu Armor",
"Bottomless Trap Hole",
"Nightmare Wheel",
"Shadow Spell",
"Trap Hole",
"Secen Tools of The Bandit",
"Robbin Goblin",
"Numinous Healer",
"Minor Goblin Official",
"Time Seal",
"Dust Tornado",
"Enchanted Javelin",
"Enchanted Javelin",
"Magic Jammer",
"Negate attack",
"Divine wrath",
"Mask of restrict",
"Waboku"
]

Trap_copy = []
#addapt list size
while len(Trap_copy) < len(Trap):
	Trap_copy.append(0)

Spell = [
"Mask of the accursed",
"Sebek blessing",
"Premature burial",
"Giant Turnade",
"Axe of Despair",
"Black Pendant",
"Stop Defense",
"Block Attack",
"Raigeki",
"Ookazi",
"Nightmare steelcage",
"Megamorph",
"Scape goat",
"Change of Heart",
"Heavy Storm",
"Mystical space typhoon",
"Giant Turnade",
"Fairy Meteor Crush",
"Meteor of Destruction",
"Lightning Vortex",
"Dark snake syndrome",
"Monster reaincarnation",
"Dian Keto the cure master",
"De-Spell",
"United We Stand",
"Spring of Rebirth",
"Emergency Provisions",
"Autonomous Action Unit",
"Smashing Ground",
"Mystic Wok",
"Goblin Thief",
"Soul Reversal",
"Hammer Shot",
"Fissure",
"Remove Trap",
"Black Pendant"
]

Spell_copy = []
#addapt list size
while len(Spell_copy) < len(Spell):
	Spell_copy.append(0)

Deck = []

#monster trap
Monster_count = 22
Trap_count = 10
Spell_count = 10

print("Monster:"+str(Monster_count))
print("Trap:"+str(Trap_count))
print("Spell:"+str(Spell_count))

while Monster_count>len(Monster):
	print("Error: Insuficient Monster list!")
	print("Reducing Monster amounth...")
	Monster_count-=1
	
while Trap_count>len(Trap):
	print("Error: Insuficient Trap list!")
	print("Reducing Trap amounth...")
	Trap_count-=1

while Spell_count>len(Spell):
	print("Error: Insuficient Spell list!")
	print("Reducing Spell amounth...")
	Spell_count-=1

Deck_Monster=[]
Deck_Trap=[]
Deck_Spell=[]

#Monster
for Card in range(Monster_count):
	Card_id = random(len(Monster))
	#Limit card copy
	while Monster_copy[Card_id] >= 3:
		Card_id = random(len(Monster))
	if Monster_copy[Card_id] <= 3:
		Deck_Monster.append(Monster[Card_id])
		Monster_copy[Card_id]+=1

#Trap
for Card in range(Trap_count):
	Card_id = random(len(Trap))
	#Limit card copy
	while Trap_copy[Card_id] >= 3:
		Card_id = random(len(Trap))
	if Trap_copy[Card_id] <= 3:
		Deck_Trap.append(Trap[Card_id])
		Trap_copy[Card_id]+=1
#Spell
for Card in range(Spell_count):
	Card_id = random(len(Spell))
	#Limit card copy
	if Spell_copy[Card_id] <= 3:
		Deck_Spell.append(Spell[Card_id])
		Spell_copy[Card_id]+=1

# Include Limited Card
if Limited == True:
	for Card in range(len(Limited_spell)):
		if random(Limited_rate)==1:
			Deck_Spell[random(len(Deck_Spell))] = Limited_spell[Card]
	for Card in range(len(Limited_trap)):
		if random(Limited_rate)==1:
			Deck_Trap[random(len(Deck_Trap))] = Limited_trap[Card]

#Must Include
for Card in range(len(Must_monster)):
	Deck_Monster[random(len(Deck_Monster))] = Must_monster[Card]

for Card in range(len(Must_trap)):
	Deck_Trap[random(len(Deck_Trap))] = Must_trap[Card]

for Card in range(len(Must_spell)):
	Deck_Spell[random(len(Deck_Spell))] = Must_spell[Card]

#Extra Card
for Card in range(len(Deck_Extra)):
	Deck_Monster.append(Deck_Extra[Card])

#Create Deck
Deck_Monster.sort()
Deck_Trap.sort()
Deck_Spell.sort()
Deck.append("# Monster:")
Deck.extend(Deck_Monster)
Deck.append("\n# Trap:")
Deck.extend(Deck_Trap)
Deck.append("\n# Spell:")
Deck.extend(Deck_Spell)

print(Deck)

Deck_name = str(input("Deck name? :"))
if Deck_name == "":
	Deck_name = "Deck_"+str(random(9))+str(random(9))+str(random(9))+str(random(9))

with open("Deck/"+Deck_name+".txt", "w") as file:
	# Writing data to a file
	# file.write(str(Deck))
	for Card in Deck:
		file.writelines(Card+"\n\n")

