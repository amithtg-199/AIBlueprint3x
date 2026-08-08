# enemies = "Skeleton"

# def increase_enemies():
#     enemies = "Zombie"
#     print(enemies)

# increase_enemies()
# print(enemies)

# Modifying a Global Scope Variable inside a local Scope
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()
print(enemies)