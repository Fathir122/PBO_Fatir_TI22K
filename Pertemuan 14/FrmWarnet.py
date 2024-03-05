import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Warnet import Warnet
from tkcalendar import DateEntry
from datetime import datetime

class FormWarnet:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Id Komputer:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtIdKomputer = Entry(mainFrame) 
        self.txtIdKomputer.grid(row=0, column=1, padx=5, pady=5) 
        self.txtIdKomputer.bind("<Return>",self.onCari) 
        
        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 
        self.txtNama.bind("<Return>",self.onCari) 

        Label(mainFrame, text='Tanggal:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtTanggal = DateEntry(mainFrame)
        self.txtTanggal.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Waktu dan Harga:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtWaktu = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtWaktu) 
        Cbo.grid(row=3, column=1, padx=5, pady=5)
        Cbo['values'] = ('1 jam Rp3000','2 jam Rp6000','3 jam Rp9000','4 jam Rp12000','5 jam Rp15000')
        Cbo.current()      

        Label(mainFrame, text='Status Pembayaran:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtStatusPembayaran = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtStatusPembayaran) 
        Cbo.grid(row=4, column=1, padx=5, pady=5)
        Cbo['values'] = ('Belum Lunas','Lunas')
        Cbo.current()           
        
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        columns = ('id', 'id_komputer', 'nama', 'tanggal','waktu','status_pembayaran')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('id_komputer', text='ID Kompuer')
        self.tree.column('id', width="30")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="60")
        self.tree.heading('tanggal', text='Tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('waktu', text='Waktu & Harga')
        self.tree.column('waktu', width="100")
        self.tree.heading('status_pembayaran', text='Status Pembayaran')
        self.tree.column('status_pembayaran', width="120")
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")
        self.txtTanggal.delete(0, END)
        self.txtStatusPembayaran.set("")
        self.txtWaktu.set("")
        self.ditemukan = False

        
    def onReload(self, event=None):
        wrt = Warnet()
        result = wrt.get_all_data()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nama = self.txtNama.get()
        wrt = Warnet()
        res = wrt.get_by_nama(nama)
        rec = wrt.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nama = self.txtNama.get()
        wrt = Warnet()
        res = wrt.get_by_nama(nama)
    
        if res:
            self.txtTanggal.set_date(wrt.tanggal.strftime('%d/%m/%Y'))
            self.txtWaktu.set(wrt.waktu)
            self.txtStatusPembayaran.set(wrt.status_pembayaran)   
            self.ditemukan = True
            self.btnSimpan.config(text="Update")
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtNama.focus()

                 
    def onSimpan(self, event=None):
        id_komputer = self.txtIdKomputer.get()
        nama = self.txtNama.get()
        tanggal_str = self.txtTanggal.get()
        waktu = self.txtWaktu.get()
        status_pembayaran = self.txtStatusPembayaran.get()

        if not tanggal_str:
            messagebox.showerror("Error", "Tanggal harus diisi")
        
        try:
            tanggal = datetime.strptime(tanggal_str, "%m/%d/%y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal tidak valid")
        

        try:
            id_komputer = int(id_komputer)
        except ValueError:
            messagebox.showerror("Error", "ID Komputer harus berupa angka")
        

        wrt = Warnet()
        wrt.id_komputer = id_komputer
        wrt.nama = nama
        wrt.tanggal = tanggal
        wrt.waktu = waktu
        wrt.status_pembayaran = status_pembayaran

        if self.ditemukan:
            res = wrt.update_by_nama(nama, id_komputer, tanggal, waktu, status_pembayaran)
        else:
            res = wrt.simpan(id_komputer, nama, tanggal, waktu, status_pembayaran)

        if res:
            messagebox.showinfo("Info", "Data berhasil disimpan")
            self.onReload()
            self.onClear()
        else:
            messagebox.showwarning("Peringatan", "Data gagal disimpan")




    def onDelete(self, event=None):
        nama = self.txtNama.get()
        wrt = Warnet()
        wrt.nama = nama
        if(self.ditemukan==True):
            res = wrt.delete_by_nama(nama)
            rec = wrt.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormWarnet(root, "Aplikasi Data Warnet")
    root.mainloop() 