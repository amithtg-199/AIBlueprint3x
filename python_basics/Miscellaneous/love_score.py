def love_score_clac(name1, name2):
    score_true=0
    score_love=0
    combined_value = name1+name2
    for i in combined_value.lower():
        if i in "love":
            score_love += 1
        if i in "true":
            score_true += 1
    print(f"{score_love}{score_true}")

love_score_clac(name1="Steven", name2="Angela")


