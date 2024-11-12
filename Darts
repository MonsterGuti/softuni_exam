# Input the player's name and initialize starting points
player_name = input()
starting_points = 301
current_points = starting_points
successful_shots = 0
unsuccessful_shots = 0

# Read the first sector input
sector = input()

# Loop until the player retires or the points reach exactly 0
while sector != "Retire":
    points = int(input())  # Read the points for the current shot
    
    # Calculate points based on sector type
    if sector == "Single":
        shot_points = points
    elif sector == "Double":
        shot_points = 2 * points
    elif sector == "Triple":
        shot_points = 3 * points
    else:
        # Invalid sector type; skip this iteration
        continue

    # Check if the shot is successful
    if current_points >= shot_points:
        # Deduct points and increase successful shots count
        current_points -= shot_points
        successful_shots += 1
        
        # Check if player has won (i.e., points are exactly 0)
        if current_points == 0:
            print(f"{player_name} won the leg with {successful_shots} shots.")
            break
    else:
        # Unsuccessful shot (points exceed current points)
        unsuccessful_shots += 1

    # Read the next sector input for the next shot
    sector = input()

if sector == "Retire":
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
