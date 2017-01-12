def longestPalindrome(string):
    text=string.lower()
    results={}
    for i in range(len(text)):
        for j in range(0,i):
            chunk=text[j:i+1]

            if chunk==chunk[::-1]:
                temp_dict={chunk:len(chunk)}
                results.update(temp_dict)
    max_key=max(results, key=results.get)
    return max_key
    





string="babad"
pal=longestPalindrome(string)
print pal
