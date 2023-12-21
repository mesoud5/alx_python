def multiple_returns(sentence):
    if len(sentence) == 0:
        return  None
    else:
        return len(sentence), sentence[0]
sentence = "At holberton school, i learn't c"
multiple_returns(sentence)
result = multiple_returns(sentence)
print(result)