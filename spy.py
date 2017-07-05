from steganography.steganography import Steganography
from spyclass import spy, Spy, chat_message, friends

status=['hey! how you doin','being lazy is a new trend','programmers on work']
print 'Welcome to spy_chat'

input='Do you want to continue as '+spy.salutation + ' '  + spy.name + '\nPress 1 for yes \nPress 2 for no'
exist=raw_input(input)

def add_status():
    updated_status= None
    if spy.current_status!= None:
        print('Your current status message is %s \n' % (spy.current_status))
    else:
        print('You don\'t have any status right now\n')

    default = raw_input('Do you want to select from the older status?\nPress 1 for yes OR 2 for no')

    if default.upper()=='2':
        new_status=raw_input("enter your status:")
        if len(new_status)>0:

            status.append(new_status)
            updated_status == new_status
    elif default.upper()== '1':

        item_position = 1
        for message in status:

            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        status_select = int(raw_input('\nChoose status'))
        if len(status) >= status_select:
            updated_status = status[status_select-1]

    else:
        print('INVALID OPTION! Press either yes or no')

    if updated_status:
        print('Your updated status is: %s'%(updated_status))
    else:
        print('No status right now')

    return updated_status

def add_friend():

    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input('enter your friend\'s name: ')
    new_friend.salutation = raw_input('Are they Mr. or Ms.?: ')

    new_friend.name = new_friend.salutation + ' ' + new_friend.name

    new_friend.age = raw_input('AGE please')
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input('RATING')
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend successfully added'
    else:
        print('Not eligible for the SPYCHAT')

    return len(friends)
def select_friend():
    item_number = 0

    for friend in friends:
        print('%d. %s %s aged %d with rating %.2f is online'% (item_number +1, friend.salutation, friend.name,friend.age,friend.rating))
        item_number = item_number + 1

    friend_choice = raw_input('Choose from your friends')
    friend_choice_pos = int(friend_choice) - 1
    return friend_choice_pos

def send_message():
    friend_choice = select_friend()
    original_image = raw_input('Enter name of the image-> ')
    output_path = 'sam'
    text = raw_input('Write a SECRET TEXT-> ')
    Steganography.encode(original_image, output_path, text)

    new_chat = chat_message(text,True)

    if len(text) > 0:
        print 'GREAT!Text is encoded '
        friends[friend_choice].chats.append(new_chat)
    else:
        print 'Something went wrong!'
        send_message()

def read_message():
    sender = select_friend()
    output_path = raw_input('Enter file name->')
    secret_text = Steganography.decode(output_path)
    new_chat = chat_message(secret_text, False)
    friends[sender].chats.append(new_chat)
    print "Your secret message is : " + secret_text

def read_chat_history():

    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print('[%s]'%chat.time.strftime('%d %B %Y'))
            print('%s'%'you said : ')
            print '%s' %chat.message
        else:
            print('[%s]' % chat.time.strftime('%d %B %Y'))
            print('%s said : '% friends[read_for].name)
            print '%s' %chat.message

def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        print 'Welcome\n' + spy.name +  '\nage : '  + str(spy.age) + '\nRating : ' + str(spy.rating)
        show_menu = True
        while show_menu:
            menu_choices = 'Choose anyone \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n'
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
        else:
            print'Thank you'

if exist == '1':
    start_chat(spy)
else:
    spy = Spy('','',0,0.0)
    spy.name = raw_input('Welcome to spy chat,enter your name->')
    if len(spy.name) > 0:
        spy.salutation = raw_input(' Mr. or Ms. or Miss.?-> ')

        spy.age = raw_input('Your Age please')
        spy.age = int(spy.age)

        spy.rating = raw_input('What\'s your spy rating-> ')
        spy.rating = float(spy.rating)
        start_chat(spy)




