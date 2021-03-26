def ism_mano(ism):
    user_message = str(ism)
    file=open('D:\ism.txt','r')
    for line in file:
        for pr in line.split(' '):
            if user_message in pr: #print(line)
                return line.capitalize()
    else:
        return "Bunday ism topilmadi!"
