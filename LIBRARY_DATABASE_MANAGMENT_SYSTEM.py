from tkinter import *
import tkinter.messagebox
import LoginOrRegister
import LibBksDatabase
import BooksinLIBRARY
import webbrowser

class Library:    
    def __init__(self,root):
        self.root = root
        self.root.title("Library Database Managment System")
        self.root.geometry("1350x650+0+0")
        
        MTy = StringVar()   #Member Type
        Ref = StringVar()   #Reference number
        Tit = StringVar()   #Title
        fna = StringVar()   #FirstName
        sna = StringVar()   #Surname
        Adr1 = StringVar()  #Address1
        Adr2 = StringVar()  #Address2
        pcd = StringVar()   #Post code
        MNo = StringVar()   #Mobile Number
        BkID = StringVar()  #Book ID
        Bkt = StringVar()   #Book Title
        Atr = StringVar()   #Author
        DBo = StringVar()   #Date borrowed
        Ddu = StringVar()   #Date due
        sPr = StringVar()   #Selling Price
        LrF = StringVar()   #Late return fine
        DoD = StringVar()   #Date over due
        DonL = StringVar()  #Selling price
        
        urltxt = StringVar()
        
        
        ######################FUNCTION########################
        
        
        
        def search_verify():
            answer=BooksinLIBRARY.searchmyBook(book_nameEntry.get())
            urltxt.set(answer)
            if(len(answer)!=0):
                webbrowser.open_new(str(answer))
        
        def search_books():
            global searchScreen
            searchScreen = Toplevel(root)
            searchScreen.title("SEARCH BOOKS")
            searchScreen.geometry("450x300")
            Label(searchScreen, text = "Please enter books name").pack()
            Label(searchScreen,textvariable=urltxt ,text = "URL: ", fg="blue", cursor="hand2").pack()
            
            
            book_nameSearch = StringVar()
            
            global book_nameEntry
            
            Label(searchScreen, text = "BOOK: ").pack()
            book_nameEntry = Entry(searchScreen, textvariable = book_nameSearch)
            book_nameEntry.pack()
            Label(searchScreen, text = "").pack()
            Button(searchScreen, text = "Search", width = 10, height = 1, command = search_verify).pack()
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Database Managment System","Sure you want to exit?")
            if iExit>0:
                root.destroy()
                return
            
            
        def ClearData():
            self.txtMType.delete(0,END)
            self.txtBkID.delete(0,END)
            self.txtRef.delete(0,END)
            self.txtBkt.delete(0,END)
            self.txtTit.delete(0,END)
            self.txtAtr.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDdu.delete(0,END)
            self.txtAdr1.delete(0,END)
            self.txtAdr2.delete(0,END)
            self.txtDonL.delete(0,END)
            self.txtLrF.delete(0,END)
            self.txtpcd.delete(0,END)
            self.txtDoD.delete(0,END)
            self.txtMNo.delete(0,END)
            self.txtsPr.delete(0,END)
            self.txtDBo.delete(0,END)
            
            
        
        def AddData():
            if(len(MTy.get())!=0):
                LibBksDatabase.addDataRec(MTy.get(), Ref.get(), Tit.get(), fna.get(), sna.get(), Adr1.get(),
                 Adr2.get(), pcd.get(), MNo.get(), BkID.get(), Bkt.get(), Atr.get(), DBo.get(), Ddu.get(),
                 sPr.get(), LrF.get(), DoD.get(), DonL.get())
            
            booklist.delete(0,END)
            booklist.insert(END,(MTy.get(), Ref.get(), Tit.get(), fna.get(), sna.get(), Adr1.get(),Adr2.get(), pcd.get(),\
                                 MNo.get(), BkID.get(), Bkt.get(), Atr.get(), DBo.get(), Ddu.get(),sPr.get(), LrF.get(), DoD.get(), DonL.get()))
        
        def DisplayData():
            booklist.delete(0,END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END,row)
        
        def SelectedBook(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb = booklist.get(searchBk)
            self.txtMType.delete(0,END)
            self.txtMType.insert(END,sb[1])
            self.txtRef.delete(0,END)
            self.txtRef.insert(END,sb[2])
            self.txtTit.delete(0,END)
            self.txtTit.insert(END,sb[3])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sb[4])
            self.txtsna.delete(0,END)
            self.txtsna.insert(END,sb[5])
            self.txtAdr1.delete(0,END)
            self.txtAdr1.insert(END,sb[6])
            self.txtAdr2.delete(0,END)
            self.txtAdr2.insert(END,sb[7])
            self.txtpcd.delete(0,END)
            self.txtpcd.insert(END,sb[8])
            self.txtMNo.delete(0,END)
            self.txtMNo.insert(END,sb[9])
            self.txtBkID.delete(0,END)
            self.txtBkID.insert(END,sb[10])
            self.txtBkt.delete(0,END)
            self.txtBkt.insert(END,sb[11])
            self.txtAtr.delete(0,END)
            self.txtAtr.insert(END,sb[12])
            self.txtDBo.delete(0,END)
            self.txtDBo.insert(END,sb[13])
            self.txtDdu.delete(0,END)
            self.txtDdu.insert(END,sb[14])
            self.txtsPr.delete(0,END)
            self.txtsPr.insert(END,sb[15])
            self.txtLrF.delete(0,END)
            self.txtLrF.insert(END,sb[16])
            self.txtDoD.delete(0,END)
            self.txtDoD.insert(END,sb[17])
            self.txtDonL.delete(0,END)
            self.txtDonL.insert(END,sb[18])
        
        def DeleteData():
            if(len(MTy.get())!=0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()
        
        def searchDatabase():
            booklist.delete(0,END)
            for row in LibBksDatabase.searchData(MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()):
                booklist.insert(END,row)

        def update():
            if(len(MTy.get())!=0):
                LibBksDatabase.dataUpdate(sb[0],MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get())       
        ################################FRAME################################
        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg="gray25", relief=RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame, font=('Times',46,'bold'), text="Library Database Managment System",fg="White",bg="gray25")
        self.lblTit.grid(sticky = W)
        
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=100, padx=20, pady=20, bg="gray25", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        FrameDetail = Frame(MainFrame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side = BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side = BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=800 ,height=300 ,padx=20 ,relief=RIDGE, 
                                   font=('Times',12,'bold'), text="Library Membership info:" ,bg="gray25",fg="White")
        DataFrameLEFT.pack(side = LEFT)
        
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450 ,height=300 ,padx=20 ,pady=3 ,relief=RIDGE, 
                                   font=('Times',12,'bold'), text="Book Details:", bg="gray25",fg="White")
        DataFrameRIGHT.pack(side = RIGHT) 


        ################################LABELS AND ENTRY################################
        
        self.lblMType = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Member Type:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblMType.grid(row=0, column=0,sticky=W)
        self.txtMType = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=MTy,width=25, bg="White")
        self.txtMType.grid(row=0, column=1)
        
        
        
        self.lblBkID = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Book ID:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblBkID.grid(row=0, column=2,sticky=W)        
        self.txtBkID = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=BkID,width=25, bg="White")
        self.txtBkID.grid(row=0, column=3)
        
        
        
        self.lblRef = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Reference no:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblRef.grid(row=1, column=0,sticky=W)        
        self.txtRef = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Ref,width=25, bg="White")
        self.txtRef.grid(row=1, column=1)
        
        
        
        self.lblBkt = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Book Title:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblBkt.grid(row=1, column=2,sticky=W)        
        self.txtBkt = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Bkt,width=25, bg="White")
        self.txtBkt.grid(row=1, column=3)
        
        
        
        self.lblTit = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Title:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblTit.grid(row=2, column=0,sticky=W)        
        self.txtTit = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Tit,width=25, bg="White")
        self.txtTit.grid(row=2, column=1)
        
        
        
        self.lblAtr = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Author:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblAtr.grid(row=2, column=2,sticky=W)        
        self.txtAtr = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Atr,width=25, bg="White")
        self.txtAtr.grid(row=2, column=3)
        
        
        
        self.lblfna = Label(DataFrameLEFT, font=('Times',12,'bold'), text="First name:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblfna.grid(row=3, column=0,sticky=W)        
        self.txtfna = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=fna,width=25, bg="White")
        self.txtfna.grid(row=3, column=1)
        
        
        
        self.lblDBo = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Date Borrowed:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblDBo.grid(row=3, column=2,sticky=W)        
        self.txtDBo = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=DBo,width=25, bg="White")
        self.txtDBo.grid(row=3, column=3)
        
        
        
        self.lblsna = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Surname:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblsna.grid(row=4, column=0,sticky=W)        
        self.txtsna = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=sna,width=25, bg="White")
        self.txtsna.grid(row=4, column=1)
        
        
        
        self.lblDdu = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Date due:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblDdu.grid(row=4, column=2,sticky=W)        
        self.txtDdu = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Ddu,width=25, bg="White")
        self.txtDdu.grid(row=4, column=3)
        
        
        
        self.lblAdr1 = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Address 1:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblAdr1.grid(row=5, column=0,sticky=W)        
        self.txtAdr1 = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Adr1,width=25, bg="White")
        self.txtAdr1.grid(row=5, column=1)
        
        
        
        self.lblDonL = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Days on Loan:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblDonL.grid(row=5, column=2,sticky=W)        
        self.txtDonL = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=DonL,width=25, bg="White")
        self.txtDonL.grid(row=5, column=3)
        
        
        
        self.lblAdr2 = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Address 2:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblAdr2.grid(row=6, column=0,sticky=W)        
        self.txtAdr2 = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=Adr2,width=25, bg="White")
        self.txtAdr2.grid(row=6, column=1)
        
        
        self.lblLrF = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Late return fine:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblLrF.grid(row=6, column=2,sticky=W)        
        self.txtLrF = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=LrF,width=25, bg="White")
        self.txtLrF.grid(row=6, column=3)
        
        
        
        self.lblpcd = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Post Code:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblpcd.grid(row=7, column=0,sticky=W)        
        self.txtpcd = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=pcd,width=25, bg="White")
        self.txtpcd.grid(row=7, column=1)
        
        
        
        self.lblDoD = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Date over due:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblDoD.grid(row=7, column=2,sticky=W)        
        self.txtDoD = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=DoD,width=25, bg="White")
        self.txtDoD.grid(row=7, column=3)
        
        
        
        self.lblMNo = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Mobile Number:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblMNo.grid(row=8, column=0,sticky=W)        
        self.txtMNo = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=MNo,width=25, bg="White")
        self.txtMNo.grid(row=8, column=1)
        
        
        
        self.lblsPr = Label(DataFrameLEFT, font=('Times',12,'bold'), text="Selling Price:", padx=2, pady=2,bg="gray25",fg="White")
        self.lblsPr.grid(row=8, column=2,sticky=W)        
        self.txtsPr = Entry(DataFrameLEFT, font=('Times',12,'bold'), textvariable=sPr,width=25, bg="White")
        self.txtsPr.grid(row=8, column=3)
        
        
                            #############SCROLLBAR and LISTBOX##################
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0 ,column=1, sticky='ns')
        
        booklist = Listbox(DataFrameRIGHT,width=45,height=12,font=('Times',12,'bold'),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        
        booklist.grid(row=0 ,column=0, padx=8)
        scrollbar.config(command=booklist.yview)
        
        
                            #################BUTTONS####################
        
        self.btnAddData = Button(ButtonFrame,text="Add Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=AddData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame,text="Display Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        
        
        self.btnClearData = Button(ButtonFrame,text="Clear Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=ClearData)
        self.btnClearData.grid(row=0,column=2)
        
        
        self.btnDeleteData = Button(ButtonFrame,text="Delete Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)
    
        
        self.btnUpdateData = Button(ButtonFrame,text="Update Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=update)
        self.btnUpdateData.grid(row=0,column=4)
        
        
        self.btnSearchData = Button(ButtonFrame,text="Search Data",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0,column=5)
                
        
        self.btnExit = Button(ButtonFrame,text="Search Books",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=search_books)
        self.btnExit.grid(row=0,column=6)
        
        self.btnExit = Button(ButtonFrame,text="Exit",font=('Times',14,'bold'),fg="White",bg="gray25",height=2,width=12,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=7)
        
            
if __name__ == '__main__':
    LoginOrRegister.main_screen()
    if(LoginOrRegister.login_success):
        root = Tk()
        application = Library(root)
        root.mainloop()