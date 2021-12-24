#NETWORKSCANNER
#Filip Rokita
#www.filiprokita.com

#import
import tkinter as tk
import ipaddress
import os

#def
def scan():
    scanB.configure(text='SCANNING...', state=tk.DISABLED)
    
    networkAddr = networkVar.get()
    network = ipaddress.ip_network(networkAddr)

    online = ''
    for host in network.hosts():
        root.update()
        host = str(host)
        if os.system(f'ping -n 1 -w 100 {host}') == 0:
            online = online + f'{host} is Online\n'

    f = open('NETWORKSCANNER-RESULTS.txt', 'w')
    f.write(online)
    f.close()

    os.system('start notepad NETWORKSCANNER-RESULTS.txt')

    scanB.configure(text='SCAN', state=tk.NORMAL)





#main
if __name__ == '__main__':
    root = tk.Tk()
    root.title('NETWORKSCANNER')
    root.geometry('300x150')
    root.resizable(False, False)

    networkVar = tk.StringVar()

    networkL = tk.Label(root, text='NETWORK ADDRESS\n(eg. 192.168.0.0/24)'); networkL.pack()
    networkE = tk.Entry(root, textvariable=networkVar); networkE.pack()
    scanB = tk.Button(root, text='SCAN', command=scan, width=10); scanB.pack(pady=5)
    authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

    root.mainloop()