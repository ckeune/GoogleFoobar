def answer(s):
    # your code here 
    if bool(s.strip()) == False:
        return(0)
    if len(s) > 200:
        return(0)
    match = 0 
    length = int(len(s))  
   # elif s[0:int(lenth/2)] == s[int(lenth/2):lenth]
    #print('going to loop now')
    for i in range(length,0,-1): 
       # print(s[0:i])
        matches = s.count(s[0:i])
        #print(matches) 
        if match < matches:
            match = matches
    return(match)
    