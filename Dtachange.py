def date_(st):
    monthdic ={
        '01':'January',
        '02' :'Febrary',
        '03': 'March',
        '04' : 'April',
        '05' :'May',
        '06' :'June',
        '07' :'July',
        '08' :'August',
        '09' :'September',
        '10' :'October',
        '11' : 'November',
        '12' : 'December'
    }

    day,time=st.split(' ')
    day,month,year=day.split('.')
    clock,minute=time.split(':')
    print(f"{int(day)} {monthdic[ month]} {int(year)} year {int(clock)} hours {int(minute)} minutes")
sentence = input("enter the date:ex 01.01.2000 12:39  ")
date_(sentence)