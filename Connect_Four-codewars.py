'''
Connect Four https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces 
which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]
The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.
'''

columnmap = dict((v, k) for k, v in enumerate("ABCDEFG"))

def who_is_winner(pieces_position_list):
    field = [["" for _ in range(6)] for _ in range(7)]
    result = "Draw"
    for move in pieces_position_list:
        column, color = parse_move(move)
        for idx in range(len(field[column])):
            if field[column][idx] == "":
                field[column][idx] = color
                break
        ended, result = check_winner(field)
        if ended:
            print_field(field)
            return result
    print_field(field)
    return result

def parse_move(string):
    col, value = string.split("_")
    column_number = columnmap[col]
    return column_number, value

def check_winner(field):
    '''
    Checking columns
    '''
    filled = 0
    for column in field:
        winning_color = ""
        count = 0
        for color in column:
            if color != "":
                filled += 1
            if color != "" and color == winning_color:
                count += 1
            elif color != "":
                winning_color = color
                count = 1
            if count == 4:
                print("Found winning column", column)
                return True, winning_color
    '''
    Checking rows
    '''
    for y in range(len(field[0])):
        row = [field[x][y] for x in range(len(field))]
        winning_color = ""
        count = 0
        for color in row:
            if color != "" and color == winning_color:
                count += 1
            elif color != "" and color != winning_color:
                winning_color = color
                count = 1
            else:
                winning_color = ""
                count = 0
            if count == 4:
                print("Found winning row", row)
                return True, winning_color
    '''
    Checking diagonals
    '''
    for i in range(4):
        for j in range(3):
            l = len(field[0])
            if field[i][j] == field[i+1][j+1] == field[i+2][j+2] == field[i+3][j+3] and field[i][j] != "":
                print("Found winning left diagonal")
                return True, field[i][j]
            if field[i][l-j-1] == field[i+1][l-j-2] == field[i+2][l-j-3] == field[i+3][l-j-4] and field[i][l-j-1] != "":
                print("Found winning right diagonal")
                return True, field[i][l-j-1]
    '''
    If no moves left this is a draw and game over
    '''
    if filled == 42:
        return True, "Draw"
    
    return False, "Draw"

def print_field(field):
    for y in range(len(field[0])):
        for x in range(len(field)):
            print(field[x][-y-1][:1], end="\t")
        print("\n")
    for k in columnmap:
        print(k, end="\t")
    print()   
    
test2 = [
"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red", 
"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red", 
"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red", 
"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red", 
"E_Yellow", "E_Red"
]

test3 = [
"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
]

print(who_is_winner(test2))
print(who_is_winner(test3))