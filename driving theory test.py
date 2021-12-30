from tkinter import *
import tkinter as tk
from tkinter.constants import END
from PIL import ImageTk, Image
import csv
from tkinter import messagebox
import random

score = 0

root = tk.Tk()

vara1 = IntVar()
vara2 = IntVar()
vara3 = IntVar()
vara4 = IntVar()

username_field = tk.Entry(root)
password_field = tk.Entry(root)

reg_username_field = tk.Entry(root)
reg_password_field = tk.Entry(root)
re_enter_password_field = tk.Entry(root)

name = username_field.get()

background = Image.open("/Users/nick/Documents/GitHub/driving-theory-test-app/background.png")
resized = background.resize((1450, 770), Image.ANTIALIAS)
app_background = ImageTk.PhotoImage(resized)

reg_background = Image.open("/Users/nick/Documents/GitHub/driving-theory-test-app/reg_background.png")
reg_resized = reg_background.resize((1450, 770), Image.ANTIALIAS)
reg_background = ImageTk.PhotoImage(reg_resized)

topics_background = Image.open("/Users/nick/Documents/GitHub/driving-theory-test-app/topics_background.png")
topics_resized = topics_background.resize((1450, 770), Image.ANTIALIAS)
topics_background = ImageTk.PhotoImage(topics_resized)

class road_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

roadsq1 = road_questions("When may you use hazard warning lights while you're driving?", "Instead of sounding the horn in a \n built-up area between 11.30pm and 7.00am", "On rural routes, after \n a sign warniing of animals", "On a motorway or undrestricted rual \n carridgeway, to warn of a hazard ahead", "On the approach to toucan crossings, \n where cyclists are waiting to cross", "/Users/nick/Documents/GitHub/driving-theory-test-app/road-question-images/hazard_lights.png")
roadsq2 = road_questions("What does this sign mean?", "No entry for traffic turning left", "Turn left for parking area", "Turn left for ferry terminal", "No through road on the left", "/Users/nick/Documents/GitHub/driving-theory-test-app/road-question-images/no_through_road.png")
roadsq3 = road_questions("What does this traffic sign mean?", "Advisory maximum speed Limit", "Compulstory maximum speed limit", "Advised seperation distance", "Compulsory minimum speed limit", "/Users/nick/Documents/GitHub/driving-theory-test-app/road-question-images/speedlimit.png")
roadsq4 = road_questions("What should you do when you're approaching traffic lights that have red and amber showing together?", "Pass the lights if the road is clear", "Wait for the green light", "Stop because the lights are changing to red", "Take care becuase there's a fault with the lights", "/Users/nick/Documents/GitHub/driving-theory-test-app/road-question-images/red_yellow.png")
roadsq5 = road_questions("You're in a tunnel and you see this sign, What does it mean?", "Beware of pedestrians crossing ahead", "Beware of pedestrians: no footpath ahead", "Diretions to an emergrency pedestrian exit", "No access for pedestrians", "/Users/nick/Documents/GitHub/driving-theory-test-app/road-question-images/exit.png")


# THESE ARE PICTURES FOR THE ROAD QUESTIONS
imgRoad1 = Image.open(roadsq1.pic)
resizedRoad1 = imgRoad1.resize((400, 300), Image.ANTIALIAS)
img_Road_1 = ImageTk.PhotoImage(resizedRoad1)

imgRoad2 = Image.open(roadsq2.pic)
resizedRoad2 = imgRoad2.resize((400, 300), Image.ANTIALIAS)
img_Road_2 = ImageTk.PhotoImage(resizedRoad2)

imgRoad3 = Image.open(roadsq3.pic)
resizedRoad3 = imgRoad3.resize((400, 300), Image.ANTIALIAS)
img_Road_3 = ImageTk.PhotoImage(resizedRoad3)

imgRoad4 = Image.open(roadsq4.pic)
resizedRoad4 = imgRoad4.resize((400, 300), Image.ANTIALIAS)
img_Road_4 = ImageTk.PhotoImage(resizedRoad4)

imgRoad5 = Image.open(roadsq5.pic)
resizedRoad5 = imgRoad5.resize((400, 300), Image.ANTIALIAS)
img_Road_5 = ImageTk.PhotoImage(resizedRoad5)


class attitude_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

