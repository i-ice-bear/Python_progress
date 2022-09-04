def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 0)
    two = 'X' if xState[2] else ('O' if zState[2] else 0)
    three = 'X' if xState[3] else ('O' if zState[3] else 0)
    four = 'X' if xState[4] else ('O' if zState[4] else 0)
    five = 'X' if xState[5] else ('O' if zState[5] else 0)
    six = 'X' if xState[6] else ('O' if zState[6] else 0)
    seven = 'X' if xState[7] else ('O' if zState[7] else 0)
    eight = 'X' if xState[8] else ('O' if zState[8] else 0)


    print(f" {zero} | {one} | {two} ")
    print(f" --|---|-- ")
    print(f" {three} | {four} | {five} ")
    print(f" --|---|-- ")
    print(f" {six} | {seven} | {eight} ")
    pass


def checkWin(xState, zState):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for wins in win:
        if sum(xState[wins[1]], xState[wins[2]], xState[wins[3]]) == 6:
            print("X wins the match")
            return 1
        if sum(zState[wins[1]], zState[wins[2]], zState[wins[3]]) == 6:
            print("Z wins the match")
            return 1
    return - 1


if __name__ == "__main__":
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    turn = 1
    print("Welcome to tic tac toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X chance")
            value = int(input("Please enter a value : "))
            xState[value] = 1
        else:
            print("O chance")
            value = int(input("Please enter a value : "))
            zState[value] = 1
        checkWin(xState, zState)
        if checkWin !=- 3:
            break
        turn = 1 - turn


