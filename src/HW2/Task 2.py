sentence = input("Введите предложение: ")
words = [word.strip('.,!?-‘“”') for word in sentence.split()]
longest_word = max(words, key=len)
print(f"Самое длинное слово в предложении: {longest_word}")
