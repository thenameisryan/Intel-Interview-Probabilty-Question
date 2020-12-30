#ryan

# Import tkinter library 
from tkinter import * 
from tkinter.ttk import *
# Import random library 
import random
  
# creates a Tk() object 
master = Tk() 
  
# root window 
master.resizable(width=True, height=True)
master.title('Probability GUI') 
  
# function to open a new window  
# on a button click 
def openSolution(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    solutionWindow = Toplevel(master) 
  
    # new window
    solutionWindow.geometry("400x350") 
    solutionWindow.title("Show Solution") 

    # display solution
    Label(solutionWindow,  
          text ="Bucket A \t Bucket B \n1 \t\t 49 \n0 \t\t 50 \n").pack() 
   
    solution = 'Solution: \n' \
            + 'Assuming that one of the two buckets is chosen at random \n' \
            + 'and then one of the balls from the bucket is chosen at random.  \n' \
            + 'I will put to put 1 red ball in 1 of the buckets and all the other 99 \n' \
            + 'balls in the other bucket. This gives a less than 75% \n' \
            + 'chance of having a red ball being chosen. Therefore, there will be a 50% chance of \n' \
            + 'selecting the bucket containing 1 ball with a 100% chance of \n' \
            + 'selecting a red ball from the bucket.  And a 50% chance of \n' \
            + 'selecting the bucket containing 99 balls with a 49.5% (49/99) \n' \
            + 'chance of selecting a red ball from the bucket.  \n' \
            + 'Average probability of selecting a red ball is \n\n' \
            + '(50% % 100%) + (50% * 49.5%) = 74.7%.'
    Label(solutionWindow,  
          text =solution).pack() 

    btnSim = Button(solutionWindow,  
             text ="Simulate",  
             command = runSims) 
    btnSim.pack(pady = 5)
    btnRun = Button(solutionWindow,  
             text ="Run Solution",  
             command = runSolution) 
    btnRun.pack()

def runSims(a_simulations = 1, b_simulations = 99):
    # Toplevel object which will  
    # be treated as a new window 
    runWindow = Toplevel(master) 
  
    # new window
    runWindow.geometry("400x400") 
    runWindow.title("Simulate")

    # create a horizontal scrollbar by 
    # setting orient to horizontal 
    h = Scrollbar(runWindow, orient = 'horizontal') 
   
    # attach Scrollbar to root window at  
    # the bootom 
    h.pack(side = BOTTOM, fill = X) 

    # create a vertical scrollbar-no need 
    # to write orient as it is by 
    # default vertical 
    v = Scrollbar(runWindow) 

    # attach Scrollbar to root window on  
    # the side 
    v.pack(side = RIGHT, fill = Y) 
       

    # create a Text widget with 15 chars 
    # width and 15 lines height 
    # here xscrollcomannd is used to attach Text 
    # widget to the horizontal scrollbar 
    # here yscrollcomannd is used to attach Text 
    # widget to the vertical scrollbar 
    t = Text(runWindow, width = 40, height = 40, wrap = NONE, 
                xscrollcommand = h.set,  
                yscrollcommand = v.set) 

    countRA = 0 # Bucket A Red Balls
    countBA = 0 # Bucket A Blue Balls

    t.insert(END,"Simulating picking a ball in A Bucket\n")

    # insert some text into the text widget 
    for i in range(a_simulations): 
        getRand = random.randint(0,1)

        if getRand == 0:
            t.insert(END,"\nCollected a Red ball\n")
            countRA = countRA + 1
        else:
            t.insert(END,"\nCollected a Blue ball\n")
            countBA = countBA + 1    

    totalA = '\nRED BALL:', countRA, '\nBLUE BALL:', countBA ,"\n"

    t.insert(END,totalA)             
   
    countRB = 0 # Bucket B Red Balls
    countBB = 0 # Bucket B Blue Balls

    t.insert(END,"\nSimulating picking a ball in B Bucket\n")

    # insert some text into the text widget 
    for i in range(b_simulations): 
        getRand = random.randint(0,1)

        if getRand == 0:
            t.insert(END,"\nCollected a Red ball\n")
            countRB = countRB + 1
        else:
            t.insert(END,"\nCollected a Blue ball\n")
            countBB = countBB + 1    

    totalB = '\nRED BALL:', countRB, '\nBLUE BALL:', countBB

    t.insert(END,totalB) 

    avgP = ((50/100)/(100/100))*100 + ((countRB/99)*(50/100))*100 

    formatting = '{:.2f}'.format(avgP)

    avgPans = "\nAverage Probabilty of getting a \n"
    avgPansCont = "RED Ball is", formatting, "%"

    join = avgPans, avgPansCont

    t.insert(END, join)

    btnRunS = Button(runWindow,  
             text ="Simulate",  
             command = runSims) 
    btnRunS.pack(pady = 10)
   
    # attach Text widget to root window at top 
    t.pack(side=TOP, fill=X) 

    # here command represents the method to 
    # be executed xview is executed on 
    # object 't' Here t may represent any 
    # widget 
    h.config(command=t.xview) 

    # here command represents the method to 
    # be executed yview is executed on 
    # object 't' Here t may represent any 
    # widget 
    v.config(command=t.yview) 

def runSolution():
    # Toplevel object which will  
    # be treated as a new window 
    runSWindow = Toplevel(master) 
  
    # new window
    runSWindow.geometry("400x400") 
    runSWindow.title("Run Solution")

    countRA = 1 # Bucket A Red Balls
    countBA = 0 # Bucket A Blue Balls
   
    countRB = 49 # Bucket B Red Balls
    countBB = 50 # Bucket B Blue Balls

    avgP = ((50/100*100/100) + ((countRB/99)*50/100))*100
    
    formatting = '{:.2f}'.format(avgP)

    avgPans = "\nAverage Probabilty of getting a RED Ball is", formatting, "%"

    label = Label(runSWindow,  
              text =avgPans) 
    label.pack(pady = 10)   
    

# display question
intro = 'There are 2 buckets named A and B and it is filled \n' \
            + 'with a total of 100 balls.  There are 50 blue balls \n' \
            + 'and 50 red balls.  Give a solution so that the average \n' \
            + 'probabilty of a red ball gets chosen is 74%. \n'  
label = Label(master,  
              text =intro) 
  
label.pack(pady = 10) 
  
# a button that opens the solution window
btn = Button(master,  
             text ="Show solution",  
             command = openSolution) 
btn.pack(pady = 10) 
  
# mainloop, runs infinitely 
mainloop() 


    
