## Deck Generator by Amos Nimos 2021
## For Yu Gi Oh Gx Duel Academy on the GBA

#Imports
from random import randrange as random


##(Other forbidden/Limited card might still be found, if so place them in the list bellow.)
#Frobidden = ["Change fo Hearth",]
Limited_spell = ["Sword of revealing light","Premature burial","Snatch steal"]
Limited_trap = ["Call of the haunted","Magic Cylinder"]

Monster = [
"Marshmallon",
"Penguin Soldier",
"Goblin attack force",
"Goblin elite attack force",
"Jinzo",
"Slate warrior",
"Skull mark ladybug",
"Des kangaroo",
"Des koala",
"Giant rat",
"Cybernetic Cyblopean",
"Cyber Dragon",
"Trap master",
"Ancient gear beast",
"Ancient gear soldier",
"Blade Rabbit",
"Bowganian",
"Chaos Necomancer",
"Magician of faith",
"Swam of scarabs",
"Man-eater bug",
"Moai interceptor cannons",
"Theban nightmare",
"Yomi ship",
"Gear Golem the moving fortress",
"Luster Dragon",
"Arsenal bug",
"Witch of the black forest",
"The fiend megacyber",
"Shadow ghoul",
"Shadowslayer",
"Kiseitai",
"Kuriboh",
"gyaku-gire panda",
"Copycat",
"Cobra jar",
"Creeping doom",
"Cure mermaid",
"Jinzo #7"
]

Monster_copy = []
#addapt list size
while len(Monster_copy) < len(Monster):
	Monster_copy.append(0)

Trap = [
"D.D. Trap Hole",
"Threatening roar",
"Spirit barrier",
"Draining shield",
"Trap jammer",
"Compulsory evacuation device",
"Raigeki break",
"Sakuretsu armor",
"Bottomless trap hole",
"Nightmare wheel",
"Shadow spell",
"Negate attack",
"Trap hole",
"Magic Jammer",
"Secen tools of the bandit",
"Robbin goblin",
"mirrot force",
"Numinous healer",
"minor goblin official",
"Time seal",
"Dust Tornado",
"Enchanted Javelin",
"Torrential tribute",
"Enchanted Javelin",
"Magic jammer",
"Negate attack",
"Mirror Force",
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
"Stop attack",
"Raigeki",
"Ookazi",
"Nightmare steelcage",
"Megamorph",
"Scape goat",
"Monster Reborn",
"Change of Heart",
"Heavy Storm",
"Mystical space typhoon",
"Giant Turnade",
"Fairy meteor crush",
"Meteor of destruction",
"Lightning Vortex",
"Dark snake syndrome",
"Monster reaincarnation",
"Dark Hole",
"Dian Keto the cure master",
"De-spell",
"United we stand",
"Spring of rebirth",
"Emergency provisions",
"Autonomous action unit",
"Smashing ground",
"Mystic wok",
"Goblin thief",
"Soul reversal",
"Hammer shot",
"Wave motion cannon",
"Block Attack"
"Block Deffence"
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

Deck_Monster=[]
Deck_Trap=[]
Deck_Spell=[]

#Monster
for Card in range(Monster_count):
	Card_id = random(len(Monster))

	if Monster_copy[Card_id] <= 3:
		Deck_Monster.append(Monster[Card_id])
		Monster_copy[Card_id]+=1

#Trap
for Card in range(Trap_count):
	Card_id = random(len(Trap))

	if Trap_copy[Card_id] <= 3:
		Deck_Trap.append(Trap[Card_id])
		Trap_copy[Card_id]+=1
#Spell
for Card in range(Spell_count):
	Card_id = random(len(Spell))

	if Spell_copy[Card_id] <= 3:
		Deck_Spell.append(Spell[Card_id])
		Spell_copy[Card_id]+=1



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

with open("Deck"+Deck_name+".txt", "w") as file:
	# Writing data to a file
	# file.write(str(Deck))
	for Card in Deck:
		file.writelines(Card+"\n\n")


