# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("yo")
#     print("sup?")
#     print("wyd?")

# greet()


#Function that allows for input

# def greet_with_name(name):
#     print(f"Hello, {name}.")
#     print(f"How do you do, {name}?")

# greet_with_name("James")


# Functions with more than 1 input
# Example of positional and keyword arguments

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

# positional argument
greet_with("Reginald", "NYC")

# keywork argument
greet_with(location = "NYC", name = "Reginald")

