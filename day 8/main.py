def calculate_love_score(name1, name2):
    true_score = 0
    combined = (name1 + name2).lower()
    for letter in "true":
        true_score += combined.count(letter)
    
    love_score = 0
    for letter in "love":
        love_score += combined.count(letter)
    
    print(f"{true_score}{love_score}")

calculate_love_score("mizan", "angle")