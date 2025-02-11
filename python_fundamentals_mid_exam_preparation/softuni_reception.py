efficiency_sum = sum(int(input()) for i in range(3))
students_count = int(input())
time_needed = 0

while students_count > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    students_count -= efficiency_sum

print(f"Time needed: {time_needed}h.")
