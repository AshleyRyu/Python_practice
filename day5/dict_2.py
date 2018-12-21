import random

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "dj1":  {
            "lecturer": "tak",
            "manager": "pro1",
            "class president": "박성민",
            "groups": {
                "1조": ["강신욱", "윤영우", "이민교", "유창오", "황여진", "김민경"],
                "2조": ["노승만", "이재찬", "이주호", "김예지", "유지원"],
                "3조": ["이민지", "김희윤", "박성민", "조인정", "김슬기", "고병석"],
                "4조": ["임동명", "김승훈", "정상영", "정태현", "한단비", "김동민"]
            }
        },
        "dj2": {
            "lecturer": "junho",
            "manager": "pro2"
        }
    }
}

"""
난이도* 1. 지역(location)은 몇개 있나요?
출력예시)
4
"""
print("==========Q1===========")
print(len(ssafy["location"]))
'''
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
'''
print("==========Q2===========")
# print(ssafy["language"]["python"]["python standard library"].find("requsets"))
print("requests" in ssafy["language"]["python"]["python standard library"])
'''
난이도** 3. dj1반의 반장의 이름을 출력하세요.
출력예시)
박성민
'''
print("==========Q3===========")
print(ssafy["classes"]["dj1"]["class president"])
'''
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
'''
print("==========Q4===========")
language = list(ssafy["language"])
for i in range (len(language)):
    print(language[i])

'''
난이도*** 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.
출력 예시)
junho
pro2
'''
print("==========Q5===========")
print(ssafy["classes"]["dj2"]["lecturer"], ssafy["classes"]["dj2"]["manager"])
'''
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
'''
print("==========Q6===========")
key = list(ssafy["language"]["python"]["frameworks"].keys())
value = list(ssafy["language"]["python"]["frameworks"].values())
# => for key, value in ssafy(["lanuage"]["python"]["frameworks"]):
#   print(f:{key}는 {vlaue}이다.")
for i in range (len(key)):
    print(f"{key[i]}는 {value[i]}이다.")
# print(f"{key[1]}는 {value[1]}이다.")
"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 고병석
"""
print("==========Q7===========")
group3 = ssafy["classes"]["dj1"]["groups"]["3조"]
# dangbun = str(random.sample(group3, 1))
dangbun = random.choice(group3)
print(f"오늘의 당번은 {dangbun}")
# print(f"오늘의 당번은 {str(random.sample(group3, 1))}")
# for i in range (len(group3)):
#     print(f"오늘의 당번은 {str(random.sample(group3, 1))}")