import tkinter as tk
import time
import combined
from tkinter import font
import sys, select
from threading import Timer
import signal

root = tk.Tk()
brightness = ['#ffffff', '#d9d9d9', '#cccccc', '#b3b3b3', '#999999', '#878787','#696969','#4f4f4f','#3b3b3b','#000000'] 
class GuiTest:
	def __init__(self,brightVal):
		self.titlefont = font.Font(family="Helvetica", size=20, underline = True)
		#self.titlefont.configure(underline = True)
		#Time Variables
		self.v_time1 = tk.StringVar()
		self.v_time2 = tk.StringVar()
		self.v_time3 = tk.StringVar()
		self.label_time1 = tk.Label(root, textvariable=self.v_time1,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '28'))
		self.label_time1.pack(anchor="w")
		self.label_time2 = tk.Label(root, textvariable=self.v_time2,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '18'))
		self.label_time2.pack(anchor="w")
		self.label_time3 = tk.Label(root, textvariable=self.v_time3,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '18'))
		self.label_time3.pack(anchor="w")
		self.v_time1.set("Good Morning")
		self.v_time2.set("Wednesday, April 3")
		self.v_time3.set("8:31 am")
		
		#Weather Variables
		self.label_weathertitle = tk.Label(root, text="Weather",bg='#000000',fg=brightness[brightVal],font=self.titlefont)
		self.label_weathertitle.pack(anchor="w")
		self.v_weather1 = tk.StringVar()
		self.label_weather1 = tk.Label(root, textvariable=self.v_weather1,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))
		self.label_weather1.pack(anchor="w")
		self.v_weather1.set("40F Sunny")


		#News
		self.label_newstitle = tk.Label(root, text="Headlines",bg='#000000',fg=brightness[brightVal],font=self.titlefont)
		self.label_newstitle.pack(anchor="w")
		self.v_news1 = tk.StringVar()
		self.v_news2 = tk.StringVar()
		self.v_news3 = tk.StringVar()
		self.v_news4 = tk.StringVar()
		self.v_news5 = tk.StringVar()
		self.label_news1 = tk.Label(root, textvariable=self.v_news1,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))
		self.label_news1.pack(anchor="w")
		self.v_news1.set("Trump Does Stuff")
		self.label_news2 = tk.Label(root, textvariable=self.v_news2,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))		
		self.label_news2.pack(anchor="w")
		self.v_news2.set("Which type of MOSFET are you? Take this quiz to find out!!")
		self.label_news3 = tk.Label(root, textvariable=self.v_news3,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))
		self.label_news3.pack(anchor="w")
		self.v_news3.set("Smart refridgerator becomes self-aware")
		self.label_news4 = tk.Label(root, textvariable=self.v_news4,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))
		self.label_news4.pack(anchor="w")
		self.v_news4.set("4 things that you should definitely be doing, you won't believe number 3")
		self.label_news5 = tk.Label(root, textvariable=self.v_news5,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '16'))
		self.label_news5.pack(anchor="w")
		self.v_news5.set("European Union bans memes")

		
		#Calendar
		self.label_caltitle = tk.Label(root, text="Upcoming Events",bg='#000000',fg=brightness[brightVal],font=self.titlefont)
		self.label_caltitle.pack(anchor="w")
		self.v_calendar1 = tk.StringVar()
		self.label_calendar1 = tk.Label(root, textvariable=self.v_calendar1,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar1.pack(anchor="w")
		self.v_calendar2 = tk.StringVar()
		self.label_calendar2 = tk.Label(root, textvariable=self.v_calendar2,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar2.pack(anchor="w")
		self.v_calendar3 = tk.StringVar()
		self.label_calendar3 = tk.Label(root, textvariable=self.v_calendar3,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar3.pack(anchor="w")
		self.v_calendar4 = tk.StringVar()
		self.label_calendar4 = tk.Label(root, textvariable=self.v_calendar4,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar4.pack(anchor="w")
		self.v_calendar5 = tk.StringVar()
		self.label_calendar5 = tk.Label(root, textvariable=self.v_calendar5,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar5.pack(anchor="w")
		self.v_calendar6 = tk.StringVar()
		self.label_calendar6 = tk.Label(root, textvariable=self.v_calendar6,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar6.pack(anchor="w")
		self.v_calendar7 = tk.StringVar()
		self.label_calendar7 = tk.Label(root, textvariable=self.v_calendar7,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar7.pack(anchor="w")
		self.v_calendar8 = tk.StringVar()
		self.label_calendar8 = tk.Label(root, textvariable=self.v_calendar8,bg='#000000',fg=brightness[brightVal],font=('Helvetica', '14'))
		self.label_calendar8.pack(anchor="w")
		self.v_calendar1.set("8:30 Brush Teeth")
		self.v_calendar2.set("8:30 Brush Teeth2")
		self.v_calendar3.set("8:30 Brush Teeth3")
		self.v_calendar4.set("8:30 Brush Teeth4")
		self.v_calendar5.set("8:30 Brush Teeth5")
		self.v_calendar6.set("8:30 Brush Teeth6")
		self.v_calendar7.set("8:30 Brush Teeth7")
		self.v_calendar8.set("8:30 Brush Teeth8")
		#self.label_calender8.pack_forget()

	def changeTime(self, time):
		self.v_time1.set(time[0])
		self.v_time2.set(time[1])
		self.v_time3.set(time[2])

	def changeWeather(self, weather):
		self.v_weather1.set(weather)

	def changeNews(self, news):
		self.v_news1.set(news[0])
		self.v_news2.set(news[1])
		self.v_news3.set(news[2])
		self.v_news4.set(news[3])
		self.v_news5.set(news[4])

	def changeCalendar(self, calendarList):
		length = len(calendarList)
		if(length < 8):
			self.v_calendar8.set("")
		else:
			self.v_calendar8.set(calendarList[7])
			
		if(length < 7):
			self.v_calendar7.set("")
		else:
			self.v_calendar7.set(calendarList[6])
		
		if(length < 6):
			self.v_calendar6.set("")
		else:
			self.v_calendar6.set(calendarList[5])
		
		if(length < 5):
			self.v_calendar5.set("")
		else:
			self.v_calendar6.set(calendarList[4])
		
		if(length < 4):
			self.v_calendar4.set("")
		else:
			self.v_calendar4.set(calendarList[3])
		
		if(length < 3):
			self.v_calendar3.set("")
		else:
			self.v_calendar3.set(calendarList[2])
		
		if(length < 2):
			self.v_calendar2.set("")
		else:
			self.v_calendar2.set(calendarList[1])
		
		if(length < 1):
			self.v_calendar1.set("")
		else:
			self.v_calendar1.set(calendarList[0])
			
	def changeString(self,newstring):
		self.v_calendar1.set(newstring)
		
	def changeBrightness(self,brightVal):
		self.label_time1.config(fg=brightness[brightVal])
		self.label_time2.config(fg=brightness[brightVal])
		self.label_time3.config(fg=brightness[brightVal])
		self.label_weather1.config(fg=brightness[brightVal])
		self.label_news1.config(fg=brightness[brightVal])
		self.label_news2.config(fg=brightness[brightVal])
		self.label_news3.config(fg=brightness[brightVal])
		self.label_news4.config(fg=brightness[brightVal])
		self.label_news5.config(fg=brightness[brightVal])

		self.label_calendar1.config(fg=brightness[brightVal])
		self.label_calendar2.config(fg=brightness[brightVal])
		self.label_calendar3.config(fg=brightness[brightVal])
		self.label_calendar4.config(fg=brightness[brightVal])
		self.label_calendar5.config(fg=brightness[brightVal])
		self.label_calendar6.config(fg=brightness[brightVal])
		self.label_calendar7.config(fg=brightness[brightVal])
		self.label_calendar8.config(fg=brightness[brightVal])
		
		self.label_weathertitle.config(fg=brightness[brightVal])
		self.label_newstitle.config(fg=brightness[brightVal])
		self.label_caltitle.config(fg=brightness[brightVal])
	def wait_for_input(self):
		user_input = input("Give me a command such as \"exit\"")
		if user_input == "exit":
			root.quit()
		else:
			self.changeString(user_input)
			root.after(0, self.wait_for_input())

	def looper(self):
		serialVar = ""
		i = 0
		while(len(serialVar) != 4):
			serialVar = combined.serialTest()
			if(i==4):
				serialVar = "1120"
				i = 0
			i+=1
		combinedCal = combined.calendarRefresh(int(serialVar[2]))
		self.changeCalendar(combinedCal)
		self.changeTime(combined.clock())
		self.changeNews(combined.news())
		self.changeWeather(combined.openWeather())
		self.changeBrightness(int(serialVar[3]))
		root.after(5000, self.looper)
def interrupted(signum, frame):
	print("interrupted")	
if __name__ == "__main__":
	root.attributes('-fullscreen',True)
	root.configure(background='black')
	test = GuiTest(0)
	root.after(0,test.looper)
	root.mainloop()	

