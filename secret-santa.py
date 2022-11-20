import itertools
import random

people = ["Ian", "Lucy", "Rosie", "Mike", "Hannah", "Graham"]

past_years = [
    # Buyer, Receiver
    # Partners
    ("Ian", "Lucy"),
    ("Lucy", "Ian"),
    ("Hannah", "Graham"),
    ("Graham", "Hannah"),
    ("Rosie", "Mike"),
    ("Mike", "Rosie"),
    # 2020
    ("Graham", "Rosie"),
    ("Mike", "Graham"),
    ("Hannah", "Lucy"),
    ("Rosie", "Ian"),
    ("Ian", "Hannah"),
    ("Lucy", "Mike"),
    # 2021
    ("Lucy", "Graham"),
    ("Hannah", "Ian"),
    ("Mike", "Lucy"),
    ("Rosie", "Hannah"),
    ("Ian", "Rosie"),
    ("Graham", "Mike"),
     # 2022
    ('Rosie', 'Lucy')
    ('Ian', 'Graham')
    ('Mike', 'Hannah')
    ('Lucy', 'Rosie')
    ('Graham', 'Ian')
    ('Hannah', 'Mike')
]

# Generate every pair-length permutation of the original list of people.
pick_pool = itertools.permutations(people, 2)
# Regenerate the pick_pool, exlcuding all previous year's picks.
pick_pool = [p for p in itertools.permutations(people, 2) if p not in past_years]

this_years_picks = []

while pick_pool:
    pick = random.choice(pick_pool)
    this_years_picks.append(pick)
    buyer, receiver = pick
    # Regenerate the pick pool, excluding the current buyer.
    pick_pool = [pick for pick in pick_pool if pick[0] != buyer]
    # Regenerate the pick pool, excluding the current receiver.
    pick_pool = [pick for pick in pick_pool if pick[1] != receiver]

for p in this_years_picks:
    print(p)