def solution(marks):
    marks.sort()
    n = len(marks)
    median = marks[n // 2] if n % 2 == 1 else (marks[n // 2 - 1] + marks[n // 2]) / 2
    return median
marks = [60,10,30,40,20,50]
result = solution(marks)
print(result)