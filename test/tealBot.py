# Import the necessary libraries
import tkinter as tk
import requests

# Set the criteria for job searches
location = 'San Francisco'
keywords = ['software', 'developer']

# Set the initial list of jobs
jobs = []

# Define the search function
def search():
  # Get the search results from the API
  response = requests.get(
    'https://jobs.github.com/positions.json',
    params={
      'location': location,
      'description': keywords
    }
  )

  # Add the new jobs to the list
  for job in response.json():
    jobs.append(job)

  # Update the widget with the new list of jobs
  update_widget()

# Define the update function
def update_widget():
  # Clear the widget
  widget.delete('1.0', tk.END)

  # Loop through the list of jobs
  for job in jobs:
    # Append the job title and company to the widget
    widget.insert(
      tk.END,
      f'{job["title"]} at {job["company"]}\n'
    )

# Create the main window
window = tk.Tk()

# Create the search button
button = tk.Button(
  window,
  text='Search',
  command=search
)
button.pack()

# Create the widget for displaying the jobs
widget = tk.Text(window)
widget.pack()

# Run the main loop
window.mainloop()
