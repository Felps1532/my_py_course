message = input(">")

# every time it finds a 'space' between the words, it will split in words[]
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output) 