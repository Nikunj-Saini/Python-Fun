def findlargestword(sentence):
    words = sentence.split()
    largest_word = max(words, key=len)
    return largest_word
sentence = input("Enter a sentence: ")
largest_word = findlargestword(sentence)
print("The largest word in the sentence is:", largest_word)
`