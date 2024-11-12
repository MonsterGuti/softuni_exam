result1 = input("Enter the score for the first game (format: team1:team2): ").split(":")
result2 = input("Enter the score for the second game (format: team1:team2): ").split(":")
result3 = input("Enter the score for the third game (format: team1:team2): ").split(":")

won = 0
lost = 0
draw = 0

if int(result1[0]) > int(result1[1]):
    won += 1
elif int(result1[0]) < int(result1[1]):
    lost += 1
else:
    draw += 1

if int(result2[0]) > int(result2[1]):
    won += 1
elif int(result2[0]) < int(result2[1]):
    lost += 1
else:
    draw += 1

if int(result3[0]) > int(result3[1]):
    won += 1
elif int(result3[0]) < int(result3[1]):
    lost += 1
else:
    draw += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")
