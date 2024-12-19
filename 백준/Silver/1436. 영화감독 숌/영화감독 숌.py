n = int(input())
end_num = 666 
cnt = 0 

while True:
    if '666' in str(end_num):
        cnt += 1 
        if cnt ==n:
            break
    end_num += 1 

print(end_num)