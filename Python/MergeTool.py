import textwrap

def merge_the_tools(string, k):
    result = []
    tool = textwrap.wrap(string, k)
    for item in tool:
        slot = []
        for c in item:
            if c not in slot:
                slot.append(c)
        result.append(slot)
    
    for group in result:
        print(''.join(group))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
