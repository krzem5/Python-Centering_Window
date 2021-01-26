import tkinter as tk



def center(toplevel):
    toplevel.update_idletasks()
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    toplevel.title("Centered!")    
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Not centered")
    win = tk.Toplevel(root)
    center(win)
    root.mainloop()
