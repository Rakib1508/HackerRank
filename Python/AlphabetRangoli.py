def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_list = []
    for i in range(size, 0, -1):
        half = alphabet[i-1:size:]
        line_list = half[::-1]
        if i != size:
            line_list += half[1:]
        line_list = '-'.join(line_list)
        final_list.append(line_list)
    
    max_width = len(final_list[-1])
    
    for c in range(size-2, -1, -1):
        item = final_list[c]
        final_list.append(item)
    
    for item in final_list:
        print(item.center(max_width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
