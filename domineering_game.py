compMove = None


def draw_table(row, column, matrix):  # board drawing
    mat = [[0 for _ in range(column * 2 + 3)] for _ in range(row * 2 + 3)]

    if mat[0][0] == 0:
        br = row
        for x in range(0, row * 2 + 3):
            for y in range(0, column * 2 + 3):
                if x == 0 or x == 1 or x == row * 2 + 1 or x == row * 2 + 2:
                    if y == 0 or y == 1 or y == column * 2 + 1 or y == column * 2 + 2:
                        if y == 1:
                            mat[x][y] = "  "
                        else:
                            mat[x][y] = " "
                    elif x == 1 or x == row * 2 + 1:
                        if y % 2 == 0:
                            mat[x][y] = "═"
                        else:
                            mat[x][y] = " "
                    elif y % 2 != 0:
                        mat[x][y] = " "
                    elif x == 0 or x == row * 2 + 2:
                        if y % 2 == 0:
                            mat[x][y] = chr(65 + y // 2 - 1)
                elif y == 0 or y == 1 or y == column * 2 + 1 or y == column * 2 + 2:
                    if x == 0 or x == 1 or x == row * 2 + 1 or x == row * 2 + 2:
                        mat[x][y] = " "
                    elif y == 1 or y == column * 2 + 1:
                        if x % 2 == 0:
                            mat[x][y] = "║"
                        else:
                            mat[x][y] = " "
                    elif x % 2 != 0:
                        mat[x][y] = "  "
                    elif y == 0 or y == column * 2 + 2:
                        if x % 2 == 0:
                            if br >= 10:
                                mat[x][y] = str(br)
                            elif y == column * 2 + 2:
                                mat[x][y] = str(br)
                            else:
                                mat[x][y] = " " + str(br)
                            if y == column * 2 + 2:
                                br -= 1
                else:
                    if x % 2 != 0:
                        if y % 2 == 0:
                            mat[x][y] = "─"
                        else:
                            mat[x][y] = " "
                    elif y % 2 != 0:
                        if x % 2 == 0:
                            mat[x][y] = "|"
                        else:
                            mat[x][y] = " "
                    else:
                        mat[x][y] = " "

    for i in range(row):
        for j in range(column):
            mat[i * 2 + 2][j * 2 + 2] = matrix[i][j][1]

    for i in range(row * 2 + 3):
        for j in range(column * 2 + 3):
            print(mat[i][j], end=" ")
        print("")


def create_matrix(row, column):  # matrix definition
    return [[(2, " ") for _ in range(column)] for _ in range(row)]


def get_opponent(player):
    if player[1] == "X":
        return ((player[0] + 1) % 2, "O")
    return ((player[0] + 1) % 2, "X")


def is_valid_move(move, matrix, player, column, row):  # checking move validity
    y = ord(move[1]) - 65
    move_valid = False

    if 1 <= move[0] <= row and 0 <= y < column:
        if player[1] == "X":
            if row - move[0] - 1 >= 0:
                if (
                    matrix[row - move[0]][y] == (2, " ")
                    and matrix[row - move[0] - 1][y] == (2, " ")
                ):
                    move_valid = True
        else:
            if y + 1 < column:
                if (
                    matrix[row - move[0]][y] == (2, " ")
                    and matrix[row - move[0]][y + 1] == (2, " ")
                ):
                    move_valid = True

    return move_valid


def play_move(matrix, player, move, column, row):  # playing moves
    if not is_valid_move(move, matrix, player, column, row):
        return False

    y = ord(move[1]) - 65

    if player[1] == "X":
        matrix[row - move[0]][y] = player
        matrix[row - move[0] - 1][y] = player
    else:
        matrix[row - move[0]][y] = player
        matrix[row - move[0]][y + 1] = player

    return True


def delete_move(matrix, move, player, row):  # deleting a specific move
    y = ord(move[1]) - 65

    if player[1] == "X":
        matrix[row - move[0]][y] = (2, " ")
        matrix[row - move[0] - 1][y] = (2, " ")
    else:
        matrix[row - move[0]][y] = (2, " ")
        matrix[row - move[0]][y + 1] = (2, " ")


def input_move_validation(user_input):  # validating input
    user_input = user_input.strip()
    parts = user_input.split()

    if len(parts) != 2:
        print("Wrong entry! Please enter the coordinates in the form -> <row><space><column>")
        return False

    if not parts[0].isnumeric():
        print("Incorrect entry!")
        return False

    if len(parts[1]) != 1 or parts[1] < "A" or parts[1] > "Z":
        print("Wrong entry! The column position must be a single uppercase letter!")
        return False

    return True


def convert_input_move(user_input):  # converting string to tuple
    user_input = user_input.strip()
    parts = user_input.split()
    return int(parts[0]), parts[1]


def end_game(matrix, player, column, row):  # end game check
    end = True

    if player[1] == "X":
        for i in range(1, row):
            for j in range(column):
                if matrix[i][j] == (2, " ") and matrix[i - 1][j] == (2, " "):
                    end = False
                    break
            if not end:
                break
    else:
        for i in range(row):
            for j in range(column - 1):
                if matrix[i][j] == (2, " ") and matrix[i][j + 1] == (2, " "):
                    end = False
                    break
            if not end:
                break

    return end


def available_moves(matrix, player, column, row):  # all possible moves for a player
    moves = []
    for i in range(1, row + 1):
        for j in range(65, column + 65):
            move = (i, chr(j))
            if play_move(matrix, player, move, column, row):
                moves.append(move)
                delete_move(matrix, move, player, row)
    return moves


def evaluate_state(matrix, ai_player, column, row):
    ai_moves = available_moves(matrix, ai_player, column, row)
    opponent = get_opponent(ai_player)
    opponent_moves = available_moves(matrix, opponent, column, row)
    return len(ai_moves) - len(opponent_moves)


def max_value(depth, alpha, beta, matrix, current_player, ai_player, column, row):
    possible_moves = available_moves(matrix, current_player, column, row)

    if depth == 0 or not possible_moves:
        return evaluate_state(matrix, ai_player, column, row)

    value = -float("inf")
    opponent = get_opponent(current_player)

    for move in possible_moves:
        play_move(matrix, current_player, move, column, row)
        value = max(
            value,
            min_value(depth - 1, alpha, beta, matrix, opponent, ai_player, column, row)
        )
        delete_move(matrix, move, current_player, row)

        alpha = max(alpha, value)
        if alpha >= beta:
            break

    return value


def min_value(depth, alpha, beta, matrix, current_player, ai_player, column, row):
    possible_moves = available_moves(matrix, current_player, column, row)

    if depth == 0 or not possible_moves:
        return evaluate_state(matrix, ai_player, column, row)

    value = float("inf")
    opponent = get_opponent(current_player)

    for move in possible_moves:
        play_move(matrix, current_player, move, column, row)
        value = min(
            value,
            max_value(depth - 1, alpha, beta, matrix, opponent, ai_player, column, row)
        )
        delete_move(matrix, move, current_player, row)

        beta = min(beta, value)
        if beta <= alpha:
            break

    return value


def minimax(matrix, player, column, row, depth=4):
    global compMove

    possible_moves = available_moves(matrix, player, column, row)
    if not possible_moves:
        compMove = None
        return

    best_value = -float("inf")
    best_move = possible_moves[0]
    opponent = get_opponent(player)

    for move in possible_moves:
        play_move(matrix, player, move, column, row)
        value = min_value(depth - 1, -float("inf"), float("inf"), matrix, opponent, player, column, row)
        delete_move(matrix, move, player, row)

        if value > best_value:
            best_value = value
            best_move = move

    compMove = best_move
    play_move(matrix, player, compMove, column, row)
    draw_table(row, column, matrix)


def start_game():  # main function
    input_table = False

    while not input_table:
        row = input("Enter number of rows: ")
        column = input("Enter number of columns: ")

        if not row.isnumeric() or not column.isnumeric():
            print("Wrong entry!")
            continue

        row = int(row)
        column = int(column)

        if row < 2 or column < 2:
            print("The board is not big enough!")
            continue

        input_table = True

    first_player_correct = False
    while not first_player_correct:
        first_player = input("Enter the choice for the first player - \n human(0) computer(1): ")

        if not first_player.isnumeric():
            print("Wrong entry!")
            continue

        first_player = int(first_player)
        if first_player not in (0, 1):
            print("Wrong entry!")
            continue

        first_player_correct = True

    player1 = (first_player, "X")
    player2 = ((first_player + 1) % 2, "O")
    player = player1

    matrix = create_matrix(row, column)
    draw_table(row, column, matrix)

    move = None
    if player[0] == 0:
        move = input("Enter the coordinates of the move: ")

    game_over = False

    while not game_over:
        if player[0] == 1:
            print("Computer on the move:")
            minimax(matrix, player, column, row)
        else:
            if not input_move_validation(move):
                move = input("Enter the coordinates of the move: ")
                continue

            move = convert_input_move(move)

            if not play_move(matrix, player, move, column, row):
                print("Move " + str(move) + " is not valid!")
                move = input("Enter the coordinates of the move: ")
                continue

            draw_table(row, column, matrix)

        if player[1] == "X":
            player = player2
        else:
            player = player1

        game_over = end_game(matrix, player, column, row)

        if not game_over:
            if player[0] == 0:
                move = input("Enter the coordinates of the move: ")
        else:
            print("GAME OVER")
            if player[1] == "X":
                print("The winner is player O")
            else:
                print("The winner is player X")


if __name__ == "__main__":
    start_game()