attitudesq1 = attitude_questions("What's the minimum time gap you should leave when following a vehicle on a wet road?", "One second", "Four seconds", "Three Seconds", "Two seconds", "/Users/nick/Documents/GitHub/driving-theory-test-app/attitudes-question-images/wet_road.png")
attitudesq2 = attitude_questions("When should you leave a two-second gap between your vehicle and the one in front?", "When it's icy", "When it's foggy", "When it's dry", "When it's raining", "/Users/nick/Documents/GitHub/driving-theory-test-app/attitudes-question-images/time_gap.png")
attitudesq3 = attitude_questions("You're approaching a zebra crossing. What should you do if pedestrians are waiting to cross", "Use your headlights to iindicate they can cross", "Slow down and prepare to stop", "Wave at them to cross the road", "Give way to older and infirm people only", "/Users/nick/Documents/GitHub/driving-theory-test-app/attitudes-question-images/pedestrians_crossing.png")
attitudesq4 = attitude_questions("You're waiting in a traffic queue at night. How can you avoid dazzliing drivers behind you?", "Keep your foot on the footbrake", "Use the parking brake and the footbrake together", "Use the parking brake and release the footbrake", "Balance the clutch with the accelerator","/Users/nick/Documents/GitHub/driving-theory-test-app/attitudes-question-images/night_traffic.png")
attitudesq5 = attitude_questions("What style of driving causes increased risk to everyone?", "Responsible", "Considerate", "Defensive", "Competative", "/Users/nick/Documents/GitHub/driving-theory-test-app/attitudes-question-images/car_road.png")

imgAttitude1 = Image.open(attitudesq1.pic)
resizedAttitude1 = imgAttitude1.resize((400, 300), Image.ANTIALIAS)
img_Attitude_1 = ImageTk.PhotoImage(resizedAttitude1)

imgAttitude2 = Image.open(attitudesq2.pic)
resizedAttitude2 = imgAttitude2.resize((400, 300), Image.ANTIALIAS)
img_Attitude_2 = ImageTk.PhotoImage(resizedAttitude2)

imgAttitude3 = Image.open(attitudesq3.pic)
resizedAttitude3 = imgAttitude3.resize((400, 300), Image.ANTIALIAS)
img_Attitude_3 = ImageTk.PhotoImage(resizedAttitude3)

imgAttitude4 = Image.open(attitudesq4.pic)
resizedAttitude4 = imgAttitude4.resize((400, 300), Image.ANTIALIAS)
img_Attitude_4 = ImageTk.PhotoImage(resizedAttitude4)

imgAttitude5 = Image.open(attitudesq5.pic)
resizedAttitude5 = imgAttitude5.resize((400, 300), Image.ANTIALIAS)
img_Attitude_5 = ImageTk.PhotoImage(resizedAttitude5)



class hazard_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

hazardq1 = hazard_questions("You're driving a car fitted with an automatic transmission. When should you use 'kick down'", "To brake progressively", "To improve fuel economy", "To engage cruise control", "To accelerate quickly", "/Users/nick/Documents/GitHub/driving-theory-test-app/hazard-question-images/automatic.png")
hazardq2 = hazard_questions("Some two-way roads are divided into three lanes. Why are they particularly dangerous", "Traffic uses the middle lane for emergencies only", "Traffic can overtake on the left", "Traffic in both directions can use the middle lane to overtake", "Traffic can travel faster in poor weather conditions", "/Users/nick/Documents/GitHub/driving-theory-test-app/hazard-question-images/twoway_lanes.png")
hazardq3 = hazard_questions("What type of vehicle could you expect to meet in the middle of the road?", "Car", "Lorry", "Bicycle", "Motorcycle", "/Users/nick/Documents/GitHub/driving-theory-test-app/hazard-question-images/bridge.png")
hazardq4 = hazard_questions("What hazard should you be aware of when travelling along this street?", "Large goods vehicles", "Lack of road markings", "Glare from the sun", "Children running out between vehicles","/Users/nick/Documents/GitHub/driving-theory-test-app/hazard-question-images/street.png")
hazardq5 = hazard_questions("What should you do if you begin to feel drowsy while you're driving?", "Continue with your journey but drive more slowly", "Close the car windows to help you concentrate", "Stop and rest as soon as possible", "Turn the heater up to keep you warm and comfortable", "/Users/nick/Documents/GitHub/driving-theory-test-app/hazard-question-images/drowsy.png")

imgHazard1 = Image.open(hazardq1.pic)
resizedHazard1 = imgHazard1.resize((400, 300), Image.ANTIALIAS)
img_Hazard_1 = ImageTk.PhotoImage(resizedHazard1)

imgHazard2 = Image.open(hazardq2.pic)
resizedHazard2 = imgHazard2.resize((400, 300), Image.ANTIALIAS)
img_Hazard_2 = ImageTk.PhotoImage(resizedHazard2)

imgHazard3 = Image.open(hazardq3.pic)
resizedHazard3 = imgHazard3.resize((400, 300), Image.ANTIALIAS)
img_Hazard_3 = ImageTk.PhotoImage(resizedHazard3)

imgHazard4 = Image.open(hazardq4.pic)
resizedHazard4 = imgHazard4.resize((400, 300), Image.ANTIALIAS)
img_Hazard_4 = ImageTk.PhotoImage(resizedHazard4)

