#NETWORKSCANNER
#Filip Rokita
#www.filiprokita.com

#import
import tkinter as tk
import ipaddress
import subprocess

#def
def scan():
    scanB.configure(text='SCANNING...', state=tk.DISABLED)
    
    networkAddr = networkVar.get()
    network = ipaddress.ip_network(networkAddr)

    spinfo = subprocess.STARTUPINFO()
    spinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    spinfo.wShowWindow = subprocess.SW_HIDE

    online = ''
    for host in network.hosts():
        root.update()
        host = str(host)
        output = subprocess.Popen(['ping', '-n', '1', '-w', '100', host], stdout=subprocess.PIPE, startupinfo=spinfo).communicate()[0]
        print(output)
        if 'Received = 1' in output.decode('utf-8'):
            online = online + f'{host} is Online\n'

    f = open('NETWORKSCANNER-RESULTS.txt', 'w')
    f.write(online)
    f.close()

    subprocess.Popen(['notepad', 'NETWORKSCANNER-RESULTS.txt'])

    scanB.configure(text='SCAN', state=tk.NORMAL)

#main
if __name__ == '__main__':
    root = tk.Tk()
    root.title('NETWORKSCANNER')
    root.geometry('300x150')
    root.resizable(False, False)

    networkVar = tk.StringVar()

    networkL = tk.Label(root, text='NETWORK ADDRESS\n(e.g. 192.168.0.0/24)'); networkL.pack()
    networkE = tk.Entry(root, textvariable=networkVar, justify=tk.CENTER); networkE.pack()
    scanB = tk.Button(root, text='SCAN', command=scan, width=10); scanB.pack(pady=5)
    authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

    root.mainloop()