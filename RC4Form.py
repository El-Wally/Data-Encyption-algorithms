import tkinter as tk
from tkinter import ttk
#from rc4_encryption import rc4 

def enc(plainText,key):

    #plainText = int(plainText)
    #key = int(key)

    key.split()
    plainText.split()

    alpha1 = list(map(int,key))
    alpha2 = list(map(int,plainText))

    print("key is - ", alpha1)
    print("plainText is - ", alpha2)

    #alpha1.split()
    #alpha2.split()

  ## Function to swap positions in a given list
    def swapPositions(list, pos1, pos2):

        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list


    # number of elements in Key
    #n = 4 
  

    ## Below line reads key from user using map() function  
    #a1 = list(map(int, input("\nEnter the numbers in 'Key': ").strip().split()))[:n] 


    #Checks if values in 'KEY' are great than 7 
    #for i in key:
    #    if i > 7:
            #a1 = list(map(int, input("\nPlease Re-input 'Key', Numbers Can't be Greather Than 7: ").strip().split()))[:n]

    #print("\nKey is - ", a1)

    #------------------------------------------------------------------------------------------#

    # number of elements in Plain Text
    #n = 4 
  

    ## Below line read plaintext from user using map() function  
    #a2 = list(map(int, input("\nEnter the numbers in 'Plain Text': ").strip().split()))[:n] 


    #Checks if values in 'Plaintext' are great than 7 
    #for i in plainText:
    #    if i > 7:
            #a2 = list(map(int, input("\nPlease Re-input 'Plain Text', Numbers Can't be Greather Than 7: ").strip().split()))[:n]


    #print("\nPlain Text is - ", a2, "\n\n")

    #------------------------------------------------------------------------------------------#

    v = alpha1

    ## Makes a list for S and a list that repeats the key T
    s = [0, 1, 2, 3, 4, 5, 6 ,7]
    t = alpha1 + alpha1

    print ("\nS[i] Array - ", s)
    print ("\nT (Repeated Key) Array -", t, "\n\n")



    ## Loop to make Intial Permutation on S 
    i = 0
    j = 0

    for i in range(7):
        j = (j + s[i] + t[i]) % 8 
        swapPositions (s, s[i], s[j]) 

    print ("\nInitial Permutation - ", s)


    ## Encryption 
    i = 0
    j = 0

    c = []

    for i in range(len(alpha2)):
        i = (i + 1) % 8

        j = (j + s[i]) % 8
        swapPositions (s, s[i], s[j])

        t = (s[i] + s[j]) % 8
        k = s[t]

        output = k ^ alpha2[i-1] 
        c.append(output)

    print("\nCipher Text - ", c)

    return c

def callbackFunc(event):
    if comboExample.get()=="PLAYFAIR":
        from playfairform import formcreate1
        formcreate1()
    if comboExample.get()=="SDES":
        from sdesform import formcreate
        formcreate()
    if comboExample.get()=="SAES":
        from SAESform import formcreate4
        formcreate4()
    if comboExample.get()=="RSA":
        from RSAForm import formcreate2
        formcreate3()


def formcreate4():
    root=tk.Tk()
    root.title('Combobox Widget')
    root.geometry("600x400")
    Key_var=tk.StringVar()
    Text_var=tk.StringVar()

    resultvar=tk.StringVar()
    res_lbl = tk.Label(root, text = 'Result', font=('calibre',10, 'bold'))
    res_ent = tk.Entry(root,textvariable = resultvar, font=('calibre',10,'normal'))
    res_lbl.grid(row=12,column=2)
    res_ent.grid(row=12,column=3)

    Key_lbl = tk.Label(root, text = 'Text', font=('calibre',10, 'bold'))
    Key_ent = tk.Entry(root,textvariable = Key_var, font=('calibre',10,'normal'))
    sub_btn=tk.Button(root,text = 'Encrypt', command = lambda: res_ent.insert(0,enc(Key_ent.get(),Txt_ent.get())))

    #sub_btn=tk.Button(root,text = 'Encrypt', command = lambda: enc(Key_ent.get(),Txt_ent.get()))

    global comboExample
    comboExample = ttk.Combobox(root,
                                    values=["RC4",
                                            "SDES",
                                            "RSA",
                                            "PLAYFAIR",
                                            "SAES"],
                                    state="readonly")


    comboExample.current(0)
    comboExample.bind("<<ComboboxSelected>>", callbackFunc)
    Txt_lbl = tk.Label(root, text = 'Key', font=('calibre',10, 'bold'))
    Txt_ent = tk.Entry(root,textvariable = Text_var, font=('calibre',10,'normal'))
    Key_lbl.grid(row=0,column=2)
    Key_ent.grid(row=0,column=3)
    Txt_lbl.grid(row=1,column=2)
    Txt_ent.grid(row=1,column=3)
    sub_btn.grid(row=9,column=2)
    comboExample.grid(row=9, column=4)










    # placing the label and entry in
    # the required position using grid
    # method


    # performing an infinite loop
    # for the window to display
    root.mainloop()
