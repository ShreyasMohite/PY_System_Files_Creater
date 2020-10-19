from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import touch
import tkinter.filedialog



class File:
    def __init__(self,root):
        self.root=root
        self.root.title("System File Extention")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo669.ico")
        self.root.resizable(0,0)

        path=StringVar()
        filename=StringVar()
        filextention=StringVar()
#======================================================================================#

        def clear():
            filename.set("")
            path.set("")
            lab_filecreated.config(text="")
            lab_selectpath.config(text="Select Path")
            filextention.set("Select System File Extention")

        def browse():
            #golbal files
            a=tkinter.filedialog.askdirectory(title="choose folder")
            path.set(a)
            if a:
                lab_selectpath.config(text="Path Is Selected")
            #files=a

        def genrate():
            try:
                if path.get()!="":
                    a=path.get()
                    lab_filecreated.config(text="File Created Successfully")

                    
                    if filextention.get()!="Select System File Extention":
                        if filename.get()!="":

                            if filextention.get()=="Backup file" and filename.get()!="":
                                touch.touch(a+"/{}.bak".format(filename.get()))
                            
                            if filextention.get()=="Windows Cabinet file" and filename.get()!="":
                                touch.touch(a+"/{}.cab".format(filename.get()))
                        

                            if filextention.get()=="Configuration file" and filename.get()!="":
                                touch.touch(a+"/{}.cfg".format(filename.get()))
                            

                            if filextention.get()=="Windows Control panel file" and filename.get()!="":
                                touch.touch(a+"/{}.cpl".format(filename.get()))

                            if filextention.get()=="Windows cursor file" and filename.get()!="":
                                touch.touch(a+"/{}.cur".format(filename.get()))

                            if filextention.get()=="DLL file" and filename.get()!="":
                                touch.touch(a+"/{}.dll".format(filename.get()))
                            
                            if filextention.get()=="Dump file" and filename.get()!="":
                                touch.touch(a+"/{}.dmp".format(filename.get()))

                            if filextention.get()=="Device driver file" and filename.get()!="":
                                touch.touch(a+"/{}.drv".format(filename.get()))

                            if filextention.get()=="macOS X icon resource file" and filename.get()!="":
                                touch.touch(a+"/{}.icns".format(filename.get()))

                            if filextention.get()=="Icon file" and filename.get()!="":
                                touch.touch(a+"/{}.ico".format(filename.get()))

                            if filextention.get()=="Initialization file" and filename.get()!="":
                                touch.touch(a+"/{}.ini".format(filename.get()))
                            
                            if filextention.get()=="Windows shortcut file" and filename.get()!="":
                                touch.touch(a+"/{}.lnk".format(filename.get()))

                            if filextention.get()=="Windows shortcut file" and filename.get()!="":
                                touch.touch(a+"/{}.lnk".format(filename.get()))
                            
                            if filextention.get()=="Windows installer package" and filename.get()!="":
                                touch.touch(a+"/{}.msi".format(filename.get()))

                            if filextention.get()=="Windows system file" and filename.get()!="":
                                touch.touch(a+"/{}.sys".format(filename.get()))

                            if filextention.get()=="Temporary file" and filename.get()!="":
                                touch.touch(a+"/{}.tmp".format(filename.get()))
                            
                        else:
                            tkinter.messagebox.showerror("Error","Please write a proper filename")

                    else:
                        tkinter.messagebox.showerror("Error","Please choose an extension ")
                else:
                    tkinter.messagebox.showerror("Error","Please choose path first")
            except Exception as e:
                print(e)

#======================================================================================#
        def on_enter1(e):
            but_browsepath['background']="black"
            but_browsepath['foreground']="cyan"
  
        def on_leave1(e):
            but_browsepath['background']="SystemButtonFace"
            but_browsepath['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_generate['background']="black"
            but_generate['foreground']="cyan"
  
        def on_leave3(e):
            but_generate['background']="SystemButtonFace"
            but_generate['foreground']="SystemButtonText"

#======================================================================================#
        mainframe=Frame(self.root,width=500,height=400,bd=4,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,bd=4,relief="ridge",bg="#70d6ff")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=90,relief="ridge",bd=3,bg="#272640")
        secondframe.place(x=0,y=300)

#======================================================================================#
        but_browsepath=Button(firstframe,text="Browse Path",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=browse)
        but_browsepath.place(x=160,y=15)
        but_browsepath.bind("<Enter>",on_enter1)
        but_browsepath.bind("<Leave>",on_leave1)

        lab_selectpath=Label(firstframe,text="Select Path",font=('times new roman',12),bg="#70d6ff")
        lab_selectpath.place(x=200,y=90)

        ent_path=Entry(firstframe,width=55,font=('times new roman',12),relief="ridge",bd=4,textvariable=path)
        ent_path.place(x=15,y=120)

        lab_filecreated=Label(firstframe,text="",font=('times new roman',12),bg="#70d6ff",fg="red")
        lab_filecreated.place(x=170,y=150)

        lab_selectfilename=Label(firstframe,text="Select FileName",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=200)

        ent_filename=Entry(firstframe,width=30,font=('times new roman',12),relief="ridge",bd=4,textvariable=filename)
        ent_filename.place(x=200,y=200)


        lab_selectfilename=Label(firstframe,text="Select File Extention",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=250)

        fileselect=["Backup file","Windows Cabinet file","Configuration file",\
                    "Windows Control panel file","Windows cursor file","DLL file",\
                    "Dump file","Device driver file","macOS X icon resource file","Icon file",\
                    "Initialization file","Windows shortcut file","Windows installer package","Windows system file","Temporary file"]
        fileselect_combo=Combobox(firstframe,values=fileselect,font=('arial',12),width=25,state="readonly",textvariable=filextention)
        fileselect_combo.set("Select System File Extention")
        fileselect_combo.place(x=200,y=250)
            

#======================================================================================#


        but_clear=Button(secondframe,text="Clear",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=clear)
        but_clear.place(x=30,y=15)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        but_generate=Button(secondframe,text="Generate File",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=genrate)
        but_generate.place(x=290,y=15)
        but_generate.bind("<Enter>",on_enter3)
        but_generate.bind("<Leave>",on_leave3)



if __name__ == "__main__":
    root=Tk()
    app=File(root)
    root.mainloop()
