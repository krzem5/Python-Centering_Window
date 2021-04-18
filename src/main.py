import tkinter as tk



def center(r):
	r.update_idletasks()
	ww=r.winfo_screenwidth()
	wh=r.winfo_screenheight()
	sz=tuple(int(e) for e in r.geometry().split("+")[0].split("x"))
	x=ww//2-sz[0]//2
	y=wh//2-sz[1]//2
	r.geometry(f"{sz[0]}x{sz[1]}+{x}+{y}")
	r.title("Centered!")



if (__name__=="__main__"):
	r=tk.Tk()
	r.title("Not centered")
	w=tk.Toplevel(r)
	center(w)
	r.mainloop()
