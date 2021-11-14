import itertools
import random

people = ["Ian", "Joel", "Robbie", "Connor", "Jason", "Jimmy", "Gareth"]

past_years = [
    # Buyer, Receiver
    # 2020
    ("Ian", "Jason"),
    ("Jimmy", "Ian"),
    ("Connor", "Robbie"),
    ("Jason", "Gareth"),
    ("Gareth", "Joel"),
    ("Joel", "Jimmy"),
    ("Robbie", "Connor"),
]

# Generate every pair-length permutation of the original list of people.
pick_pool = itertools.permutations(people, 2)
# Regenerate the pick_pool, exlcuding all previous year's picks.
pick_pool = [p for p in itertools.permutations(people, 2) if p not in past_years]

this_years_picks = []

while pick_pool:
    pick = random.choice(pick_pool)
    this_years_picks.append(pick)
    buyer, _ = pick
    # Regenerate the pick pool, excluding the current buyer.
    pick_pool = [pick for pick in pick_pool if pick[0] != buyer]

print(this_years_picks)

