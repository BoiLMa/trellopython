import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for x in people:
    print(x)

w = "Waldo"
i = 0 
length = len(people)
index = []

while i < length:
    if w == people[i]:
        index.append(i)
    i += 1
print(f'{w} zit op stoel {index}')

   