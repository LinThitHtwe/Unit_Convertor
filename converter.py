from tkinter import *
from tkinter.ttk import Combobox, Notebook 
import math
#hello

def convertLn():
    unit1 = UnitListbox1.get()
    unit2 = UnitListbox2.get()

    num = int(enternum.get())

    try:
        #mm
        if unit1 == "mm" and unit2 == "cm":
            ans = float(num)/10
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num)/1000
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num)/1000000
        elif unit1 == "mm" and unit2 == "inch":
            ans = float(num)*0.0393
        elif unit1 == "mm" and unit2 == "ft":
            ans = float(num)*0.00328
        elif unit1 == "mm" and unit2 == "yard":
            ans = float(num)*0.00109
        elif unit1 == "mm" and unit2 == "mile":
            ans = float(num)*0.00000062137

        #cm
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num)*10
        elif unit1 == "cm" and unit2 == "m":
            ans = float(num)/100
        elif unit1 == "cm" and unit2 == "km":
            ans = float(num)/100000
        elif unit1 == "cm" and unit2 == "inch":
            ans = float(num)*0.3937
        elif unit1 == "cm" and unit2 == "ft":
            ans = float(num)*0.0328
        elif unit1 == "cm" and unit2 == "yard":
            ans = float(num)*0.0109
        elif unit1 == "cm" and unit2 == "mile":
            ans = float(num)*0.0000062137

        #m    
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num)*1000
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num)*100
        elif unit1 == "m" and unit2 == "km":
            ans = float(num)/1000
        elif unit1 == "m" and unit2 == "inch":
            ans = float(num)*39.37
        elif unit1 == "m" and unit2 == "ft":
            ans = float(num)*3.280839
        elif unit1 == "m" and unit2 == "yard":
            ans = float(num)*1.0936
        elif unit1 == "m" and unit2 == "mile":
            ans = float(num)*0.00062136

        #km
        elif unit1 == "km" and unit2 == "mm":
            ans = float(num)*1000000
        elif unit1 == "km" and unit2 == "cm":
            ans = float(num)*100000
        elif unit1 == "km" and unit2 == "m":
            ans = float(num)*1000
        elif unit1 == "km" and unit2 == "inch":
            ans = float(num)*39370.07
        elif unit1 == "km" and unit2 == "ft":
            ans = float(num)*3280.83
        elif unit1 == "km" and unit2 == "yard":
            ans = float(num)*1093.61
        elif unit1 == "km" and unit2 == "mile":
            ans = float(num)*0.621368

        #inch
        elif unit1 == "inch" and unit2 == "mm":
            ans = float(num)*25.4
        elif unit1 == "inch" and unit2 == "cm":
            ans = float(num)*2.54
        elif unit1 == "inch" and unit2 == "m":
            ans = float(num)*0.0254
        elif unit1 == "inch" and unit2 == "km":
            ans = float(num)*0.0000254
        elif unit1 == "inch" and unit2 == "ft":
            ans = float(num)*0.083333
        elif unit1 == "inch" and unit2 == "yard":
            ans = float(num)*0.02777
        elif unit1 == "inch" and unit2 == "mile":
            ans = float(num)*0.00001578

        #ft
        elif unit1 == "ft" and unit2 == "mm":
            ans = float(num)*304.8
        elif unit1 == "ft" and unit2 == "cm":
            ans = float(num)*30.48
        elif unit1 == "ft" and unit2 == "m":
            ans = float(num)*0.3048
        elif unit1 == "ft" and unit2 == "km":
            ans = float(num)*0.0003048
        elif unit1 == "ft" and unit2 == "inch":
            ans = float(num)*12
        elif unit1 == "ft" and unit2 == "yard":
            ans = float(num)*0.3333333
        elif unit1 == "ft" and unit2 == "mile":
            ans = float(num)*0.0001893

        #yard
        elif unit1 == "yard" and unit2 == "mm":
            ans = float(num)*914.4
        elif unit1 == "yard" and unit2 == "cm":
            ans = float(num)*91.44
        elif unit1 == "yard" and unit2 == "m":
            ans = float(num)*0.9144
        elif unit1 == "yard" and unit2 == "km":
            ans = float(num)*0.0009144
        elif unit1 == "yard" and unit2 == "inch":
            ans = float(num)*36
        elif unit1 == "yard" and unit2 == "ft":
            ans = float(num)*3
        elif unit1 == "yard" and unit2 == "mile":
            ans = float(num)*0.0005682

        #mile
        elif unit1 == "mile" and unit2 == "mm":
            ans = float(num)*1609350
        elif unit1 == "mile" and unit2 == "cm":
            ans = float(num)*160935
        elif unit1 == "mile" and unit2 == "m":
            ans = float(num)*1609.35
        elif unit1 == "mile" and unit2 == "km":
            ans = float(num)*1.60935
        elif unit1 == "mile" and unit2 == "inch":
            ans = float(num)*63360.236
        elif unit1 == "mile" and unit2 == "ft":
            ans = float(num)*5280.0197
        elif unit1 == "mile" and unit2 == "yard":
            ans = float(num)*1760.0066

        #same
        elif unit1=='mm' and unit2 == 'mm':
            ans= num
        elif unit1=='cm' and unit2 == 'cm':
            ans= num
        elif unit1=='m' and unit2 == 'm':
            ans= num
        elif unit1=='km' and unit2 == 'km':
            ans= num
        elif unit1=='inch' and unit2 == 'inch':
            ans= num
        elif unit1=='ft' and unit2 == 'ft':
            ans= num
        elif unit1=='yard' and unit2 == 'yard':
            ans= num
        elif unit1=='mile' and unit2 == 'mile':
            ans= num

        AnswerLength.config(text=str(ans))
        
    except SyntaxError:
        AnswerLength.config(text='SyntaxError!')
    except:
        AnswerLength.config(text='Something wrong')



