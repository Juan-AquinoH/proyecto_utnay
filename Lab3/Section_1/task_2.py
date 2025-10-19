
# Diccionario original con animales
animals = {
    1: "ferret",
    2: "boar",
    3: "jaguar",
    4: "giraffe",
    5: "lizard",
    6: "locust",
    7: "lion",
    8: "wolf",
    9: "parrot",
    10: "raccoon",
    11: "butterfly",
    12: "jellyfish",
    13: "fly",
    14: "gnat",
    15: "bat",
    16: "otter",
    17: "bear",
    18: "polar bear",
    19: "oyster",
    20: "sheep",
    21: "bee",
    22: "eagle",
    23: "antelope",
    24: "spider",
    25: "squirrel",
    26: "tuna",
    27: "ostrich",
    28: "wasp",
    29: "whale",
    30: "bison",
    31: "buffalo",
    32: "owl",
    33: "donkey",
    34: "horse",
    35: "goat",
    36: "squid",
    37: "chameleon",
    38: "camel",
    39: "crab",
    40: "kangaroo",
    41: "cat",
    42: "dog"
}
#Diccionario con palabras que contienen la letra a
print("Diccionario con la letra 'a':")
a_dict = {}
for key, value in animals.items():
    if "a" in value:
        a_dict[key] = value1
print(a_dict)
#Diccionario con palabras que contienen la letra b
print("Diccionario con la letra 'b':")
b_dict = {}
for key, value in animals.items():
    if "b" in value:
        b_dict[key] = value
print(b_dict)
        
        # c. Diccionario con palabras que contienen la letra "y"
print("Diccionario con la letra 'y':")
y_dict = {}
for key, value in animals.items():
    if "y" in value:
        y_dict[key] = value
print(y_dict)

# Nuevo diccionario con palabras que contienen 'y' y 'b'
yb_dict = {}

for key, value in animals.items():
    if "y" in value and "b" in value:
        yb_dict[key] = value

print("Diccionario con palabras que contienen 'y' y 'b':")
print(yb_dict)

#Diccionario con la letra 'a':
#{2: 'boar', 3: 'jaguar', 4: 'giraffe', 5: 'lizard', 9: 'parrot', 10: 'raccoon', 14: 'gnat', 15: 'bat', 17: 'bear', 18: 'polar bear', 22: 'eagle', 23: 'antelope', 26: 'tuna', 28: 'wasp', 29: 'whale', 31: 'buffalo', 35: 'goat', 37: 'chameleon', 38: 'camel', 39: 'crab', 40: 'kangaroo', 41: 'cat'}
#Diccionario con la letra 'b':
#{2: 'boar', 11: 'butterfly', 15: 'bat', 17: 'bear', 18: 'polar bear', 21: 'bee', 30: 'bison', 31: 'buffalo', 39: 'crab'}
#Diccionario con la letra 'y':
#{11: 'butterfly', 12: 'jellyfish', 13: 'fly', 19: 'oyster', 33: 'donkey'}
#Diccionario con palabras que contienen 'y' y 'b':
#{11: 'butterfly'}