for _ in range(int(input())):
    string = input()
    while ' && ' in string or ' || ' in string:
        string = string.replace(' && ', ' and ').replace(' || ', ' or ')
    print(string)