def convertTemp():
    temp1 = UnitListbox3.get()
    temp2 = UnitListbox4.get()
    
    num = int(enternum.get())

    try:
        if temp1=='Celsius' and temp2=='Kelvin':
            ans = float(num)*274.15
        elif temp1=='Celsius' and temp2=='Fahrenheit':
            ans = float(num)*33.8
        elif temp1=='Celsius' and temp2=='Celsius':
            ans = num
        elif temp1=='Kelvin' and temp2=='Celsius':
            ans = float(num)*-272.15
        elif temp1=='Kelvin' and temp2=='Fahrenheit':
            ans = float(num)*-457.87
        elif temp1=='Kelvin' and temp2=='Kelvin':
            ans = num
        elif temp1=='Fahrenheit' and temp2=='Celsius':
            ans = float(num)*-17.2222
        elif temp1=='Fahrenheit' and temp2=='Kelvin':
            ans = float(num)*255.92778
        elif temp1=='Fahrenheit' and temp2=='Fahrenheit':
            ans = num

        AnswerLength2.config(text=str(ans))
    except:
        AnswerLength2.config(text='Something wrong')

def convertWeight():

    weight1 = UnitListbox5.get()
    weight2 = UnitListbox6.get()
    
    num = int(enternum.get())

    try:
        #mg
        if weight1=='mg' and weight2=='g':
            ans = float(num)*0.001
        elif weight1=='mg' and weight2=='kg':
            ans = float(num)*0.000001
        elif weight1=='mg' and weight2=='lb':
            ans = float(num)*0.0000022046
        elif weight1=='mg' and weight2=='oz':
            ans = float(num)*0.000035274
        elif weight1=='mg' and weight2=='mg':
            ans = num

        #g
        elif weight1=='g' and weight2=='mg':
            ans = float(num)*1000
        elif weight1=='g' and weight2=='kg':
            ans = float(num)*0.001
        elif weight1=='g' and weight2=='lb':
            ans = float(num)*0.0022046244
        elif weight1=='g' and weight2=='oz':
            ans = float(num)*0.0352739907
        elif weight1=='g' and weight2=='g':
            ans = num
        
        #kg
        elif weight1=='kg' and weight2=='mg':
            ans = float(num)*1000000
        elif weight1=='kg' and weight2=='g':
            ans = float(num)*1000
        elif weight1=='kg' and weight2=='lb':
            ans = float(num)*2.2046244202
        elif weight1=='kg' and weight2=='oz':
            ans = float(num)*35.273990723
        elif weight1=='kg' and weight2=='kg':
            ans = num

        #lb
        elif weight1=='lb' and weight2=='mg':
            ans = float(num)*453592
        elif weight1=='lb' and weight2=='g':
            ans = float(num)*453.592
        elif weight1=='lb' and weight2=='kg':
            ans = float(num)*0.453592
        elif weight1=='lb' and weight2=='oz':
            ans = float(num)*16
        elif weight1=='lb' and weight2=='lb':
            ans = num

        #oz
        elif weight1=='oz' and weight2=='mg':
            ans = float(num)*28349.5
        elif weight1=='oz' and weight2=='g':
            ans = float(num)*28.3495
        elif weight1=='oz' and weight2=='kg':
            ans = float(num)*0.0283495
        elif weight1=='oz' and weight2=='lb':
            ans = float(num)*0.0625
        elif weight1=='oz' and weight2=='oz':
            ans = num
    
        AnswerLength3.config(text=str(ans))
    except:
        AnswerLength3.config(text='Something wrong')

