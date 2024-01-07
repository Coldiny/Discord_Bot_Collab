player = {
  "Qi" : 0,
  "Qi_Max" : 100,
  "Base" : 1,
  "Multiplier" : 1,
  "Talent" : 1,
  "Talent_Max" : 100,
  "Qi Gain Speed" : 100,  
}
#Qi Gain Speed Formula is Multiplier * Base * Talent

cultivation_level = ["Mortal", "Qi Refining", 
"Foundation", "Crystallization", "Golden Core", 
"Spirit Tempering", "Nascent Soul", "Soul Formation",
"Enlightenment", "Ascension", "Immortal"]
# Mortal = 0
# Qi Refining = 1 
# Foundation = 2 
# Crystallization = 3 
# Golden Core = 4 
# Spirit Tempering = 5 
# Nascent Soul = 6
# Soul Formation = 7
# Enlightenment = 8 
# Ascension = 9
# Immortal = 10

cultivation_stages = ["Early", "Mid", "Late", "Peak"]
#Early = 0
# Mid = 1
# Late = 2
# Peak = 3

#idk man
#manual_level = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#manual_upgrade_cost = [25, 50, 75, 100, 150, 300, 500, 750, 1000, 1500, 3000, 5000, 7500, 10000, 12500]
pills = ["Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Low Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "Medium Quality Qi Pill", "High Quality Qi Pill", "High Quality Qi Pill", "High Quality Qi Pill", "High Quality Qi Pill", "High Quality Qi Pill", "Perfect Qi Pill", "Death Pill" ]


armor = ["Leather Armor", "Steel Armor", "Martial Artists Robe", "Demonic Armor", ]

Leather_Armor = {
  "Defense" : 1,
}
Steel_Armor = {
  "Defense" : 5,
}
Martial_Artists_Robe = {
  "Defense" : 8,
}
Demonic_Armor = {
  "Defense" : -5,
  "Attack" : 5
}

weapons = ["Rusty Knife", "Old Knife", "Dagger", "Short Sword", "Long Sword", "Mace", "Warhammer", "Great Sword"]

#idk if this works
Rusty_Knife = ["Stab", "Slash"]
Old_Knife = ["Stab", "Slash"]
Dagger = ["Stab", "Slash"]
Short_Sword = ["Cut", "Slash"]
Long_Sword = ["Cut", "Slash", "Triple Slash"]
Mace = ["Bash", "Swing"]
Warhammer = ["Bash", "Swing", "Pierce", "Stab"]
Greatsword = ["Slash", "Bash"]

Enemies = ["Boar", "Thug", "Thief", "Demonic Creature"]