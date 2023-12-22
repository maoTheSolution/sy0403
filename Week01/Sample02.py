import random 
temp = [each for each in range(11)]
newList = []
while(len(newList) < len(temp)):
    index = random.randint(0, len(temp)-1)
    newList.append(temp[index])

print(temp)
print(newList)
print(max(newList))
print(newList)


result = list()


while(len(newList) > 0):
    target = max(newList)
    newList.remove(target)
    result.append(target)
    
print(result)

# # print([each for each in temp if each % 2 != 0])

# filter(lambda each: each%2 !=0, temp)

# # lambda 
# # filter
# for each in filter(lambda each: each%2 !=0, temp):
#     print(each)