def convertTime():
    time1 = UnitListbox7.get()
    time2 = UnitListbox8.get()
    
    num = int(enternum.get())

    try:
        #second
        if time1=='second' and time2 == 'minute':
            ans = float(num)*0.0166666667
        elif time1=='second' and time2 == 'hour':
            ans = float(num)*0.0002777778
        elif time1=='second' and time2 == 'day':
            ans = float(num)*0.0000115741
        elif time1=='second' and time2 == 'week':
            ans = float(num)*0.0000016534
        elif time1=='second' and time2 == 'month':
            ans = float(num)*0.00000038026
        elif time1=='second' and time2 == 'year':
            ans = float(num)*0.000000031688


        #minute
        elif time1=='minute' and time2 == 'second':
            ans = float(num)*60
        elif time1=='minute' and time2 == 'hour':
            ans = float(num)*0.01667
        elif time1=='minute' and time2 == 'day':
            ans = float(num)*0.00069444
        elif time1=='minute' and time2 == 'week':
            ans = float(num)*0.0000992063
        elif time1=='minute' and time2 == 'month':
            ans = float(num)*0.0000228154
        elif time1=='minute' and time2 == 'year':
            ans = float(num)*0.0000019013

        #hour
        elif time1=='hour' and time2 == 'second':
            ans = float(num)*3600
        elif time1=='hour' and time2 == 'minute':
            ans = float(num)*60
        elif time1=='hour' and time2 == 'day':
            ans = float(num)*0.0416666667
        elif time1=='hour' and time2 == 'week':
            ans = float(num)*0.005952381
        elif time1=='hour' and time2 == 'month':
            ans = float(num)*0.0013689254
        elif time1=='hour' and time2 == 'year':
            ans = float(num)*0.0001140771

        #day
        elif time1=='day' and time2 == 'second':
            ans = float(num)*86400
        elif time1=='day' and time2 == 'minute':
            ans = float(num)*1440
        elif time1=='day' and time2 == 'hour':
            ans = float(num)*24
        elif time1=='day' and time2 == 'week':
            ans = float(num)*0.1428571429
        elif time1=='day' and time2 == 'month':
            ans = float(num)*0.032854
        elif time1=='day' and time2 == 'year':
            ans = float(num)*0.0027379
        

        #week
        elif time1=='week' and time2 == 'second':
            ans = float(num)*604800
        elif time1=='week' and time2 == 'minute':
            ans = float(num)*10080
        elif time1=='week' and time2 == 'hour':
            ans = float(num)*168
        elif time1=='week' and time2 == 'day':
            ans = float(num)*7
        elif time1=='week' and time2 == 'month':
            ans = float(num)*0.2299795
        elif time1=='week' and time2 == 'year':
            ans = float(num)*0.01916496

        #month
        elif time1=='month' and time2 == 'second':
            ans = float(num)*2629800
        elif time1=='month' and time2 == 'minute':
            ans = float(num)*43830
        elif time1=='month' and time2 == 'hour':
            ans = float(num)*730.5
        elif time1=='month' and time2 == 'day':
            ans = float(num)*7
        elif time1=='month' and time2 == 'week':
            ans = float(num)*30.4375
        elif time1=='month' and time2 == 'year':
            ans = float(num)*0.0833333

        #year
        elif time1=='year' and time2 == 'second':
            ans = float(num)*31557600
        elif time1=='year' and time2 == 'minute':
            ans = float(num)*525960
        elif time1=='year' and time2 == 'hour':
            ans = float(num)*8766
        elif time1=='year' and time2 == 'day':
            ans = float(num)*365.25
        elif time1=='year' and time2 == 'week':
            ans = float(num)*52.17857
        elif time1=='year' and time2 == 'month':
            ans = float(num)*12


        #same
        elif time1=='second' and time2 == 'second':
            ans = num
        elif time1=='minute' and time2 == 'minute':
            ans = num
        elif time1=='hour' and time2 == 'hour':
            ans = num
        elif time1=='day' and time2 == 'day':
            ans = num
        elif time1=='week' and time2 == 'week':
            ans = num
        elif time1=='month' and time2 == 'month':
            ans = num
        elif time1=='year' and time2 == 'year':
            ans = num

        AnswerLength4.config(text=str(ans))
    except:
        AnswerLength4.config(text='Something wrong')

