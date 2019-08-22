# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
import webbrowser


# in the text entry box
from ubidots_handler.build_graph import build_graph


#def press(num):
    #todo
    #elif bigML_btn:
    #todo
    #elif pred_btn:

# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="white")

	# set the title of GUI window
	gui.title("SauSmart")

	# set the configuration of GUI window
	gui.geometry("256x256")


	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	last_hour_btn = Button(gui, text=' last hour graph ', fg='black', bg='light green',
					command=lambda: webbrowser.open('https://industrial.ubidots.com/app/dashboards/public/widget/Xh2CwDpvLj1KwU9dE0vHWpH0OpQ'), height=2, width=15)
	last_hour_btn.grid(row=2, column=0)

	selected_date_btn = Button(gui, text=' selected date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=2, width=15)
	selected_date_btn.grid(row=3, column=0)

	bigML_btn = Button(gui, text=' selected date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=2, width=15)
	bigML_btn.grid(row=4, column=0)

	pred_btn = Button(gui, text=' selected date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=2, width=15)
	pred_btn.grid(row=5, column=0)

	# start the GUI
	gui.mainloop()



