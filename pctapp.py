from tkinter import *
from base64 import*
from tkinter import messagebox
class encdec:
    def __init__(self,hello):
        self.hello=hello
        hello.title('pct app')
        hello.geometry('335x398')
        hello.resizable(False,False)
        # photo=PhotoImage(file='C:\\Users\\pavan\\Desktop\\keys.png')
        # hello.iconphoto(False,photo)
        self.data=StringVar()
        Label(hello,text='Enter text for Encryption and Decryption',font=('calbri',13)).place(x=10,y=10)
        self.text1=Text(font=('robote',20),relief=GROOVE,wrap=WORD,bd=5)
        self.text1.place(x=10,y=50,width=315,height=100)
        Label(hello,text='Enter secret key for Encryption and Decryption',font=('calbri',11)).place(x=10,y=160)
        Entry(textvariable=self.data,show='*',font=('Arial Bold',12),bd=5).place(x=10,y=200,width=315)
        Button(hello,text='Encrypt',bg='red',bd=5,activeforeground='red',fg='white',relief=RAISED,command=self.encoded).place(x=10,y=240,width=150)
        Button(hello,text='Decrypt',bg='green',bd=5,activeforeground='green',fg='white',relief=RAISED,command=self.decoded).place(x=175,y=240,width=150)
        Button(hello,text='reset',bg='blue',bd=5,activeforeground='blue',fg='white',relief=RAISED,command=self.reset).place(x=10,y=300,width=315)
    def encoded(self):
        password=self.data.get()
        
        if password=="1234":
            screen1=Toplevel(self.hello)
            screen1.title('encryption')
            screen1.geometry('400x200')
            screen1.configure(bg='#ed3833')
            message=self.text1.get(1.0,END)
            encode_message=message.encode('ascii')
            base64_bytes=b64encode(encode_message)
            encrypt=base64_bytes.decode('ascii')
            Label(screen1,text='ENCRYPT',font='arial',fg='white',bg='#ed3833').place(x=10,y=0)
            text2=Text(screen1,font=('rpbote',10),bg='white',relief=GROOVE,wrap=WORD)
            text2.place(x=10,y=40,width=380,height=150)
            text2.insert(END,encrypt)
        elif password == '':
            messagebox.showerror('encryption','Input Password')
        elif password !='1234':
            messagebox.showerror('encryption','Invalid Password')
    def decoded(self):
        password=self.data.get()
        if password=="1234":
            screen2=Toplevel(self.hello)
            screen2.title('decryption')
            screen2.geometry('400x200')
            screen2.configure(bg='#00bd56')
            message=self.text1.get(1.0,END)
            decode_message=message.encode('ascii')
            base64_bytes=b64decode(decode_message)
            decrypt=base64_bytes.decode('ascii')
            Label(screen2,text='DECRYPT',font='arial',fg='white',bg='#00bd56').place(x=10,y=0)
            text2=Text(screen2,font=('rpbote',10),bg='white',relief=GROOVE,wrap=WORD)
            text2.place(x=10,y=40,width=380,height=150)
            text2.insert(END,decrypt)
        elif password == '':
            messagebox.showerror('decryption','Input Password')
        elif password !='1234':
            messagebox.showerror('decryption','Invalid Password')
    def reset(self):
        self.data.set('')
        self.text1.delete(1.0,END)
root=Tk()
encrypty=encdec(root)
root.mainloop()