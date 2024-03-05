import tkinter as tk
from tkinter import Menu
from FrmLogin import FormLogin
from FrmAdmin import FrmAdmin
from FrmWarnet import FormWarnet

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Menu Demo')
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)

        self.menu_index = {}

        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        self.admin_menu.add_command(label='Data Admin', command=lambda: self.new_window("Data Admin", FrmAdmin))

        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        if _class == FormLogin:
            new = tk.Toplevel(self.root)
            new.transient()
            new.grab_set()
            _class(new, number, self.update_main_window)
        elif _class == FrmAdmin:
                pass# ... (existing code)
        elif _class == FormWarnet:
                pass# ... (existing code)
        else:
                pass

    def update_main_window(self, data):
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if loginvalid:
            index = self.file_menu.index('Login')
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            if level == 'admin':
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
                self.menu_index[self.__level] = self.menubar.index("Admin")
            else:
                self.__level = None

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        if self.__level in self.menu_index:
            index = self.menu_index[self.__level]
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()