
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter your name: ")
date = input("Enter date: ");

print(letter.format("<|Name|>",name))
print(letter.format("<|Date|>",date))

# print(letter);
