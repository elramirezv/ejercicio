test_string = "PAYPALISHIRING"
n_rows = 3
output = "PAHNAPLSIIGYIR"


def zizag_converter(string, n_rows):
    final = ""
    step = 2 * (n_rows - 1)
    for i in range(n_rows):
        for j in range(i, len(string), step):
            r = j + step - 2 * i
            final += string[j]  # Con este agregamos los extremos
            if i > 0 and i < n_rows - 1 and r < len(string):
                final += string[r]  # Con este agregamos los del centro

    return final


print(zizag_converter(test_string, 4))
