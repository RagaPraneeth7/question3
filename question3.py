for _ in range(int(input())):               # read number of test cases
    n= int(input())                         # read the nth strip
    h=list(map(int,input().split()))        # read the heights of the ground ino list
    b=h.reverse()                           # reversing the list h 
    c=0                                     # initialize c as 0
    if n%2!=0:                              # checking as odd
        for i in range((n//2)+1):           # for every i in range between a and odd+1
            if (h[i]==i+1 and h[i]==h[n-1-i]):          # if condition satisfies pass it 
                pass
            else:                           # else increment c with 1 and break
                c+=1
                break
        if(c==0):                           # if c equals 0, print yes
            print('yes')
        else:                               # else print no
            print('no')
    else:                                   #else print no
        print('no')