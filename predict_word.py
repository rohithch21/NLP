import json
import ast


with open('model.txt','r') as f:
    d = ast.literal_eval(f.read())

s = ["today","the"]
sentence_length = 15
i = 0
count = 2
while count < sentence_length:
    bi_gram = (s[i],s[i+1])
    next_word_dict = d[bi_gram]
    next_word = sorted(next_word_dict,key=next_word_dict.get,reverse=True)[0]
    s.append(next_word)
    i+=1
    count+=1

print(' '.join(s))