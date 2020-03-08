from graphics import *
from math import *

count = 0      # Survival count needs to be implemented in all definitions
inventory = []
# All Story related texts have to be in seperate def function()
# This in order to not repeat unwanted text and only repeat 'count and questions + if-solutions'
# 'count and questions + if-solutions' have to be able to get called seperately ('in def function()')
# Calling needs to be more precise depending on importance of function
#Parameter/arguments = within () to call in seperate function
#There will be survival count, based on the amount of steps you take to complete
#Inventory has impact on users possible decisions

def YourDeath():
    print("""Coronavirus has gone crazy:
            But it hasn’t affected you yet and you decide you’re still young and life is fun 
            so you go with 2 friends skydiving.You fly up to 50,000m and your two friends jump first, followed by you.
            You are all falling really fast but you are all having the time of your life…30,000m…
            You start filming each other in the air while you fall…10,000m…You look at your height watch…5,000m….
            Now is the time to deploy your parachute…Your two friends go first…
            Perfect… no problem…You pull on your parachute…Nothing…3,000m 
            You pull on your reserve parachute… 2,000m It only half deploys slowing you slightly down… 
            but it's not slow enough… 1,000m….That's the last thing you remember.""")
def Introduction():
    print("""...2 years later...
You wake up from a deep deep coma.
Your eyes open... 
You're expecting to be greeted by your family… No one is there:
Your head is feeling funny and your rib cage hurts slightly along with your legs. Your eyes begin to focus…
You realise you are in a hospital room and your memory comes back. You remember everything up to 1000m…. 
You realise why you are here... You wonder where everyone is, especially your family, and why it is so quiet… 
*YOUR GOAL IS TO FIND OUT OF THE HOSPITAL IN THE BEST WAY POSSIBLE*""")
def Firstscene(count, Inventory):
    count = count + 1
    print("Click door to leave your room or click bed to stay in your room:\n")
    win = GraphWin("Hospital room", 500 , 500)
    win.setBackground('black')

    bed = Rectangle(Point(490, 160), Point(250,490))
    bed.setFill('White')
    bed.draw(win)

    bedsheet = Rectangle(Point(480,170), Point(260,480))
    bedsheet.setFill('blue')
    bedsheet.draw(win)

    text3 = Text(Point(375,325), "*click here to stay*").draw(win)
    text3.setSize(10)
    text3.setFill('white')

    pillow = Rectangle(Point(445,400), Point(300,465))
    pillow.setFill('dark blue')
    pillow.draw(win)

    desk = Rectangle(Point(265,15), Point(480,30))
    desk.setFill('White')
    desk.draw(win)

    deskright = Rectangle(Point(465,30), Point(480,100))
    deskright.setFill('White')
    deskright.draw(win)

    deskleft = Rectangle(Point(280,30), Point(265,100))
    deskleft.setFill('White')
    deskleft.draw(win)

    deskcolor = Rectangle(Point(280, 15), Point(265, 100))
    deskcolor.setFill('brown')
    deskcolor.draw(win)

    deskcolor = Rectangle(Point(260, 15), Point(480, 100))
    deskcolor.setFill('brown')
    deskcolor.draw(win)

    centre = Point(0, 0)
    circ = Circle((centre),110)
    circ.setFill('gainsboro')
    circ.draw(win)

    text2 = Text(Point(45, 50), "*click to leave*").draw(win) #text
    text2.setSize(10)

    door = Rectangle(Point(109, 15), Point(0, 0))
    door.setFill('grey')
    door.draw(win)

    drawer = Rectangle(Point(280, 100), Point(360, 110))
    drawer.setFill('White')
    drawer.draw(win)

    centre = Point(323,105)
    circ1 = Circle(centre, 3)
    circ1.setFill('brown')
    circ1.draw(win)

    click = win.getMouse()
    while not (250 < click.getX() < 490 and 160 < click.getY() < 490)\
        and not (0 < click.getX() < 110 and 0 < click.getY() < 110):
        click = win.getMouse()
    win.close()
    if 250 < click.getX() < 490 and 160 < click.getY() < 490:
        StayinRoom(count, Inventory)
    elif 0 < click.getX() < 110 and 0 < click.getY() < 110:
        TextBox1()
        WalkoutRoom(count, Inventory)
    else:
        print("retry")
