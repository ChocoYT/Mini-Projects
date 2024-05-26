text = ""
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numbers = []
points = []
remove = []

for i, char in enumerate(text):
    if char in number:
        numbers.append(i)
    elif char == ".":
        points.append(i)

for i, char in enumerate(text):
    if i - 1 in points:
        remove.append(i)
    elif (i - 1 in remove) and (char in number):
        remove.append(i)

text_list = []
for i, char in enumerate(text):
    if not ((i in remove) or (i in points)):
        text_list.append(char)

text = ""
for _i, char in enumerate(text_list):
    text += char

print(text)