def convertArea():
    area1 = UnitListbox9.get()
    area2 = UnitListbox10.get()
    
    num = int(enternum.get())

    try:
        #sq m
        if area1=='Square m' and area2 == 'Square m':
            ans = num
        elif area1=='Square m' and area2 == 'Square km':
            ans =float(num)*0.000001
        elif area1=='Square m' and area2 == 'Square ft':
            ans =float(num)*10.76391
        elif area1=='Square m' and area2 == 'Square yard':
            ans =float(num)*1.195990
        elif area1=='Square m' and area2 == 'Square mile':
            ans =float(num)*0.0000003861
        elif area1=='Square m' and area2 == 'Acre':
            ans =float(num)*0.0002471054

        #sq km
        elif area1=='Square km' and area2 == 'Square m':
            ans = float(num)*1000000
        elif area1=='Square km' and area2 == 'Square km':
            ans = num
        elif area1=='Square km' and area2 == 'Square ft':
            ans =float(num)*10763910.417
        elif area1=='Square km' and area2 == 'Square yard':
            ans =float(num)*1195990.0463
        elif area1=='Square km' and area2 == 'Square mile':
            ans =float(num)*0.38610188
        elif area1=='Square km' and area2 == 'Acre':
            ans =float(num)*247.105381

        #sq ft
        elif area1=='Square ft' and area2 == 'Square m':
            ans = float(num)*0.09290304
        elif area1=='Square ft' and area2 == 'Square km':
            ans = float(num)*0.000000092903
        elif area1=='Square ft' and area2 == 'Square ft':
            ans = num
        elif area1=='Square ft' and area2 == 'Square yard':
            ans =float(num)*0.1111111
        elif area1=='Square ft' and area2 == 'Square mile':
            ans =float(num)*0.00000003587
        elif area1=='Square ft' and area2 == 'Acre':
            ans =float(num)*0.0000229568



        #sq yard
        elif area1=='Square yard' and area2 == 'Square m':
            ans = float(num)*0.83612736
        elif area1=='Square yard' and area2 == 'Square km':
            ans = float(num)*0.00000083613
        elif area1=='Square yard' and area2 == 'Square ft':
            ans = float(num)*9
        elif area1=='Square yard' and area2 == 'Square yard':
            ans = num
        elif area1=='Square yard' and area2 == 'Square mile':
            ans =float(num)*0.00000032283
        elif area1=='Square yard' and area2 == 'Acre':
            ans =float(num)*0.0002066116

        #sq mile
        elif area1=='Square mile' and area2 == 'Square m':
            ans = float(num)*2589990
        elif area1=='Square mile' and area2 == 'Square km':
            ans = float(num)*2.58999
        elif area1=='Square mile' and area2 == 'Square ft':
            ans = float(num)*27878420.34
        elif area1=='Square mile' and area2 == 'Square yard':
            ans = float(num)*3097602.26
        elif area1=='Square mile' and area2 == 'Square mile':
            ans = num
        elif area1=='Square mile' and area2 == 'Acre':
            ans =float(num)*640.00047

        #acre
        elif area1=='Acre' and area2 == 'Square m':
            ans = float(num)*4046.8564
        elif area1=='Acre' and area2 == 'Square km':
            ans = float(num)*0.00404686
        elif area1=='Acre' and area2 == 'Square ft':
            ans = float(num)*43560
        elif area1=='Acre' and area2 == 'Square yard':
            ans = float(num)*4840
        elif area1=='Acre' and area2 == 'Square mile':
            ans = float(num)*0.0015625  
        elif area1=='Acre' and area2 == 'Acre':
            ans = num

        AnswerLength5.config(text=str(ans))
    except:
        AnswerLength5.config(text='Something wrong')