def StayinRoom(count, Inventory):   # Go back to the Firstscene()
    print(""" You wait for 2 hours but nothing happens… you think to yourself “ah I’ll watch some tv to pass the time”
              you click on the on button but nothing happens… you try again… nothing.
              You decide no I can't stay here… I'll get bored… you look around your room once more... 
              only one option really remains....""")
    Firstscene(count, Inventory)
def TextBox1():
    print("""...Horror...The corridor is dark but there is a shadow standing in front of you… 
                    coughing silently… you call out “Hello”...
                    the shadow turns around violently and without hesitation begins to run in your direction...:
                    """)

def WalkoutRoom(count,Inventory):#solution path
    graphics2()
    count = count + 1
    userInput2 = input("The corona Zombie is coming for u, What do you do(<enter>A = fight, B = Run, C = Lock door)\n:")
    if userInput2 == "A":
        TextBox2()
        FightZombie(count,Inventory)
    elif userInput2 == "B": #solution path2
        TextBoxRun2()
        RunAwayZombie(count,Inventory)
    elif userInput2 == "C":
        print("""You lock the door and start feeling safer for a while, but the corona zombie is hammering on your door.
                 After a while he gave up and you are now safe. 
                 However after some time you decide to go out on the corridor and find a way out of the hospital.""")
        WalkoutRoom(count,Inventory)  # has to include text so maybe make seperate TextPart function = 1 more step
    else:
        WalkoutRoom(count,Inventory)
def TextBox2():
    print("""The Zombie is coming closer to you and you don’t know how to defend yourself.
                    There are some objects lying around you…. Which one could fit your situation the best?""")
def FightZombie(count,Inventory):  # graphics with objects #INVENTORY
    print("Which of the objects could help you? (Put to inventory:  Crutches,  Wheelchair,  Gun )\n:")
    win = GraphWin("Corona Zombie Corridor", 500, 500)
    win.setBackground("grey")
    endc = Rectangle(Point(225, 0), Point(275, 500))
    endc.setFill("black")
    endc.draw(win)

    p1 = Point(250, 250)
    p2 = Point(0, 500)
    p3 = Point(500, 500)

    begc = Polygon(p1, p2, p3)
    begc.setFill("black")
    begc.draw(win)

    block = Rectangle(Point(500, 0), Point(-5, 150))
    block.setFill('grey')
    block.draw(win)

    lampstring = Line(Point(250, 30), Point(250, 80))
    lampstring.draw(win)

    light = Circle(Point(250, 100), 15)
    light.setFill("yellow")
    light.draw(win)

    p4 = Point(250, 80)
    p5 = Point(200, 100)
    p6 = Point(300, 100)

    lamp = Polygon(p4, p5, p6)
    lamp.setFill("black")
    lamp.draw(win)

    head = Circle(Point(250, 200), 15)
    head.setFill("dark green")
    head.draw(win)

    body = Line(Point(250, 200), Point(250, 250))
    body.setOutline("dark green")
    body.draw(win)

    leg1 = Line(Point(250, 250), Point(225, 300))
    leg1.setOutline("dark green")
    leg1.draw(win)

    leg2 = Line(Point(250, 250), Point(275, 300))
    leg2.setOutline("dark green")
    leg2.draw(win)

    arm1 = Line(Point(250, 225), Point(290, 235))
    arm1.setOutline("dark green")
    arm1.draw(win)

    arm2 = Line(Point(250, 225), Point(210, 235))
    arm2.setOutline("dark green")
    arm2.draw(win)

    crutches = Rectangle(Point(20, 420), Point(150, 470))
    message1 = Text(Point(65.0, 436.7), "CRUTCHES")
    crutches.setFill("red")
    crutches.draw(win)
    message1.draw(win)

    wheelchair = Rectangle(Point(166, 420), Point(296, 470))
    message2 = Text(Point(231.0, 436.7), "WHEELCHAIR")
    wheelchair.setFill("red")
    wheelchair.draw(win)
    message2.draw(win)

    gun = Rectangle(Point(312, 420), Point(442, 470))
    message3 = Text(Point(377.0, 436.7), "GUN")
    gun.setFill("red")
    gun.draw(win)
    message3.draw(win)

    click2 = win.getMouse()
    while not (20 < click2.getX() < 150 and 420 < click2.getY() < 470) \
            and not (166 < click2.getX() < 296 and 420 < click2.getY() < 470) \
            and not (312 < click2.getX() < 442 and 420 < click2.getY() < 470):
        click2 = win.getMouse()
    win.close()
    if 20 < click2.getX() < 150 and 420 < click2.getY() < 470:  # put to inventory
        Inventory.append("Crutches")
        count = count + 1
        print("You pick up crutches and want to use them but how?")
        userInput5 = input("How do you want to use the crutches?(Type= Hit, Use)\n:")
        if userInput5 == "Hit":
            print("""You hit it well on the head… but it lets out a loud shriek… you hit it again... 
                     and this time it collapses on to the floor with a loud thud… You think to yourself... 
                     What was that thing… but before you can figure it out...
                     you see another dark figure running towards you from the shadows…
                     This time you choose to run…""")
            TextBoxRun2()
            RunAwayZombie(count, Inventory)
        elif userInput5 == "Use":
            print("""You support yourself with the crutches and do a Bruce Lee sideways Karate kick… 
            you hit it well on the head… but it lets out a loud shriek… you kick it again... 
            and this time it collapses on to the floor with a loud thud… You think to yourself...'What was that thing
            ...but before you can figure it out you see another dark figure running towards you from the shadows…""")
            TextBoxRun2()
            RunAwayZombie(count, Inventory)  # going back to
    elif 166 < click2.getX() < 296 and 420 < click2.getY() < 470:  # put to inventory
        Inventory.append("Wheelchair")
        count = count + 1
        print("""You look hesitantly at it not 100% sure on how to use it… 
        unsure and panicked you push it towards the mysterious figure hoping it knocks it over… 
        NOPE…it merely made it stumble slightly… you look to your other options:""")
        WalkoutRoom(count, Inventory)
    elif 312 < click2.getX() < 442 and 420 < click2.getY() < 470: # put to inventory
        Inventory.append("Gun")
        count = count + 1
        print("You pick up the gun, but is is light and is made out of plastic....you are running out of time!")
        WalkoutRoom(count, Inventory)
    else:
        FightZombie(count, Inventory)

