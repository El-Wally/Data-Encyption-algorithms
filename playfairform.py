
from playfair import playfair




import tkinter as tk
from tkinter import ttk
def enc(plainText,key):

#    plainText = "Modasa"
    #cipherText = "GTBFQY"
#    key = "playfair"

    ob = playfair(key)
    return ob.encode(plainText)


def dec(cipherText,key):

#    plainText = "Modasa"
    #cipherText = "GTBFQY"
#    key = "playfair"

    ob = playfair(key)


    return ob.decode(cipherText)




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
    if comboExample.get()=="RSA":
        from RSAForm import formcreate3
        formcreate3()


def formcreate1():
    root=tk.Tk()
    root.title('')
    root.geometry("600x400")
    Key_var=tk.StringVar()
    Text_var=tk.StringVar()
    resultvar1=tk.StringVar()
    Key_lbl = tk.Label(root, text = 'Key', font=('calibre',10, 'bold'))
    Key_ent = tk.Entry(root,textvariable = Key_var, font=('calibre',10,'normal'))
    Txt_lbl = tk.Label(root, text = 'Text', font=('calibre',10, 'bold'))
    Txt_ent = tk.Entry(root,textvariable = Text_var, font=('calibre',10,'normal'))
    res_lbl = tk.Label(root, text = 'Result', font=('calibre',10, 'bold'))
    res_ent = tk.Entry(root,textvariable = resultvar1, font=('calibre',10,'normal'))


    sub_btn=tk.Button(root,text = 'Encrypt', command = lambda:res_ent.insert(0,enc(Txt_ent.get(),Key_ent.get())))
    sub_btn1=tk.Button(root,text = 'Decrypt', command = lambda:res_ent.insert(0,dec(Txt_ent.get(),Key_ent.get())))
        #Key_var.get(),Text_var.get(),P10_var.get(),P8_var.get(),IP_var.get())

    global comboExample
    comboExample = ttk.Combobox(root,
                                    values=["PLAYFAIR",
                                            "SDES",
                                            "SAES",
                                            "RC4",
                                            "RSA"],
                                    state="readonly")


    comboExample.current(0)
    comboExample.bind("<<ComboboxSelected>>", callbackFunc)





    # placing the label and entry in
    # the required position using grid
    # method
    Key_lbl.grid(row=0,column=2)
    Key_ent.grid(row=0,column=3)
    Txt_lbl.grid(row=1,column=2)
    Txt_ent.grid(row=1,column=3)
    sub_btn.grid(row=2,column=2)
    sub_btn1.grid(row=2,column=3)
    res_lbl.grid(row=4,column=2)
    res_ent.grid(row=11,column=3)
    comboExample.grid(column=4, row=2)
    # performing an infinite loop
    # for the window to display
    root.mainloop()
