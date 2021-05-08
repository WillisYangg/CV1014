#Creating User Interface, input Buttons and tabs

import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import PIL
from PIL import ImageTk, Image
import math

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title('Where are the parks?')
root.geometry('1300x1300')
style = ttk.Style()

#Create home_screen with 3 tabs
home_screen = Frame(root)
map_screen = Frame(root)
region_screen = Frame(root, bg = 'white')
activities_screen = Frame(root, bg ='white')

for frame in (home_screen, map_screen, region_screen, activities_screen):
    frame.place(x=0, y=0, height=1500, width=1500)
    
#Background Image
background_image = ImageTk.PhotoImage(Image.open('coverphoto.png'))
background_label = Label(home_screen, image=background_image)
background_label.place(x=0, y=0, height=900, width=1300)
background_image2 = ImageTk.PhotoImage(Image.open('sgmaps.png'))
background_label2 = Label(map_screen, image=background_image2)
background_label2.place(x=-198, y=0, height=700, width=1400)

background_image100 = ImageTk.PhotoImage(Image.open('background3.png'))
background_label = Label(region_screen, image= background_image100)
background_label.place(x=0, y=0, height=900,width=1300)

#Create listbox in map_screen
listbox = Listbox(map_screen, width = 30, height =17)
listbox.pack(pady = 100)
listbox.place(x=1000, y=100)

#Buttons
map_info = Button(home_screen, text="View Map", fg='black', bg='alice blue', command=lambda: raise_frame(map_screen)) \
      .place (x=250, y=510, height=50, width=250)
region_info = Button(home_screen, text="Region and Type", fg='black', bg='alice blue',\
              command=lambda: raise_frame(region_screen)).place(x=575, y=510, height=50, width=250)
activities_info = Button(home_screen, text= "Activities", fg='black', bg='alice blue',\
                          command=lambda: raise_frame(activities_screen)).place(x=900, y=510, height=50, width=250)
goback = Button(map_screen, text="Return", command=lambda: raise_frame(home_screen)) \
            .place(x=1050, y=0, height=50, width=250)
