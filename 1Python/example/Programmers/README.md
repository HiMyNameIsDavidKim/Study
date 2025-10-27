# 프로그래머스 피드백

## `[구현]`

### [유용한 라이브러리]
* 대소문자 변환: lower() upper(), (Lv1_1)
* 앞뒤에 모든 점 제거: strip('.'), (Lv1_1)
* 길이로 리스트 소팅하기: sort(key=len), (Lv2_1)
* 세트 자료형, (Lv2_1)
    * 중복 제거: seen = set()
    * 원소 추가: seen.add(item)
* 숫자인지 확인하기: isdigit(), (Lv2_2)
* 카운터 라이브러리, (Lv2_3)
    * 등장 횟수 세는 라이브러리
    * from collections import Counter
    * a = ['a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    * c = Counter(a)
    * print(c) # Counter({'a': 1, 'b': 3, 'c': 4, 'd': 1})
    * c['a'] -= 1
    * print(c) # Counter({'a': 0, 'b': 3, 'c': 4, 'd': 1})
    * if c['a'] == 0: del c['a']
    * print(c) # Counter({'b': 3, 'c': 4, 'd': 1})
<br><br>

### [오타 주의]
* endwith() 가 아니라 endswith(), (Lv1_1)
<br><br>




