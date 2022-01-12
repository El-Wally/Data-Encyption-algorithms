#SDES Encrypt
def Rotate(input,l,d):
    text2=""
    text1=""
    # slice string in two parts for left and right
    if d==0:

        text1 = input[0 : l]
        text2 = input[l :]
    if d==1:
        text1 = input[0 : len(input)-l]
        text2 = input[len(input)-l : ]



    # now concatenate two parts together

    #print(text2+text1)
    return text2+text1
def Arrange(data,key):
    result=''
    for i in data:
        result+=key[int(i)-1]

    return result

def KeyGen(key,p10,p8,step):
    data=p10.split()
    data1=p8.split()
    temp = Arrange(data,key)
    temp1=temp[0:5]
    temp2=temp[5:11]
    if step==1:

        temp1=Rotate(temp1,1,0)
        temp2=Rotate(temp2,1,0)


    if step==2:
        temp1=Rotate(temp1,3,0)
        temp2=Rotate(temp2,3,0)


    temp = Arrange(data1,temp1+temp2)
    return temp

def XOR(v1,v2):
    temp=""
    for x,y in zip(v1,v2):
        if x==y:
            temp+='0'
        else:
            temp+='1'
    return temp


def sbox(s0,s1,s2):
    l=s0[:4]
    r=s0[4:]
    col=calc(l[1:3])
    row=calc(l[0]+l[-1])
    x=s1[row][col]
    x=calc(x)
    col=calc(r[1:3])
    row=calc(r[0]+r[-1])
    y=s2[row][col]
    y=calc(y)
    return x+y

def calc(val):
    if val=='11':
        return 3
    elif val=='00':
        return 0
    elif val=='01':
        return 1
    elif val=='10':
        return 2
    elif val=='0':
        return '00'
    elif val=='1':
        return '01'
    elif val=='2':
        return '10'
    elif val=='3':
        return '11'

def inverse(round2):
    k=1
    i=0
    temp=""
    while(1):




        if round2[i]==str(k):

            temp+=(str(i+1))
            k+=1
            i=0
            if k==9:
                return temp
        else:
            i+=1




def SDESencrypt(key,text,p10,p8,p4,ep,ip,s0,s1,ipinv=''):

     '''
        This function encrypt the given text using
        SDES ciphering algorithm

        Parameters Key:- string of the key itself
                   Text string for text to be encrypted
                   S1- 2D matrix
                   S2- 2D matrix

         Returns :- Encrypted text

     '''

     temp=""
     temp1=""
     for i in key:
         if i!='0' and i!='1':
             for k in key:
                 temp+=hextobinary(k)
             break

     for i in text:
         if i!='0' and i!='1':
             for k in text:
                 temp1+=hextobinary(k)
             break

     if len(temp)>2:
         key=temp
     if len(temp1)>2:
         text=temp1



     key1=KeyGen(key,p10,p8,1)
     key2=KeyGen(key,p10,p8,2)

     perm=Arrange(ip.split(),text)
     perm1=perm[int(len(perm)/2):]

     perm1=Arrange(ep.split(),perm1)

     perm1=XOR(perm1,key1)

     perm1=sbox(perm1,s0.split(),s1.split())

     perm1=Arrange(p4.split(),perm1)
     perm1=XOR(perm1,perm[:int(len(perm)/2)])
     round2=perm1+perm[int(len(perm)/2):]
     round2=perm[int(len(perm)/2):]+perm1
     #print(round2)
     round2=Arrange(ep.split(),perm1)
     round2=XOR(round2,key2)
     #print(round2)
     round2=sbox(round2,s0.split(),s1.split())
     round2=Arrange(p4.split(),round2)
     round2=XOR(round2,perm[int(len(perm)/2):])
     round2=round2+perm1
     #print(round2)
     if len(ipinv)>2:
         return Arrange(ipinv.split(),round2)

     ipinv=inverse(ip.split())
     return Arrange(ipinv,round2)



def SDESdecrypt(key,text,p10,p8,p4,ep,ip,s0,s1,ipinv=''):

     '''
        This function decrypt the given text using
        SDES ciphering algorithm

        Parameters Key:- string of the key itself
                   Text string for text to be encrypted
                   S1- 2D matrix
                   S2- 2D matrix

         Returns :- decrypted text

     '''
     temp=""
     temp1=""
     for i in key:
         if i!='0' and i!='1':
             for k in key:
                 temp+=hextobinary(k)
                 #print(temp)
             break
     for i in text:
         if i!='0' and i!='1':
             for k in text:
                 temp1+=hextobinary(k)
             break


     if len(temp)>2:
         key=temp
     if len(temp1)>2:
         text=temp1

     key1=KeyGen(key,p10,p8,1)
     key2=KeyGen(key,p10,p8,2)
    # print(key1)
    # print(key2)
     perm=Arrange(ip.split(),text)
     perm1=perm[int(len(perm)/2):]
    # print(perm)
     perm1=Arrange(ep.split(),perm1)
    # print(perm1)
     perm1=XOR(perm1,key2)
    # print(perm1)
     perm1=sbox(perm1,s0.split(),s1.split())
    # print(perm1)
     perm1=Arrange(p4.split(),perm1)
     perm1=XOR(perm1,perm[:int(len(perm)/2)])
     round2=perm1+perm[int(len(perm)/2):]
     round2=perm[int(len(perm)/2):]+perm1
    # print(round2)
     round2=Arrange(ep.split(),perm1)
     round2=XOR(round2,key1)
    # print(round2)
     round2=sbox(round2,s0.split(),s1.split())
     round2=Arrange(p4.split(),round2)
     round2=XOR(round2,perm[int(len(perm)/2):])
     round2=round2+perm1
     hexv=''
    # print(round2)
     ipinv=ipinv.split()
     if len(ipinv)>2:

         ipinv=Arrange(ipinv,round2)
         for i in range(0, len(ipinv), 4):
             print(ipinv[i:i+4])
             hexv+=binarytohex(ipinv[i:i+4])
         return ipinv+" Hex is ="+ hexv


     ipinv=inverse(ip.split())
     ipinv=Arrange(ipinv,round2)
     for i in range(0, len(ipinv), 4):
         print(ipinv[i:i+4])
         hexv+=binarytohex(ipinv[i:i+4])
     return ipinv+" Hex="+ hexv





def hextobinary(character):
     '''
        This function converts non binary character(hex)
        to binary(0,1)

        Parameters Key:- no binary character received to
                   be converted into binary

         Returns :- Binary digit

     '''

     keyhold='00'
     string=''
     hexvalues = [('A',10),('B',11),('C',12),('D',13),('E',14),('F',15)]
     for i in hexvalues:
         if character==i[0]:
            keyhold=i[1]
            break
     if keyhold=='00':
         keyhold=int(character)

     for i in range(4):
         keyhold-=(2**(3-len(string)))
         if keyhold>=0:
             string = string+'1'
         else:
             keyhold+=(2**(3-len(string)))
             string =  string + '0'
     return string
def binarytohex(character):
     '''
        This function converts non binary character(hex)
        to binary(0,1)

        Parameters Key:- no binary character received to
                   be converted into binary

         Returns :- Binary digit

     '''

     string=''

     keyhold=0


     for i in range(4):
         if character[i]=='1':
             keyhold+=(2**(3-i))
             print(keyhold)
     hexvalues = [('A',10),('B',11),('C',12),('D',13),('E',14),('F',15)]
     string=str(keyhold)
     for i in hexvalues:
         if keyhold==i[1]:
             string=i[0]
             break
     print(string)
     return string