imgHazard5 = Image.open(hazardq5.pic)
resizedHazard5 = imgHazard5.resize((400, 300), Image.ANTIALIAS)
img_Hazard_5 = ImageTk.PhotoImage(resizedHazard5)



class motorway_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

motorwayq1 = motorway_questions("What helps to reduce traffic bunching on a motorway", "National speed limits", "Lane closures", "Variable speed limits", "Contraflow Systems", "/Users/nick/Documents/GitHub/driving-theory-test-app/motorway-question-images/traffic_bunching.png")
motorwayq2 = motorway_questions("What's the national speed limit on motorways for cars and motorcycles?", "70 mph", "30 mph", "60 mph", "50mph", "/Users/nick/Documents/GitHub/driving-theory-test-app/motorway-question-images/speed_limit.png")
motorwayq3 = motorway_questions("You're towing a trailer along a three-lane motorway. When may you use the right-hand lane?", "When there are lane closures", "When you can maintain a high speed", "When large vehicles are in the left and centre lanes", "When there's slow moving traffic", "/Users/nick/Documents/GitHub/driving-theory-test-app/motorway-question-images/towing_trailer.png")
motorwayq4 = motorway_questions("On a smart motorway, what does this sign mean?", "Use the three right-hand lanes only", "Use the hard shoulder only", "Use all the lanes, including the hard shoulder", "Use any lanes except the hard shoulder", "/Users/nick/Documents/GitHub/driving-theory-test-app/motorway-question-images/smart_motorway.png")
motorwayq5 = motorway_questions("You're in a motorway. What must you do if there's a red cross showing above every lane?", "Slow down and watch for further signals", "Leave at the next exit", "Pull onto the hard shoulder", "Stop and wait", "/Users/nick/Documents/GitHub/driving-theory-test-app/motorway-question-images/crossed_motorway.png")

imgMotorway1 = Image.open(motorwayq1.pic)
resizedMotorway1 = imgMotorway1.resize((400, 300), Image.ANTIALIAS)
img_Motorway_1 = ImageTk.PhotoImage(resizedMotorway1)

imgMotorway2 = Image.open(motorwayq2.pic)
resizedMotorway2 = imgMotorway2.resize((400, 300), Image.ANTIALIAS)
img_Motorway_2 = ImageTk.PhotoImage(resizedMotorway2)

imgMotorway3 = Image.open(motorwayq3.pic)
resizedMotorway3 = imgMotorway3.resize((400, 300), Image.ANTIALIAS)
img_Motorway_3 = ImageTk.PhotoImage(resizedMotorway3)

imgMotorway4 = Image.open(motorwayq4.pic)
resizedMotorway4 = imgMotorway4.resize((400, 300), Image.ANTIALIAS)
img_Motorway_4 = ImageTk.PhotoImage(resizedMotorway4)

imgMotorway5 = Image.open(motorwayq5.pic)
resizedMotorway5 = imgMotorway5.resize((400, 300), Image.ANTIALIAS)
img_Motorway_5 = ImageTk.PhotoImage(resizedMotorway5)


class alertness_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

alertnessq1 = alertness_questions("Why should you switch your headlights on when it first starts to get dark?", "So others can see you more easily", "So that you blend in with other drivers", "Because the street lights are lit", "To make your dials easier to see", "/Users/nick/Documents/GitHub/driving-theory-test-app/alertness-question-images/headlights.png")
alertnessq2 = alertness_questions("What does the term 'blind spot' mean?", "An area covered by your left-hand mirror", "An area not covered by your headlights", "An area covered by your right-hand mirror", "An area you can't see through the mirrors", "/Users/nick/Documents/GitHub/driving-theory-test-app/alertness-question-images/blind_spot.png")
alertnessq3 = alertness_questions("What should you do if your mobile phone rings while you're driving or riding?", "Leave it until you have stopped in a safe place", "Pull up at the nearest kerb", "Answer it immediately", "Answer it after 30min", "/Users/nick/Documents/GitHub/driving-theory-test-app/alertness-question-images/car_phone.png")
alertnessq4 = alertness_questions("Whats likely to happen if you use a hands-free phone while driving?", "It will divert your attention", "It will improve your saftey", "It will increase your concentration", "It will reduce your view", "/Users/nick/Documents/GitHub/driving-theory-test-app/alertness-question-images/hands_free.png")
alertnessq5 = alertness_questions("What should you do when you're approaching traffic lights that have been green for some time?", "Be ready to stop", "Brake hard", "Mantain your speed", "Accelerate hard", "/Users/nick/Documents/GitHub/driving-theory-test-app/alertness-question-images/green_light.png")

