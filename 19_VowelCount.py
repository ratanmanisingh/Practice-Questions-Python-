def vowel(text):
    v = "AEIOUaeiou"
    count = 0
    for i in text:
        if i in v:
            count += 1
    return count

text = input()
print(vowel(text))