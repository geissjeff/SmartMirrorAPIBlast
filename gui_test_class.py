import tkinter as tk


class GuiTest:
	def __init__(self):
		self.v_calendar = tk.StringVar()
		self.label_calender = tk.Label(root, textvariable=v_calendar)
		label_calender.pack()
	
	def changeString(newstring):
		v_calendar.set(newstring)
		
		
	
	def wait_for_input():
		user_input = input("Give me a command such as \"exit\"")
		if user_input == "exit":
			root.quit()
		else:
			changeString(user_input)
			root.after(0, self.wait_for_input)
			

if __name == "__main__":
	root= tk.Tk()
	root.attributes('-fullscreen',True)
	test = GuiTest()		
	test.wait_for_input()
	#root.after(0, wait_for_input)
