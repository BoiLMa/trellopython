import random 


naam = input("type name: ")
print("Name: " + naam)
print("choose pet")
print("dog, cat, fish")
pet = input()
if pet == "dog":
    b = ["Husky", "Golden retriever", "Doberman", "Affenpinscher"]
elif pet == "cat":
    b = ["Ragdoll", "Sphynx", "Rusty-Spotted cat", "Tiger"]
elif pet == "fish":
    b = ["Shark", "Goldfish", "Ray", "Blowfish"]

print(str(random.choice(b)))   
pet = input("type pet name: ")
print("Name: " + pet)
print("PET STATS")
print("HP: " + str(random.randint(0, 20)) + "/20")
print("Level: " + str(random.randint(0, 50)))
a = ["Barrier", "Teleport", "Bonecrush", "Stun"]
print("Special Power: " + str(random.choice(a)))
print("Special Powerbar: " + str(random.randint(0, 40)))
print("PLAYER STATS")
print("HP: " + str(random.randint(0, 100)) + "/100")
print("Level: " + str(random.randint(0, 999)))
a = ["Fly", "Teleport", "strength", "Magic"]
print("Special Power: " + str(random.choice(a)))
print("Special Powerbar: " + str(random.randint(0, 100)))
print("jumpforce: " + str(random.randint(0,50)))



