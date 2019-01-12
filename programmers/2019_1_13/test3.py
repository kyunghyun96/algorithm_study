# 문제 설명
# String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
#
# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# Kim은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    answer = ''
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

arr = [["Jane", "Kim"]]
return_list = ["김서방은 1에 있다"]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 3 min
