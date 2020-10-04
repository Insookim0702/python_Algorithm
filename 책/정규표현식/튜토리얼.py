
n = 'NKMD849320jkfelw'

l = list(n)
all_arr = []
alpha_arr = []
num_arr = []
for i in l:
    if i.isalpha():
        alpha_arr.append(i)

    if i.isdigit():
        num_arr.append(i)

    if i.isalnum():
        all_arr.append(i)


print((''.join(alpha_arr)))
print((''.join(num_arr)))
print((''.join(all_arr)))


# re 모듈의 compile 함수는 정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴하는데,
# 즉 re.compile(검색할문자열) 와 같이 함수를 호출하면 정규식 객체 (re.RegexObject 클래스 객체)를 리턴하게 된다.

import re
# r = re.compile()

# re.RegexObject 클래스가 가지는 메서드
# 1. match() :
# 2. search() : 처음 매칭된 문자열만 리턴한다. 반환값은 처음 매칭된 문자열을 리턴한다. 없으면, None을 리턴한다.
# 3. findall() : 매칭된 모든 경우를 리턴한다.
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류 에러 1033: 아"
regex = re.compile("에러 1033")
search = regex.search(text)
print(search)
print(search.group())
print(search.span())
print(search.start())
print(search.end())
mo = regex.findall(text)
print(mo)

# 전화번호 추출
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
regex = re.compile('\d{3}-\d{3}-\d{4}')
match_obj = regex.search(text)
phone_num = match_obj.group()
print(phone_num)

text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)

# 문자열 시작부터 끝까지 a-z 또는 0-9가 들어가야한다.
text = '123'
regex = re.compile('[a-z]+')
match = regex.match(text)
text1 = 'qwe1'
match = regex.search(text1)
print(match)


