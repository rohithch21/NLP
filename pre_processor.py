import re


def lowerCase(s):
    if type(s) is str:
        return s.lower()
    raise Exception("Input data must be of type - string")

def tokenizer(s):
    if type(s) is str:
        return list(s.split(" "))
    raise Exception("Input data must be of type - string")

def noise_removal(tokens):
    if type(tokens) is list:
        i=0
        l = len(tokens)
        while i < l:
            tokens[i] = re.sub('[^a-zA-Z0-9]+','',tokens[i])
            if tokens[i] == '':
                tokens.remove(tokens[i])
                l -= 1
            i += 1
    return tokens

def main(s):
    if type(s) is str:
        tokens = noise_removal(tokenizer(lowerCase(s)))
        return tokens
    raise Exception("Input data must be a string")

    


