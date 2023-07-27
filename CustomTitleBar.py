import tkinter as tk

class CustomTitleBar:

    def __init__(self, root):
        self.root = root

        self.root.overrideredirect(True)

        self.build()

    def build(self):

        self.topbar = tk.Canvas(self.root,background="#ef4c96",border=0,highlightthickness=0,height=30)
        self.topbar.pack(fill="both")

        y = 35

        self.topbar.create_line((0,15),(500,15),fill="#251428",width=5)
        self.topbar.create_line((457,0),(457,35),fill="#f79ee7",width=5)

        lx= 200

        for i in range(4):
            
            self.topbar.create_line((lx-20,-5),(lx,15),fill="#251428",width=5)
            self.topbar.create_line((lx,15),(lx-20,35),fill="#251428",width=5)

            lx += 60

        self.topbar.create_line((420,-5),(400,15),fill="#f79ee7",width=5)
        self.topbar.create_line((400,15),(420,35),fill="#f79ee7",width=5)
        self.topbar.create_line((382,15),(500,15),fill="#f79ee7",width=5)


        self.topbar.create_oval(((40,0-y),(140,100-y)),fill="#ef679d",outline="#ef679d")
        self.topbar.create_oval(((15,0-y),(115,100-y)),fill="#ef67e2",outline="#ef67e2")
        self.topbar.create_oval(((-10,0-y),(90,100-y)),fill="#d642c7",outline="#d642c7")
        self.topbar.create_oval(((-40,0-y),(60,100-y)),fill="#b967ef",outline="#b967ef")

        self.close_button = tk.Button(self.topbar,height=0, text='X', bg='#ef67a4', fg='white', relief='flat', command=self.root.destroy,highlightthickness=0,font=("Silkscreen"))
        self.close_button.pack(side='right')

        self.topbar.bind('<ButtonPress-1>', self.start_move)
        self.topbar.bind('<ButtonRelease-1>', self.stop_move)
        self.topbar.bind('<B1-Motion>', self.on_move)

    def start_move(self, event):
        self.root._offsetx = event.x
        self.root._offsety = event.y

    def stop_move(self, event):
        del self.root._offsetx
        del self.root._offsety

    def on_move(self, event):
        x = self.root.winfo_x() + event.x - self.root._offsetx
        y = self.root.winfo_y() + event.y - self.root._offsety
        self.root.geometry(f'+{x}+{y}')