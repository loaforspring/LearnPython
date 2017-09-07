# #list 列表
# classmates = ['Michael', 'Bob', 'Tracy']
# print('classmates:', classmates)
# classmates.append('Adam')
# print('after append:', classmates)
# classmates.insert(1, 'Jack')
# print('after insert:', classmates)
# classmates.pop()
# print('after pop:', classmates)
# classmates.pop(1)
# print('after pop(1):', classmates)
# classmates[1] = 'Sarah'
# print('after change:', classmates)

# listTwo = ['1', '2', ['a', 'b'], '3', '4']
# print('listTwo:', listTwo)
# print(listTwo[2][0])

# #tuple 有序列表：元组
# tuple1 = ('a', 'b', 'c') #注意这里是小括号
# print(tuple1)
# #元组一但定义就不可变

# line = '\nabc\n'
# print(line)
# print('==============')
# line = line.rstrip()
# print(line)
# print('over')
# s = '{0}.eggs,and{1}'.format ('spam', 'SPAM!')
# print(s)

# #list comprehension expression 列表解析表达式
M = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
# print(M)
# col = [row[1] for row in M] #M中循环每一行，将索引1对应的元素产生一个新的list
# print(col)
# col2 = [row[1]+1 for row in M] #M中循环每一行，将索引1对应的元素+1之后产生一个新的list
# print(col2)
# col3 = [row[1] for row in M if row[1] %2 ==0] #M中循环每一行，将索引1对应的元素中能被2整除的元素产生一个新的list
# print(col3)

# 循环
for m in M:
    print(m)

i = 0
while i < 10:
    if i > 5:
        break
    print(i)
    i = i+1

