# Mehraneh 30062786
# AT2.5 - Question 1
# Using a for loop to print out each line of the text file
# Your code must also close the file after reading from it.


# open the file in read mode
file = open("vehicles.txt", "r")
# using a for loop to print out each line of the text file
for line in file:
    print(line, end="")
# close the file
file.close()
