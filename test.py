import data

def test_legal_inputs():
    total = 0;
    failed = 0;
    print('\n----- Testing legal inputs')
    for col_k, col_v in data.colors.items():
        print(f"---------- Color {col_v}")
        for pie_k, pie_v in data.pieces.items():
            total += 1
            print(f"Testing {col_v}, and {pie_v}")
            val = col_k | pie_k
            color, piece = data.new_get_values(val)
            if color != col_v:
                print(f"FAILED: Color does not match\n\t{col_v} - {color}")
                failed += 1
                continue
            if piece != pie_v:
                print(f"FAILED: Piece does not match\n\t{pie_v} - {piece}")
                failed += 1
                continue

            print(f"SUCCESS: Color and Piece matches")
    return total, failed

def test_illegal_inputs():
    total = 1
    failed = 0
    print('\n---- Testing illegal inputs')
    val = 32 | 64
    try:
        color, piece = data.new_get_values(val)
        if color == None or piece == None:
            print(f"SUCCESS: Caught error, and returned null")
    except TypeError as e:
        print(f"FAILED: failed to catch error, and returned: {e}")
        failed +=1

    return total, failed

if __name__ == '__main__':
    total, failed = 0,0

    t, f = test_legal_inputs()
    total += t
    failed += f

    t, f = test_illegal_inputs()
    total += t
    failed += f

    print(f"\nSTATUS: failed/total\t{failed}/{total}")
