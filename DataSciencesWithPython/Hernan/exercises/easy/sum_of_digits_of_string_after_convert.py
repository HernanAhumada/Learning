s = input('Enter you string: ')
k = int(input('Enter the times: '))

if (len(s) > 1 and len(s) <= 100):
    print("s: " + s)
    if s.islower():
        if (k >= 1 and k <= 10):
            print("K: " + str(k))
            alphabet = ''
            for i in range(97, 123):
                alphabet = alphabet + chr(i)
            sum = 0
            for i in s:
                index = alphabet.index(i) + 1
                sum = sum + index
            i = 2
            index = 0
            while k >= i:
                sum_total = 0
                for j in str(sum):
                    sum_total = sum_total + int(j)
                sum = sum_total
                i += 1            
            print("sum Final:" + str(sum))
        else:
            print("Number of time must be between 1 and 10")
    else:
        print("Your string must consist of lowercase English letters only")
else:
    print("Your string must be greater than 1 and lower than 100")