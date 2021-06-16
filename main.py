# -*- coding: utf-8 -*-

try:
	import os
	import sys
	import json
	import tkinter as tk
	from tkinter import filedialog

	from src import python_style as pys

except Exception as e:
	raise e


class Stylizer():

	
	def __str__(self):

		return 'Stylizer class'

	def create_python_style(self):
		pass


	# Gettings file extension
	def style(self, file_path):
		
		file_name = os.path.basename(file_path)
		file_extension = os.path.splitext(file_name)[1]
		
		if file_extension == ".py":

			with open("config/python.json", "r") as config_file:

				config = json.load(config_file)
				config_file.close()

			target_path = os.path.abspath(__file__)


			pys.Python_Stylizer(file_path, config, target_path)

		else:

			print("not supported")



class Main():


	def __init__(self):

		self.stylizer = Stylizer()

		self.create_window()
		self.render_widgets()
		self.root.mainloop()


	def create_window(self):

		self.root = tk.Tk()
		self.root.title("Web code stylizer")
		self.root.geometry("1080x580")
		self.root.configure(bg="#212121")


	def file_path(self):

		filename = filedialog.askopenfilename(initialdir ="Téléchargements")
		return filename

	def start_app(self):

		self.stylizer.style(self.file_path())


	def render_widgets(self):

		self.TITLE = tk.Label(self.root, text="Web code stylizer", fg="white", bg="#212121", font=("impact", 50))
		self.TITLE.pack()

		self.FILE_INPUT = tk.Button(self.root, text="Sélectionner un fichier", bg="#313232", fg="white", font=("impact", 25))
		self.FILE_INPUT.configure(command=self.start_app)
		self.FILE_INPUT.pack(pady=50)



if __name__ == '__main__':

	main=Main()