imgAlertness1 = Image.open(alertnessq1.pic)
resizedAlertness1 = imgAlertness1.resize((400, 300), Image.ANTIALIAS)
img_Alertness_1 = ImageTk.PhotoImage(resizedAlertness1)

imgAlertness2 = Image.open(alertnessq2.pic)
resizedAlertness2 = imgAlertness2.resize((400, 300), Image.ANTIALIAS)
img_Alertness_2 = ImageTk.PhotoImage(resizedAlertness2)

imgAlertness3 = Image.open(alertnessq3.pic)
resizedAlertness3 = imgAlertness3.resize((400, 300), Image.ANTIALIAS)
img_Alertness_3 = ImageTk.PhotoImage(resizedAlertness3)

imgAlertness4 = Image.open(alertnessq4.pic)
resizedAlertness4 = imgAlertness4.resize((400, 300), Image.ANTIALIAS)
img_Alertness_4 = ImageTk.PhotoImage(resizedAlertness4)

imgAlertness5 = Image.open(alertnessq5.pic)
resizedAlertness5 = imgAlertness5.resize((400, 300), Image.ANTIALIAS)
img_Alertness_5 = ImageTk.PhotoImage(resizedAlertness5)


class documents_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

documentsq1 = documents_questions("What's the maximum fine for the driving or riding without insurance?", "Unlimited", "£1000", "£500", "£5000", "/Users/nick/Documents/GitHub/driving-theory-test-app/documents-question-images/driving_no_insurance.png")
documentsq2 = documents_questions("Your car needs to pass an MOT test. What may be invalidated if you drive the car without a current MOT certificate", "The vehicle service record", "The vehicle tax", "The vehicle registration document", "The vehicle insurance", "/Users/nick/Documents/GitHub/driving-theory-test-app/documents-question-images/mot.png")
documentsq3 = documents_questions("For how long is an MOT certificate normally valid?", "30,000 miles", "One year after the date it was issued", "Three years after the date it was issued", "10,000 miles", "/Users/nick/Documents/GitHub/driving-theory-test-app/documents-question-images/mot_expire.png")
documentsq4 = documents_questions("What information is found on a vehicle registration document?", "The date of the MOT", "The regisered keeper", "The type of insurance cover", "The service history details", "/Users/nick/Documents/GitHub/driving-theory-test-app/documents-question-images/registration.png")
documentsq5 = documents_questions("For how long is a Statutory Off-Road Notification (SORN) valid?", "Until the vehicle is repaired or modified", "Until the vehicle is used on the road", "Until the vehicle is insured and MOT'd", "Until the vehicle is taxed, sold or scrapped", "/Users/nick/Documents/GitHub/driving-theory-test-app/documents-question-images/sorn.png")

imgDocuments1 = Image.open(documentsq1.pic)
resizedDocuments1 = imgDocuments1.resize((400, 300), Image.ANTIALIAS)
img_Documents_1 = ImageTk.PhotoImage(resizedDocuments1)

imgDocuments2 = Image.open(documentsq2.pic)
resizedDocuments2 = imgDocuments2.resize((400, 300), Image.ANTIALIAS)
img_Documents_2 = ImageTk.PhotoImage(resizedDocuments2)

imgDocuments3 = Image.open(documentsq3.pic)
resizedDocuments3 = imgDocuments3.resize((400, 300), Image.ANTIALIAS)
img_Documents_3 = ImageTk.PhotoImage(resizedDocuments3)

imgDocuments4 = Image.open(documentsq4.pic)
resizedDocuments4 = imgDocuments4.resize((400, 300), Image.ANTIALIAS)
img_Documents_4 = ImageTk.PhotoImage(resizedDocuments4)

imgDocuments5 = Image.open(documentsq5.pic)
resizedDocuments5 = imgDocuments5.resize((400, 300), Image.ANTIALIAS)
img_Documents_5 = ImageTk.PhotoImage(resizedDocuments5)



class incidents_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

incidentsq1 = incidents_questions("What should you do if your vehicle breaks down in a tunnel?", "Stand in the lane behind your vehicle to warn others", "Switch on hazard warning light, then go and call for help", "Stand in front of your vehicle to warn oncoming drivers", "Stay in your vehicle and wait for the police", "/Users/nick/Documents/GitHub/driving-theory-test-app/incidents-question-images/breakdown_tunnel.png")
incidentsq2 = incidents_questions("What information should you share if you're involved in a collision that causes damage to another vehicle?", "Your name, address and vehicle registration number", "Your occupation and reason for your journey", "Your national insurance number", "Your interent service provider", "/Users/nick/Documents/GitHub/driving-theory-test-app/incidents-question-images/crash.png")
incidentsq3 = incidents_questions("What should you do if you see a large box fall from a lorry onto the motorway?", "Go to the next emergency telephone and report the hazard", "Catch up with the lorry and try to get the drivers attention", "Pull over to the hard shoulder, then remove the box", "Stop close to the box until the police arrive", "/Users/nick/Documents/GitHub/driving-theory-test-app/incidents-question-images/truck_box.png")
incidentsq4 = incidents_questions("Which lights should you use when you're driving in a tunnel", "Dipped headlights", "Sidelights", "Front spotlights", "Rear fog lights", "/Users/nick/Documents/GitHub/driving-theory-test-app/incidents-question-images/tunnel.png")
incidentsq5 = incidents_questions("You're driving behind a large goods vehicle. What should you do if it signals left but steers right?", "Hold your speed and sound your horn", "Overtake on the right of it", "Drive on, keeping to the left", "Slowdown and let the vehicle turn", "/Users/nick/Documents/GitHub/driving-theory-test-app/incidents-question-images/largegoods.png")

