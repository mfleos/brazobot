from tkinter import *
from tkinter import ttk

from serial import *

connected = False
currentPort = ""

def move_motor(num_btn):
    port = str_port.get()
    print( "Hola", num_btn, port )
    if connected == True:
        fserial.write(num_btn)

def connectPort():
    port = str_port.get()
    str_port_status.set("Disconnected")
    if len(port) > 0:
        print( "Connecting to port:", port )
        currentPort = port
        try:
            fserial = Serial(
                    port=currentPort,
                    baudrate=9600,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS
                    )
            str_port_status.set("Connected to", currentPort)
        except SerialException:
            print( "Port not found. Specify another" )
            str_error.set("Not found" )
            return
            
    else:
        print( "Please specify an available Port" )
        str_error.set("Port not found. Specify another")

    fserial.open()

    if fserial.isOpen():
        connected = True
    else:
        connected = False
        currentPort = ""

root = Tk()
root.title( "Motor Control v0.1" )

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

str_port = StringVar()
str_error = StringVar()
str_port_status = StringVar()

ttk.Label(mainframe, text="Port:").grid(column=1, row=1, sticky=(W,E))
port_entry = ttk.Entry( mainframe, width=7, textvariable=str_port)
port_entry.grid( column=2, row=1, sticky=(W,E))
port_btn = ttk.Button(mainframe, width=7, text="Set Port", command=lambda: connectPort())
port_btn.grid( column=3, row=1, sticky=(W,E))

m1_btn = ttk.Button(mainframe, width=7, text="Motor 1", command=lambda: move_motor(1))
m1_btn.grid( column=1, row=3, sticky=(W,E))
m2_btn = ttk.Button(mainframe, width=7, text="Motor 2", command=lambda: move_motor(2))
m2_btn.grid( column=2, row=3, sticky=(W,E))
m3_btn = ttk.Button(mainframe, width=7, text="Motor 3", command=lambda: move_motor(3))
m3_btn.grid( column=3, row=3, sticky=(W,E))
m4_btn = ttk.Button(mainframe, width=7, text="Motor 4", command=lambda: move_motor(4))
m4_btn.grid( column=1, row=4, sticky=(W,E))
m5_btn = ttk.Button(mainframe, width=7, text="Motor 5", command=lambda: move_motor(5))
m5_btn.grid( column=2, row=4, sticky=(W,E))

ttk.Label(mainframe, textvariable=str_error).grid(column=1, row=5, columnspan=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=str_port_status).grid(column=3, row=5, sticky=(W,E))
'''
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet )
feet_entry.grid( column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
btn_test = ttk.Button(mainframe, text="Test Button")
btn_test.grid(column=1, row=3, sticky=E)

ttk.Label(mainframe, text="feet").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
'''
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
'''
feet_entry.focus()
root.bind('<Return>', calculate)'''

root.mainloop()
