def find_doubles(nums):
    unique = []
    repeats = []
    
    for n in nums:
        if n in unique:
            if n not in repeats:
                repeats.append(n)
        else:
            unique.append(n)
            
    return repeats

# New values list
vals = [12, 45, 12, 8, 99, 45, 10, 12, 7]
result = find_doubles(vals)
print("Repeated numbers:", result)