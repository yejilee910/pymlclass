'''
2020.03.20 파이썬 
'''

a = 200

msg = "I love Python"

list_data = ['a', 'b', 'c']

dic_data = {'a': 97, 'b': 98}

print(a)
print(msg)
print(list_data)
print(list_data[0])
print(list_data[0:2])
print(dic_data)
print(dic_data['a'])
print(dic_data['b'])

''' ----------
기본구문 if, list 
-----------
'''

if 'a' in list_data:
    print("\'a\'가 list_data에 있습니다.")
    print(list_data)
else:
    print('a가 list_data에 존재하지 않습니다.')

'''----------
기본구문 - for + if
---------'''

scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)
    break
else:
    print('Perfect')

'''-----------
기본구분 - while + 탈출 
-------------
'''

x = 1
total = 0
while 1:
    total += x
    if total > 10000:
        print(x)
        print(total)
        break
    x += 1


'''--------------
복소수표시
----------'''

c1 = 1+7j
print(c1.real)
print(c1.imag)
c2 = complex(2, 3)
print(c2)
