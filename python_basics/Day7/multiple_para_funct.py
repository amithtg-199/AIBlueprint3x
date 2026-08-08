def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    true_count = 0
    love_count = 0
    for i in combined_name.lower():
        if i in "love":
            love_count += 1
        if i in "true":
            true_count += 1
    love_score = str(true_count) + str(love_count)
    print(f"Love Score = {love_score}")
calculate_love_score("Angela Yu","Jack Bauer")