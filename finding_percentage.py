n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
query_scores = student_marks[query_name]
print([query_scores])
print("{0:.2f}".format(sum(query_scores)/len(query_scores)))
