options= True
start=False
while options:
    options= input(">>")
    if options == 'start':
        if start:
            print('The car has been already started')
        else:
            print('''The car has started. and going''')
            start=True
    elif options == "help":
        print('start - To start car \nstop to stop car \nquit - To Quit')

    elif options == 'fast':
        print('''the car is going fast''')
    elif options == 'quit':
        print('''You quit the game''')
        break
    elif options == 'stop':
        print('''the car has stopped.''')
    else:
        print('I Cant get it')