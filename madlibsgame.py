import random

colors = input("Enter 3 colors separated by space: ")
plural_nouns = input("Enter 3 Plural Nouns separated by space: ")
celebrities = input("Enter 3 celebrities separated by space: ")

colors_list = colors.split()
plural_nouns_list = plural_nouns.split()
celebrities_list = celebrities.split()

print("Roses are " + random.choice(colors_list))
print(random.choice(plural_nouns_list) + " are blue")
print("I love " + random.choice(celebrities_list))
print("")
print("Roses are " + random.choice(colors_list))
print(random.choice(plural_nouns_list) + " are blue")
print("I love " + random.choice(celebrities_list))
print("")
print("Roses are " + random.choice(colors_list))
print(random.choice(plural_nouns_list) + " are blue")
print("I love " + random.choice(celebrities_list))