imgIncidents1 = Image.open(incidentsq1.pic)
resizedIncidents1 = imgIncidents1.resize((400, 300), Image.ANTIALIAS)
img_Incidents_1 = ImageTk.PhotoImage(resizedIncidents1)

imgIncidents2 = Image.open(incidentsq2.pic)
resizedIncidents2 = imgIncidents2.resize((400, 300), Image.ANTIALIAS)
img_Incidents_2 = ImageTk.PhotoImage(resizedIncidents2)

imgIncidents3 = Image.open(incidentsq3.pic)
resizedIncidents3 = imgIncidents3.resize((400, 300), Image.ANTIALIAS)
img_Incidents_3 = ImageTk.PhotoImage(resizedIncidents3)

imgIncidents4 = Image.open(incidentsq4.pic)
resizedIncidents4 = imgIncidents4.resize((400, 300), Image.ANTIALIAS)
img_Incidents_4 = ImageTk.PhotoImage(resizedIncidents4)

imgIncidents5 = Image.open(incidentsq5.pic)
resizedIncidents5 = imgIncidents5.resize((400, 300), Image.ANTIALIAS)
img_Incidents_5 = ImageTk.PhotoImage(resizedIncidents5)



class vulnerable_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

vulnerableq1 = vulnerable_questions("What should you do if an instrument panel warning light comes on while your driving?", "Deal with the problem when there's more time", "Check out the problem quickly and safely", "Hope that it's just a temporary electrical fault", "Continue if the engine sounds all right", "/Users/nick/Documents/GitHub/driving-theory-test-app/vulnerable-question-images/instrument.png") 
vulnerableq2 = vulnerable_questions("What could you do to help injured people at an incident?", "Keep them on the move by walking them around", "Give them a warm drink", "Give them something to eat", "Keep them warm and comfortable", "/Users/nick/Documents/GitHub/driving-theory-test-app/vulnerable-question-images/incident.png") 
vulnerableq3 = vulnerable_questions("What should you do if you see a large box fall from a lorry onto the motorway", "Pull over to the hard shoulder, then remove the box", "Catch up with the lorry and try to get the drivers attention", "Go to the next emergency telephone and report the hazard", "Stop close to the box until the police arrive", "/Users/nick/Documents/GitHub/driving-theory-test-app/vulnerable-question-images/box.png") 
vulnerableq4 = vulnerable_questions("What should you do if the left-hand pavement is closed to street repairs?", "Position close to the left-hand kerb", "Use your right-hand mirror more often", "Watch out for pedestrains walking in the road", "Speed up to get past the roadworks more quickly", "/Users/nick/Documents/GitHub/driving-theory-test-app/vulnerable-question-images/closed.png") 
vulnerableq5 = vulnerable_questions("Why is it dangerous to drive too close to the vehicle ahead?", "Your satnav will be confused", "Your mirrors will need adjusting", "Your view of the road ahead will be restricted", "Your engine will overheat", "/Users/nick/Documents/GitHub/driving-theory-test-app/vulnerable-question-images/tailgating.png") 

imgVulnerable1 = Image.open(vulnerableq1.pic)
resizedVulnerable1 = imgVulnerable1.resize((400, 300), Image.ANTIALIAS)
img_Vulnerable_1 = ImageTk.PhotoImage(resizedVulnerable1)

imgVulnerable2 = Image.open(vulnerableq2.pic)
resizedVulnerable2 = imgVulnerable2.resize((400, 300), Image.ANTIALIAS)
img_Vulnerable_2 = ImageTk.PhotoImage(resizedVulnerable2)

imgVulnerable3 = Image.open(vulnerableq3.pic)
resizedVulnerable3 = imgVulnerable3.resize((400, 300), Image.ANTIALIAS)
img_Vulnerable_3 = ImageTk.PhotoImage(resizedVulnerable3)

