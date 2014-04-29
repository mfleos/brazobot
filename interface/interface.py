from tkinter import *
from tkinter import ttk

from serial import *

'''Enums'''
def enum(**enums):
    return type( 'Enum', (), enums)	

def move_motor(num_btn, direction):
    port = str_port.get()
    print( "Hola", num_btn, port, direction )
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

def createInterface():
    root.title( "Brazobot Interface v0.02" )

    mainframe = ttk.Frame(root, padding="5 5 12 12")
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Port:").grid(column=1, row=1, sticky=(W,E))
    port_entry = ttk.Entry( mainframe, width=7, textvariable=str_port )
    port_entry.grid( column=2, row=1, sticky=(W, E))
    port_btn = ttk.Button( mainframe, width=7, text="Set Port", command=lambda: connectPort())
    port_btn.grid( column=3, row=1, sticky=(W,E))

    # Motor 1
    ttk.Label(mainframe, text="Motor 1").grid(column=1, row=3, sticky=(W,E))
    motor_btn = ttk.Button(mainframe, width=7, text="UP1", command=lambda: move_motor( 1, direction.UP))
    motor_btn.grid( column=1, row=4, sticky=(W,E) )
    motor_btn = ttk.Button(mainframe, width=7, text="DOWN1", command=lambda: move_motor( 1, direction.DOWN ))
    motor_btn.grid( column=1, row=5, sticky=(W,E) )
    # Motor 2
    ttk.Label(mainframe, text="Motor 2").grid(column=2, row=3, sticky=(W,E))
    motor_btn = ttk.Button(mainframe, width=7, text="UP2", command=lambda: move_motor( 2, direction.UP))
    motor_btn.grid( column=2, row=4, sticky=(W,E) )
    motor_btn = ttk.Button(mainframe, width=7, text="DOWN2", command=lambda: move_motor( 2, direction.DOWN ))
    motor_btn.grid( column=2, row=5, sticky=(W,E) )
    # Motor 3
    ttk.Label(mainframe, text="Motor 3").grid(column=3, row=3, sticky=(W,E))
    motor_btn = ttk.Button(mainframe, width=7, text="UP3", command=lambda: move_motor( 3, direction.UP))
    motor_btn.grid( column=3, row=4, sticky=(W,E) )
    motor_btn = ttk.Button(mainframe, width=7, text="DOWN3", command=lambda: move_motor( 3, direction.DOWN ))
    motor_btn.grid( column=3, row=5, sticky=(W,E) )
    # Motor 4
    ttk.Label(mainframe, text="Motor 4").grid(column=4, row=3, sticky=(W,E))
    motor_btn = ttk.Button(mainframe, width=7, text="UP4", command=lambda: move_motor( 4, direction.UP))
    motor_btn.grid( column=4, row=4, sticky=(W,E) )
    motor_btn = ttk.Button(mainframe, width=7, text="DOWN4", command=lambda: move_motor( 4, direction.DOWN ))
    motor_btn.grid( column=4, row=5, sticky=(W,E) )
    # Motor 5
    ttk.Label(mainframe, text="Motor 5").grid(column=5, row=3, sticky=(W,E))
    motor_btn = ttk.Button(mainframe, width=7, text="UP5", command=lambda: move_motor( 5, direction.UP))
    motor_btn.grid( column=5, row=4, sticky=(W,E) )
    motor_btn = ttk.Button(mainframe, width=7, text="DOWN5", command=lambda: move_motor( 5, direction.DOWN ))
    motor_btn.grid( column=5, row=5, sticky=(W,E) )

    ttk.Label(mainframe, textvariable=str_error).grid(column=1, row=6, columnspan=2, sticky=(W,E))
    ttk.Label(mainframe, textvariable=str_port_status).grid(column=3, row=6, sticky=(W,E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=6, pady=6)

direction = enum(UP=1, DOWN=2)

connected = False
currentPort = ""

root = Tk()
str_port = StringVar()
str_error = StringVar()
str_port_status = StringVar()

createInterface()

root.mainloop()
