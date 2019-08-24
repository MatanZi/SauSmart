# Python program to create a simple GUI
# calculator using Tkinter
import webbrowser
import tkinter as tk
from ubidots_handler.build_graph import build_graph
from ubidots_handler.get_data import get_last_sample
from ML.Bigml_handler import BIGML_Model
# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = tk.Tk()

	# set the background colour of GUI window
	gui.configure()

	# set the title of GUI window
	gui.title("SauSmart")


	# set the configuration of GUI window
	gui.geometry("400x600")

	# Create label
	w = tk.Label(gui, text="\nWelcome to SauSmart place choose a button\n", height=1, width=0, font=20 ,fg='blue', bg='yellow')
	w.grid()



	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	last_hour_btn = tk.Button(gui, text=' last hour graph ', fg='black', bg='light green',
							  command=lambda: webbrowser.open('https://industrial.ubidots.com/app/dashboards/public/widget/Xh2CwDpvLj1KwU9dE0vHWpH0OpQ')
							  , height=5, width=20, font=16)
	last_hour_btn.grid(row=2, column=0)

	selected_date_btn = tk.Button(gui, text=' selected date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=5, width=20, font=16)
	selected_date_btn.grid(row=3, column=0)

	bigML_btn = tk.Button(gui, text=' select date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=5, width=20, font=16)
	bigML_btn.grid(row=4, column=0)

	pred_btn = tk.Button(gui, text=' select date graph ', fg='black', bg='light green',
					command=lambda: print(BIGML_Model('modelid').get_predict(get_last_sample())),
                         height=5, width=20, font=16)
	pred_btn.grid(row=5, column=0)

	# start the GUI
	gui.mainloop()
