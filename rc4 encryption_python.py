## Function to swap positions in a given list
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# number of elements in Key
n = 4 
  

# Below line read inputs from user using map() function  
a1 = list(map(int, input("\nEnter the numbers in 'Key': ").strip().split()))[:n] 


#Checks if values in 'KEY' are great than 7 
for i in a1:
    if i > 7:
        a1 = list(map(int, input("\nPlease Re-input 'Key', Numbers Can't be Greather Than 7: ").strip().split()))[:n]


print("\nKey is - ", a1)

#------------------------------------------------------------------------------------------#

# number of elements in Plain Text
n = 4 
  

# Below line read inputs from user using map() function  
a2 = list(map(int, input("\nEnter the numbers in 'Plain Text': ").strip().split()))[:n] 


#Checks if values in 'KEY' are great than 7 
for i in a2:
    if i > 7:
        a2 = list(map(int, input("\nPlease Re-input 'Plain Text', Numbers Can't be Greather Than 7: ").strip().split()))[:n]


print("\nPlain Text is - ", a2, "\n\n")

#------------------------------------------------------------------------------------------#

v = a1

## Makes a list for S and a list that repeats the key T
s = [0, 1, 2, 3, 4, 5, 6 ,7]
t = v + v 

print ("\nS[i] Array - ", s)
print ("\nT (Repeated Key) Array -", t, "\n\n")



## Loop to make Intial Permutation on S 
j = 0
for i in range(7):
    j = (j + s[i] + t[i]) % 8 
    swapPositions (s, s[i], s[j]) 

print ("\nInitial Permutation - ", s)


## Encryption 

j = 0
i = 0

c = []

for i in range(4):
    i = (i + 1) % 8

    j = (j + s[i]) % 8
    swapPositions (s, s[i], s[j])

    t = (s[i] + s[j]) % 8
    k = s[t]

    output = k ^ a2[i-1] 
    c.append(output)

print("\nCipher Text - ", c)


