import tkinter as tk
from tkinter import filedialog

import matplotlib
matplotlib.use('Agg')

from google_auth_oauthlib.flow import Flow

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename
print(file_path)

# flowSession = Flow.from_client_secrets_file("client_secret_199415634341-fqauvjaqj7c84b3rbnvnpsh8b9tt1m1e.apps.googleusercontent.com.json",["email"])

#(x,y) = flowSession.authorization_url()

#print(x)
