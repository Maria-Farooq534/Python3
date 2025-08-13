'''
Challenge For each word in words, add "d" to the end of the word if the word ends in “e” to make it past tense. 
Otherwise, add "ed" to make it past tense. Save these past tense words to a list called past_tense.
'''
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[-1] == 'e':
        word = word + 'd'
        past_tense.append(word)
    else:
        word = word + 'ed'
        past_tense.append(word)
print(past_tense)
