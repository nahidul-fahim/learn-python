# string are immutable in python. Meaning, we can't change the value of the variable. We can only assign a new value to the variable.

# here I have declared a string variable and I am trying to change the value of the variable
username = "Nahid"

print(username)

username = "Another value"

print(username)

# Explanation: here I have assigned another value to the variable username. But strings are immutable in python. So, the original value of the variable username is not changed. It has just been replaced by the new value.

# We are changing the string Nahid here. We are just assigning a new reference to the variable username. As, Nahid is not being used in anywhere else, so Python garbage collector will remove it from the memory.


# Here is another example of mutable and immutable

x = 10
y = x
x = 15
print(x)
print(y)

# Explanation: here x value is 15, but y value is still 10. Because, when we assign x = 10, a reference is created in the memory and y is also pointing to the same reference. But when we assign x = 15, a new reference is created in the memory and x is pointing to the new reference. So, y is still pointing to the original reference.