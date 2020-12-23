from janome.tokenizer import Tokenizer
t = Tokenizer()
result = []
for token in t.tokenize(u'私はタイ人です'):
    result.append(token)

print(result[0])
