import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pytube import YouTube

def downloader():
    zelda = link.get()
    calidad = variable.get()
    yt = YouTube(zelda)
    if calidad == '720p':
        videos = yt.streams.filter(progressive=True, file_extension='mp4', resolution=calidad)
    else:
        videos = yt.streams.filter(adaptive=True, file_extension='mp4', resolution=calidad)
        audios = yt.streams.filter(only_audio=True, abr='128kbps')
        audio = list(enumerate(audios))
        dn_audio = audios[0]
    title = yt.title
    video = list(enumerate(videos))
    dn_video = videos[0]

    dn_video.download()

resolutions = ['720p',
               '1080p',
               '1440p']


                #Window creation#
windows = Tk()
windows.geometry('800x600')
windows.resizable(width=False, height=False)
windows.title('Youtube Downloader')

                #Interface#
text = Label(windows, text='Inserte el link debajo', font='30')
text.pack()
text.place(x=325, y=220)

text2 = Label(windows, text='Seleccione la calidad del video que desea', font='15')
text2.pack()
text2.place(x=110, y=330)

text3 = Label(windows, text='Developed by Lucas Skywalker', font='10')
text3.pack()
text3.place(x=4, y=570)

text4 = Label(windows, text='alpha 0.1')
text4.pack()
text4.place(x=740, y=580)

link = tkinter.Entry(windows, font='10')
link.pack()
link.place(x=100,y=260, width=600, height=40)

variable = tkinter.StringVar(windows)
variable.set(resolutions[0])

desplegable_menu = tkinter.OptionMenu(windows, variable, *resolutions)
desplegable_menu.pack()
desplegable_menu.place(x=500, y=330, width=100)

enter_button = tkinter.Button(text='Download', font='15', command= lambda: downloader())
enter_button.pack()
enter_button.place(x=340, y=500, width=120)

exit_button = tkinter.Button(text='Exit', font='15', command=windows.destroy)
exit_button.pack()
exit_button.place(x= 720, y=550 ,width=60)


#Photos
icon1 = PhotoImage(file='Youtube_icon.png')
image = ImageTk.PhotoImage(Image.open('Youtube_icono2.png'))
windows.iconphoto(False, icon1)
label = Label(image=image)
label.pack()
label.place(x=250, y=70)


windows.mainloop()