import data

failed = 0
total = 0

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
print('----------')

print(f"STATUS: failed/total\t{failed}/{total}")
