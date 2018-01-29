text = "ThiS is String with Upper and lower case Letters"
m = list(text.lower())
m.sort()
Text = {}

for letter in m:
    Text[letter] = Text.get(letter, 0) + 1

del Text[' ']

for text, count in Text.items():
    print(text, count, end =" ")
    print()
