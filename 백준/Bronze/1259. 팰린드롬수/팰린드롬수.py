while True:
    str = input().strip()
    if int(str) == 0:
        break
    
    reverse_str = str[::-1]

    if str == reverse_str:
        print("yes")
    else:
        print("no")