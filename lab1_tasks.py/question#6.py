txt = input("Enter text: ")

long = ""
sub = ""

for char in txt:
    if char in sub:
        cut = sub.find(char)
        sub = sub[cut + 1:]
        
    sub += char
    
    if len(sub) > len(long):
        long = sub

print("Longest unique part is:", long)
