def print_formatted(number):
    spacing = len(str(bin(number))[2:]) + 1
    for n in range(1, number+1):
        final = str(n).rjust(spacing-1, ' ')
        final += str(oct(n)[2:]).rjust(spacing, ' ')
        hex_value = str(hex(n)[2:]).upper()
        final += hex_value.rjust(spacing, ' ')
        final += str(bin(n)[2:]).rjust(spacing, ' ')
        print(final)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
