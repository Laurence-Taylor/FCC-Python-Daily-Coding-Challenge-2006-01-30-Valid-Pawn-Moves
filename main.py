def find_pawn_moves(position):
    # create a set of all possible paw initial positions
    pawn_initial_pos = {'A2','B2','C2','D2','E2','F2','G2','H2'}
    # if position is initial return the two possibles values
    if position in pawn_initial_pos:return [position[:1]+'3',position[:1]+'4']
    # else return the only one possible value
    else:return [position[:1]+str(int(position[1:])+1)]

if __name__ == '__main__':
    print(find_pawn_moves("D4"))
    print('------')
    print(find_pawn_moves("B2"))
    print('------')
    print(find_pawn_moves("A7"))
    print('------')
    print(find_pawn_moves("G2"))
    print('------')
    print(find_pawn_moves("E3"))