def TextBoxRun2():
    print("""You are a good runner, but your leg still slightly hurts so you can’t run as fast as you once were able to.
             You turn right and run along the dark corridor being chased by a weird figure. 
             You need to find a way out of the hospital.""")
def RunAwayZombie(count, Inventory):
    win = GraphWin("corridor two doors", 500, 500)
    win.setBackground("grey")

    doorleft = Rectangle(Point(160, 200), Point(100, 400))
    doorleft.setFill('navy')
    doorleft.draw(win)

    doorright = Rectangle(Point(400,200), Point(340,450))
    doorright.setFill('navy')
    doorright.draw(win)

    centre = Point(145, 280)
    circ = Circle(centre, 8)
    circ.setFill('brown')
    circ.draw(win)

    centre = Point(355, 275)
    circ = Circle(centre, 8)
    circ.setFill('brown')
    circ.draw(win)

    endc = Rectangle(Point(225, 0), Point(275, 500))
    endc.setFill("black")
    endc.draw(win)

    p1 = Point(250, 250)
    p2 = Point(0, 500)
    p3 = Point(500, 500)

    begc = Polygon(p1, p2, p3)
    begc.setFill("black")
    begc.draw(win)

    block = Rectangle(Point(500,0), Point(-5,150))
    block.setFill('grey')
    block.draw(win)

    lampstring = Line(Point(250, 30), Point(250, 80))
    lampstring.draw(win)

    light = Circle(Point(250, 100), 15)
    light.setFill("yellow")
    light.draw(win)

    p4 = Point(250, 80)
    p5 = Point(200, 100)
    p6 = Point(300, 100)

    lamp = Polygon(p4, p5, p6)
    lamp.setFill("black")
    lamp.draw(win)

    text = Text(Point(250, 400), " Click Right or Left door")
    text.setFill('white')
    text.draw(win)


    click5 = win.getMouse()
    while not (100 < click5.getX() < 160 and 200 < click5.getY() < 400)\
        and not(340 < click5.getX() < 400 and 200 < click5.getY() < 450):
        click5 = win.getMouse()
    win.close()
    if 100 < click5.getX() < 160 and 200 < click5.getY() < 400:   #going to count more
        count = count + 1
        print("You walk into a room full of Zombies")
        Zombieroom()
        RunAwayZombie(count, Inventory)
    elif 340 < click5.getX() < 400 and 200 < click5.getY() < 450:  #solution path3
        count = count + 1
        ShowCorridor(count, Inventory)
    else:
        RunAwayZombie(count, Inventory)
