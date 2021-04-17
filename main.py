import sys
import io


def get_max_letter(letter):
    max_letter = 0
    i = 0
    j = 0
    for u in letter:
        if(int(u)>max_letter):
            max_letter = u
            i = j
        j+=1
    return i




letters = [0]*26
words = 0


file = open('dict.txt')

while 1:
    char = file.read(1)

    if(char=='a'):
        letters[0]+=1
    elif(char=='b'):
        letters[1]+=1
    elif(char=='c'):
        letters[2]+=1
    elif(char=='d'):
        letters[3]+=1
    elif(char=='e'):
        letters[4]+=1
    elif(char=='f'):
        letters[5]+=1
    elif(char=='g'):
        letters[6]+=1
    elif(char=='h'):
        letters[7]+=1
    elif(char=='i'):
        letters[8]+=1
    elif(char=='j'):
        letters[9]+=1
    elif(char=='k'):
        letters[10]+=1
    elif(char=='l'):
        letters[11]+=1
    elif(char=='m'):
        letters[12]+=1
    elif(char=='n'):
        letters[13]+=1
    elif(char=='o'):
        letters[14]+=1
    elif(char=='p'):
        letters[15]+=1
    elif(char=='q'):
        letters[16]+=1
    elif(char=='r'):
        letters[17]+=1
    elif(char=='s'):
        letters[18]+=1
    elif(char=='t'):
        letters[19]+=1
    elif(char=='u'):
        letters[20]+=1
    elif(char=='v'):
        letters[21]+=1
    elif(char=='w'):
        letters[22]+=1
    elif(char=='x'):
        letters[23]+=1
    elif(char=='y'):
        letters[24]+=1
    elif(char=='z'):
        letters[25]+=1
    elif(char=='\n'):
        words+=1
    elif not char:
        break

index = get_max_letter(letters)

print("MOST USED LETTER = "+str(index)+" WITH "+str(letters[index])+" USES")
print("WORDS = "+str(words))



file.close()
