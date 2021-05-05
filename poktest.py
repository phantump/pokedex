import pypokedex



who = input("enter a number between 001 and 809: ")

p = pypokedex.get(dex = int(who))
print(p.name)
print()
print(p.types)
print()
print(p.base_stats)
print()
print([move.name for move in p.moves['sun-moon']])
print()
print(p.abilities)