def minion_game(s):
    # your code goes here
    vow='AEIUOaeiou'
    ar=[]
    for i in range(len(s)):
        for j in range(len(s)):
            while i<j:
                ar.append(s[i:j])
    print(ar)


s="banana"
minion_game(s)