goback2 = Button(activities_screen, text="Return", command=lambda: raise_frame(home_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback3 = Button(region_screen, text="Return", command=lambda: raise_frame(home_screen))\
            .place(x=1050, y=0, height=50, width=250)
            
#time
def tick():
    time1 = time.strftime('%A, %Y/%m/%d\n %H:%M:%S')
    time2 = time.strftime('%A %Y/%m/%d %H:%M:%S')
    clock.configure(text= time1)
    clock2.configure(text= time2)
    clock3.configure(text= time2)
    clock4.configure(text= time2)
    clock.after(200, tick)
    
time_string = time.strftime('%A \n %Y/%m/%d \n %H:%M:%S')
clock = Label(home_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg='alice blue')
clock.place(x=0, y=5)
clock2 = Label(map_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg='alice blue')
clock2.place(x=550, y=640)
clock3 =Label(activities_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock3.place(x=0,y=5)
clock4 = Label(region_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock4.place(x=0, y=5)

tick()

#Creating Nparks list with coordinates for map
npark_list = [[375,400,'Chinese Garden'], [825,380, 'East Coast Park'],[545,180,'Admiralty Park'], \
              [655,360,'Bishan-AngMoKio Park'],[475,380,'Bukit Timah Nature Reserve'],\
              [705,500, 'Esplanade Park'], [545,500,'Fort Canning Park'], [725,550,'Gardens By The Bay'],\
              [595,310, 'Macritchie Reservoir'], [825,280,'Punggol Waterway Park'], [625, 460, ' Botanic Gardens'],\
              [875,430,'Bedok Reservoir'], [1045,430,'Changi Beach Park'], [465, 440,'Jurong Lake Gardens'],\
              [375,300,'Choa Chu Kang Park']]

for c in npark_list:
    l = Label(map_screen, text=c[2])
    l.place(x=c[0]-198, y=c[1])

#Moveable Widget(my location)
icon_img = ImageTk.PhotoImage(Image.open('location-small.png'))
iconlabel = Label(map_screen, image = icon_img)
icon_position = iconlabel.place(x=0,y=0)


#pythagoras theorem to calculate distance
def calculateDistance(x1, y1):
    park_list = [[375,400,'Chinese Garden'], [825,380, 'East Coast Park'],[545,180,'Admiralty Park'], \
              [655,360,'Bishan-AngMoKio Park'],[475,380,'Bukit Timah Nature Reserve'],\
              [705,500, 'Esplanade Park'], [545,500,'Fort Canning Park'], [725,550,'Gardens By The Bay'],\
              [595,310, 'Macritchie Reservoir'], [825,280,'Punggol Waterway Park'], [625, 460, ' Botanic Gardens'],\
              [875,430,'Bedok Reservoir'], [1045,430,'Changi Beach Park'], [465, 440,'Jurong Lake Gardens'],\
              [375,300,'Choa Chu Kang Park']]
        
    dist_dic = {}
    dist_list = []
    new_list = []

#input distance at the bottom of the map(box)
    for a in park_list:
        dist = round(math.sqrt((a[0]-198 - x1) ** 2 + (a[1] - y1) ** 2)*0.1, 0)
        #print(a[2], ': ', dist)
        dist_dic[a[2]] = dist
        sorted_dist_dic = sorted(dist_dic.items(), key=lambda x: x[1], reverse=False)
        
    for key, value in sorted_dist_dic:
        temp = [key,value]
        dist_list.append(temp)
  
    listbox.delete(0, END)  
    listbox.insert(END, 'Nearest Park from You! (in KM)') 
    listbox.insert(END, '')
    
    for b in dist_list:
        listbox.insert('end', b)
#moving widgets to calculate distance from where you are and updates rankings of locations from nearest to furthest
def move_up(event):
    #global iconlabel.place(x,y)
    iconlabel.place(x = iconlabel.winfo_x(), y = iconlabel.winfo_y()-10)
    map_screen.update()
    print('Current Location: ', iconlabel.winfo_x(), iconlabel.winfo_y())
    print(calculateDistance(iconlabel.winfo_x(), iconlabel.winfo_y()))
    #icon_position.update()
    #cood_update()
    
def move_right(event):
    #global iconlabel.place(x,y)
    iconlabel.place(x = iconlabel.winfo_x()+10, y = iconlabel.winfo_y())
    map_screen.update()
    print('Current Location: ', iconlabel.winfo_x(), iconlabel.winfo_y())
    print(calculateDistance(iconlabel.winfo_x(), iconlabel.winfo_y()))
    #icon_position.update()
    #cood_update()
    
def move_down(event):
    #global iconlabel.place(x,y)
    iconlabel.place(x = iconlabel.winfo_x(), y = iconlabel.winfo_y()+10)
    map_screen.update()
    print('Current Location: ', iconlabel.winfo_x(), iconlabel.winfo_y())
    print(calculateDistance(iconlabel.winfo_x(), iconlabel.winfo_y()))
    #icon_position.update()
    #cood_update()
    
def move_left(event):
    #global iconlabel.place(x,y)
    iconlabel.place(x = iconlabel.winfo_x()-10, y = iconlabel.winfo_y())
    map_screen.update()
    print('Current Location: ', iconlabel.winfo_x(), iconlabel.winfo_y())
    print(calculateDistance(iconlabel.winfo_x(), iconlabel.winfo_y()))
    #icon_position.update()
    #cood_update()

root.bind("<w>", move_up)
root.bind("<d>", move_right)
root.bind("<s>", move_down)
root.bind("<a>", move_left)

#Button

reg_screen = Frame(root, bg = 'white')
type_screen = Frame(root, bg = 'white')

goback = Button(reg_screen, text="Return", command=lambda: raise_frame(region_screen))\
            .place(x=1050, y=0, height=50, width=250)

south_screen = Frame(root, bg = 'white')
north_screen = Frame(root, bg = 'white')      
central_screen = Frame(root, bg = 'white')
east_screen = Frame(root, bg = 'white')
west_screen = Frame(root, bg = 'white')

nature_screen = Frame(root, bg = 'white')   
community_screen = Frame(root, bg = 'white')   
gardens_screen = Frame(root, bg = 'white')   
coastal_screen = Frame(root, bg = 'white')   
artsandheritage_screen = Frame(root, bg = 'white')      
riverine_screen = Frame(root, bg = 'white')

admiralty_screen = Frame(root, bg = 'white')
bukittimah_screen = Frame(root, bg = 'white')
bedok_screen = Frame(root, bg = 'white')
bishan_screen = Frame(root, bg = 'white')
choa_screen = Frame(root, bg = 'white')
chinesegarden_screen = Frame(root, bg = 'white')
botanic_screen = Frame(root, bg = 'white')
juronglake_screen = Frame(root, bg = 'white')
eastcoast_screen = Frame(root, bg = 'white')   
changibeach_screen = Frame(root, bg = 'white')
esplanade_screen = Frame(root, bg = 'white')
fortcanning_screen = Frame(root, bg = 'white')
gardensby_screen = Frame(root, bg = 'white')
macritchie_screen = Frame(root, bg = 'white')
punggol_screen = Frame(root, bg = 'white')

admiralty2_screen = Frame(root, bg = 'white')
bukittimah2_screen = Frame(root, bg = 'white')
bedok2_screen = Frame(root, bg = 'white')
bishan2_screen = Frame(root, bg = 'white')
choa2_screen = Frame(root, bg = 'white')
chinesegarden2_screen = Frame(root, bg = 'white')
botanic2_screen = Frame(root, bg = 'white')
juronglake2_screen = Frame(root, bg = 'white')
eastcoast2_screen = Frame(root, bg = 'white')   
changibeach2_screen = Frame(root, bg = 'white')
esplanade2_screen = Frame(root, bg = 'white')
fortcanning2_screen = Frame(root, bg = 'white')
gardensby2_screen = Frame(root, bg = 'white')
macritchie2_screen = Frame(root, bg = 'white')
punggol2_screen = Frame(root, bg = 'white')

#background 1
for frame in (reg_screen, type_screen, south_screen, north_screen, central_screen, east_screen, west_screen, nature_screen, community_screen, gardens_screen, coastal_screen, artsandheritage_screen, riverine_screen):
    frame.place(x=0, y=0, height=1500, width=1500)
    
background_image3 = ImageTk.PhotoImage(Image.open('background3.png'))
background_label = Label(reg_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(type_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(south_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(north_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(central_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(east_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(west_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(nature_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(community_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(gardens_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(coastal_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(artsandheritage_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)
background_label = Label(riverine_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)

#background 2

for frame in (admiralty_screen, bukittimah_screen, bedok_screen, bishan_screen, choa_screen, chinesegarden_screen, botanic_screen, juronglake_screen, eastcoast_screen, changibeach_screen, esplanade_screen, fortcanning_screen, gardensby_screen, macritchie_screen, punggol_screen, admiralty2_screen, bukittimah2_screen, bedok2_screen, bishan2_screen, choa2_screen, chinesegarden2_screen, botanic2_screen, juronglake2_screen, eastcoast2_screen, changibeach2_screen, esplanade2_screen, fortcanning2_screen, gardensby2_screen, macritchie2_screen, punggol2_screen):
    frame.place(x=0, y=0, height=1500, width=1500)
background_image4 = ImageTk.PhotoImage(Image.open('admiraltypark.png'))
background_label = Label(admiralty_screen, image= background_image4)
background_label.place(x=0, y=0, height=900,width=1300)

background_image5 = ImageTk.PhotoImage(Image.open('bukittimah.png'))
background_label = Label(bukittimah_screen, image= background_image5)
background_label.place(x=0, y=0, height=900,width=1300)

background_image6 = ImageTk.PhotoImage(Image.open('bedok.png'))
background_label = Label(bedok_screen, image= background_image6)
background_label.place(x=0, y=0, height=900,width=1300)

background_image7 = ImageTk.PhotoImage(Image.open('bishanangmaokio.png'))
background_label = Label(bishan_screen, image= background_image7)
background_label.place(x=0, y=0, height=900,width=1300)

background_image8 = ImageTk.PhotoImage(Image.open('choachukang.png'))
background_label = Label(choa_screen, image= background_image8)
background_label.place(x=0, y=0, height=900,width=1300)

background_image9 = ImageTk.PhotoImage(Image.open('chinesegardens.png'))
background_label = Label(chinesegarden_screen, image= background_image9)
background_label.place(x=0, y=0, height=900,width=1300)

background_image10 = ImageTk.PhotoImage(Image.open('botanicgarden.png'))
background_label = Label(botanic_screen, image= background_image10)
background_label.place(x=0, y=0, height=900,width=1300)

background_image11 = ImageTk.PhotoImage(Image.open('juronglakegardens.png'))
background_label = Label(juronglake_screen, image= background_image11)
background_label.place(x=0, y=0, height=900,width=1300)

background_image12 = ImageTk.PhotoImage(Image.open('eastcoastpark.png'))
background_label = Label(eastcoast_screen, image= background_image12)
background_label.place(x=0, y=0, height=900,width=1300)

background_image13 = ImageTk.PhotoImage(Image.open('changibeachpark.png'))
background_label = Label(changibeach_screen, image= background_image13)
background_label.place(x=0, y=0, height=900,width=1300)

background_image14 = ImageTk.PhotoImage(Image.open('esplanadepark.png'))
background_label = Label(esplanade_screen, image= background_image14)
background_label.place(x=0, y=0, height=900,width=1300)

background_image15 = ImageTk.PhotoImage(Image.open('fortcanningpark.png'))
background_label = Label(fortcanning_screen, image= background_image15)
background_label.place(x=0, y=0, height=900,width=1300)

background_image16 = ImageTk.PhotoImage(Image.open('gardensbythebay.png'))
background_label = Label(gardensby_screen, image= background_image16)
background_label.place(x=0, y=0, height=900,width=1300)

background_image17 = ImageTk.PhotoImage(Image.open('macritchie.png'))
background_label = Label(macritchie_screen, image= background_image17)
background_label.place(x=0, y=0, height=900,width=1300)

background_image18 = ImageTk.PhotoImage(Image.open('punggol.png'))
background_label = Label(punggol_screen, image= background_image18)
background_label.place(x=0, y=0, height=900,width=1300)

background_image19 = ImageTk.PhotoImage(Image.open('admiraltypark.png'))
background_label = Label(admiralty2_screen, image= background_image19)
background_label.place(x=0, y=0, height=900,width=1300)

background_image20 = ImageTk.PhotoImage(Image.open('bukittimah.png'))
background_label = Label(bukittimah2_screen, image= background_image20)
background_label.place(x=0, y=0, height=900,width=1300)

background_image21 = ImageTk.PhotoImage(Image.open('bedok.png'))
background_label = Label(bedok2_screen, image= background_image21)
background_label.place(x=0, y=0, height=900,width=1300)

background_image22 = ImageTk.PhotoImage(Image.open('bishanangmaokio.png'))
background_label = Label(bishan2_screen, image= background_image22)
background_label.place(x=0, y=0, height=900,width=1300)

background_image23 = ImageTk.PhotoImage(Image.open('choachukang.png'))
background_label = Label(choa2_screen, image= background_image23)
background_label.place(x=0, y=0, height=900,width=1300)

background_image24 = ImageTk.PhotoImage(Image.open('chinesegardens.png'))
background_label = Label(chinesegarden2_screen, image= background_image24)
background_label.place(x=0, y=0, height=900,width=1300)

background_image25 = ImageTk.PhotoImage(Image.open('botanicgarden.png'))
background_label = Label(botanic2_screen, image= background_image25)
background_label.place(x=0, y=0, height=900,width=1300)

background_image26 = ImageTk.PhotoImage(Image.open('juronglakegardens.png'))
background_label = Label(juronglake2_screen, image= background_image26)
background_label.place(x=0, y=0, height=900,width=1300)

background_image27 = ImageTk.PhotoImage(Image.open('eastcoastpark.png'))
background_label = Label(eastcoast2_screen, image= background_image27)
background_label.place(x=0, y=0, height=900,width=1300)

background_image28 = ImageTk.PhotoImage(Image.open('changibeachpark.png'))
background_label = Label(changibeach2_screen, image= background_image28)
background_label.place(x=0, y=0, height=900,width=1300)

background_image29 = ImageTk.PhotoImage(Image.open('esplanadepark.png'))
background_label = Label(esplanade2_screen, image= background_image29)
background_label.place(x=0, y=0, height=900,width=1300)

background_image30 = ImageTk.PhotoImage(Image.open('fortcanningpark.png'))
background_label = Label(fortcanning2_screen, image= background_image30)
background_label.place(x=0, y=0, height=900,width=1300)

background_image31 = ImageTk.PhotoImage(Image.open('gardensbythebay.png'))
background_label = Label(gardensby2_screen, image= background_image31)
background_label.place(x=0, y=0, height=900,width=1300)

background_image32 = ImageTk.PhotoImage(Image.open('macritchie.png'))
background_label = Label(macritchie2_screen, image= background_image32)
background_label.place(x=0, y=0, height=900,width=1300)

background_image33 = ImageTk.PhotoImage(Image.open('punggol.png'))
background_label = Label(punggol2_screen, image= background_image33)
background_label.place(x=0, y=0, height=900,width=1300)


def tick():
    time1 = time.strftime('%A, %Y%m/%d\n %H:%M:%S')
    time2 = time.strftime('%A %Y/%m/%d %H:%M:%S')
    time3 = time.strftime('%A %Y/%m/%d %H:%M:%S')
    clock.configure(text= time2)
    clock18.configure(text= time2)
    clock6.configure(text= time2)
    clock7.configure(text= time2)
    clock8.configure(text= time2)
    clock9.configure(text= time2)
    clock10.configure(text= time2)
    clock11.configure(text= time2)
    clock12.configure(text= time2)
    clock13.configure(text= time2)
    clock14.configure(text= time2)
    clock15.configure(text= time2)
    clock16.configure(text= time2)
    clock17.configure(text= time2)
    clock.after(200, tick)
time_string = time.strftime('%A \n %Y/%m/%d \n %H:%M:%S')    
clock18 = Label(reg_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg='alice blue')
clock18.place(x=0, y=5)
clock6 =Label(type_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock6.place(x=0,y=5)
clock7 = Label(north_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock7.place(x=0, y=5)
clock8 = Label(south_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock8.place(x=0, y=5)
clock9 = Label(central_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock9.place(x=0, y=5)
clock10 = Label(east_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock10.place(x=0, y=5)
clock11 = Label(west_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock11.place(x=0, y=5)
clock12 = Label(nature_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock12.place(x=0, y=5)
clock13 = Label(community_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock13.place(x=0, y=5)
clock14 = Label(gardens_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock14.place(x=0, y=5)
clock15 = Label(coastal_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock15.place(x=0, y=5)
clock16 = Label(artsandheritage_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock16.place(x=0, y=5)
clock17 = Label(riverine_screen, font=('Comic Sans MS', 15, 'bold'), fg = 'black', bg= 'alice blue')
clock17.place(x=0, y=5)

#region and type
reg_info = Button(region_screen, text="Region", fg='black', bg='alice blue', command=lambda: raise_frame(reg_screen)) \
    .place(x=300, y=510, height=50, width=250)
type_info = Button(region_screen, text= "Type", fg='black', bg='alice blue', command=lambda: raise_frame(type_screen)) \
    .place(x=800, y=510, height=50, width=250)
goback = Button(reg_screen, text="Return", fg='black', bg='alice blue', command=lambda: raise_frame(region_screen)) \
            .place(x=1050, y=0, height=50, width=250)
goback = Button(type_screen, text="Return", fg='black', bg='alice blue', command=lambda: raise_frame(region_screen))\
            .place(x=1050, y=0, height=50, width=250)
            
#region
south_info = Button(reg_screen, text="South", fg='black', bg='alice blue',\
             command=lambda: raise_frame(south_screen)).place(x=50, y=510, height=50, width=200)
north_info = Button(reg_screen, text="North", fg='black', bg='alice blue',\
             command=lambda: raise_frame(north_screen)).place(x=300, y=510, height=50, width=200)
central_info = Button(reg_screen, text="Central", fg='black', bg='alice blue',\
             command=lambda: raise_frame(central_screen)).place(x=550, y=510, height=50, width=200)  
east_info = Button(reg_screen, text="East", fg='black', bg='alice blue',\
             command=lambda: raise_frame(east_screen)).place(x=800, y=510, height=50, width=200)
west_info = Button(reg_screen, text="West", fg='black', bg='alice blue',\
             command=lambda: raise_frame(west_screen)).place(x=1050, y=510, height=50, width=200)

#type
nature_info = Button(type_screen, text="Nature", fg='black', bg='alice blue',\
             command=lambda: raise_frame(nature_screen)).place(x=25, y=510, height=50, width=150)
community_info = Button(type_screen, text="Community", fg='black', bg='alice blue',\
             command=lambda: raise_frame(community_screen)).place(x=245, y=510, height=50, width=150)
gardens_info = Button(type_screen, text="Gardens", fg='black', bg='alice blue',\
             command=lambda: raise_frame(gardens_screen)).place(x=465, y=510, height=50, width=150)
coastal_info = Button(type_screen, text="Coastal", fg='black', bg='alice blue',\
             command=lambda: raise_frame(coastal_screen)).place(x=685, y=510, height=50, width=150)
artsandheritage_info = Button(type_screen, text="Arts and Heritage", fg='black', bg='alice blue',\
             command=lambda: raise_frame(artsandheritage_screen)).place(x=905, y=510, height=50, width=150)
riverine_info = Button(type_screen, text="Riverine", fg='black', bg='alice blue',\
             command=lambda: raise_frame(riverine_screen)).place(x=1125, y=510, height=50, width=150)


goback = Button(south_screen, text="Return", command=lambda: raise_frame(reg_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(north_screen, text="Return", command=lambda: raise_frame(reg_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(central_screen, text="Return", command=lambda: raise_frame(reg_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(east_screen, text="Return", command=lambda: raise_frame(reg_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(west_screen, text="Return", command=lambda: raise_frame(reg_screen))\
            .place(x=1050, y=0, height=50, width=250)  
goback = Button(nature_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(community_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(gardens_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(coastal_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(artsandheritage_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(riverine_screen, text="Return", command=lambda: raise_frame(type_screen))\
            .place(x=1050, y=0, height=50, width=250) 
            
#region part
admiralty_info = Button(south_screen, text="Admiralty Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(admiralty_screen)).place(x=140, y=510, height=50, width=150)   
choa_info = Button(south_screen, text="Choa Chu Kang Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(choa_screen)).place(x=430, y=510, height=50, width=150)
bukittimah_info = Button(south_screen, text="Bukit Timah Nature Reserve", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bukittimah_screen)).place(x=720, y=510, height=50, width=150)   
macritchie_info = Button(south_screen, text="MacRitchie Reservoir Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(macritchie_screen)).place(x=1010, y=510, height=50, width=150)
bishan_info = Button(north_screen, text="Bishan-Ang Mao Kio Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bishan_screen)).place(x=200, y=510, height=50, width=150)
punggol_info = Button(north_screen, text="Punggol Waterway Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(ounggol_screen)).place(x=950, y=510, height=50, width=150)
esplanade_info = Button(central_screen, text="Esplanade", fg='black', bg='alice blue',\
             command=lambda: raise_frame(esplanade_screen)).place(x=140, y=510, height=50, width=150)
fortcanning_info = Button(central_screen, text="Fort Canning Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(fortcanning_screen)).place(x=430, y=510, height=50, width=150)
gardensby_info = Button(central_screen, text="Gardens by The Bay", fg='black', bg='alice blue',\
             command=lambda: raise_frame(gardensby_screen)).place(x=720, y=510, height=50, width=150)
botanic_info = Button(central_screen, text="Singapore Botanic Garden", fg='black', bg='alice blue',\
             command=lambda: raise_frame(botanic_screen)).place(x=1010, y=510, height=50, width=150)
eastcoast_info = Button(east_screen, text="East Coast Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(eastcoast_screen)).place(x=175, y=510, height=50, width=150)
changibeach_info = Button(east_screen, text="Changi Beach Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(changibeach_screen)).place(x=575, y=510, height=50, width=150)
bedok_info = Button(east_screen, text="Bedok Reservoir", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bedok_screen)).place(x=975, y=510, height=50, width=150)
chinesegarden_info = Button(west_screen, text="Chinese Garden", fg='black', bg='alice blue',\
             command=lambda: raise_frame(chinesegarden_screen)).place(x=200, y=510, height=50, width=150)
juronglake_info = Button(west_screen, text="Jurong Lake Gardens", fg='black', bg='alice blue',\
             command=lambda: raise_frame(juronglake_screen)).place(x=950, y=510, height=50, width=150)

goback = Button(admiralty_screen, text="Return", command=lambda: raise_frame(south_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(choa_screen, text="Return", command=lambda: raise_frame(south_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bukittimah_screen, text="Return", command=lambda: raise_frame(south_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(macritchie_screen, text="Return", command=lambda: raise_frame(south_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bishan_screen, text="Return", command=lambda: raise_frame(north_screen))\
            .place(x=1050, y=0, height=50, width=250)  
goback = Button(punggol_screen, text="Return", command=lambda: raise_frame(north_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(esplanade_screen, text="Return", command=lambda: raise_frame(central_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(fortcanning_screen, text="Return", command=lambda: raise_frame(central_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(gardensby_screen, text="Return", command=lambda: raise_frame(central_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(botanic_screen, text="Return", command=lambda: raise_frame(central_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(eastcoast_screen, text="Return", command=lambda: raise_frame(east_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(changibeach_screen, text="Return", command=lambda: raise_frame(east_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bedok_screen, text="Return", command=lambda: raise_frame(east_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(chinesegarden_screen, text="Return", command=lambda: raise_frame(west_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(juronglake_screen, text="Return", command=lambda: raise_frame(west_screen))\
            .place(x=1050, y=0, height=50, width=250)
    
#type part
admiralty2_info = Button(nature_screen, text="Admiralty Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(admiralty2_screen)).place(x=175, y=510, height=50, width=150)   
choa2_info = Button(community_screen, text="Choa Chu Kang Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(choa2_screen)).place(x=950, y=510, height=50, width=150)
bukittimah2_info = Button(nature_screen, text="Bukit Timah Nature Reserve", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bukittimah2_screen)).place(x=575, y=510, height=50, width=150)   
macritchie2_info = Button(riverine_screen, text="MacRitchie Reservoir Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(macritchie2_screen)).place(x=200, y=510, height=50, width=150)
bishan2_info = Button(community_screen, text="Bishan-Ang Mao Kio Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bishan2_screen)).place(x=200, y=510, height=50, width=150)
punggol2_info = Button(riverine_screen, text="Punggol Waterway Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(punggol2_screen)).place(x=950, y=510, height=50, width=150)
esplanade2_info = Button(artsandheritage_screen, text="Esplanade", fg='black', bg='alice blue',\
             command=lambda: raise_frame(esplanade2_screen)).place(x=175, y=510, height=50, width=150)
fortcanning2_info = Button(artsandheritage_screen, text="Fort Canning Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(fortcanning2_screen)).place(x=575, y=510, height=50, width=150)
gardensby2_info = Button(artsandheritage_screen, text="Gardens by The Bay", fg='black', bg='alice blue',\
             command=lambda: raise_frame(gardensby2_screen)).place(x=975, y=510, height=50, width=150)
botanic2_info = Button(gardens_screen, text="Singapore Botanic Garden", fg='black', bg='alice blue',\
             command=lambda: raise_frame(botanic2_screen)).place(x=575, y=510, height=50, width=150)
eastcoast2_info = Button(coastal_screen, text="East Coast Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(eastcoast2_screen)).place(x=200, y=510, height=50, width=150)
changibeach2_info = Button(coastal_screen, text="Changi Beach Park", fg='black', bg='alice blue',\
             command=lambda: raise_frame(changibeach2_screen)).place(x=950, y=510, height=50, width=150)
bedok2_info = Button(nature_screen, text="Bedok Reservoir", fg='black', bg='alice blue',\
             command=lambda: raise_frame(bedok2_screen)).place(x=975, y=510, height=50, width=150)
chinesegarden2_info = Button(gardens_screen, text="Chinese Garden", fg='black', bg='alice blue',\
             command=lambda: raise_frame(chinesegarden2_screen)).place(x=175, y=510, height=50, width=150)
juronglake2_info = Button(gardens_screen, text="Jurong Lake Gardens", fg='black', bg='alice blue',\
             command=lambda: raise_frame(juronglake2_screen)).place(x=975, y=510, height=50, width=150)

goback = Button(admiralty2_screen, text="Return", command=lambda: raise_frame(nature_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(choa2_screen, text="Return", command=lambda: raise_frame(community_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bukittimah2_screen, text="Return", command=lambda: raise_frame(nature_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(macritchie2_screen, text="Return", command=lambda: raise_frame(riverine_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bishan2_screen, text="Return", command=lambda: raise_frame(community_screen))\
            .place(x=1050, y=0, height=50, width=250)  
goback = Button(punggol2_screen, text="Return", command=lambda: raise_frame(riverine_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(esplanade2_screen, text="Return", command=lambda: raise_frame(artsandheritage_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(fortcanning2_screen, text="Return", command=lambda: raise_frame(artsandheritage_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(gardensby2_screen, text="Return", command=lambda: raise_frame(artsandheritage_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(botanic2_screen, text="Return", command=lambda: raise_frame(artsandheritage_screen))\
            .place(x=1050, y=0, height=50, width=250) 
goback = Button(eastcoast2_screen, text="Return", command=lambda: raise_frame(coastal_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(changibeach2_screen, text="Return", command=lambda: raise_frame(coastal_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(bedok2_screen, text="Return", command=lambda: raise_frame(nature_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(chinesegarden2_screen, text="Return", command=lambda: raise_frame(gardens_screen))\
            .place(x=1050, y=0, height=50, width=250)
goback = Button(juronglake2_screen, text="Return", command=lambda: raise_frame(gardens_screen))\
            .place(x=1050, y=0, height=50, width=250)

#Set background image
background_label = Label(activities_screen, image= background_image3)
background_label.place(x=0, y=0, height=900,width=1300)

#Return to main screen button
goback2 = Button(activities_screen, text="Return", command=lambda: raise_frame(home_screen))\
            .place(x=1050, y=0, height=50, width=250)

#Options list
options = [
    'Jogging',
    'Water Sports',
    'Hiking',
    'Cycling',
    'Sightseeing',
    'Nature',
    'Fishing'
]

#define function to clear previous selection
def clear():
    for widget in activities_screen.winfo_children():
        if widget != background_label:
            if widget != myCombo:
                widget.destroy()
                goback2 = Button(activities_screen, text="Return", command=lambda: raise_frame(home_screen))\
                    .place(x=1050, y=0, height=50, width=250)
                
#define function to show result according to selection
#results are shown in clickable buttons
def activity(event):
    if myCombo.get() == 'Jogging':
        clear()
        admiralty_button = Button(activities_screen, text="Admiralty Park", command=lambda: pop1())\
            .place(x=200, y=300, height=50, width=900)
        bishan_button = Button(activities_screen, text="Bishan-Ang Mo Kio Park", command=lambda: pop4())\
            .place(x=200, y=350, height=50, width=900)
        punggol_button = Button(activities_screen, text="Punggol Waterway Park", command=lambda: pop15())\
            .place(x=200, y=400, height=50, width=900)
        bedok_button = Button(activities_screen, text="Bedok Reservoir", command=lambda: pop3())\
            .place(x=200, y=450, height=50, width=900) 
    elif myCombo.get() == 'Water Sports':
        clear()
        eastcoast_button = Button(activities_screen, text="East Coast Park", command=lambda: pop9())\
            .place(x=200, y=300, height=50, width=900)
        macritchie_button = Button(activities_screen, text="Mac Ritchie Reservoir Park", command=lambda: pop14())\
            .place(x=200, y=350, height=50, width=900)
        bedok_button = Button(activities_screen, text="Bedok Reservoir", command=lambda: pop3())\
            .place(x=200, y=400, height=50, width=900)
    elif myCombo.get() == 'Hiking':
        clear()
        bukit_button = Button(activities_screen, text="Bukit Timah Nature Reserve", command=lambda: pop2())\
            .place(x=200, y=300, height=50, width=900)
        macritchie_button = Button(activities_screen, text="Mac Ritchie Reservoir Park", command=lambda: pop14())\
            .place(x=200, y=350, height=50, width=900)
    elif myCombo.get() == 'Cycling':
        clear()
        bukit_button = Button(activities_screen, text="Bukit Timah Nature Reserve", command=lambda: pop2())\
            .place(x=200, y=300, height=50, width=900)
        eastcoast_button = Button(activities_screen, text="East Coast Park", command=lambda: pop9())\
            .place(x=200, y=350, height=50, width=900)
        bedok_button = Button(activities_screen, text="Bedok Reservoir", command=lambda: pop3())\
            .place(x=200, y=400, height=50, width=900)
        changi_button = Button(activities_screen, text="Changi Beach Park", command=lambda: pop10())\
            .place(x=200, y=450, height=50, width=900)
        punggol_button = Button(activities_screen, text="Punggol Waterway Park", command=lambda: pop15())\
            .place(x=200, y=500, height=50, width=900)
    elif myCombo.get() == 'Sightseeing':
        clear()
        gardensby_button = Button(activities_screen, text="Gardens By The Bay", command=lambda: pop13())\
            .place(x=200, y=300, height=50, width=900)
        esplanade_button = Button(activities_screen, text="Esplanade", command=lambda: pop11())\
            .place(x=200, y=350, height=50, width=900)
    elif myCombo.get() == 'Nature':
        clear()
        chinesegarden_button = Button(activities_screen, text="Chinese Garden", command=lambda: pop6())\
            .place(x=200, y=300, height=50, width=900)
        fortcanningt_button = Button(activities_screen, text="Fort Canning Park", command=lambda: pop12())\
            .place(x=200, y=350, height=50, width=900)
        juronglake_button = Button(activities_screen, text="Jurong Lake Gardens", command=lambda: pop8())\
            .place(x=200, y=400, height=50, width=900)
        botanic_button = Button(activities_screen, text="Botanic Gardens", command=lambda: pop7())\
            .place(x=200, y=450, height=50, width=900)
        choa_button = Button(activities_screen, text="Choa Chu Kang Park", command=lambda: pop5())\
            .place(x=200, y=500, height=50, width=900)
    elif myCombo.get() == 'Fishing':
        clear()
        bedok_button = Button(activities_screen, text="Bedok Reservoir", command=lambda: pop3())\
            .place(x=200, y=300, height=50, width=900)
        changi_button = Button(activities_screen, text="Changi Beach Park", command=lambda: pop10())\
            .place(x=200, y=350, height=50, width=900)

#create pop up message for each park            
def pop1():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Admiralty Park')
    pop.geometry('600x600')
    
    adm_frame1 = Frame(pop)
    adm_frame1.pack()
    
    global background_image4
    background_image4 = Image.open('admiraltypark.png')
    background_image4 = background_image4.resize((520, 360), Image.ANTIALIAS)
    background_image4 = ImageTk.PhotoImage(background_image4)
    
    pop_label = Label(pop, text= "Admiralty Park")
                      
    pop_label.pack()
    
    background_label = Label(adm_frame1, image= background_image4)
    background_label.grid()
    
def pop2():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Bukit Timah Nature Reserve')
    pop.geometry('600x600')
    
    adm_frame2 = Frame(pop)
    adm_frame2.pack()
    
    global background_image5
    background_image5 = Image.open('bukittimah.png')
    background_image5 = background_image5.resize((520, 360), Image.ANTIALIAS)
    background_image5 = ImageTk.PhotoImage(background_image5)
    
    pop_label = Label(pop, text= "Bukit Timah Nature Reserve")
    pop_label.pack()
    
    background_label = Label(adm_frame2, image= background_image5)
    background_label.grid()
    
def pop3():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Bedok Reservoir')
    pop.geometry('600x600')
    
    adm_frame3 = Frame(pop)
    adm_frame3.pack()
    
    global background_image6
    background_image6 = Image.open('bedok.png')
    background_image6 = background_image6.resize((520, 360), Image.ANTIALIAS)
    background_image6 = ImageTk.PhotoImage(background_image6)
    
    pop_label = Label(pop, text= "Bedok Reservoir")
    pop_label.pack()
    
    background_label = Label(adm_frame3, image= background_image6)
    background_label.grid()
    
def pop4():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Bishan-Ang Mo Kio Park')
    pop.geometry('600x600')
    
    adm_frame4 = Frame(pop)
    adm_frame4.pack()
    
    global background_image7
    background_image7 = Image.open('bishanangmaokio.png')
    background_image7 = background_image7.resize((520, 360), Image.ANTIALIAS)
    background_image7 = ImageTk.PhotoImage(background_image7)
    
    pop_label = Label(pop, text= "Bishan-Ang Mo Kio Park")
    pop_label.pack()
    
    background_label = Label(adm_frame4, image= background_image7)
    background_label.grid()
    
def pop5():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Choa Chu Kang Park')
    pop.geometry('600x600')
    
    adm_frame5 = Frame(pop)
    adm_frame5.pack()
    
    global background_image8
    background_image8 = Image.open('choachukang.png')
    background_image8 = background_image8.resize((520, 360), Image.ANTIALIAS)
    background_image8 = ImageTk.PhotoImage(background_image8)
    
    pop_label = Label(pop, text= "Choa Chu Kang Park")
    pop_label.pack()
    
    background_label = Label(adm_frame5, image= background_image8)
    background_label.grid()
    
def pop6():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Chinese Garden')
    pop.geometry('600x600')
    
    adm_frame6 = Frame(pop)
    adm_frame6.pack()
    
    global background_image9
    background_image9 = Image.open('chinesegardens.png')
    background_image9 = background_image9.resize((520, 360), Image.ANTIALIAS)
    background_image9 = ImageTk.PhotoImage(background_image9)
    
    pop_label = Label(pop, text= "Chinese Garden")
    pop_label.pack()
    
    background_label = Label(adm_frame6, image= background_image9)
    background_label.grid()
    
def pop7():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Botanic Gardens')
    pop.geometry('600x600')
    
    adm_frame7 = Frame(pop)
    adm_frame7.pack()
    
    global background_image10
    background_image10 = Image.open('botanicgarden.png')
    background_image10 = background_image10.resize((520, 360), Image.ANTIALIAS)
    background_image10 = ImageTk.PhotoImage(background_image10)
    
    pop_label = Label(pop, text= "Botanic Gardens")
    pop_label.pack()
    
    background_label = Label(adm_frame7, image= background_image10)
    background_label.grid()
    
def pop8():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Jurong Lake Gardens')
    pop.geometry('600x600')
    
    adm_frame8 = Frame(pop)
    adm_frame8.pack()
    
    global background_image11
    background_image11 = Image.open('juronglakegardens.png')
    background_image11 = background_image11.resize((520, 360), Image.ANTIALIAS)
    background_image11 = ImageTk.PhotoImage(background_image11)
    
    pop_label = Label(pop, text= "Jurong Lake Gardens")
    pop_label.pack()
    
    background_label = Label(adm_frame8, image= background_image11)
    background_label.grid()
    
def pop9():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('East Coast Park')
    pop.geometry('600x600')
    
    adm_frame9 = Frame(pop)
    adm_frame9.pack()
    
    global background_image12
    background_image12 = Image.open('eastcoastpark.png')
    background_image12 = background_image12.resize((520, 360), Image.ANTIALIAS)
    background_image12 = ImageTk.PhotoImage(background_image12)
    
    pop_label = Label(pop, text= "East Coast Park")
    pop_label.pack()
    
    background_label = Label(adm_frame9, image= background_image12)
    background_label.grid()
    
def pop10():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Changi Beach Park')
    pop.geometry('600x600')
    
    adm_frame10 = Frame(pop)
    adm_frame10.pack()
    
    global background_image13
    background_image13 = Image.open('changibeachpark.png')
    background_image13 = background_image13.resize((520, 360), Image.ANTIALIAS)
    background_image13 = ImageTk.PhotoImage(background_image13)
    
    pop_label = Label(pop, text= "Changi Beach Park")
    pop_label.pack()
    
    background_label = Label(adm_frame10, image= background_image13)
    background_label.grid()
    
def pop11():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Esplanade Park')
    pop.geometry('600x600')
    
    adm_frame11 = Frame(pop)
    adm_frame11.pack()
    
    global background_image14
    background_image14 = Image.open('esplanadepark.png')
    background_image14 = background_image14.resize((520, 360), Image.ANTIALIAS)
    background_image14 = ImageTk.PhotoImage(background_image14)
    
    pop_label = Label(pop, text= "Esplanade Park")
    pop_label.pack()
    
    background_label = Label(adm_frame11, image= background_image14)
    background_label.grid()
    
def pop12():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Fort Canning Park')
    pop.geometry('600x600')
    
    adm_frame12 = Frame(pop)
    adm_frame12.pack()
    
    global background_image15
    background_image15 = Image.open('fortcanningpark.png')
    background_image15 = background_image15.resize((520, 360), Image.ANTIALIAS)
    background_image15 = ImageTk.PhotoImage(background_image15)
    
    pop_label = Label(pop, text= "Fort Canning Park")
    pop_label.pack()
    
    background_label = Label(adm_frame12, image= background_image15)
    background_label.grid()
    
def pop13():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Gardens By The Bay')
    pop.geometry('600x600')
    
    adm_frame13 = Frame(pop)
    adm_frame13.pack()
    
    global background_image16
    background_image16 = Image.open('gardensbythebay.png')
    background_image16 = background_image16.resize((520, 360), Image.ANTIALIAS)
    background_image16 = ImageTk.PhotoImage(background_image16)
    
    pop_label = Label(pop, text= "Gardens By The Bay")
    pop_label.pack()
    
    background_label = Label(adm_frame13, image= background_image16)
    background_label.grid()
    
def pop14():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Mac Ritchie Reservoir Park')
    pop.geometry('600x600')
    
    adm_frame14 = Frame(pop)
    adm_frame14.pack()
    
    global background_image17
    background_image17 = Image.open('macritchie.png')
    background_image17= background_image17.resize((520, 360), Image.ANTIALIAS)
    background_image17 = ImageTk.PhotoImage(background_image17)
    
    pop_label = Label(pop, text= "Mac Ritchie Reservoir Park")
    pop_label.pack()
    
    background_label = Label(adm_frame14, image= background_image17)
    background_label.grid()
    
def pop15():
    global pop
    pop = Toplevel(activities_screen)
    pop.title('Punggol Waterway Park')
    pop.geometry('600x600')
    
    adm_frame15 = Frame(pop)
    adm_frame15.pack()
    
    global background_image18
    background_image18 = Image.open('punggol.png')
    background_image18 = background_image18.resize((520, 360), Image.ANTIALIAS)
    background_image18 = ImageTk.PhotoImage(background_image18)
    
    pop_label = Label(pop, text= "Punggol Waterway Park")
    pop_label.pack()
    
    background_label = Label(adm_frame15, image= background_image18)
    background_label.grid()
    
#create combobox         
myCombo = ttk.Combobox(activities_screen, justify='center', value=options)
myCombo.set('Choose your activity!')
myCombo.bind('<<ComboboxSelected>>', activity)
myCombo.grid()
myCombo.place(x=525, y=200, height=50, width=250)
myCombo['state'] = 'readonly'

tick()
raise_frame(home_screen)
root.mainloop()










