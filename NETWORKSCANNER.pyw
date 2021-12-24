#NETWORKSCANNER
#Filip Rokita
#www.filiprokita.com

#import
import ipaddress
import tkinter as tk
import socket

#def
def scan():
    ip = ipVar.get()
    mask = maskVar.get()
    networkip = str(f'{ip}/{mask}')
    net4 = ipaddress.ip_network(networkip)





#main
if __name__ == '__main__':
    root = tk.Tk()
    root.title('NETWORKSCANNER')
    root.geometry('300x300')
    root.resizable(False, False)

    ipVar = tk.StringVar()
    maskVar = tk.StringVar()

    ipL = tk.Label(root, text='NETWORK IP'); ipL.pack()
    ipE = tk.Entry(root, textvariable=ipVar); ipE.pack()
    maskOM = tk.OptionMenu(root, maskVar, '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1'); maskOM.pack()
    scanB = tk.Button(root, text='SCAN', command=scan); scanB.pack(pady=10)
    authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

    root.mainloop()