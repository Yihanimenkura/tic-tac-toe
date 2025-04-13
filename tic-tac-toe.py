lis = ["1","2","3","4","5","6","7","8","9"]

print()
for i in range (3):
    print ("", board [i*3],"|", board [i*3+1], "|", board [i*3+2],"|")

def draw_the_board(list):
    for i in range(3):
        print (list [i*3],"|",list[i*3+1],"|",list[i*3+2])
        print ("---------")

draw_the_board(lis)

def check_winner(list):
    win_status = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for xx in win_status: 
        if list[xx[0]] != " " and list[xx[0]] == list[xx[1]] == list[xx[2]]:
            return list[xx[0]] 
    return 0 

def main():
    count = 0 
    while True: 
        if count % 2 == 0:
            a = int(input("O Please type location to place: "))
            list [a] = "O"
        else: 
            a = int(input("Please type location to place: "))
            list[a] = "X"
        draw
        a = check_winner (list)
        if a == "X":
            print ("a wins")
            break
        elif a == "O":
            print ("a wins")
            break
        elif a == 0:
            continue
        check_winner(lis)
        draw_the_board(lis)
        count += 1 
        if count == 9:
            print("Tie")
            break
        current_player = "O" if current_player == "X" else "X"

if "__name__" == "__main__":
    main()

#["","","","","","","","",""]