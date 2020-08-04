# def sum_all(a, b, c):
#     return a + b + c
#
#
# def mul(a, b):
#     return a * b
#
#
# result = sum_all(1, 2, 3) + mul(10, 10)
#
# print(result)
# print 로 값 확인해보기
# result라는 변수의 값은?

# 조건문 01
# def is_even(num): # is_even이라는 이름의 함수를 정의한다. num을 변수로 받는다.
#     if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
#         return True # 참을 반환한다
#     else: # 아니면,
#         return False # 거짓을 반환한다
#
# result = is_even(24)
# print(result)

# 조건문 02
# def is_adult(age):
#     if age >=20:
#         print('성인입니다!')
#     else:
#         print('청소년이에요!')
#
# is_adult(30)

# 조건문 03 if/elif/else
# 조건을 여러 개 사용하고 싶을 때
# def check_generation(age):
#     if age > 120:
#         print('와 19세기에 태어나셨군요!')
#     elif age> 80:
#         print('80세 이상! 인생은 여든부터!')
#     else:
#         print('젊으시군요! 장래희망이 뭔가요?')
#
# my_age = 55
# check_generation(my_age)

#반복문 01
# fruits = ['사과', '배', '감', '귤']
#
# for fruit in fruits:
#     print(fruit)

# 반복문 02-1 과일 갯수 세기 함수
# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
#
# count = 0
# for fruit in fruits:
#     if fruit == '사과':
#         count += 1
#
# # 사과의 개수를 출력합니다
# print(count)

# 반복문 02-2
# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
# def count_fruits(name):
#     count = 0
#     for fruit in fruits:
#         if fruit == name:
#             count +=1
#     return count
#
# subak_count = count_fruits('수박')
# print(subak_count)
#
# gam_count = count_fruits('감')
# print(gam_count)

# 반복문 03-1
# wizards = [
#     {'name' : '해리', 'age' : 40},
#     {'name' : '허마이오니','age' : 40},
#     {'name' : '론', 'age': 41}
# ]
#
# #모든 마법사의 이름과 나이 출력
# for wizard in wizards:
#     print(wizard['name'], wizard['age'])

# 반복문 03-2
professor_wizards =[
    {'name': '덤블도어', 'age': 116},
    {'name' : '맥고나걸','age' : 85},
    {'name' : '스네이프', 'age': 60},
]

# 이번엔, 반복문과 조건문을 활용한 함수를 만들어 봅시다
# 마법사의 이름을 받으면, age를 리턴해주는 함수
def get_age(name, wizards):
    #wizards! 윗 줄 함수 선언에서 사용한 변수죠? 함수 사용하는 쪽에서 쓰는 변수명 아닙니다!
    for wizard in wizards:
        if wizard['name'] == name:
            return wizard['age']
    return '해당하는 이름이 없습니다.'

print(get_age('덤블도어', professor_wizards))
print(get_age('말포이', professor_wizards))
