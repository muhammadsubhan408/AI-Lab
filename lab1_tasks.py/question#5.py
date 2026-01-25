def analyzing_string(text):
    vowels_list = "aeiou"
    
    vowels_count = 0
    consonants_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels_list:
                vowels_count = vowels_count +1
            else:
                consonants_count = consonants_count+1
                
    # 3.creating dict
    result = {
        "total_characters": len(text),
        "vowels": vowels_count,
        "consonants": consonants_count
    }
    
    return result

user_input = input("Enter a string to analyze: ")
data = analyzing_string(user_input)

print("\nAnalysis Results:")
print(data)