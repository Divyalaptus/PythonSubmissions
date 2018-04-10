############################ SPY CHAT #############################
import csv

from termcolor import colored
print(colored("let's get started","red"))

####################### ( Get spy details ) ########################

spy_name = 'Bond'
spy_salutation = 'Mr.'
spy_age = 23
spy_rating = 4.7

######################## adding a friend ########################
friends = []
friends_name = []
friends_rating = []
friends_age = []
friends_is_online = []
friends_status = []


def add_friends():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats' : []

    }
    new_friend['name'] = raw_input("Please add your friend\'s name:")
    new_friend['salutation'] = raw_input("Are they Mr or Mrs? ")
    new_friend['name'] = new_friend['salutation'] + ". " + new_friend['name']
    new_friend['age'] = int(raw_input("Age?"))
    new_friend['rating'] = float(raw_input("Spy rating?"))
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50 and new_friend[
        'rating'] >= spy_rating:
        friends.append(new_friend)
        with open('friends.csv','a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend['name'], new_friend['salutation'], new_friend['rating'], new_friend['age']])
        print(colored("Friend added!!!","blue"))
    else:
        print('Sorry! we can\'t add spy with the details you provided')
    return len(friends)


############## function to send a message ##############
from steganography.steganography import Steganography
from datetime import datetime


friend = []
def send_message():
    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image")
    output_path = 'output_image.png'
    text = raw_input("What do you want to say?")
    print(text)
    Steganography.encode(original_image, output_path, text)
    new_chat={
        "message":text,
        "time":datetime.now(),
        "Sent_by_me":True
    }
    friends[friend_choice]['chats'].append(new_chat)
    with open("chats.csv", 'a') as chats_data:
        write = csv.writer(chats_data)
        write.writerow([friends[friend_choice].name, text, new_chat.time, new_chat.sent_by_me])

    print("Your secret message is ready!!!")
    print (friend)




def read_message():
    sender = select_friend()
    output_file = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_file)
    print(secret_text)
    new_chat={
        "message":secret_text,
        "time":datetime.now(),
        "sent_by_me":False

    }
    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"

    with open("chats.csv", 'ab') as chats_data:
        write = csv.writer(chats_data)
        write.writerow([friends[sender].name, secret_text, new_chat.time, new_chat.sent_by_me])

    print "Your secret message has been saved!"

######################## for loading friends from friends.csv ##################################
def load_friends():
    with open('friends.csv', 'r') as friends_data:
        reader = csv.reader(friends_data)
        new_friend=[]

        for row in reader:
            #spy = Spy(name=row[0], salutation=row[1], age=int(row[3]), rating=float(row[2]))
            new_friend['name'] = row[0]
            new_friend['salutation'] = row[1]

            new_friend['age'] = row[3]
            new_friend['rating'] = row[2]
            friends.append(new_friend)


######################## function to select a friend  ################

def select_friend():
    item_number = 0
    for friend in friends:
        print("%d. %s" % ((item_number), friend['name']))
        item_number = item_number + 1
    friend_choice = int(raw_input("Choose from your friends"))
    friend_choice_position = friend_choice - 1
    return friend_choice_position


##################### function to add and update status #############
STATUS_MESSAGES = ['My name is James Bond', 'I am SPY', 'shaken, not stirred']  ##### list that stores status


def add_status(current_status_message):
    if current_status_message != None:
        print("Your current status message is " + current_status_message + "\n")
    else:
        print("You don\'t have any status message currently\n")

    default = raw_input("Do you want to select from the older status(y/n)?")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
            # current_status_message = updated_status_message
    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print("%d. %s" % (item_position, message))
            item_position = item_position + 1
        message_selection = int(raw_input("\n Choose from the above message."))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            # current_status_message = update_status_message
    return updated_status_message


#################### function to choose menu ##############


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None;
    show_menu = True
    load_friends()
    while show_menu:
        print( colored("What do you want to do? \n 1) Add a status update 2) Add a friend 3) Send a secret message 4) Read a secret message 5) Read chats from a user 6) Show friend 7) Close application","blue"))
        menu_choice = raw_input()

        # Add Status Update
        if menu_choice == "1":
            print("You chose to update status")
            current_status_message = add_status(current_status_message)

        # Add friends
        elif menu_choice == "2":
            number_of_friend = int(add_friends())
            print("You have %d friends" % (number_of_friend))

        # Send secret message
        elif menu_choice == "3":
            send_message()

        # Read secret message
        elif menu_choice == "4":
            read_message()

        elif menu_choice == "6":
            for data in friends:
                print("Name is " + str(data.name) + " age is " + str(data.age) + " rating is " + str(data.rating))

                # read_old_chat()
            pass



        elif menu_choice == "7":
            show_menu = False
        # Exit Application


print(colored("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?","green"))
existing = raw_input()

if existing == "Y" or existing == "y":
    start_chat(spy_name, spy_age, spy_rating)
else:
    ####### get spyname and welcome him ########
    spy_name = int(raw_input("Welcome to spy chat, you must tell me your spy name first:\n"))
    if len(spy_name) > 0:
        print("Welcome!!! " + spy_name + ". Glad to have you back with us.")
        ########## get spy's gender #######
        spy_salutation = input("What shall we call you (Mr. or Mrs.?)")
        ######### concatinate salutation and name ########
        spy_name = spy_salutation + " " + spy_name
        ######### get more details from spy ###########
        print("Alright " + spy_name + ". I'd like to know a little bit more about...")


    else:  ########### if the spy inputs a space #############
        print("A Spy needs to have a valid name. Try again please. ")

    ############## initialize spy_age, spy_rating, and spy_is_online ##################
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    ################### input spy_age #####################
    spy_age = int(raw_input("What is your age?"))
    print(type(spy_age))

    ##################### checking whether spy is of correct age and input rating of spy ######################
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(raw_input("What is your spy rating?"))

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

    print ("Authentication complete. Welcome %s of age: %d and rating of: %.1f. Proud to have you onboard." % (
    spy_name, spy_age, spy_rating))