def ShowCorridor(count, Inventory):
    win = GraphWin("corridor two doors", 500, 500)
    win.setBackground("grey")

    doorleft = Rectangle(Point(160, 200), Point(100, 400))
    doorleft.setFill('navy')
    doorleft.draw(win)

    centre = Point(145, 280)
    circ = Circle(centre, 8)
    circ.setFill('brown')
    circ.draw(win)

    endc = Rectangle(Point(225, 0), Point(275, 500))
    endc.setFill("black")
    endc.draw(win)

    p1 = Point(250, 250)
    p2 = Point(0, 500)
    p3 = Point(500, 500)

    begc = Polygon(p1, p2, p3)
    begc.setFill("black")
    begc.draw(win)

    block = Rectangle(Point(500,0), Point(-5,150))
    block.setFill('grey')
    block.draw(win)

    lampstring = Line(Point(250, 30), Point(250, 80))
    lampstring.draw(win)

    light = Circle(Point(250, 100), 15)
    light.setFill("yellow")
    light.draw(win)

    p4 = Point(250, 80)
    p5 = Point(200, 100)
    p6 = Point(300, 100)

    lamp = Polygon(p4, p5, p6)
    lamp.setFill("black")
    lamp.draw(win)
    Text(Point(250, 125), "Click left door or end of the corridor").draw(win)

    click3 = win.getMouse()
    while not (100 < click3.getX() < 160 and 200 < click3.getY() < 400) \
            and not (225< click3.getX() < 275 and 0 < click3.getY() < 500):
        click3 = win.getMouse()
    win.close()
    if 100 < click3.getX() < 160 and 200 < click3.getY() < 400:#go to door
        count = count + 1
        print("""You run in and the door closes behind you with a big bang… 
                   maybe the Corona Zombie heard you but this door has locked itself now and so you feel slightly relieved… Until...
                   from the dark shadows of the room… 4 more figures emerge… 
                   you realise you just ran into a room full of corona zombies… your screams are echoed in the hospital corridors 
                   along with their infections chorus of coughs.""")

        win = GraphWin("Wrong room", 500, 500) #Zombie room #bylegend
        win.setBackground("black")

        p1 = Point(250, 250)
        p2 = Point(0, 0)
        p3 = Point(500, 0)

        top = Polygon(p1, p2, p3)
        top.setFill("dim grey")
        top.draw(win)

        p4 = Point(250, 250)
        p5 = Point(0, 0)
        p6 = Point(0, 500)

        left = Polygon(p4, p5, p6)
        left.setFill("dim grey")
        left.draw(win)

        p7 = Point(250, 250)
        p8 = Point(0, 500)
        p9 = Point(500, 500)

        bottom = Polygon(p7, p8, p9)
        bottom.setFill("dim grey")
        bottom.draw(win)

        p10 = Point(250, 250)
        p11 = Point(500, 500)
        p12 = Point(500, 0)

        right = Polygon(p10, p11, p12)
        right.setFill("dim grey")
        right.draw(win)

        back = Rectangle(Point(150, 150), Point(350, 350))
        back.setFill("black")
        back.draw(win)

        body1 = Line(Point(250, 380), Point(255, 350))
        body1.setOutline("dark green")
        body1.draw(win)
        arm1 = Line(Point(252.5, 365.0), Point(270, 430))
        arm1.setOutline("dark green")
        arm1.draw(win)
        arm2 = Line(Point(252.5, 365.0), Point(230, 430))
        arm2.setOutline("dark green")
        arm2.draw(win)
        head1 = Circle(Point(250, 380), 15)
        head1.setFill("dark green")
        head1.draw(win)

        body2 = Line(Point(170, 300), Point(140, 260))
        body2.setOutline("dark green")
        body2.draw(win)
        arm4 = Line(Point(155, 280), Point(120, 290))
        arm4.setOutline("dark green")
        arm4.draw(win)
        arm3 = Line(Point(155, 280), Point(200, 270))
        arm3.setOutline("dark green")
        arm3.draw(win)
        head2 = Circle(Point(140, 260), 15)
        head2.setFill("dark green")
        head2.draw(win)

        body3 = Line(Point(320, 255), Point(320, 310))
        body3.setOutline("dark green")
        body3.draw(win)
        arm5 = Line(Point(320.0, 282.5), Point(350, 290))
        arm5.setOutline("dark green")
        arm5.draw(win)
        arm6 = Line(Point(320.0, 282.5), Point(340, 300))
        arm6.setOutline("dark green")
        arm6.draw(win)
        head3 = Circle(Point(330, 255), 15)
        head3.setFill("dark green")
        head3.draw(win)

        win.getMouse()
        win.close()

        ShowCorridor(count, Inventory)
    elif 225 < click3.getX() < 275 and 0 < click3.getY() < 500:#continue running
        count = count + 1
        TextBoxRun1()
        ContinueRunning(count, Inventory)
    else:
        ShowCorridor(count, Inventory)
