
s = 'azcbobobegghakl'
count = 0
for x in s:
    if (x == 'a' or x == 'o' or x == 'e' or x == 'i' or x == 'u'):
        count = count + 1

print('Number of vowels: ' + str(count))


count = 0
spot = 0
for x in s:
    spot = spot + 1
    if x == 'b':
        if s[spot] == 'o' and s[spot+1] == 'b':
            count = count + 1
print('number of times bob occurs: ' + str(count))
