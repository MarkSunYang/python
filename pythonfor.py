#1.列表截取

# item in list  判断列表中是否存在
#cmp(1,2)


# for item in 'python':
#     print(' current letter',item)#遍历字符串中的字母
#
# for item in '12345':
#     print('number ',item)

#python 数组分为  1.list的普通列表  2.Tuple的元组  3.Dictionary 字典 Hash数组

a=[1,2,3,4,5]
b=['1','2','3','4','5']
c=['123','abc',1,'222']

# print(a[0])
# print(b[0])
# print(c[0])
# print(a[0:5])

# for i in range(0,len(a)):#从 0到len(a)  range(5) 从0-5不包含5
#     print(a[i])

fruit=['apple','banana','pear']
for i in range(len(fruit)):
    print('current fruit'+str(i)+fruit[i] )

#print(cmp(1,2))