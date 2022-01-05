import pyperclip
import tkinter
text=pyperclip.paste()
def func(textbox,root):
    def inner(e):
        addtext=textbox.get()
        if addtext != "" and e.keysym=="Return":
            returntext=addtext+text.replace("\n","\n"+addtext)
            pyperclip.copy(returntext)
            root.destroy()
    return inner
if text !="":
    root=tkinter.Tk()
    root.geometry("220x30+600+600")
    label=tkinter.Label(root,text="追加する文字")
    textbox=tkinter.Entry(root)
    textbox.bind("<KeyPress>", func(textbox=textbox,root=root))
    label.grid(row=0,column=0)
    textbox.grid(row=0,column=1)
    root.mainloop()



