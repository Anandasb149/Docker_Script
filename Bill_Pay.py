import random
names = input("Enter the name in the group :")
names_list=names.split(",")
l=len(names_list)
random_name=random.randint(0,l-1)
print(f"{names_list[random_name]} Will pay the bill")
