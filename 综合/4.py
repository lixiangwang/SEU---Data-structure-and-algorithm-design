import time

def cross(A, B):
    return [a+b for a in A for b in B]

def arr_to_dict(A, B):
    return dict(zip(A, B))

def str_to_arr(str_sudoku):
    return [c for c in str_sudoku if c in cols or c in '0.']

def show_str_sudoku(str_sudoku):
    for i, value in enumerate(str_sudoku):
        if i%3 == 0 and i%9 != 0:
            print('|', end=' ')
        print(value, end=' ')
        if (i+1)%9 == 0:
            print()
        if i == 26 or i == 53:
            print('------+-------+------')

def show_dict_sudoku(dict_sudoku):
    width = 1 + max(len(dict_sudoku[s]) for s in squares)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(dict_sudoku[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    print()

cols = '123456789'
rows = 'ABCDEFGHI'

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], []))-set([s])) for s in squares)


def parse_sudoku(str_sudoku):
    values = dict((s, cols) for s in squares)
    arr_sudoku = str_to_arr(str_sudoku)
    dict_sudoku = arr_to_dict(squares, arr_sudoku)# {'A1': '4', 'A2': '.', ... , 'I8': '.', 'I9': '.'}

    for key,value in dict_sudoku.items():
        if value in cols and not assign(values, key, value):
            return False

    return values

def assign(values, key, value):
    other_values = values[key].replace(value, '')
    if all(eliminate(values, key, num) for num in other_values):
        return values
    else:
        return False

def eliminate(values, key, num):
    if num not in values[key]:
        return values
    values[key] = values[key].replace(num, '')

    if len(values[key]) == 0:
        return False
    elif len(values[key]) == 1:
        only_value = values[key]
        if not all(eliminate(values, peer, only_value) for peer in peers[key]):
            return False

    for unit in units[key]:
        dplaces = [s for s in unit if num in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            only_key = dplaces[0]
            if not assign(values, only_key, num):
                return False

    return values

def solve_sudoku(str_sudoku):
    return search_sudoku(parse_sudoku(str_sudoku))

def search_sudoku(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values

    n, key = min((len(values[key]), key) for key in squares if len(values[key]) > 1)
    return some_result(search_sudoku(assign(values.copy(), key, num)) for num in values[key])

def some_result(values):
    for result in values:
        if result:
            return result
    return False

if __name__ == '__main__':
    str_sudoku = ['4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......']

    for sudoku in str_sudoku:
        start = time.clock()
        solve_result = solve_sudoku(sudoku)
        end = time.clock()
        print('初始数独为：')
        show_str_sudoku(sudoku)
        print('解为：')
        show_dict_sudoku(solve_result)
        print("求解数独运行时间为: %f s" % (end - start))