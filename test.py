import random
menu = '쫄면', '육계장', '비빔밥', '돈까스'
# 메뉴 출력
print(menu)  
# 그중에 아무거나 하나 출력
print(random.choice(menu))

a = '1. 쫄면'
b = '2. 육계장'
c = '3. 비빔밥'
d = '4. 돈까스'

# 메뉴 리스트 만들기
munulist = ['1. 쫄면', '2. 육계장', '3. 비빔밥', '4. 돈까스', '5. 짜장면']
print("메뉴 출력")
print("메뉴 갯수: ", len(munulist))
for i in range(len(munulist)):
    print(munulist[i])
# print(munulist[0])
# print(munulist[1])
# print(munulist[2])
# print(munulist[3])
# print(munulist[4])
# print(a)
# print(b)
# print(c)
# print(d)
test_list = ['짜장', '짬뽕', '턍슉']
# for i in munulist:
#     print(i)
