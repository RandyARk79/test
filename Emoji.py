def msg(sta):
    sta= sta.title()
    fgt = sta.split()
    emoji={
        ':)':'😊😊',
        ':(': '😒'
    }
    output=''
    for ch in fgt:
        output+= emoji.get(ch, ch)+" "

    return output

print('Enter your msg:')
x=msg(sta=input())
print(x)