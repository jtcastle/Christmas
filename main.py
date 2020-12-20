move_count = 5
score = 0
position = [0, 4]
direction = None

gridx = 5
gridy = 5

def move(position, direction):
    if direction == "up" and position[1] < gridy:
        position[1] += 1
    elif direction == "down" and position[1] > 0:
        position[1] -= 1
    elif direction == "left" and position[0] > 0:
        position[0] -= 1
    elif direction == "right" and position[0] < gridx:
        position[0] += 1
    else:
        print("Invalid Direction")
      
    print("Current Position: ", position)


coin_list = [[0,3],[2,2],[3,2]]

while direction != "exit" and move_count > 0:
    direction = input("Where to? ")
    move(position, direction)
    #coins(score, position)
    if position in coin_list: 
        score += 5
        print("Coin found!")
        print("Score = ", score)
        coin_list.remove(position)
    else:
        print("No Coin found")
        print("Score = ", score)
    
    move_count -= 1
    print("Moves Left: ", move_count)
    #print (coin_list)


print("Game Over")
print("Final Score =", score)

#Things that need fixing

# 1. Takes a turn away for an invalid direction
