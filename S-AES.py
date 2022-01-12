import numpy

print("S-AES Method")
plain = []

Key = []

RoundKey = []

sbnibRoundKey = []

ShiftRoundKey = []

Key0 = []

Key1 = []

Key2 = []

w0 = []

w1 = []

w2 = []

w3 = []

w4 = []

w5 = []

tempw1 = []

sbnibRoundKey2 = []

ShiftRoundKey2 = []

Round1Key = []

mixcolumns = []

Round2Key = []

flag = 0

n = 0

print("Please Enter your Plaintext")

while n < 16:
   plaintext = int(input())
   plain.append(plaintext)
   n += 1

print("Please Enter your Key")
n = 0

while n < 16:
    key = int(input())
    Key.append(key)
    if n < 8:
        w0.append(key)
    if 7 < n < 16:
        w1.append(key)
    n += 1

print("Plaintext: ", plain, '\n')

print("Your Key is:", Key, '\n')

print("Your W0 is:", w0, '\n')

print("Your W1 is:", w1, '\n')


def XOR(word1, word2, flag):
    wT1 = []
    wT2 = []
    wT3 = []
    wT1.extend(word1)
    wT2.extend(word2)
    wm = [1,0,0,0,0,0,0,0]
    wm2 = [0, 0, 1, 1, 0, 0, 0, 0]
    templist = []
    tempw1 = []
    i = 0
    if flag == 0:
        while i < 8:
            if wT1[i] == wT2[i]:
                wT3.append(0)
            else:
                wT3.append(1)
            i += 1

    if flag == 1:
        while i < 8:
            if wT1[i] == wm[i]:
                templist.append(0)
            else:
                templist.append(1)
            i += 1
        tempw1.extend(SubNib(RotNib(wT2), 0))
        i = 0
        while i < 8:
            if templist[i] == tempw1[i]:
                wT3.append(0)
            else:
                wT3.append(1)
            i += 1

    if flag == 2:
        while i < 8:
            if wT1[i] == wm2[i]:
                templist.append(0)
            else:
                templist.append(1)
            i += 1
        tempw1.extend(SubNib(RotNib(wT2), 0))
        i = 0
        while i < 8:
            if templist[i] == tempw1[i]:
                wT3.append(0)
            else:
                wT3.append(1)
            i += 1

    if flag == 3:
        while i < 16:
            if wT1[i] == wT2[i]:
                wT3.append(0)
            else:
                wT3.append(1)
            i += 1
    return wT3

def RotNib(w1):
    i = 4
    tempw1 = []
    while 4 <= i < 8:
        tempw1.append(w1[i])
        i += 1
    i = 0
    while i < 4:
        tempw1.append(w1[i])
        i += 1
    return tempw1

