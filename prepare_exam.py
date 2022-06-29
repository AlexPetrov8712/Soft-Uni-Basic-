bad_grades = int(input())
fail_time = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True
while fail_time < bad_grades:
    problem = input()
    if problem == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        fail_time += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem
if has_failed:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')