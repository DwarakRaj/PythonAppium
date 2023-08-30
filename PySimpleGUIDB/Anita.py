s="AAABBBCCC"
s1=" "
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        s1 = str(count) + s[i]
        count = 1
print(s1)