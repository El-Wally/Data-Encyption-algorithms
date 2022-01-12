
import tkinter as tk
from tkinter import ttk
from rsa import rsa
from playfair import playfair

def rsas(p,q,e,message):



    p=int(p)
    q=int(q)
    e=int(e)
    #####
    # rsa

    print(p,q,e)
    #p = 17
    #q = 11
    #e = 7
    #message = 'XX' #88 ascii
    #message_binary = 88

    ob = rsa(p, q, e)

    publicKey = ob.getPublicKey()

    cipherText = ob.encrypt(publicKey, message)
    return cipherText


def rsasdec(p,q,e,message):

    #message_binary = 88
    p=int(p)
    q=int(q)
    e=int(e)

    ob = rsa(p, q, e)

    privateKey = ob.getPrivateKey()

    cipherText=[message]
    plainText = ""
    for cipherChunck in cipherText:
        plainText = plainText + ob.decrypt(privateKey, str(cipherChunck))
    print(plainText)
    return plainText


def callbackFunc(event):
        if comboExample.get()=="SAES":
            from SAESform import formcreate2
            formcreate2()
        if comboExample.get()=="SDES":
            from sdesform import formcreate
            formcreate()
        if comboExample.get()=="RC4":
            from RC4Form import formcreate4
            formcreate4()
        if comboExample.get()=="PLAYFAIR":
            from playfairform import formcreate1
            formcreate1()


def formcreate3():
    root=tk.Tk()
    root.title('')
    root.title('RSA ALGORITHM')
    root.geometry("600x400")
    P_var=tk.StringVar()
    Q_var=tk.StringVar()
    E_var=tk.StringVar()
    Mess_var=tk.StringVar()
    resultvar=tk.StringVar()
    P_lbl = tk.Label(root, text = 'P', font=('calibre',10, 'bold'))
    P_ent = tk.Entry(root,textvariable = P_var, font=('calibre',10,'normal'))
    Q_lbl = tk.Label(root, text = 'Q', font=('calibre',10, 'bold'))
    Q_ent = tk.Entry(root,textvariable = Q_var, font=('calibre',10,'normal'))
    E_lbl = tk.Label(root, text = 'E', font=('calibre',10, 'bold'))
    E_ent = tk.Entry(root,textvariable = E_var, font=('calibre',10,'normal'))
    Mess_lbl = tk.Label(root, text = 'Message', font=('calibre',10, 'bold'))
    Mess_ent = tk.Entry(root,textvariable = Mess_var, font=('calibre',10,'normal'))
    res_lbl = tk.Label(root, text = 'Result', font=('calibre',10, 'bold'))
    res_ent = tk.Entry(root,textvariable = resultvar, font=('calibre',10,'normal'))




    sub_btn=tk.Button(root,text = 'Encrypt', command = lambda:res_ent.insert(0,rsas(P_ent.get(),Q_ent.get(),E_ent.get(),Mess_ent.get())))
    sub_btn1=tk.Button(root,text = 'Decrypt', command = lambda:res_ent.insert(0,rsasdec(P_ent.get(),Q_ent.get(),E_ent.get(),Mess_ent.get())))

        #Key_var.get(),Text_var.get(),P10_var.get(),P8_var.get(),IP_var.get())


    global comboExample
    comboExample = ttk.Combobox(root,
                                    values=["RSA",
                                            "SDES",
                                            "SAES",
                                            "PLAYFAIR","RC4"],
                                    state="readonly")


    comboExample.current(0)
    comboExample.bind("<<ComboboxSelected>>", callbackFunc)





    # placing the label and entry in
    # the required position using grid
    # method
    P_lbl.grid(row=0,column=2)
    P_ent.grid(row=0,column=3)
    Q_lbl.grid(row=1,column=2)
    Q_ent.grid(row=1,column=3)
    E_lbl.grid(row=2,column=2)
    E_ent.grid(row=2,column=3)
    Mess_lbl.grid(row=3,column=2)
    Mess_ent.grid(row=3,column=3)
    sub_btn.grid(row=4,column=2)
    sub_btn1.grid(row=4,column=3)
    comboExample.grid(column=5, row=4)
    res_lbl.grid(row=11,column=2)
    res_ent.grid(row=11,column=3)
    # performing an infinite loop
    # for the window to display
    root.mainloop()
