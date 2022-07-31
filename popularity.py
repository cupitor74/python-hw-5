def popularity(text):

    array_text = text.lower().split(' ')
    values = dict(( x, array_text.count(x)) for x in set(array_text) )
    values_sorted = sorted(values.items(), key = lambda x: (-x[1], x[0]))
    
    result = list( i[0] for i in values_sorted )
    return result


# popularity('apple kiwi pineapple kiwi apple kiwi') #-> ['kiwi', 'apple', 'pineapple']
# popularity('aPPle pine Apple kiwi Apple kiwi') #-> ['apple', 'kiwi', 'pine']
# popularity('aPPle pine Apple kiwi Apple kiwi') #-> ['apple', 'kiwi', 'pine']
# popularity('aab aaa a aac da aab bb aac bb aaa xxx x b xxx') #-> ['aaa', 'aab', 'aac', 'x']