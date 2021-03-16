"""

# Example One


my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = my_list1

# How would you verify that my_list1 and my_list2 have the same identity?
print(my_list1 is my_list2)  # True

my_list1.append(7)
# Check if my_list1 and my_list2 still have the same identity.
# If they do, why is that?
print(my_list1)  # [1, 2, 3, 4, 5, 6, 7]
print(my_list2)  # [1, 2, 3, 4, 5, 6, 7]
print(my_list1 is my_list2)  # True

"""



"""
# Example Two

my_text1 = "Lambda School"
my_text2 = my_text1
# How would you verify that my_text1 and my_text2 have the same identity?
print(my_text1 is my_text2)  # True
print(my_text1)  # Lambda School
print(my_text2)  # Lambda School

my_text1 += " is awesome!"
# Check if my my_text1 and my_text2 still have the same identity?
print(my_text1 is my_text2)   # False
print(my_text1)  # Lambda School is awesome
print(my_text2)  # Lambda School
# If they do  noe, why is that?

my_text2 += " is awesome!"
# Now check if my_text1 and my_text2 have the same value?
print(my_text1 is my_text2)  # False
# do they? Explain why and why not.
"""



"""
# Example three
"""
# Initialize a list and assign to produce
produce = ["Apple", "Banana", "Carrot"]
# Initialize a tuple and include a reference to the produce list in the tuple
store = ("Bill's Grocery", produce)
print(id(store))  #140240549769984
# Add a new item to the produce list
produce.append("Dragonfruit")
produce = ['TOTALLY NEW LIST']
print(id(store))  #140240549769984

# Did you notice that the identity of store remmained the same?
# But I thought if you changed a mutable object, a new object would be created in memory?
# Why did that not occur here?