def TextBoxRun1():
    print("""You are a good runner, but your leg still slightly hurts so you can’t run as fast as you once were able to.
     You turn right and run along the dark corridor being chased by a weird figure. 
     You need to find a way out of the hospital. There are two options""")
def ContinueRunning(count, Inventory):  # solutions path
    userInput8 = input("Type: Look,  Hide:")  # graphical reception or text with items to pick up
    count = count + 1
    if userInput8 == "Look":   #solution path5 # look for items
        print("There is some stuff lying around...Which of these items could fit your situation best")
        PickupMap(count, Inventory)
    elif userInput8 == "Hide":
        print("""You sit there… your heart is racing… your breathing... loud…
        you try to breathe quietly but it's difficult and hurting your lungs… the air wants to escape your body.
        Suddenly a faint groan fills the large reception area… followed by a weak cough. It’s here…""")
        ContinueRunning(count,Inventory)
    else:
        ContinueRunning(count, Inventory)
def PickupMap(count,Inventory):
    UserInput9 = input("Pick up: Map, Pencils ,Paper ,Staple ,Paperclip, Chair\n:")  # look for items in reception desk#Maybe str() need
    while UserInput9 != "Map":
        count = count + 1
        print("This item will not help you")
        PickupMap(count, Inventory)
    if UserInput9 == "Map": #solution path6
        Inventory.append("Map")
        print("This is your Inventory now:", Inventory)
        count = count + 1
        RuntoQuiz(count, Inventory)
    return "Map"

def RuntoQuiz(count, Inventory):
    userInput10 = input("<enter> 'Hide' or 'Run'\n:")
    count = count + 1
    if userInput10 == "Hide":
        print("The Zombie is coming closer to you!!!")
        RuntoQuiz(count, Inventory)
    elif userInput10 == "Run": #solutions path 7 #Graphical window quiz# select a)b)c) of pictures Final door
        FinalDoor(count, Inventory) #Input in graphic
    else:
        RuntoQuiz(count,Inventory)

