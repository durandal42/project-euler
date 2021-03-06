'''
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2;
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

import common
import itertools

data = file("p042.txt")
words = [word.strip('"') for word in data.readline().split(",")]

max_word_length = max(len(w) for w in words)
max_word_score = max_word_length * 26
triangles = set(itertools.takewhile(lambda x: x < max_word_score,
                                    (n*(n+1)/2 for n in itertools.count())))

def triangle_word(w):
  return common.wordvalue(w) in triangles

common.assertEquals(True, triangle_word('SKY'))

count = sum(1 for w in words if triangle_word(w))

common.submit(count, expected=162)
