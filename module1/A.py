flag = True
res = 0

while flag:
    try:
        inp = input()
        if (inp == ''):
            res += 0
        else:
            i = 0
            temp = ''
            checksmth = ''
            while i < len(inp):
                if (not '0' <= inp[i] <= '9' and temp != ''):
                    res += int(temp)
                    temp = ''
                    checksmth = ''

                if ('0' <= inp[i] <= '9'):
                    if (checksmth == '-'):
                        temp += '-'
                        checksmth = ''
                    temp += inp[i]
                else:
                    if (inp[i] == '-'):
                        if (temp == ''):
                            checksmth = '-'
                        else:
                            checksmth = ''

                i += 1
            if (temp != ''):
                res += int(temp)

    except Exception:
        flag = False

print(str(res))