import sqlite3

def ConnectData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, MTy text, Ref text, Tit text, fna text, \
                                                      sna text, Adr1 text, Adr2 text, pcd text, MNo text, BkID text, Bkt text, \
                                                       Atr text, DBo text, Ddu text, sPr text, LrF text, DoD text, DonL text)")
    
    con.commit()
    con.close()
    
    
def addDataRec(MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL))
    con.commit()
    con.close()
    
def viewData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("DELETE FROM libbooks WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(MTy="",Ref="",Tit="",fna="",sna="",Adr1="",Adr2="",pcd="",MNo="",BkID="",Bkt="",Atr="",DBo="",Ddu="",sPr="",LrF="",DoD="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks WHERE MTy=? OR Ref=? OR Tit=? OR fna=? OR sna=? OR Adr1=? OR ADR2=? OR PCD=? OR MNO=? OR BKID=? OR BKT=? OR ATR=? OR DBO=? OR DDU=? OR SPR=? OR LRF=? OR DOD=? OR DONL=?",(MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL))
    rows=cur.fetchall()
    con.close()
    return rows
    
def dataUpdate(id,MTy="",Ref="",Tit="",fna="",sna="",Adr1="",Adr2="",pcd="",MNo="",BkID="",Bkt="",Atr="",\
               DBo="",Ddu="",sPr="",LrF="",DoD="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("UPDATE libbooks SET MTY=? , REF=? , TIT=? , FNA=? , SNA=? , ADR1=? , ADR2=? , PCD=? , MNO=? , BKID=?,\
                BKT=?, ATR=?, DBO=?, DDU=?, SPR=?, LRF=?, DOD=?, DONL=? WHERE id=?", \
                (MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL, id))
    con.commit()
    con.close()

ConnectData()
    