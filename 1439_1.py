s = input()

count = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count += 1

result = count // 2
print(result)