#unitsVolume = ['Cubic Cm','Cubic m','Cubic km','Liter','Cubic foot','Cubic yard','Cubic mile']    
def convertVolume():
    vol1 = UnitListbox11.get()
    vol2 = UnitListbox12.get()
    
    num = int(enternum.get())

    try:
    #cm3
        if vol1=='Cubic Cm' and vol2=='Cubic Cm':
            ans = num
        elif vol1=='Cubic Cm' and vol2=='Cubic m':
            ans = float(num)*0.000001
        elif vol1=='Cubic Cm' and vol2=='Cubic km':
            ans = float(num)*0.000000000000001
        elif vol1=='Cubic Cm' and vol2=='Liter':
            ans = float(num)*0.001
        elif vol1=='Cubic Cm' and vol2=='Cubic foot':
            ans = float(num)*0.0000353147
        elif vol1=='Cubic Cm' and vol2=='Cubic yard':
            ans = float(num)*0.000001308
        elif vol1=='Cubic Cm' and vol2=='Cubic mile':
            ans = float(num)*0.00000000000000023991

        #m3
        elif vol1=='Cubic m' and vol2=='Cubic Cm':
            ans = float(num)*1000000
        elif vol1=='Cubic m' and vol2=='Cubic m':
            ans = num
        elif vol1=='Cubic m' and vol2=='Cubic km':
            ans = float(num)*0.000000001
        elif vol1=='Cubic m' and vol2=='Liter':
            ans = float(num)*1000
        elif vol1=='Cubic m' and vol2=='Cubic foot':
            ans = float(num)*35.314667
        elif vol1=='Cubic m' and vol2=='Cubic yard':
            ans = float(num)*1.3079506
        elif vol1=='Cubic m' and vol2=='Cubic mile':
            ans = float(num)*0.00000000023991

        #km3
        elif vol1=='Cubic km' and vol2=='Cubic Cm':
            ans = float(num)*1000000000000000
        elif vol1=='Cubic km' and vol2=='Cubic m':
            ans = float(num)*1000000000
        elif vol1=='Cubic km' and vol2=='Cubic km':
            ans = num
        elif vol1=='Cubic km' and vol2=='Liter':
            ans = float(num)*1000000000000
        elif vol1=='Cubic km' and vol2=='Cubic foot':
            ans = float(num)*35314666721
        elif vol1=='Cubic km' and vol2=='Cubic yard':
            ans = float(num)*1307950619.3
        elif vol1=='Cubic km' and vol2=='Cubic mile':
            ans = float(num)*0.23991286

        #l3
        elif vol1=='Liter' and vol2=='Cubic Cm':
            ans = float(num)*1000
        elif vol1=='Liter' and vol2=='Cubic m':
            ans = float(num)*0.001
        elif vol1=='Liter' and vol2=='Cubic km':
            ans = float(num)*0.000000000001
        elif vol1=='Liter' and vol2=='Liter':
            ans = num
        elif vol1=='Liter' and vol2=='Cubic foot':
            ans = float(num)*0.0353147
        elif vol1=='Liter' and vol2=='Cubic yard':
            ans = float(num)*0.00130795
        elif vol1=='Liter' and vol2=='Cubic mile':
            ans = float(num)*0.00000000000023991

        #ft3  
        elif vol1=='Cubic foot' and vol2=='Cubic Cm':
            ans = float(num)*28316.846592
        elif vol1=='Cubic foot' and vol2=='Cubic m':
            ans = float(num)*0.0283168466
        elif vol1=='Cubic foot' and vol2=='Cubic km':
            ans = float(num)*0.000000000028317
        elif vol1=='Cubic foot' and vol2=='Liter':
            ans = float(num)*28.316847
        elif vol1=='Cubic foot' and vol2=='Cubic foot':
            ans = num
        elif vol1=='Cubic foot' and vol2=='Cubic yard':
            ans = float(num)*0.0370370
        elif vol1=='Cubic foot' and vol2=='Cubic mile':
            ans = float(num)*0.0000000000067936

        #yard3
        elif vol1=='Cubic yard' and vol2=='Cubic Cm':
            ans = float(num)*764554.85798
        elif vol1=='Cubic yard' and vol2=='Cubic m':
            ans = float(num)*0.764554858
        elif vol1=='Cubic yard' and vol2=='Cubic km':
            ans = float(num)*0.00000000076455
        elif vol1=='Cubic yard' and vol2=='Liter':
            ans = float(num)*764.55486
        elif vol1=='Cubic yard' and vol2=='Cubic foot':
            ans = float(num)*27
        elif vol1=='Cubic yard' and vol2=='Cubic yard':
            ans = num
        elif vol1=='Cubic yard' and vol2=='Cubic mile':
            ans = float(num)*0.00000000018343

        #mile3  
        elif vol1=='Cubic mile' and vol2=='Cubic Cm':
            ans = float(num)*4168180000000000
        elif vol1=='Cubic mile' and vol2=='Cubic m':
            ans = float(num)*4168180000
        elif vol1=='Cubic mile' and vol2=='Cubic km':
            ans = float(num)*4.16818
        elif vol1=='Cubic mile' and vol2=='Liter':
            ans = float(num)*4168180000000
        elif vol1=='Cubic mile' and vol2=='Cubic foot':
            ans = float(num)*147197887535
        elif vol1=='Cubic mile' and vol2=='Cubic yard':
            ans = float(num)*5451773612.4
        elif vol1=='Cubic mile' and vol2=='Cubic mile':
            ans = num

        AnswerLength6.config(text=str(ans))
    except:
       AnswerLength6.config(text='Something wrong')

