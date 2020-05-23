s = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 맨 앞 문자가 1일 때, 전부 0으로 바꾸고자하는 경우,
# 맨 앞 문자에 대해 0으로 뒤집어주고 시작해야하므로 +1
if s[0] == '1':
    count0 += 1
# 위와 반대의 경우 +1 
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))