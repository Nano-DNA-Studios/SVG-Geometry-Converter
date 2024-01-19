import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import pyperclip

# Open file dialog to select SVG file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[('SVG files', '*.svg')])

# Parse SVG file and extract path data
tree = ET.parse(file_path)
root = tree.getroot()
namespace = {'svg': 'http://www.w3.org/2000/svg'}
path_data = root.find('svg:path', namespace).get('d')

# Ask for key name
key_name = input("Enter the key name: ")

# Format output
output = f'<Geometry x:Key="{key_name}">\n    {path_data}\n</Geometry>'

print("")
print(output)
print("")

# Copy output to clipboard
pyperclip.copy(output)

print("Output copied to clipboard.")