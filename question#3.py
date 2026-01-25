num_list = []

while True :
    users_entry =(input(" "))
    if users_entry=="done":
        break
    num_list.append(int(users_entry))

if len(num_list)>0:
    total_sum =0
    minimum = num_list[0]
    maximum = num_list[0]



for values in num_list :
    print(values)
    total_sum = total_sum + values

    if values> maximum:
        maximum = values

    if values < minimum : 
        minimum =values


print("the total sum off all the number entered is " , total_sum)
print("the minimuum of all the number entered is :" , minimum)
print("the maximum of all the number entered is :" , maximum)