def FinalDoor(count,Inventory):
    count = count + 1
    win = GraphWin("corridor two doors", 500, 500)
    win.setBackground("grey")

    doorleft = Rectangle(Point(160, 200), Point(100, 400))
    doorleft.setFill('navy')
    doorleft.draw(win)

    doorright = Rectangle(Point(400,200), Point(340,450))
    doorright.setFill('navy')
    doorright.draw(win)

    centre = Point(145, 280)
    circ = Circle(centre, 8)
    circ.setFill('brown')
    circ.draw(win)

    centre = Point(355, 275)
    circ = Circle(centre, 8)
    circ.setFill('brown')
    circ.draw(win)

    endc = Rectangle(Point(225, 0), Point(275, 500))
    endc.setFill("black")
    endc.draw(win)

    p1 = Point(250, 250)
    p2 = Point(0, 500)
    p3 = Point(500, 500)

    begc = Polygon(p1, p2, p3)
    begc.setFill("black")
    begc.draw(win)

    block = Rectangle(Point(500,0), Point(-5,150))
    block.setFill('grey')
    block.draw(win)

    lampstring = Line(Point(250, 30), Point(250, 80))
    lampstring.draw(win)

    light = Circle(Point(250, 100), 15)
    light.setFill("yellow")
    light.draw(win)

    p4 = Point(250, 80)
    p5 = Point(200, 100)
    p6 = Point(300, 100)

    lamp = Polygon(p4, p5, p6)
    lamp.setFill("black")
    lamp.draw(win)

    text = Text(Point(250, 400), " Click Right or Left door to Freedom")
    text.setFill('white')
    text.draw(win)

    text7 = Text(Point(250, 430), " choose wisely ")
    text7.setFill('white')
    text7.draw(win)

    click4 = win.getMouse()
    while not (100 < click4.getX() < 160 and 200 < click4.getY() < 400)\
        and not (340 < click4.getX() < 400 and 200 < click4.getY() < 450):
        click4 = win.getMouse()
    win.close()
    if 100 < click4.getX() < 160 and 200 < click4.getY() < 400:
        print("HAHA Almost")
        FinalDoor(count, Inventory)
    elif 340 < click4.getX() < 400 and 200 < click4.getY() < 450:
        win = GraphWin("Exit Door", 500, 500)
        win.setBackground('white')

        grass = Rectangle(Point(360, 200), Point(140, 500))
        grass.setFill('yellowgreen')
        grass.draw(win)

        p1 = Point(255, 120)
        p2 = Point(140, 500)
        p3 = Point(360, 500)

        path = Polygon(p1, p2, p3)
        path.setFill("slategrey")
        path.draw(win)

        sky = Rectangle(Point(360, 200), Point(140, 40))
        sky.setFill('deepskyblue')
        sky.draw(win)

        centre = Point(150, 50)
        circ = Circle(centre, 45)
        circ.setFill('yellow')
        circ.draw(win)

        doorleft = Rectangle(Point(140, 500), Point(0, 0))
        doorleft.setFill('grey')
        doorleft.draw(win)

        doorright = Rectangle(Point(360, 0), Point(500, 500))
        doorright.setFill('grey')
        doorright.draw(win)

        sealing = Rectangle(Point(0, 0), Point(500, 40))
        sealing.setFill("grey")
        sealing.draw(win)

        exit = Rectangle(Point(205, 10), Point(300, 30))
        exit.setFill('green')
        exit.draw(win)

        Text(Point(254, 21), "E X I T").draw(win)

        glassleft = Rectangle(Point(0, 480), Point(120, 60))
        glassleft.setFill('cornflowerblue')
        glassleft.draw(win)

        glassright = Rectangle(Point(500, 480), Point(380, 60))
        glassright.setFill('cornflowerblue')
        glassright.draw(win)

        Text(Point(254, 60), "W E L C O M E").draw(win)
        Text(Point(254, 80), "T O    F R E E D O O M").draw(win)

        win.getMouse()
        win.close()
        # insert graphics picture win a nice finish
        print("Your survival count is:", count, "Points. Optimal score is: 8")
        print("Your Inventory contains:", Inventory)
        print("Enjoy the Freedom")
    else:
        FinalDoor(count, Inventory)
