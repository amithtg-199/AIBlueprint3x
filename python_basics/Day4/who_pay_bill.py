import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
choice = random.randint(0, len(friends)-1)
print(f"Bill will be paid by {friends[choice]}")

#Easy one using choice function
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
