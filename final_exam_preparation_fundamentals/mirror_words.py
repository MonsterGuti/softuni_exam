import re

text_string = input()

regex = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.findall(regex, text_string)

mirror_words = []

for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")