imgVulnerable4 = Image.open(vulnerableq4.pic)
resizedVulnerable4 = imgVulnerable4.resize((400, 300), Image.ANTIALIAS)
img_Vulnerable_4 = ImageTk.PhotoImage(resizedVulnerable4)

imgVulnerable5 = Image.open(vulnerableq5.pic)
resizedVulnerable5 = imgIncidents5.resize((400, 300), Image.ANTIALIAS)
img_Vulnerable_5 = ImageTk.PhotoImage(resizedVulnerable5)





def loginScreen():
    global username_field
    global password_field
    global root
    global name
    
    root.geometry("1450x770")

    canvas = tk.Canvas(root, height=1750, width=770, bd=-2)
    canvas.pack()

    #Resizes the background image to fit the dimentions of the canvas
    background_label = tk.Label(root, image=app_background)
    background_label.place(anchor="nw")

    username_field = tk.Entry(root)
    username_field.place(x=650, y=350, height= 30, width=200)
    
    password_field = tk.Entry(root)
    password_field.place(x=650, y=426, height= 30, width=200)

    submit_button = tk.Button(root, text= "Submit",bg = 'gray' ,padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:[loginProcess(), clearTextboxinLogin()])
    submit_button.place(x=900, y=375, height= 60, width=150)

    reg_new_acc_button = tk.Button(root, text= "Click here to register an account if you dont have one", padx= 60, pady= 20, font=("Helvitca", 18) ,command=lambda:registering_new_acc_Screen())
    reg_new_acc_button.place(x=530, y=575, height= 60, width=450)

    def clearTextboxinLogin():
        username_field.delete(0, END)
        password_field.delete(0, END)
    
    def loginProcess():
        global root
        global name
        with open("/Users/nick/Documents/GitHub/driving-theory-app/usernames_passwords.csv", 'r') as csv_file:

            usernames = []
            passwords = []

            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            for line in csv_reader:
                usernames.append(line[0])
                passwords.append(line[1])
            
            user_bool = False
            pass_bool = False
            a = 0

            for x in range(0, len(usernames)):

                if username_field.get() == usernames[a]:
                    user_bool = True
                
                if password_field.get() == passwords[a]:
                    pass_bool = True

                if pass_bool and user_bool:
                    name = username_field.get()
                    topicsScreen()
                else:
                    user_bool = False
                    pass_bool = False
                    a+=1
            if user_bool == False and pass_bool == False:
                message_popup('login')
                print("incorrect")

