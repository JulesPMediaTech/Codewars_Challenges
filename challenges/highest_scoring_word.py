"""
Docstring for Dev.CodeWars_challenges.highest_scoring_word

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

def high(sentence):
    words = sentence.split()
    scores = [sum (map(' abcdefghijklmnopqrstuvwxyz'.index, w) ) for w in words]
    return words[scores.index(max(scores))]


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

words = "what time are we climbing up the volcano"
words = 'semyekzz take me to trout'
words = 'aaa b ba'

print (f'''\n{words}
highest scoring word: {high(words)}
       ''')