###################################################################################################
###################################################################################################
def graphics2():
    win = GraphWin("Corona Zombie Corridor", 500, 500)
    win.setBackground("grey")
    endc = Rectangle(Point(225, 0), Point(275, 500))
    endc.setFill("black")
    endc.draw(win)

    p1 = Point(250, 250)
    p2 = Point(0, 500)
    p3 = Point(500, 500)

    begc = Polygon(p1, p2, p3)
    begc.setFill("black")
    begc.draw(win)

    block = Rectangle(Point(500, 0), Point(-5, 150))
    block.setFill('grey')
    block.draw(win)

    head = Circle(Point(250, 200), 15)
    head.setFill("dark green")
    head.draw(win)

    body = Line(Point(250, 200), Point(250, 250))
    body.setOutline("dark green")
    body.draw(win)

    leg1 = Line(Point(250, 250), Point(225, 300))
    leg1.setOutline("dark green")
    leg1.draw(win)

    leg2 = Line(Point(250, 250), Point(275, 300))
    leg2.setOutline("dark green")
    leg2.draw(win)

    arm1 = Line(Point(250, 225), Point(290, 235))
    arm1.setOutline("dark green")
    arm1.draw(win)

    arm2 = Line(Point(250, 225), Point(210, 235))
    arm2.setOutline("dark green")
    arm2.draw(win)

    lampstring = Line(Point(250, 30), Point(250, 80))
    lampstring.draw(win)

    light = Circle(Point(250, 100), 15)
    light.setFill("yellow")
    light.draw(win)

    p4 = Point(250, 80)
    p5 = Point(200, 100)
    p6 = Point(300, 100)

    lamp = Polygon(p4, p5, p6)
    lamp.setFill("black")
    lamp.draw(win)

    text10 = Text(Point(250, 125), "*click to continue*").draw(win)

    win.getMouse()# need to change this
    win.close()
def Zombieroom():
    win = GraphWin("Wrong room", 500, 500)  # Zombie room #bylegend
    win.setBackground("black")

    p1 = Point(250, 250)
    p2 = Point(0, 0)
    p3 = Point(500, 0)

    top = Polygon(p1, p2, p3)
    top.setFill("dim grey")
    top.draw(win)

    p4 = Point(250, 250)
    p5 = Point(0, 0)
    p6 = Point(0, 500)

    left = Polygon(p4, p5, p6)
    left.setFill("dim grey")
    left.draw(win)

    p7 = Point(250, 250)
    p8 = Point(0, 500)
    p9 = Point(500, 500)

    bottom = Polygon(p7, p8, p9)
    bottom.setFill("dim grey")
    bottom.draw(win)

    p10 = Point(250, 250)
    p11 = Point(500, 500)
    p12 = Point(500, 0)

    right = Polygon(p10, p11, p12)
    right.setFill("dim grey")
    right.draw(win)

    back = Rectangle(Point(150, 150), Point(350, 350))
    back.setFill("black")
    back.draw(win)

    body1 = Line(Point(250, 380), Point(255, 350))
    body1.setOutline("dark green")
    body1.draw(win)
    arm1 = Line(Point(252.5, 365.0), Point(270, 430))
    arm1.setOutline("dark green")
    arm1.draw(win)
    arm2 = Line(Point(252.5, 365.0), Point(230, 430))
    arm2.setOutline("dark green")
    arm2.draw(win)
    head1 = Circle(Point(250, 380), 15)
    head1.setFill("dark green")
    head1.draw(win)

    body2 = Line(Point(170, 300), Point(140, 260))
    body2.setOutline("dark green")
    body2.draw(win)
    arm4 = Line(Point(155, 280), Point(120, 290))
    arm4.setOutline("dark green")
    arm4.draw(win)
    arm3 = Line(Point(155, 280), Point(200, 270))
    arm3.setOutline("dark green")
    arm3.draw(win)
    head2 = Circle(Point(140, 260), 15)
    head2.setFill("dark green")
    head2.draw(win)

    body3 = Line(Point(320, 255), Point(320, 310))
    body3.setOutline("dark green")
    body3.draw(win)
    arm5 = Line(Point(320.0, 282.5), Point(350, 290))
    arm5.setOutline("dark green")
    arm5.draw(win)
    arm6 = Line(Point(320.0, 282.5), Point(340, 300))
    arm6.setOutline("dark green")
    arm6.draw(win)
    head3 = Circle(Point(330, 255), 15)
    head3.setFill("dark green")
    head3.draw(win)

    win.getMouse()
    win.close()

def main():
    count = 0
    Inventory = []
    YourDeath()#txt
    Introduction() #txt
    Firstscene(count, Inventory)
main()
#optimal step count = 8
