filename = '/home/bambo/Desktop/cal.txt'
meet_title = []
meet_len = []
meet_start = []
meet_end = []
x = True
print('\nHey, I\'m interactive calendar !')
print('\nPlease don\'t quit program with  ctrl + C ! Want to quit? Use \'q\'! \n')
while x == True:
    n = 0
    print('\nYour schedule for the day: \n')
    for meet in meet_title:
        print( meet_start[n], '-', meet_end[n], ' ', meet_title[n])
        n = n+1
    if not meet_title:
        print('(empty)\n')
    else:
        duration = sum(meet_len)
        print('\nTotal meeting duration: ', duration)

    print('\nMenu:\n'+'(s) schedule a new meeting\n' + '(c) cancel an existing meeting\n' + '(q) quit\n')
    option = input()
    if option != 's' and option != 'c' and option != 'q':
        print('\nMenu:\n'+'(s) schedule a new meeting\n' + '(c) cancel an existing meeting\n' + '(q) quit\n')

    if option == 's':
        print('\nYour choice: s\n'
            'Schedule a new meeting.\n')
        meetlist = ['(empty)']
        meetlist.remove('(empty)')
        a = input('co to za spotkanko byku?\n')
        b = int(input('ile tam posiedzisz se ? 1 or 2 hours meet ?\n'))
        if b < 1:
            print('Meeting time has to be 1 or 2 hours')
        else:
            if b > 2:
                print('Meeting time has to be 1 or 2 hours')
            else:
                c = int(input('na ktora godzine sie umawiasz ?\n'))
                if c in meet_start:
                    print('\nERROR: Meeting overlaps with existing meeting!!\n')
                elif c < 8:
                    print('\nERROR: Meeting is outside of your working hours (8 to 18)!\n')
                else:
                    d = c + b
                    if d > 18:
                        print('\nERROR: Meeting is outside of your working hours (8 to 18)!\n')
                    elif d in meet_end:
                        print('\nERROR: Meeting overlaps with existing meeting!\n')
                    else:
                        meet_title.append(a)
                        meet_len.append(b)
                        if c != 8:
                            if meet_start != []:
                                o = c - max(meet_end)
                            c = 8
                            d = c + b
                            for c in meet_start:
                                if b == 1:
                                    print('\nMeeting will be ' + str(o) + ' hour(s) earlier')
                                    c = max(meet_end)
                                    d = c + b
                                elif b == 2:
                                    print('\nMeeting will be ' + str(o) + ' hour(s) earlier')
                                    c = max(meet_end)
                                    d = c + b
                        meet_start.append(c)
                        meet_end.append(d)
                        print('\nMeeting added.\n')
                        a = str(a)
                        d = str(d)
                        c = str(c)
                        note = c, d, a
                        note = str(note)
                        with open(filename,'a') as filex:
                            note = note.replace('(', '')
                            note = note.replace(')', '')
                            note = note.replace('\'', '')
                            filex.write(note)
                            filex.write('\n')

    if option =='c':
        print('\nYour choice: c\n'
            'Cancel an existing meeting.\n')
        e = int(input('Enter the start time of meeting you want cancel: \n'))

        if e not in meet_start:
            print('\nNie masz o tej godzinie spotkania\n')
        if e in meet_start:
            v = meet_start.index(e)
            meet_len.pop(v)
            meet_start.pop(v)
            meet_end.pop(v)
            meet_title.pop(v)
            print('\nMeeting canceled.\n')
            e = str(e)
            with open(filename,'r') as filex:
                lines = filex.readlines()
            with open(filename, 'w') as filex:
                for line in lines:
                    bang = line[0:2]
                    if e not in bang.strip('\n'):
                        filex.write(line)

    if option == 'q':
        open(filename, "w").close()
        meet_title.clear()
        meet_len.clear()
        meet_start.clear()
        meet_end.clear()
        print('OK bye !')
        break
