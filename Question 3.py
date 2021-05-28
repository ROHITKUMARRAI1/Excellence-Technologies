def getMax(x):
    max = 0
    k = ''
    for key in x:
        if x[key] > max:
            max = x[key]
            k = key
    return {k, max}

dict1 = {'1': "sanjay", '2': "Rohit", '3': "Mayank", '4': "sunny", '5': "jass"}
marks = {'1': 30, '2': 40, '3': 70, '4': 43, '5': 55}
d = getMax(marks)
print(d)