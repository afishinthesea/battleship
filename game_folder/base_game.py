board_size = (10,10) #horizontal, vertical

number_to_letter = {
1:"A",  2:"B",  3:"C",  4:"D",  5:"E",  6:"F",  7:"G",  8:"H",
9:"I",  10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",
17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X",
25:"Y", 26:"Z" }

#outputs a board, as a list of lists
def init_board(board_size):
    output = []
    for line in range(board_size[1]):
        temp = []
        for i in range(board_size[0]):
            temp.append(str(number_to_letter[line]) + str(i))
        output.append(temp)

print(init_board(board_size))
