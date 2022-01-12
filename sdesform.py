
from sdes import SDESencrypt
from sdes import SDESdecrypt
import tkinter as tk
from tkinter import ttk





def callbackFunc(event):
        if comboExample.get()=="SAES":
            from SAESform import formcreate2
            formcreate2()
        if comboExample.get()=="RSA":
            from RSAForm import formcreate3
            formcreate3()
        if comboExample.get()=="RC4":
            from RC4Form import formcreate4
            formcreate4()
        if comboExample.get()=="PLAYFAIR":
            from playfairform import formcreate1
            formcreate1()


def formcreate():
    root=tk.Tk()
    root.title('Combobox Widget')
    root.geometry("600x400")
    Key_var=tk.StringVar()
    Text_var=tk.StringVar()
    P10_var=tk.StringVar()
    resultvar=tk.StringVar()
    P8_var=tk.StringVar()
    IP_var=tk.StringVar()
    EP_var=tk.StringVar()
    P4_var=tk.StringVar()
    S0_var=tk.StringVar()
    S1_var=tk.StringVar()
    IPinv_var=tk.StringVar()
    P10_lbl = tk.Label(root, text = 'P10', font=('calibre',10, 'bold'))
    P10_ent = tk.Entry(root,textvariable = P10_var, font=('calibre',10,'normal'))

    P8_lbl = tk.Label(root, text = 'P8', font=('calibre',10, 'bold'))
    P8_ent = tk.Entry(root,textvariable = P8_var, font=('calibre',10,'normal'))

    IP_lbl = tk.Label(root, text = 'IP', font=('calibre',10, 'bold'))
    IP_ent = tk.Entry(root,textvariable = IP_var, font=('calibre',10,'normal'))

    EP_lbl = tk.Label(root, text = 'EP', font=('calibre',10, 'bold'))
    EP_ent = tk.Entry(root,textvariable = EP_var, font=('calibre',10,'normal'))

    P4_lbl = tk.Label(root, text = 'P4', font=('calibre',10, 'bold'))
    P4_ent = tk.Entry(root,textvariable = P4_var, font=('calibre',10,'normal'))
    S0_lbl = tk.Label(root, text = 'S0', font=('calibre',10, 'bold'))
    S0_ent = tk.Entry(root,textvariable = S0_var, font=('calibre',10,'normal'))
    S1_lbl = tk.Label(root, text = 'S1', font=('calibre',10, 'bold'))
    S1_ent = tk.Entry(root,textvariable = S1_var, font=('calibre',10,'normal'))
    IPinv_lbl = tk.Label(root, text = 'IPinv', font=('calibre',10, 'bold'))
    IPinv_ent = tk.Entry(root,textvariable = IPinv_var, font=('calibre',10,'normal'))
    Key_lbl = tk.Label(root, text = 'Key', font=('calibre',10, 'bold'))
    Key_ent = tk.Entry(root,textvariable = Key_var, font=('calibre',10,'normal'))
    res_lbl = tk.Label(root, text = 'Result', font=('calibre',10, 'bold'))
    res_ent = tk.Entry(root,textvariable = resultvar, font=('calibre',10,'normal'))
    Txt_lbl = tk.Label(root, text = 'Text', font=('calibre',10, 'bold'))
    Txt_ent = tk.Entry(root,textvariable = Text_var, font=('calibre',10,'normal'))
    #sub_btn=tk.Button(root,text = 'Encrypt', command = lambda: SDESencrypt(Key_var.get(),Text_var.get(),P10_var.get(),P8_var.get(),P4_var.get(),EP_var.get(),IP_var.get(),S0_var.get(),S1_var.get()))
    sub_btn=tk.Button(root,text = 'Encrypt', command = lambda: res_ent.insert(0,SDESencrypt(Key_ent.get(),Txt_ent.get(),P10_ent.get(),P8_ent.get(),P4_ent.get(),EP_ent.get(),IP_ent.get(),S0_ent.get(),S1_ent.get(),IPinv_ent.get())))
    sub_btn1=tk.Button(root,text = 'Decrypt', command = lambda: res_ent.insert(0,SDESdecrypt(Key_ent.get(),Txt_ent.get(),P10_ent.get(),P8_ent.get(),P4_ent.get(),EP_ent.get(),IP_ent.get(),S0_ent.get(),S1_ent.get(),IPinv_ent.get())))
    global comboExample
    comboExample = ttk.Combobox(root,
                                    values=["SDES",
                                            "RSA",
                                            "SAES",
                                            "PLAYFAIR",
                                            "RC4"],
                                    state="readonly")


    comboExample.current(0)
    comboExample.bind("<<ComboboxSelected>>", callbackFunc)


    P10_lbl.grid(row=2,column=2)
    P10_ent.grid(row=2,column=3)
    P8_lbl.grid(row=3,column=2)
    P8_ent.grid(row=3,column=3)
    IP_lbl.grid(row=4,column=2)
    IP_ent.grid(row=4,column=3)
    EP_lbl.grid(row=5,column=2)
    EP_ent.grid(row=5,column=3)
    P4_lbl.grid(row=6,column=2)
    P4_ent.grid(row=6,column=3)
    S0_lbl.grid(row=7,column=2)
    S0_ent.grid(row=7,column=3)
    S1_lbl.grid(row=8,column=2)
    S1_ent.grid(row=8,column=3)
    IPinv_lbl.grid(row=10,column=2)
    IPinv_ent.grid(row=10,column=3)
    Key_lbl.grid(row=0,column=2)
    Key_ent.grid(row=0,column=3)
    Txt_lbl.grid(row=1,column=2)
    Txt_ent.grid(row=1,column=3)
    sub_btn.grid(row=11,column=2)
    sub_btn1.grid(row=11,column=3)
    res_lbl.grid(row=12,column=2)
    res_ent.grid(row=12,column=3)
    comboExample.grid(row=11, column=4)










    # placing the label and entry in
    # the required position using grid
    # method


    # performing an infinite loop
    # for the window to display
    root.mainloop()
formcreate()
