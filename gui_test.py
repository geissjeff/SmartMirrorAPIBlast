import tkinter as tk

root= tk.Tk()

#canvas1 = tk.Canvas(root, width = 1000, height = 350)
#canvas1.pack()
def wait_for_input():
	user_input = input("Give me a command such as \"exit\"")
	if user_input == "exit":
		root.quit()
	else:
		label = tk.Label(root, text=user_input)
		label.pack()
		#v=user_input
		root.after(0, wait_for_input)
v = tk.StringVar()
label = tk.Label(root, textvariable=v)
label.pack()
v.set("New Text")
v.set("This thing")
root.after(0, wait_for_input)
root.mainloop()  
