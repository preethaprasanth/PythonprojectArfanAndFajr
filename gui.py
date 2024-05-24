import tkinter as tk
import plotting


 #Function to accept user input , number of hours spend in each day ,and a Button to plot the data
#Hints -Use label,entry box and Button widgets

def run_app():

   #Invoke 'plot_data' function in plotting.py to plot days vs no of hours
    plotting.plot_data(days, study_hours)
