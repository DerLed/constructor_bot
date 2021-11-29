def check_win(game_field):
    """Checking the winning combination. If the function wins,
    it returns a tuple of the True value and the winning symbol.
    If there is no winner, returns False.
    """
    lenght = len(game_field[0])
            
    # Check row
    for it in game_field:
        if it.count(it[0]) == lenght:
            return (True, it[0])
        
    # Check column
    for it in range(0, lenght):
        row_from_column = []
        for jt in range(0, lenght):
            row_from_column.append(game_field[jt][it])
        if row_from_column.count(row_from_column[0]) == lenght:
            return (True, row_from_column[0])
    
    # Check main diagonal
    row_from_diagonal = []
    for it in range(0, lenght):
        row_from_diagonal.append(game_field[it][it])
    if row_from_diagonal.count(row_from_diagonal[0]) == lenght:
            return (True, row_from_diagonal[0])
    
    # Check reverse diagonal
    row_from_diagonal = []
    for it, jt in zip(range(lenght-1, -1, -1), range(0, lenght)):
        row_from_diagonal.append(game_field[jt][it])
    if row_from_diagonal.count(row_from_diagonal[0]) == lenght:
            return (True, row_from_diagonal[0])
    
    return False
