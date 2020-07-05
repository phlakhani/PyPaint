from tkinter import *
from tkinter import filedialog, simpledialog
import PIL
from PIL import ImageTk, Image,ImageDraw, ImageEnhance
import os
import tkinter.messagebox



class App:
    def __init__(self,app):
        self.app=app
        self.app.title("PyPaint")
        self.app.geometry("1250x650")
        self.app.resizable(False,False)
        self.app.configure(bg='#128ce3')


        self.filepath= None
        self.pillowimage = None    # we need to make it self bcoz it we are not just using this open_photo, but also in rotate
        self.newwidth = None
        self.newheight = None
        self.saveasflag = 0

        self.menubar = Menubar(self)


        self.canvas = Canvas(app, width=1250, height= 650, bg='#e2c8e8')
        self.canvas.pack(padx=5, pady=5, side=LEFT)






    def developerMsgBox(self):
            tkinter.messagebox.showinfo(title='About Developer', message='This PyPaint is Developed by Piyush Lakhani')

    def versionMsgBox(self):
        tkinter.messagebox.showinfo(title='Version Info', message='PyPaint Version-1.01 updated on April,2020')

    def howtoresize(self):
        tkinter.messagebox.showinfo(title='How to Resize', message='To resize your image\n Enter Width & Height in formate "123x123"')

    def resize(self):
        if self.saveasflag == 1:
            global photo
            inputwindow = Tk()
            inputwindow.withdraw()
            newsize = simpledialog.askstring(title="Resizing Image", prompt="Enter your new Dimension")
            X = newsize.index('x')
            newwidth = int(newsize[0:X])
            newheight = int(newsize[X+1:])

            self.pillowimage = self.pillowimage.resize((newwidth,newheight), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(self.pillowimage)
            print(photo.width(), photo.height())
            self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def open_photo(self,*args):
        self.canvas.delete('all')
        global photo                  # need to declare global due to garbage colllection
        self.filepath = filedialog.askopenfilename(filetypes=[("jpg file", "*.jpg"),
                                                              ("jpeg file", "*.jpeg"),
                                                              ("png file", "*.png"),
                                                              ("gif file", "*.gif"),
                                                              ("tiff file", "*.tiff"),
                                                              ("bmp file", "*.bmp"),
                                                              ("webp file", "*.webp")])
        #print(self.filepath)

        self.pillowimage = Image.open(self.filepath)
        width,height = self.pillowimage.size
        print(width,height)
        if width>=1250 or height>=650:
            self.newwidth=1220
            self.newheight=620
            self.pillowimage =self.pillowimage.resize((self.newwidth, self.newheight), Image.ANTIALIAS)
        else:
            self.newheight = height
            self.newwidth = width
        photo = ImageTk.PhotoImage(self.pillowimage)
        print(photo.width(), photo.height())
        self.canvas.create_image(10, 10, anchor=NW, image=photo)
        self.saveasflag=1

    def reset(self):
        global photo
        self.pillowimage = Image.open(self.filepath)
        self.pillowimage = self.pillowimage.resize((self.newwidth, self.newheight), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('Reset all')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def rotateby90(self):
        global photo
        self.pillowimage = self.pillowimage.rotate(90)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('rotating done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def rotateby45(self):
        global photo
        self.pillowimage = self.pillowimage.rotate(45)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('rotating done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def grayscale(self):
        global photo
        self.pillowimage = self.pillowimage.convert(mode='L')
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('convert done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def bluish(self):
        rgb2xyz = (
            0.412453, 0.357580, 0.180423, 1,
            0.512671, 0.215160, 0.072169, 1,
            0.419334, 0.619193, 0.950227, 1)
        global photo
        self.pillowimage = self.pillowimage.convert("RGB",rgb2xyz)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('convert done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def olddays(self):
        rgb2xyz = (
            0.912453, 0.957580, 0.180423, 1,
            0.912671, 0.915160, 0.072169, 1,
            0.919334, 0.919193, 0.950227, 1)
        global photo
        self.pillowimage = self.pillowimage.convert("RGB",rgb2xyz)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('convert done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def pinkish(self):
        rgb2xyz = (
            0.912453, 0.057580, 0.00423, 0,
            0.0912671, 0.415160, 0.072169, 0,
            0.0919334, 0.919193, 0.0950227, 0)
        global photo
        self.pillowimage = self.pillowimage.convert("RGB",rgb2xyz)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('convert done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def bw(self):
        rgb2xyz = (
            1.0, 0.0, 0.0, 0,
            1.0, 0.0, 0.0, 0,
            1.0, 0.0, 0.0, 0)
        global photo
        self.pillowimage = self.pillowimage.convert("RGB", rgb2xyz)
        photo = ImageTk.PhotoImage(self.pillowimage)
        print('convert done')
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def brightnessIncrease(self):
        global photo
        imgenhance = ImageEnhance.Brightness(self.pillowimage)
        self.pillowimage = imgenhance.enhance(1.1)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def brightnessDecrease(self):
        global photo
        imgenhance = ImageEnhance.Brightness(self.pillowimage)
        self.pillowimage = imgenhance.enhance(0.9)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def contrastIncrease(self):
        global photo
        imgenhance = ImageEnhance.Contrast(self.pillowimage)
        self.pillowimage = imgenhance.enhance(1.1)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def contrastDecrease(self):
        global photo
        imgenhance = ImageEnhance.Contrast(self.pillowimage)
        self.pillowimage = imgenhance.enhance(0.9)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def tempIncrease(self):
        global photo
        imgenhance = ImageEnhance.Color(self.pillowimage)
        self.pillowimage = imgenhance.enhance(1.1)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)

    def tempDecrease(self):
        global photo
        imgenhance = ImageEnhance.Color(self.pillowimage)
        self.pillowimage = imgenhance.enhance(0.9)
        print('brightness done')
        photo = ImageTk.PhotoImage(self.pillowimage)
        self.canvas.create_image(10, 10, anchor=NW, image=photo)


    def save(self):
        if self.saveasflag == 1:  # this flag will be 1 only after open or create image function is used bcoz only after that we need save_as
            if self.filepath:
                onlyfilename = os.path.basename(self.filepath)
                file = onlyfilename[0:-4]
                extension = onlyfilename[-3:]
                print(file, extension)
                self.pillowimage.save('{}_edited.{}'.format(file,extension))
            else:
                self.image1.save('myimage.jpg')

    def save_as(self):
        if self.saveasflag==1:      # this flag will be 1 only after open or create image function is used bcoz only after that we need save_as
            if self.filepath:
                filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file", defaultextension = "*.jpg",
                                                filetypes = (("all files","*.*"),
                                                             ("jpg files", "*.jpg"),
                                                             ("jpeg file", "*.jpeg"),
                                                             ("png file", "*.png"),
                                                             ("gif file", "*.gif"),
                                                             ("tiff file", "*.tiff"),
                                                             ("bmp file", "*.bmp"),
                                                             ("webp file", "*.webp")
                                                             ))
                self.pillowimage.save(filename)
                #print('save as done')
            else:
                filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",  defaultextension = "*.jpg",
                                                 filetypes = (("all files","*.*"),
                                                             ("jpg files", "*.jpg"),
                                                             ("jpeg file", "*.jpeg"),
                                                             ("png file", "*.png"),
                                                             ("gif file", "*.gif"),
                                                             ("tiff file", "*.tiff"),
                                                             ("bmp file", "*.bmp"),
                                                             ("webp file", "*.webp")))
                self.image1.save(filename)
                #print('save as done')


    def createimage(self):
        self.canvas.delete('all')  # need to clear canvas if someone wants to create another image after drawing something
        self.image1 = PIL.Image.new("RGB", (1250, 650), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image1)

        # do the Tkinter canvas drawings (visible)
        # self.canvas.create_line([0, 100, 200, 100], fill='green')

        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.saveasflag = 1

    def paint(self,event):
        # python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw.line([x1, y1, x2, y2], fill="black", width=5)


class Menubar:
    def __init__(self,App):
        menubar = Menu()
        App.app.config(menu=menubar)

        menuoption1 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menuoption1)
        menuoption1.add_command(label="Create", command=App.createimage)
        menuoption1.add_command(label="Open", command=App.open_photo)
        menuoption1.add_command(label="Save", command=App.save)
        menuoption1.add_command(label="Save as", command=App.save_as)
        menuoption1.add_command(label="Exit", command=exit)   # if u write exit(), window will be close in no time after it appear,
                                                              # bcoz with exit() instead of exit cause function to invoke instantly


        menuoption2 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=menuoption2)
        menuoption2.add_command(label="About Developer", command=App.developerMsgBox)
        menuoption2.add_command(label="Version", command=App.versionMsgBox)

        menuoption3 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Rotate", menu=menuoption3)
        menuoption3.add_command(label="Rotate by 90", command=App.rotateby90)
        menuoption3.add_command(label="Rotate by 45", command=App.rotateby45)

        menuoption5 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Color Effects", menu=menuoption5)
        menuoption5.add_command(label="GrayScale", command=App.grayscale)
        menuoption5.add_command(label="Bluish", command=App.bluish)
        menuoption5.add_command(label="Olddays", command=App.olddays)
        menuoption5.add_command(label="Pinkish", command=App.pinkish)
        menuoption5.add_command(label="BW", command=App.bw)

        menuoption6 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Brightness", menu=menuoption6)
        menuoption6.add_command(label="Increase", command=App.brightnessIncrease)
        menuoption6.add_command(label="Decrease", command=App.brightnessDecrease)

        menuoption7 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Contrast", menu=menuoption7)
        menuoption7.add_command(label="Increase", command=App.contrastIncrease)
        menuoption7.add_command(label="Decrease", command=App.contrastDecrease)

        menuoption8 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Temperature", menu=menuoption8)
        menuoption8.add_command(label="Increase", command=App.tempIncrease)
        menuoption8.add_command(label="Decrease", command=App.tempDecrease)

        menuoption9 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Resize", menu=menuoption9)
        menuoption9.add_command(label="Enter WxH", command=App.resize)
        menuoption9.add_command(label="How to Resize", command=App.howtoresize)


        menuoptionL = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Reset", menu=menuoptionL)
        menuoptionL.add_command(label="Reset All", command=App.reset)






root = Tk()
window = App(root)
root.mainloop()

