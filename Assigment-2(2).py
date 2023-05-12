ascii_dict = {}
start = ord(input("Enter the starting character (a-z): "))
end = ord(input("Enter the ending character (a-z): "))

for i in range(start, end+1):
    ascii_dict[chr(i)] = i
    
print("Dictionary:", ascii_dict)
