import threading
import os
from multiprocessing import Process

# count
text = 'hi, a7, good'
count = text.count(',')
print(count)

# find
text = 'hi, a7, good'
position = text.find('a7')
print(position)

# index
text = 'hi, a7, good'
try:
    position = text.index('good')
    print(position)
except ValueError:
    print("찾는 문자열이 없습니다.")

# join
text = ['boyoung', 'bobo', 'hanilcome']
join_text = ','.join(text)
print(join_text)

# upper, lower
text = ['boyoung', 'bobo', 'hanilcome']
up = text.upper()
low = text.lower()
print(up)
print(low)

# replace
text = 'hi, a7, good'
replace_text = text.replace("good", "very good")
print(replace_text)

# split
text = 'boyoung,bobo,hanilcome'
name = text.split(',')
print(name)

# len
number = [1,2,3,4,5]
print(len(number))

# del
number = [1,2,3,4,5]
del number[0]
print(number)

# append
number = [1,2,3,4,5]
number.append('10')
print(number)

# sort
number = [1,2,3,4,5]
number.sort()
print(number)

# reverse
number = [1,'b','3','4','a']
number.reverse()
print(number)

# index
text = ['boyoung', 'bobo', 'hanilcome']
print(text.index('bobo'))

# insert
number = [1,2,3,4,5]
number.insert(2, 10)
print(number)

# remove
number = ['1',2,3,4,5]
number.remove(1)
print(number)

# pop
number = [1,2,3,4,5]
number.pop(1)
print(number)

# count
number = [1,2,3,3,4,5]
print(number.count(3))

# extend
number = [1,2,3,3,4,5]
number.extend([6,7,8])
print(number)

# += 연산자
number = [1,2,3]
number += [4,6,8]
print(number)

# 딕셔너리 초기화
my_dict = {}
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

# 딕셔너리 쌍 추가
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4
print(my_dict)

# 딕셔너리 특정 요소 삭제
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["a"]
print(my_dict)

# 딕셔너리에서 특정 key에 해당하는 value값 얻기
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["a"])

# 딕셔너리에서 모든 key를 리스트로 만들기
my_dict = {"a": 1, "b": 2, "c": 3}
key_list = list(my_dict.keys())
print(key_list)

# 딕셔너리에서 모든 value를 리스트로 만들기
my_dict = {"a": 1, "b": 2, "c": 3}
values_list = list(my_dict.values())
print(values_list)

# item: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
person = {"name" : "boyoung", "age" : "26"}
items = person.items()
print(items)

# clear: 딕셔너리의 모든 요소를 삭제
person = {"name" : "boyoung", "age" : "26"}
person.clear()
print(person)

# get: 딕셔너리에서 지정한 키에 대응하는 값을 반환(딕셔너리에 key가 없는 경우, None을 반환)
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.get('a'))
print(my_dict.get('e'))
print(my_dict.get('a', 'e'))

# in: 해당 키가 딕셔너리 안에 있는지 확인
my_dict = {"a": 1, "b": 2, "c": 3}
print('a' in my_dict)
print('e' in my_dict)

# 프로세스와 스레드
def foo():
    print('child process', os.getpid())
    
if __name__ == '__main__':
    print('parent process', os.getpid())
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()


def foo():
    print('This is foo')
    
def bar():
    print('This is bar')
    
def baz():
    print('This is baz')

if __name__ == '__main__':
    print('parent process', os.getpid())
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()


def foo():
    print('process id', os.getpid())
    
if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = Process(target=foo).start()