def registering_new_acc_Screen():
    global root
    global name
    for widgets in root.winfo_children():
      widgets.destroy()
    
    reg_background_label = tk.Label(root, image=reg_background)
    reg_background_label.place(anchor="nw")

    reg_username_field = tk.Entry(root)
    reg_username_field.place(x=650, y=280, height= 30, width=200)

    reg_password_field = tk.Entry(root)
    reg_password_field.place(x=650, y=400, height= 30, width=200)

    re_enter_password_field = tk.Entry(root)
    re_enter_password_field.place(x=650, y=520, height= 30, width=200)

    submit_button = tk.Button(root, text= "Submit", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:[uploading_details_and_logging_in(), clearTextboxinReg()])
    submit_button.place(x=670, y=600, height= 30, width=150)

    back_button = tk.Button(root, text= "Back", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:loginScreen())
    back_button.place(x=470, y=580, height= 30, width=100)

    def clearTextboxinReg():
        reg_username_field.delete(0, END)
        reg_password_field.delete(0, END)
        re_enter_password_field.delete(0, END)

    def uploading_details_and_logging_in():
        if reg_password_field.get() == re_enter_password_field.get():
            with open("/Users/nick/Documents/GitHub/driving-theory-app/usernames_passwords.csv",'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([reg_username_field.get(),reg_password_field.get()])
                name = username_field.get()
                topicsScreen()
        else: 
            message_popup('reg')

def topicsScreen():
    global root
    for widgets in root.winfo_children():
      widgets.destroy()
    topics_background_label = tk.Label(root, image=topics_background)
    topics_background_label.place(anchor="nw")

    road_and_traffic_button = tk.Button(root, text= "Road and Traffic signs", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('road'))
    road_and_traffic_button.place(x=100, y=250, height= 40, width=200)

    attitude_button = tk.Button(root, text= "Attitude", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('attitude'))
    attitude_button.place(x=470, y=250, height= 40, width=200)

    hazard_awareness_button = tk.Button(root, text= "Hazard Awareness", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('hazard'))
    hazard_awareness_button.place(x=840, y=250, height= 40, width=200)

    motorway_rules_button = tk.Button(root, text= "Motorwawy Rules", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('motorway'))
    motorway_rules_button.place(x=1180, y=250, height= 40, width=200)

    alertness_button = tk.Button(root, text= "Alertness", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('alertness'))
    alertness_button.place(x=100, y=530, height= 40, width=200)

    documents_button = tk.Button(root, text= "Documents", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('documents'))
    documents_button.place(x=470, y=520, height= 40, width=200)

    incidents_button = tk.Button(root, text= "Incidents", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('incidents'))
    incidents_button.place(x=850, y=530, height= 40, width=200)

    vulnerable_button = tk.Button(root, text= "Vulnerable Road Users", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('vulnerable'))
    vulnerable_button.place(x=1190, y=540, height= 40, width=200)

    random_button = tk.Button(root, text= "Random", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('random'))
    random_button.place(x=1070, y=80, height= 40, width=160)

    welcome_text = tk.Label(root, text= "Hello "+ name + " - Pick the specific topic you would like to practice. \n You can also select Random for a mixture of all the topics", font=("Helvitca", 18))
    welcome_text.place(x=350, y=40, height= 120, width=590)

    

def questionsScreen(topic):

    global vara1
    global vara2 
    global vara3 
    global vara4
    global score
    global root
    global name

    for widgets in root.winfo_children():
      widgets.destroy()

    if topic == 'road':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Road_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(roadsq1.q, roadsq1.a1, roadsq1.a2, roadsq1.a3, roadsq1.a4, 1)
        
        def question2():
            displayQuestion(roadsq2.q, roadsq2.a1, roadsq2.a2, roadsq2.a3, roadsq2.a4, 2)

        def question3():
            displayQuestion(roadsq3.q, roadsq3.a1, roadsq3.a2, roadsq3.a3, roadsq3.a4, 3)

        def question4():
            displayQuestion(roadsq4.q, roadsq4.a1, roadsq4.a2, roadsq4.a3, roadsq4.a4, 4)
        
        def question5():
            displayQuestion(roadsq5.q, roadsq5.a1, roadsq5.a2, roadsq5.a3, roadsq5.a4, 5)

        question1()

    if topic == 'attitude':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
    
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_attitudes_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(attitudesq1.q, attitudesq1.a1, attitudesq1.a2, attitudesq1.a3, attitudesq1.a4, 1)
        
        def question2():
            displayQuestion(attitudesq2.q, attitudesq2.a1, attitudesq2.a2, attitudesq2.a3, attitudesq2.a4, 2)

        def question3():
            displayQuestion(attitudesq3.q, attitudesq3.a1, attitudesq3.a2, attitudesq3.a3, attitudesq3.a4, 3)

        def question4():
            displayQuestion(attitudesq4.q, attitudesq4.a1, attitudesq4.a2, attitudesq4.a3, attitudesq4.a4, 4)
        
        def question5():
            displayQuestion(attitudesq5.q, attitudesq5.a1, attitudesq5.a2, attitudesq5.a3, attitudesq5.a4, 5)


        question1()
        
    if topic == 'hazard':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_attitudes_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Hazard_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Hazard_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Hazard_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Hazard_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Hazard_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(hazardq1.q, hazardq1.a1, hazardq1.a2, hazardq1.a3, hazardq1.a4, 1)
        
        def question2():
            displayQuestion(hazardq2.q, hazardq2.a1, hazardq2.a2, hazardq2.a3, hazardq2.a4, 2)

        def question3():
            displayQuestion(hazardq3.q, hazardq3.a1, hazardq3.a2, hazardq3.a3, hazardq3.a4, 3)

        def question4():
            displayQuestion(hazardq4.q, hazardq4.a1, hazardq4.a2, hazardq4.a3, hazardq4.a4, 4)
        
        def question5():
            displayQuestion(hazardq5.q, hazardq5.a1, hazardq5.a2, hazardq5.a3, hazardq5.a4, 5)

        question1()

    if topic == 'motorway':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_attitudes_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Motorway_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Motorway_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Motorway_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Motorway_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Motorway_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(motorwayq1.q, motorwayq1.a1, motorwayq1.a2, motorwayq1.a3, motorwayq1.a4, 1)
        
        def question2():
            displayQuestion(motorwayq2.q, motorwayq2.a1, motorwayq2.a2, motorwayq2.a3, motorwayq2.a4, 2)

        def question3():
            displayQuestion(motorwayq3.q, motorwayq3.a1, motorwayq3.a2, motorwayq3.a3, motorwayq3.a4, 3)

        def question4():
            displayQuestion(motorwayq4.q, motorwayq4.a1, motorwayq4.a2, motorwayq4.a3, motorwayq4.a4, 4)
        
        def question5():
            displayQuestion(motorwayq5.q, motorwayq5.a1, motorwayq5.a2, motorwayq5.a3, motorwayq5.a4, 5)

        question1()


    if topic == 'alertness':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Alertness_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(alertnessq1.q, alertnessq1.a1, alertnessq1.a2, alertnessq1.a3, alertnessq1.a4, 1)
        
        def question2():
            displayQuestion(alertnessq2.q, alertnessq2.a1, alertnessq2.a2, alertnessq2.a3, alertnessq2.a4, 2)

        def question3():
            displayQuestion(alertnessq3.q, alertnessq3.a1, alertnessq3.a2, alertnessq3.a3, alertnessq3.a4, 3)

        def question4():
            displayQuestion(alertnessq4.q, alertnessq4.a1, alertnessq4.a2, alertnessq4.a3, alertnessq4.a4, 4)
        
        def question5():
            displayQuestion(alertnessq5.q, alertnessq5.a1, alertnessq5.a2, alertnessq5.a3, alertnessq5.a4, 5)

        question1()

    
    if topic == 'documents':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root

            if questionNum == 1:

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Alertness_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Documents_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Documents_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Documents_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Documents_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Alertness_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(documentsq1.q, documentsq1.a1, documentsq1.a2, documentsq1.a3, documentsq1.a4, 1)
        
        def question2():
            displayQuestion(documentsq2.q, documentsq2.a1, documentsq2.a2, documentsq2.a3, documentsq2.a4, 2)

        def question3():
            displayQuestion(documentsq3.q, documentsq3.a1, documentsq3.a2, documentsq3.a3, documentsq3.a4, 3)

        def question4():
            displayQuestion(documentsq4.q, documentsq4.a1, documentsq4.a2, documentsq4.a3, documentsq4.a4, 4)
        
        def question5():
            displayQuestion(documentsq5.q, documentsq5.a1, documentsq5.a2, documentsq5.a3, documentsq5.a4, 5)

        question1()

    if topic == 'incidents':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root

            if questionNum == 1:

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara4.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara2.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Alertness_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Incidents_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Incidents_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Incidents_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Incidents_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Incidents_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(incidentsq1.q, incidentsq1.a1, incidentsq1.a2, incidentsq1.a3, incidentsq1.a4, 1)
        
        def question2():
            displayQuestion(incidentsq2.q, incidentsq2.a1, incidentsq2.a2, incidentsq2.a3, incidentsq2.a4, 2)

        def question3():
            displayQuestion(incidentsq3.q, incidentsq3.a1, incidentsq3.a2, incidentsq3.a3, incidentsq3.a4, 3)

        def question4():
            displayQuestion(incidentsq4.q, incidentsq4.a1, incidentsq4.a2, incidentsq4.a3, incidentsq4.a4, 4)
        
        def question5():
            displayQuestion(incidentsq5.q, incidentsq5.a1, incidentsq5.a2, incidentsq5.a3, incidentsq5.a4, 5)

        question1()

    if topic == 'vulnerable':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root

            if questionNum == 1:

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara1.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara3.get() == 0 and vara2.get() == 0 and vara1.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara2.get() == 0 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara3.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara3.get() == 0 and vara1.get() == 0 and vara4.get() == 0 and vara2.get() == 0:
                    message_popup('select')
                elif vara1.get() == 1 and vara4.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Alertness_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Vulnerable_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Vulnerable_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Vulnerable_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Vulnerable_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Vulnerable_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        
        def question1():
            displayQuestion(vulnerableq1.q, vulnerableq1.a1, vulnerableq1.a2, vulnerableq1.a3, vulnerableq1.a4, 1)
        
        def question2():
            displayQuestion(vulnerableq2.q, vulnerableq2.a1, vulnerableq2.a2, vulnerableq2.a3, vulnerableq2.a4, 2)

        def question3():
            displayQuestion(vulnerableq3.q, vulnerableq3.a1, vulnerableq3.a2, vulnerableq3.a3, vulnerableq3.a4, 3)

        def question4():
            displayQuestion(vulnerableq4.q, vulnerableq4.a1, vulnerableq4.a2, vulnerableq4.a3, vulnerableq4.a4, 4)
        
        def question5():
            displayQuestion(vulnerableq5.q, vulnerableq5.a1, vulnerableq5.a2, vulnerableq5.a3, vulnerableq5.a4, 5)

        question1()

    if topic == 'random':

        topics = ('vulnerable', 'incidents', 'documents', 'alertness', 'motorway', 'hazard', 'attitude', 'road')

        random_topic = random.choice(topics)

        questionsScreen(random_topic)
        

def resultsScreen():
    print("results", score)

def message_popup(reason):
    if reason == 'login':
        messagebox.showerror("Error", "Username and password don't match. Try again.")
    elif reason == 'reg':
        messagebox.showerror("Error", "Password doesn't match. Try again.")
    elif reason == 'select':
        messagebox.showerror("Error", "You have not selected an answer")

# loginScreen()
topicsScreen()
root.mainloop()
