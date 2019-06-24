n=input()
n=int(n)
score=[0 for i in range(n)]
for i in range(n):
    s=input()
    o=[0 for k in range(len(s))]
    for j in range(len(s)):
        if s[j]=='O':
            if j==0:
                o[j]=1
            elif o[j-1]!=0:
                o[j]+=(o[j-1]+1)
            else:
                o[j]=1
    for l in o:
        score[i]+=l
for i in score:
    print(i)