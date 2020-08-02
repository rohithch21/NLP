from nltk.corpus import reuters
import pre_processor

def trigram(sentence):
    # sentence = list(sentence.split(' '))
    l = len(sentence)
    i = 0
    trigram_list = []
    while i < l-2:
        trigram_list.append((sentence[i],sentence[i+1],sentence[i+2]))
        i += 1
    return trigram_list

def build_model(sentences):
    model = {}
    for sentence in sentences:
        sentence = ' '.join(sentence)
        sentence = pre_processor.main(sentence)
        for ele in trigram(sentence):       
            w1,w2,w3 = ele
            if (w1,w2) not in model.keys():
                model.update({(w1,w2): {w3 : 1}})
            else:
                if w3 not in model[(w1,w2)]:
                    model[(w1,w2)].update({w3:1})
                else:
                    model[(w1,w2)][w3] += 1
    
    for item in model:
        total = float(sum(model[item].values()))
        for word in model[item]:
            model[item][word] /= total
    
    with open('model.txt','w') as f:
        f.write(str(model))


build_model(reuters.sents())