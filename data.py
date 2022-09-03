pieces = {
    0: 'none',
    1: 'king',
    2: 'pawn',
    3: 'knight',
    4: 'bishop',
    5: 'rook',
    6: 'queen',
}
i_pieces = {v: k for k, v in pieces.items()}

colors = {
    8:  'white',
    16: 'black',
}
i_colors = {v: k for k, v in colors.items()}

def new_get_values(val):
    # 00     000
    # |Color |Type
    #
    binary = '{0:05b}'.format(val)

    try:
        color = colors[int(binary[:2],2) << 3]
    except KeyError:
        color = None

    try:
        piece = pieces[int(binary[2:], 2)]
    except KeyError:
        piece = None

    # print(binary)
    # print(color)
    # print(piece)
    return color, piece