def clear():
    enternum.delete(0,'end')
    AnswerLength.config(text='')
    AnswerLength2.config(text='')
    AnswerLength3.config(text='')
    AnswerLength4.config(text='')
    AnswerLength5.config(text='')
    AnswerLength6.config(text='')


#--------------------------------------------
#window
window = Tk()
window.title('Units Converter')
window.geometry('550x400')
window.config(bg='#b0c4de')
window.resizable(FALSE,FALSE)
window.bind('<Return>',convertLn)

#new tabs
notebook = Notebook(window)
length = Frame(notebook,bg='#b0c4de')
temperature = Frame(notebook,bg='#b0c4de')
weight = Frame(notebook,bg='#b0c4de')
time = Frame(notebook,bg='#b0c4de')
area = Frame(notebook,bg='#b0c4de')
volume = Frame(notebook,bg='#b0c4de')

notebook.add(length,text='Length')
notebook.add(temperature,text='Temperature')
notebook.add(weight,text='Weight')
notebook.add(time,text='Time')
notebook.add(area,text='Area')
notebook.add(volume,text='Volume')
notebook.pack(expand=True,fill='both')

#Label---------------------------------------
Mylabel = Label(window,text="The Unit Converter",font=('Courier',20),bg='#b0c4de',fg='#000000')
Mylabel.place(x=140,y=23)

unitsLn = ['mm','cm','m','km',"inch",'ft','yard','mile']

