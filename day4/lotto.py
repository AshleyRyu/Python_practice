import requests
import random

#1.url로 요청을 보낸다
url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

#2.응답된 결과를 json으로 바꿔서 dictionary처럼 활용한다.
response = requests.get(url).json()
# lotto_numbers = response.json()
drwNo = response["drwNo"]
# print(type(drwNo))

drwtNo = []
for i in range (1,7):
    drwtNo.append(response[f'drwtNo{i}'])

bnusNo = response["bnusNo"]

# print(drwNo)
# print(drwtNo)

# #3. 랜덤으로 로또 번호 하나를 추출한다

# # -> 복원추출이므로 ban
# # myNum = []
# # for i in range (1,7):
# #     myNum.append(random.randrange(1,46))
# # print(myNum)

# myNum = []
# myNum = random.sample(range(1,46),6)
# print(myNum)

# #4. 몇 등인지 알아본다
# # 1등 : 6개, 2등: 5개+보너스번호
# # 3등 : 5개, 4등 : 4개, 5등 : 3개
# cnt = 0
# # print(len(myNum))
# for i in range (len(myNum)):
#     if myNum[i] in drwtNo:
#        cnt += 1

# flag = 1
# count = 0
# print(cnt)

# while (flag): 
#     if cnt == 6:
#         print("1등 !")
#         flag = 0
#     elif cnt == 5:
#         # print("3등 !")
#         for i in range (len(myNum)):
#             if bnusNo in drwNo:
#                 print(" 2등 !")
#             else:
#                 print(" 3등 !")
#     elif cnt == 4:
#         print(" 4등 !")
#     elif cnt == 3:
#         print(" 5등 !")
#     else :
#         count += 1
#         # print("다음 기회에 . . .")



'''set 자료형
파이선에는 set이라는 자료혀이 있다.
list를 set으로 형변환 할 수 있다.ArithmeticError혹은 a= {1,2,5}직접 만들 수도 있다.
ex. a = [1,2,2]
set(a)
>> [1,2]

'''
# matched = len(set(drwNo) & set (myNum))
# print(matched)

lucky = [0,0,0,0,0]
for i in range(100000000):
    myNum = random.sample(range(1,46),6)
    matched = len(set(drwtNo) & set(myNum))

    if matched == 6 :
        lucky[0] += 1
        print(i)
        print(3100000000*lucky[0]+66000000*lucky[1]+1500000*lucky[2]+50000*lucky[3]+5000*lucky[4])
        break
    elif matched == 5 and bnusNo in myNum:
        lucky[1] += 1
    elif matched == 5:
        lucky[2] += 1        
    elif matched == 4:
        lucky[3] += 1
    elif matched == 3:
        lucky[4] += 1
    # elif matched == 2:
    #     lucky[5] += 1

    print(lucky, i, end="\r") 