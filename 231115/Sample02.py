f = open('./1984.txt', 'r')
temp = f.read().split(' ')
edited = list()
for each in temp:
    if '\n' in each:
        for eachW in each.split('\n'):
            if eachW != '\n' and eachW != '':
                if '.' in eachW or ',' in eachW:
                    edited.append(eachW[:-1])
                else :
                    edited.append(eachW)
    else:
        if '.' in each or ',' in each:
            edited.append(each[:-1])
        else:
            edited.append(each)

result = dict()
for each in edited:
    if each in result:
        result[each] = result[each] + 1
    else :
        result[each] = 1

answer = list()

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break
for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break

for each in result.items():
    if each[1] == max(result.values()):
        answer.append(each)
        result.pop(each[0])
        break    
print(answer)
# print(result)

f = open('./outcome.txt', 'w')
for each in answer:
    f.write(each[0] + '\t' + str(each[1]) +'\n')