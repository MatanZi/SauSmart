# Python program to create a simple GUI
# calculator using Tkinter
import webbrowser
import tkinter as tk
from ubidots_handler.build_graph import build_graph
from ubidots_handler.get_data import get_last_sample
from feature_handler.FeatureExtractor import FeatureExtractor
from ML.Bigml_handler import BIGML_Model
# Driver code
if __name__ == "__main__":

	# create a GUI window
	gui = tk.Tk()

	# set the background colour of GUI window
	gui.configure(background="black")

	# set the title of GUI window
	gui.title("SauSmart")

	# set the configuration of GUI window
	gui.geometry("400x750")

	# Create label
	w = tk.Label(gui, text="\nWelcome to SauSmart place choose a button\n", height=1, width=0, font=20 ,fg='blue', bg='yellow')
	w.grid()

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .

	last_hour_btn = tk.Button(gui, text=' show last hour chart ', fg='black', bg='light green',
							  command=lambda: webbrowser.open('https://industrial.ubidots.com/app/dashboards/public/widget/Xh2CwDpvLj1KwU9dE0vHWpH0OpQ')
							  , height=5, width=20, font=16)
	last_hour_btn.grid(row=2, column=0)

	selected_date_btn = tk.Button(gui, text=' show date graph ', fg='black', bg='light green',
					command=lambda: build_graph(), height=5, width=20, font=16)
	selected_date_btn.grid(row=3, column=0)

	bigML_btn = tk.Button(gui, text=' show decision tree ', fg='black', bg='light green',
						  command=lambda: webbrowser.open('https://bigml.com/dashboard/model/5d66af8c42129f066f00002b'),
						  height=5, width=20, font=16)
	bigML_btn.grid(row=4, column=0)

	tank_btn = tk.Button(gui, text=' show tank value ', fg='black', bg='light green',
						  command=lambda: webbrowser.open(
							  'https://industrial.ubidots.com/app/dashboards/public/widget/8TY39vGV8Tv7mLitDlb5wYOCxcE'),
						  height=5, width=20, font=16)
	tank_btn.grid(row=5, column=0)

	w2 = tk.Label(gui, text="\n\n\n\n", height=1, width=0, font=20, fg='blue')

	pred_btn = tk.Button(gui, text='Get last prediction', fg='black', bg='light green',
						 command=lambda: w2.config(text=BIGML_Model(model_path='model/5d66af8c42129f066f00002b').
												   get_predict(FeatureExtractor.convert_sample(get_last_sample()))),
						 height=5, width=20, font=16)
	pred_btn.grid(row=6, column=0)

	w2.grid()
	#rint()
	# start the GUI
	gui.mainloop()
