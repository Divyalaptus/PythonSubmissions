############################ SPY CHAT #############################

print("let's get started")


####################### ( Get spy details ) ########################

####### get spyname and welcome him ########

spy_name = input("Welcome to spy chat, you must tell me your spy name first:\n")
if len(spy_name)>0 :
    print("Welcome!!! "+spy_name+". Glad to have you back with us.")
    ########## get spy's gender ########
    spy_salutation = input("What shall we call you (Mr. or Mrs.?)")
    ######### concatinate salutation and name ########
    spy_name = spy_salutation+" "+spy_name
    ######### get more details from spy ###########
    spy_status = input("Alright "+spy_name+". I'd like to know a little bit more about...")

else: ########### if the spy inputs a space #############
    print("A Spy needs to have a valid name. Try again please. ")

############## initialize spy_age, spy_rating, and spy_is_online ##################
spy_age = 0
spy_rating = 0.0
spy_is_online = False

################### input spy_age #####################
spy_age = int(input("What is your age?"))
print(type(spy_age))
 
##################### checking whether spy is of correct age and input rating of spy ######################
if spy_age > 12 and spy_age < 50 :
     spy_rating = float(input("What is your spy rating?"))

################# if spy is not in the age range #############
else:
    print ("Sorry you are not of the correct age to be a spy")

if spy_rating > 4.5:
         print ("Great ace!")
         
elif spy_rating > 3.5 and spy_rating <= 4.5:
         print ("You are one of the good ones.")
         
elif spy_rating >= 2.5 and spy_rating <= 3.5:
         print ("You can always do better")
else:
         print ("We can always use somebody to help in the office.")

############# concatinating string with int and float #################
spy_is_online = True
welcome_note = "Authentication complete. Welcome "
welcome_note += spy_name+" age: "
welcome_note += str(spy_age)
welcome_note += " and rating of: "
welcome_note += str(spy_rating)
welcome_note += " Proud to have you onboard"
print (welcome_note)

    
           
