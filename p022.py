'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

import common

names = [word.strip('"') for word in file('p022.txt').readline().split(',')]
names.sort()

common.assertEquals('COLIN', names[938-1])

def score(index, name):
  return common.wordvalue(name) * (index+1)

common.assertEquals(49714, score(938-1, 'COLIN'))

total_score = sum(score(i, name) for i, name in enumerate(names))
common.submit(total_score, expected=871198282)
