import string
fileptr0= open("Files//diffchars.txt","r")
data = fileptr0.read()
if data:
    countwords = 0
    words = data.split(" ")
    while words:
        countwords = countwords +1
    print("NO of words in total::",countwords)
    countvowel = 0
    countconsonants = 0
    countdigits = 0
    countwhitespace = 0
    countspecial = 0
    vowel = set("aeiouAEIOU")
    for i in data:
        if i in vowel:
            countvowel = countvowel+1
        elif(i>='a' and i<='z') or (i>='A' and i<='Z'):
            countconsonants = countconsonants+1
        elif i.isdigit():
            countdigits = countdigits+1
        elif i in string.whitespace:
             countwhitespace = countwhitespace+1
        else:
            countspecial = countspecial+1
    fileptr0.close()
    fileptr1 = open("Files//diffchars.txt","w")
    fileptr1.write("NO of Vowel in total is::"+countvowel+"\n")
    fileptr1.write("NO of Consonants in total is::"+countconsonants+"\n")
    fileptr1.write("NO of Digits in total is::"+countdigits+"\n")
    fileptr1.write("NO of Whitespaces in total is::"+countwhitespace+"\n")
    fileptr1.write("NO of Special charachters in total is::"+countspecial+"\n")
    fileptr1.close()
else:
    print("----------NO DATA FOUND IN FILE----------------")

 