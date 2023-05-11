import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")

    except:
        finishLabel.configure(text="Download Error!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update Progress Bar
    progressBar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link", text_color="#FF8080", font=("Consolas", 18))
title.pack(pady=10, padx=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="", font=("Consolas", 18))
finishLabel.pack()

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", font=("Consolas", 18), command=startDownload)
download.pack(padx=10, pady=10)


# Resolution Dropdown
def combobox_callback(choice):
    print("Combobox dropdown clicked:", choice)


# resolution_var = customtkinter.StringVar(value="Video Resolution")
# resolution = customtkinter.CTkComboBox(app, width=200, font=("Consolas", 12), dropdown_font=("Consolas", 12),
#                                       corner_radius=5, justify="center",
#                                       values=["Highest "
#                                               "Resolution",
#                                               "Lowest "
#                                               "Resolution"],
#                                       command=combobox_callback, variable=resolution_var)
# resolution_var.set("Video Resolution")
# resolution.pack(padx=10, pady=10)

app.mainloop()
