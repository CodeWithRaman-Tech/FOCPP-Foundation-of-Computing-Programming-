'''
10.The Unicode characters corresponding to these codes: 80, 121, 116, 104, 111, 110.
'''
# Given Unicode codes
codes = [80, 121, 116, 104, 111, 110]

# Convert each code to character
characters = [chr(code) for code in codes]

# Join and display as a string
result = ''.join(characters)
print("The corresponding characters are:", result)
