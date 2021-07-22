
import random

bchpoint=0
fac_point=[]
shp_point=[]
hwy_point=[]
hse_point=[]

BCH, FAC, HSE, SHP, HWY = 8, 8, 8, 8, 8

turn_count = 0

fail_turn=False

house_lists = ['BCH', 'FAC', 'HSE', 'SHP', 'HWY']
letters = ['A', 'B', 'C', 'D']
board = [[' ', ' ', ' ', ' ']
       , [' ', ' ', ' ', ' ']
       , [' ', ' ', ' ', ' ']
       , [' ', ' ', ' ', ' ']]

def print_each_list():
    for index, number in enumerate(number_list):
        print(str(number),end='')
        if index == len(number_list) - 1:
            print(' = ', end='')
        else:
            print(' + ', end='')
    print(sum(number_list))

def find_neighbours():
    neighbours=[]
    for i in [-1,1]:
        if 0<=row + i<len(board):
            neighbours.append(board[row+i][column])
    for j in [-1,1]:
        if 0<=column + i<len(board[row]):
            neighbours.append(board[row][column+j])
    return neighbours

def find_neighbours_for_HWY():
    neighbours=[]
    for a in [-1,1]:
        if 0<=row + i<len(board):
            neighbours.append(board[row+i][column])
    return neighbours


def has_neighbour():
    #check if there are neighbours above or below
    for i in [-1, 1]: 
        if 0 <= row + i < len(board): #check if row is inside of the (4x4)board
            if board[row + i][column] != ' ': #check if the space is not empty
                return True
            
    #check if there are neighbours left right
    for j in [-1, 1]:
        if 0 <= column + i < len(board[row]): #check if row is inside of the (4x4)board
            if board[row][column + j] != ' ': #check if the space is not empty
                return True  
    return False

random_build1 = random.choice(house_lists)
random_build2 = random.choice(house_lists)


def display_board():
    print('     ' + '     '.join(str(a) for a in letters))
    print('  +-----' + '+-----' + '+-----' + '+-----' + '+')
    count = 1
    for row in board:
        elem_row = '| '
        for col in row:
            elem_row += str(col) + " " * (4 - len(col)) + "| "
        print(count, elem_row)
        print('  +-----' + '+-----' + '+-----' + '+-----' + '+')
        count += 1

def display_game_menu():
    print('1. Build a ' + random_build1)
    print('2. Build a ' + random_build2)
    print('3. See remaining buildings')
    print('4. See current score')
    print("\n")
    print('5. Save game')
    print('0. Exit to game menu')

def remaining_buildings():
    print('{:20s}{:20s}'.format('Building','Remaining'))
    print('--------            ---------')
    print('HSE                 '+str(HSE))
    print('FAC                 '+str(FAC))
    print('SHP                 '+str(SHP))
    print('HWY                 '+str(HWY))
    print('BCH                 '+str(BCH))

def menu():
    print('Welcome, mayor of Simp City! ')
    print('-----------------------------')
    print('1. Start new game')
    print('2. Load saved game')
    print('0. Exit')
    choice1 = input('Your choice? ')

print('Welcome, mayor of Simp City! ')
print('-----------------------------')
print('1. Start new game')
print('2. Load saved game')
print('0. Exit')
choice1 = input('Your choice? ')

# Game loop
if choice1=='1':
    while turn_count < 16:
        turn_count = turn_count + 1
        print("\n")
        print('Turn ' + str(turn_count))
        display_board()
        if not fail_turn:
            random_build1 = random.choice(house_lists)
            random_build2 = random.choice(house_lists)
        display_game_menu()

        your_choice = ''
        while your_choice not in ('1', '2' , '3' , '4', '5', '0'):

            your_choice = input('Your choice? ')

            if (your_choice == '1'):
                building = random_build1

            elif (your_choice == '2'):
                building = random_build2

            elif (your_choice == '3'):
                print('\n')
                remaining_buildings()
                turn_count=turn_count-1
                print('\n')
                
            elif (your_choice == '4'):
                print('option 4 remaining')

            elif (your_choice == '5'):
                print('option 5 remaining')

            elif (your_choice == '0'):
                menu()
                turn_count=turn_count-1

            else:
                print('Please type again.')
            
        if (your_choice=='1') or (your_choice=='2'):
            build_where = input('Build where? ')
            x = build_where[0]
            row = int(build_where[1]) - 1

            if (x == 'a'):
                column = 0
            elif (x == 'b'):
                column = 1
            elif (x == 'c'):
                column = 2
            elif (x == 'd'):
                column = 3
                
            if has_neighbour() or turn_count == 1:
                
                if (your_choice=='1') or (your_choice=='2'):
                    
                    if (building == 'BCH'):
                        BCH -= 1
                    if (building == 'FAC'):
                        FAC -= 1
                    if (building == 'HSE'):
                        HSE -= 1
                    if (building == 'SHP'):
                        SHP -= 1
                    if (building == 'HWY'):
                        HWY -= 1
                
                board[row][column] = building
                fail_turn=False
                
            else:
                print('You must build next to an axisting building')
                turn_count=turn_count-1
                fail_turn=True
                
        for i in range(len(building)):
            if ('BCH' in board[i][0]) or ('BCH' in board[i][3]):
                bch_point = 3
            else:
                bch_point = 1
        
        #BCH points
        bch_point=[]
        for i in range(len(board)):
            if ('BCH' in board[i][0]) or ('BCH' in board[i][3]):
                bchpoint=3
            if ('BCH' in board[i][1]) or ('BCH' in board[i][2]):
                bchpoint=1
        
        #FAC points
        FAC_built = 8-FAC
        if FAC_built<5:
            facpoint=[FAC_built]*FAC_built
        else:
            facpoint=([4]*4+[1]*(FAC_built - 4))
        
        #SHP points
        shp_neighbours=find_neighbours()
        shppoint=0
        for building2 in shp_neighbours:
            if building2 == 'FAC':
                shppoint+=1
            elif building2 == 'HSE':
                shppoint+=1
            elif building2 == 'HWY':
                shppoint+=1
            elif building2 == 'BCH':
                shppoint+=1
        
        #HSE points
        hse_neighbours=find_neighbours()
        hsepoint=0
        for building1 in hse_neighbours:
            if building1 == 'FAC':
                hsepoint=1
                break
            elif building1 == 'SHP':
                hsepoint+=1
                break
            elif building1 == 'HSE':
                hsepoint+=1
                break
            elif building1 == 'BCH':
                hsepoint+=2
                break
        
        #HWY points
        if HWY==8:
            hwypoint=0
        hwy_neighbours=find_neighbours_for_HWY()
        hwypoint=0
        for building3 in hwy_neighbours:
            if building3 == 'HWY':
                hwypoint+=1
        
        if turn_count==16:
            number_list=hsepoint
            print_each_list()
            
            number_list=facpoint
            print_each_list()
            
            number_list=shppoint
            print_each_list()

            number_list=hwypoint
            print_each_list()

            number_list=bchpoint
            print_each_list()














        


{"mode":"full","isActive":false}