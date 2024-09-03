# final working code
def func(s):
    sub = s[0]
    longest = ''
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            sub += s[i+1]
        else:
            sub = s[i+1]
        if len(sub) > len(longest):
            longest = sub
        print(sub)
    print('Longest substring in alphabetical order is: ' + longest)


s = 'azcbobobegghakl'
func(s)
