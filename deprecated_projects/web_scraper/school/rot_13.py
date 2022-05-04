
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rotation = int(input("How much would you like your code to be rotated (<26): "))
in_string = input("What would you like to encode? ")
out_string = ""
for char in in_string:
    out_string += letter[letter.index(char) - 13]

print(out_string)
