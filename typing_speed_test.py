
def labelslider():
    global count,sliderwords
    text='Welcome To Typing Speed Test Game '
    if(count >=len(text)):
        count = 0
        sliderwords=''
    sliderwords+=text[count] 
    count+=1   
    fontlable1.configure(text=sliderwords)
    fontlable1.after(200,labelslider)
 

def time():
    global timeleft,score,miss
    if(timeleft>0):
        timeleft-=1
        timerlabelcounter.configure(text=timeleft)
        timerlabelcounter.after(1000,time)
    else:
        instruction.configure(text='Hit = {} | Miss = {} | TotalScore = {}'.format(score,miss,(score-miss)))    
        rr = messagebox.askretrycancel('Notification',"For play again hit Retry button")
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timerlabelcounter.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcounter.configure(text=score)
            instruction.configure(text='Type Word And Hit Enter')
        # else:
        #     root.quit()
            

def startgame(event):
    global score,miss
    if (timeleft==60):
       time()
       timerlabelcounter.configure(fg='red')

    instruction.configure(text='')

    if(wordentry.get()==wordlabel['text']):
       score +=1
       scorelabelcounter.configure(text=score)

    else:
        miss +=1

    random.shuffle(words)
    wordlabel.configure(text=words[0])    
    wordentry.delete(0,END)


def onclick():
      mixer.music.pause()


def onclickf():
      mixer.music.play()

#------------------Root-------------------------------------

from tkinter import *
import random
from pygame import mixer
from tkinter import messagebox

mixer.init()
root = Tk()
root.geometry('800x590+270+70')
root.configure(bg='black')
root.title('Typing Speed Test')
mixer.music.load('audio.wav')
mixer.music.play(-1)
btn=Button(root,text='music off',command=onclick)
btn.place(x=630,y= 550)
btn1=Button(root,text='music on',command=onclickf)
btn1.place(x=550,y= 550)

#-------------------variable--------------------------------

score = 0
miss=0
timeleft=60
count=0
sliderwords=''
words=["apple","banana","grapes","kiwi","coconut","lion","tiger"
,"zebra","dog","cat","bike","car","boat","trains","computer","furious",
"turbo","wikipedia","adobe","google","abundant","adorable","anxious","awesome"
,"beautiful","boring","camera","careful","careless","cartoon","damage",
"delicate","delicious","diamond","different","easter","energy","fairly","faithful",
"famous","fancy","generously","gentle","handsome","healthy","huge","humorous",
"hungry","island","India","juice","jealous","king","kiss","knife",
"library","magazine","monkey","narrow","nasty","obey","ocean","offend",
"official","paint","parrot","queen","quick","quiet","rain","rainbow",
"safety","software","sea","surface","talented","tasty","teaching","touch","technique",
"transformer","ugly","uniform","utopia","umbrella","universe","violet","vulture",
"violent","window","wire","wax","wise","xenic","xenon","xeroxes","xanatahes",
"young","youthful","yowls","you","york","yoghourt","zaag","zany","zap","zapper"]

#-------------------lable-----------------------------------

fontlable1=Label(root,text='',font= ('airal',25,'italic bold'),bg = 'black',fg='red',width=35)
fontlable1.place(x= 10,y=10)
labelslider()

random.shuffle(words)
wordlabel=Label(root,text=words[0],font= ('airal',25,' bold'),bg = 'black',fg='green')
wordlabel.place(x=330,y= 250)

scorelabel=Label(root,text='Your Score :',font= ('airal',25,' bold'),bg = 'black',fg='dark green')
scorelabel.place(x=10,y=80)

scorelabelcounter=Label(root,text=score,font= ('airal',25,' bold'),bg = 'black',fg='dark green')
scorelabelcounter.place(x=80,y=130)

timerlabel=Label(root,text='Time Left :',font= ('airal',25,'bold'),bg = 'black',fg='green')
timerlabel.place(x=600,y=80)

timerlabelcounter=Label(root,text=timeleft,font= ('airal',25,'bold'),bg = 'black',fg='green')
timerlabelcounter.place(x=650,y=130)

instruction=Label(root,text='Type Word And Hit Enter',font= ('airal',25,' bold'),bg = 'black',fg='green')
instruction.place(x=200,y=400)

#-----------------entry--------------------------------------

wordentry= Entry(root,font= ('airal',25,'bold'),bd = 10,justify='center')
wordentry.place(x=220,y=310)
wordentry.focus_set()

####################################################################

root.bind('<Return>',startgame)
root.mainloop()