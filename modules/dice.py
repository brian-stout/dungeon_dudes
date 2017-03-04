import random

"""
    Returns an int 1 to 6.  Used for combat and picking a random monster
"""
def d6():
    return random.randint(1,6)


"""
    Returns an int 1 to 10.  Used for the loot table
"""
def d10():
    return random.randint(1,10)


"""
    Returns an int 1 to 20.  Used for intiative rolls
"""
def d20():
    return random.randint(1,20)
