

def discount_application (amount):
    if amount >5000:
        return 0.85*amount
    if amount < 1000:
        return 0.95*amount
    if amount < 5000 :
        return 0.9*amount
    
    if amount<=0 :
        return amount
    
amount =int(input("enter the purchase amount :"))
discounted_amount = discount_application(amount)

print("payable amount after the discount is : ", discounted_amount)
    