def solution(n):
    answer = ''
    for num in range(n):
        if num % 2 == 0 and num <= 10000:
            answer += '수'
        else:
            answer += '박'

    return answer

print(solution(5))