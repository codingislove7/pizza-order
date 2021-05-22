# Say Hello and be nice with user
print("Welcome to our pizza store:)")
# Get some data 
size = input("What size of pizza do you want? s, m or l")
add_pepperoni = input("Do you want pepperoni? y or n")
extra_cheese = input("Do you want extra cheese? y or n")
bill = 0
# Do some calculations 
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    "input is not valid"

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese =="y":
    bill+=1

#Print the result 
print(f"You final ${bill}")