def SubNib(tempw1, flag):
    tempw1sub = []
    i = 0
    if flag == 0:
        while i < 4:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])

            i += 4

        i = 4
        while i < 8:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])

            i += 4
    if flag == 1:
        while i < 4:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])

            i += 4

        i = 4
        while i < 8:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])

            i += 4

        i = 8
        while i < 12:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])

            i += 4

        i = 12
        while i < 16:
            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 1, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 0, 1, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 0, 1])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 0, 0, 0])

            if tempw1[i] == 0 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 0, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([0, 0, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 0 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 0, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 0, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 0 and tempw1[i + 3] == 1:
                tempw1sub.extend([1, 1, 1, 0])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 0:
                tempw1sub.extend([1, 1, 1, 1])

            if tempw1[i] == 1 and tempw1[i + 1] == 1 and tempw1[i + 2] == 1 and tempw1[i + 3] == 1:
                tempw1sub.extend([0, 1, 1, 1])
            i += 4

    return tempw1sub

def KeyGen(word1,word2):
    TempKey = []
    TempKey.extend(word1)
    TempKey.extend(word2)
    return TempKey

def Shift(w1):
    Wt = []
    word = []
    word.extend(w1)
    i = 0
    while i < 4:
        Wt.append(word[i])
        i += 1
    i = 12
    while i < 16:
        Wt.append(word[i])
        i += 1
    i = 8
    while i < 12:
        Wt.append(word[i])
        i += 1
    i = 4
    while i < 8:
        Wt.append(word[i])
        i += 1
    return Wt

def decToHex(word):
    wordTemp = []
    wordTemp.extend(word)
    HexNum = []
    i = 0
    while i < 4:
        if wordTemp[i] == 0 and wordTemp[i+1] == 0 and wordTemp[i+2] == 0 and wordTemp[i+3] == 0:
            HexNum.append(0)
        if wordTemp[i] == 0 and wordTemp[i+1] == 0 and wordTemp[i+2] == 0 and wordTemp[i+3] == 1:
            HexNum.append(1)
        if wordTemp[i] == 0 and wordTemp[i+1] == 0 and wordTemp[i+2] == 1 and wordTemp[i+3] == 0:
            HexNum.append(2)
        if wordTemp[i] == 0 and wordTemp[i+1] == 0 and wordTemp[i+2] == 1 and wordTemp[i+3] == 1:
            HexNum.append(3)
        if wordTemp[i] == 0 and wordTemp[i+1] == 1 and wordTemp[i+2] == 0 and wordTemp[i+3] == 0:
            HexNum.append(4)
        if wordTemp[i] == 0 and wordTemp[i+1] == 1 and wordTemp[i+2] == 0 and wordTemp[i+3] == 1:
            HexNum.append(5)
        if wordTemp[i] == 0 and wordTemp[i+1] == 1 and wordTemp[i+2] == 1 and wordTemp[i+3] == 0:
            HexNum.append(6)
        if wordTemp[i] == 0 and wordTemp[i+1] == 1 and wordTemp[i+2] == 1 and wordTemp[i+3] == 1:
            HexNum.append(7)
        if wordTemp[i] == 1 and wordTemp[i+1] == 0 and wordTemp[i+2] == 0 and wordTemp[i+3] == 0:
            HexNum.append(8)
        if wordTemp[i] == 1 and wordTemp[i+1] == 0 and wordTemp[i+2] == 0 and wordTemp[i+3] == 1:
            HexNum.append(9)
        if wordTemp[i] == 1 and wordTemp[i+1] == 0 and wordTemp[i+2] == 1 and wordTemp[i+3] == 0:
            HexNum.append('A')
        if wordTemp[i] == 1 and wordTemp[i+1] == 0 and wordTemp[i+2] == 1 and wordTemp[i+3] == 1:
            HexNum.append('B')
        if wordTemp[i] == 1 and wordTemp[i+1] == 1 and wordTemp[i+2] == 0 and wordTemp[i+3] == 0:
            HexNum.append('C')
        if wordTemp[i] == 1 and wordTemp[i+1] == 1 and wordTemp[i+2] == 0 and wordTemp[i+3] == 1:
            HexNum.append('D')
        if wordTemp[i] == 1 and wordTemp[i+1] == 1 and wordTemp[i+2] == 1 and wordTemp[i+3] == 0:
            HexNum.append('E')
        if wordTemp[i] == 1 and wordTemp[i+1] == 1 and wordTemp[i+2] == 1 and wordTemp[i+3] == 1:
            HexNum.append('F')

        i += 4

    i = 4
    while i < 8:
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(0)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(1)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(2)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(3)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(4)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(5)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(6)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(7)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(8)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(9)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('A')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('B')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append('C')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append('D')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('E')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('F')

        i += 4

    i = 8
    while i < 12:
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(0)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(1)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(2)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(3)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(4)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(5)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(6)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(7)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(8)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(9)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('A')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('B')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append('C')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append('D')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('E')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('F')
        i += 4

    i = 12
    while i < 16:
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(0)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(1)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(2)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(3)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(4)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(5)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append(6)
        if wordTemp[i] == 0 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append(7)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append(8)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append(9)
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('A')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 0 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('B')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 0:
            HexNum.append('C')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 0 and wordTemp[i + 3] == 1:
            HexNum.append('D')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 0:
            HexNum.append('E')
        if wordTemp[i] == 1 and wordTemp[i + 1] == 1 and wordTemp[i + 2] == 1 and wordTemp[i + 3] == 1:
            HexNum.append('F')
        i += 4
    return HexNum

def Hextodec(word):
    array = []
    temp = []
    i = 0
    temp.extend(word)
    while i < 4:
        if temp[i] == 0:
            array.extend([0,0,0,0])
        if temp[i] == 1:
            array.extend([0,0,0,1])
        if temp[i] == 2:
            array.extend([0,0,1,0])
        if temp[i] == 3:
            array.extend([0,0,1,1])
        if temp[i] == 4:
            array.extend([0,1,0,0])
        if temp[i] == 5:
            array.extend([0,1,0,1])
        if temp[i] == 6:
            array.extend([0,1,1,0])
        if temp[i] == 7:
            array.extend([0,1,1,1])
        if temp[i] == 8:
            array.extend([1,0,0,0])
        if temp[i] == 9:
            array.extend([1,0,0,1])
        if temp[i] == 'A':
            array.extend([1,0,1,0])
        if temp[i] == 'B':
            array.extend([1,0,1,1])
        if temp[i] == 'C':
            array.extend([1,1,0,0])
        if temp[i] == 'D':
            array.extend([1,1,0,1])
        if temp[i] == 'E':
            array.extend([1,1,1,0])
        if temp[i] == 'F':
            array.extend([1,1,1,1])
        i += 1
    return array

def Multiply(Mat):
    Me = [
        [1, 4],
        [4, 1]
    ]
    Multiplication = [
        [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'],
        [2,4,6,8,'A','C','E',3,1,7,5,'B',9,'F','D'],
        [3,6,5,'C','F','A',9,'B',8,'D','E',7,4,1,2],
        [4,8,'C',3,7,'B','F',6,2,'E','A',5,1,'D',9],
        [5,'A','F',7,2,'D',8,'E','B',4,1,9,'C',3,6],
        [6,'C','A', 'B', 'D',7,1,5,3,9,'F','E',2,4],
        [7,'E',9,'F',8,1,6,'D','A',3,4,2,5,'C','B'],
        [8,3,'B',6,'E',5,'D','C',4,'F',7,'A',2,9,1],
        [9,1,8,2,'B',3,'A',4,'D',5,'C',6,'F',7,'C'],
        ['A',7,'D','E',4,9,3,'F',5,8,2,1,'B',6,'C'],
        ['B',5,'E','A',1,'F',4,7,'C',2,9,'D',6,8,3],
        ['C','B',7,5,9,'E',2,'A',6,1,'D','F',3,4,8],
        ['D',9,4,1,'C',8,5,2,'F','B',6,3,'E','A',7],
        ['E','F',1,'D',3,2,'C',9,7,6,8,4,'A','B',5],
        ['F','D',2,9,6,4,'B',1,'E','C',3,8,7,5,'A']
    ]
    i = 0
    rows = 2
    columns = 2
    temp = numpy.full((columns,rows), 0).tolist()
    wordMat = [
        [Mat[0],Mat[2]],
        [Mat[1],Mat[3]]
    ]
    AddedWord = []
    if wordMat[0][0] == 1:
        temp[0][0] = 1
    if wordMat[0][1] == 1:
        temp[0][1] = 1
    if wordMat[1][0] == 1:
        temp[1][0] = 1
    if wordMat[1][1] == 1:
        temp[1][1] = 1
    if wordMat[0][0] == 2:
        temp[0][0] = 2
    if wordMat[0][1] == 2:
        temp[0][1] = 2
    if wordMat[1][0] == 2:
        temp[1][0] = 2
    if wordMat[1][1] == 2:
        temp[1][1] = 2
    if wordMat[0][0] == 3:
        temp[0][0] = 3
    if wordMat[0][1] == 3:
        temp[0][1] = 3
    if wordMat[1][0] == 3:
        temp[1][0] = 3
    if wordMat[1][1] == 3:
        temp[1][1] = 3
    if wordMat[0][0] == 4:
        temp[0][0] = 4
    if wordMat[0][1] == 4:
        temp[0][1] = 4
    if wordMat[1][0] == 4:
        temp[1][0] = 4
    if wordMat[1][1] == 4:
        temp[1][1] = 4
    if wordMat[0][0] == 5:
        temp[0][0] = 5
    if wordMat[0][1] == 5:
        temp[0][1] = 5
    if wordMat[1][0] == 5:
        temp[1][0] = 5
    if wordMat[1][1] == 5:
        temp[1][1] = 5
    if wordMat[0][0] == 6:
        temp[0][0] = 6
    if wordMat[0][1] == 6:
        temp[0][1] = 6
    if wordMat[1][0] == 6:
        temp[1][0] = 6
    if wordMat[1][1] == 6:
        temp[1][1] = 6
    if wordMat[0][0] == 7:
        temp[0][0] = 7
    if wordMat[0][1] == 7:
        temp[0][1] = 7
    if wordMat[1][0] == 7:
        temp[1][0] = 7
    if wordMat[1][1] == 7:
        temp[1][1] = 7
    if wordMat[0][0] == 8:
        temp[0][0] = 8
    if wordMat[0][1] == 8:
        temp[0][1] = 8
    if wordMat[1][0] == 8:
        temp[1][0] = 8
    if wordMat[1][1] == 8:
        temp[1][1] = 8
    if wordMat[0][0] == 9:
        temp[0][0] = 9
    if wordMat[0][1] == 9:
        temp[0][1] = 9
    if wordMat[1][0] == 9:
        temp[1][0] = 9
    if wordMat[1][1] == 9:
        temp[1][1] = 9
    if wordMat[0][0] == 'A':
        temp[0][0] = 10
    if wordMat[0][1] == 'A':
        temp[0][1] = 10
    if wordMat[1][0] == 'A':
        temp[1][0] = 10
    if wordMat[1][1] == 'A':
        temp[1][1] = 10
    if wordMat[0][0] == 'B':
        temp[0][0] = 11
    if wordMat[0][1] == 'B':
        temp[0][1] = 11
    if wordMat[1][0] == 'B':
        temp[1][0] = 11
    if wordMat[1][1] == 'B':
        temp[1][1] = 11
    if wordMat[0][0] == 'C':
        temp[0][0] = 12
    if wordMat[0][1] == 'C':
        temp[0][1] = 12
    if wordMat[1][0] == 'C':
        temp[1][0] = 12
    if wordMat[1][1] == 'C':
        temp[1][1] = 12
    if wordMat[0][0] == 'D':
        temp[0][0] = 13
    if wordMat[0][1] == 'D':
        temp[0][1] = 13
    if wordMat[1][0] == 'D':
        temp[1][0] = 13
    if wordMat[1][1] == 'D':
        temp[1][1] = 13
    if wordMat[0][0] == 'E':
        temp[0][0] = 14
    if wordMat[0][1] == 'E':
        temp[0][1] = 14
    if wordMat[1][0] == 'E':
        temp[1][0] = 14
    if wordMat[1][1] == 'E':
        temp[1][1] = 14
    if wordMat[0][0] == 'F':
        temp[0][0] = 15
    if wordMat[0][1] == 'F':
        temp[0][1] = 15
    if wordMat[1][0] == 'F':
        temp[1][0] = 15
    if wordMat[1][1] == 'F':
        temp[1][1] = 15

    val3 = Multiplication[Me[0][0] - 1][temp[0][0] - 1]
    val4 = Multiplication[Me[0][1] - 1][temp[1][0] - 1]
    AddedWord.append(Add(val3, val4))

    val5 = Multiplication[Me[1][0] - 1][temp[0][0] - 1]
    val6 = Multiplication[Me[1][1] - 1][temp[1][0] - 1]
    AddedWord.append(Add(val5, val6))

    val7 = Multiplication[Me[0][0] - 1][temp[0][1] - 1]
    val8 = Multiplication[Me[0][1] - 1][temp[1][1] - 1]
    AddedWord.append(Add(val7, val8))

    val9 = Multiplication[Me[1][0] - 1][temp[0][1] - 1]
    val0 = Multiplication[Me[1][1] - 1][temp[1][1] - 1]
    AddedWord.append(Add(val9, val0))

    print("Mix Columns in Hex: ", AddedWord)
    mixcolumn = []
    mixcolumn.extend(Hextodec(AddedWord))
    return mixcolumn

def Add(val, val2):
    tempval = 0
    tempval2 = 0
    Addition = [
        [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'],
        [1,0,3,2,5,4,7,6,9,8,'B','A','D','C','F','E'],
        [2,3,0,1,6,7,4,5,'A','B',8,9,'E','F','C','D'],
        [3,2,1,0,7,6,5,4,'B','A',9,8,'F','E','D','C'],
        [4,5,6,7,0,1,2,3,'C','D','E','F',8,9,'A','B'],
        [5,4,7,6,1,0,3,2,'D','C','F','E',9,8,'B','A'],
        [6,7,4,5,2,3,0,1,'E','F','C','D','A','B',8,9],
        [7,6,5,4,3,2,1,0,'F','E','D','C','B','A',9,8],
        [8,9,'A','B','C','D','E','F',0,1,2,3,4,5,6,7],
        [9,8,'B','A','D','C','F','E',1,0,3,2,5,4,7,6],
        ['A','B',8,9,'E','F','C','D',2,3,0,1,6,7,4,5],
        ['B','A',9,8,'F','E','D','C',3,2,1,0,7,6,5,4],
        ['C','D','E','F',8,9,'A','B',4,5,6,7,0,1,2,3],
        ['D','C','F','E',9,8,'B','A',5,4,7,6,1,0,3,2],
        ['E','F','C','D','A','B',8,9,6,7,4,5,2,3,0,1],
        ['F','E','D','C','B','A',9,8,7,6,5,4,3,2,1,0]
    ]

    if val == 1:
        tempval = 1
    if val == 2:
        tempval = 2
    if val == 3:
        tempval = 3
    if val == 4:
        tempval = 4
    if val == 5:
        tempval = 5
    if val == 6:
        tempval = 6
    if val == 7:
        tempval = 7
    if val == 8:
        tempval = 8
    if val == 9:
        tempval = 9
    if val == 'A':
        tempval = 10
    if val == 'B':
        tempval = 11
    if val == 'C':
        tempval = 12
    if val == 'D':
        tempval = 13
    if val == 'E':
        tempval = 14
    if val == 'F':
        tempval = 15
    if val2 == 1:
        tempval2 = 1
    if val2 == 2:
        tempval2 = 2
    if val2 == 3:
        tempval2 = 3
    if val2 == 4:
        tempval2 = 4
    if val2 == 5:
        tempval2 = 5
    if val2 == 6:
        tempval2 = 6
    if val2 == 7:
        tempval2 = 7
    if val2 == 8:
        tempval2 = 8
    if val2 == 9:
        tempval2 = 9
    if val2 == 'A':
        tempval2 = 10
    if val2 == 'B':
        tempval2 = 11
    if val2 == 'C':
        tempval2 = 12
    if val2 == 'D':
        tempval2 = 13
    if val2 == 'E':
        tempval2 = 14
    if val2 == 'F':
        tempval2 = 15

    result = Addition[tempval][tempval2]

    return result

print("1.1: Key Generation \n")
w2.extend(XOR(w0, w1, 1))
print("Word 2 = ", w2, '\n')

w3.extend(XOR(w2, w1, 0))
print("Word 3 = ", w3, '\n')

w4.extend(XOR(w2, w3, 2))
print("Word 4 = ", w4, '\n')

w5.extend(XOR(w4, w3, 0))
print("Word 5 = ", w5, '\n')

Key0 = KeyGen(w0, w1)
print("Key 0: ", Key0, '\n')

Key1 = KeyGen(w2, w3)
print("Key 1: ", Key1, '\n')

Key2 = KeyGen(w4, w5)
print("Key 2: ", Key2, '\n')

RoundKey.extend(XOR(plain, Key0, 3))
print("RoundKey: ", RoundKey, '\n')

# Round 1

print("1.2.1: Round 1")

sbnibRoundKey.extend(SubNib(RoundKey, 1))
print("Round Key After SubNib", sbnibRoundKey)

ShiftRoundKey = Shift(sbnibRoundKey)
print("Shifted Round Key: ", ShiftRoundKey)

hex = decToHex(ShiftRoundKey)

mixcolumns.extend(Multiply(hex))
print("Mix Columns: ",mixcolumns)


Round1Key.extend(XOR(mixcolumns,Key1,3))
print("Round 1 Key: ", Round1Key)

# Round 2

print("1.2.2: Round 2")

sbnibRoundKey2.extend(SubNib(Round1Key, 1))
print("Round 1 Key After SubNib", sbnibRoundKey2)

ShiftRoundKey2.extend(Shift(sbnibRoundKey2))
print("Round 1 Key After Shift: ", ShiftRoundKey2)

Round2Key.extend(XOR(ShiftRoundKey2, Key2, 3))
print("Round 2 Key: ", Round2Key)

print("Ciphertext: ", Round2Key)