l1 = Label(window,text='From',bg='#b0c4de')
l1.place(x=5,y=60)
UnitListbox1 = Combobox(length,width=35,values=unitsLn)
UnitListbox1.place(x=40,y=40)

l2 = Label(window,text='To',bg='#b0c4de')
l2.place(x=271,y=62)
UnitListbox2 = Combobox(length,width=35,values=unitsLn,background='#191970')
UnitListbox2.place(x=295,y=40)

enterLb = Label(window,text='Put the number to convert',bg='#b0c4de')
enterLb.place(x=23,y=100)
enternum = Entry(window,width=31,font=40)
enternum.place(x=170,y=100)

convertButton = Button(length,text='Convert',font=50,command=convertLn)
convertButton.place(x=260,y=180)

AnsLabel = Label(window,text='Your answer is',font=30,bg='#b0c4de')
AnsLabel.place(x=50,y=320)

AnswerLength = Label(length,width=30,font=30)
AnswerLength.place(x=158,y=300)

clearB = Button(window,text='Clear',font=50,bg='#66cdaa',fg='#000000',command=clear)
clearB.place(x=440,y=320)

#temperature--------------------------------------------

unitsTemp = ['Celsius','Kelvin','Fahrenheit']

UnitListbox3 = Combobox(temperature,width=35,values=unitsTemp)
UnitListbox3.place(x=40,y=40)

UnitListbox4 = Combobox(temperature,width=35,values=unitsTemp)
UnitListbox4.place(x=293,y=40)

convertButton2 = Button(temperature,text='Convert',font=50,command=convertTemp)
convertButton2.place(x=260,y=180)

AnswerLength2 = Label(temperature,width=30,font=30)
AnswerLength2.place(x=158,y=300)

#weight--------------------------

unitsWeight = ['mg','g','kg','lb','oz']

UnitListbox5 = Combobox(weight,width=35,values=unitsWeight)
UnitListbox5.place(x=40,y=40)

UnitListbox6 = Combobox(weight,width=35,values=unitsWeight)
UnitListbox6.place(x=293,y=40)

convertButton3 = Button(weight,text='Convert',font=50,command=convertWeight)
convertButton3.place(x=260,y=180)

AnswerLength3 = Label(weight,width=30,font=30)
AnswerLength3.place(x=158,y=300)

#Time--------------------

unitsTime = ['second','minute','hour','day','week','month','year']

UnitListbox7 = Combobox(time,width=35,values=unitsTime)
UnitListbox7.place(x=40,y=40)

UnitListbox8 = Combobox(time,width=35,values=unitsTime)
UnitListbox8.place(x=293,y=40)

convertButton4 = Button(time,text='Convert',font=50,command=convertTime)
convertButton4.place(x=260,y=180)

AnswerLength4 = Label(time,width=30,font=30)
AnswerLength4.place(x=158,y=300)

#area-----------------------

unitsArea = ['Square m','Square km','Square ft'
,'Square yard','Square mile','Acre']

UnitListbox9 = Combobox(area,width=35,values=unitsArea)
UnitListbox9.place(x=40,y=40)

UnitListbox10 = Combobox(area,width=35,values=unitsArea)
UnitListbox10.place(x=293,y=40)

convertButton5 = Button(area,text='Convert',font=50,command=convertArea)
convertButton5.place(x=260,y=180)

AnswerLength5 = Label(area,width=30,font=30)
AnswerLength5.place(x=158,y=300)

#volume----------------

unitsVolume = ['Cubic Cm','Cubic m','Cubic km','Liter'
,'Cubic foot','Cubic yard','Cubic mile']

UnitListbox11 = Combobox(volume,width=35,values=unitsVolume)
UnitListbox11.place(x=40,y=40)

UnitListbox12 = Combobox(volume,width=35,values=unitsVolume)
UnitListbox12.place(x=293,y=40)

convertButton6 = Button(volume,text='Convert',font=50,command=convertVolume)
convertButton6.place(x=260,y=180)

AnswerLength6 = Label(volume,width=30,font=30)
AnswerLength6.place(x=158,y=300)

#--------------
window.mainloop() 