from tkinter import *
from tkinter import ttk
import tkinter as tk
root = Tk()

root = root
root.title("Vehicle Details")
root.geometry("1366x768+0+0")

# =================test tab=========
# Create Tab Control
TAB_CONTROL = ttk.Notebook(root)
# Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='General',)

# Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Attachment')
TAB_CONTROL.grid(row=0, column=0)

# Tab Name Labels
ttk.Label(TAB1, text="Vehicle details", foreground='orange', font=25,).grid(column=0, row=0, padx=10, pady=10)
ttk.Label(TAB2, text="Attachment").grid(column=0, row=0, padx=10, pady=10)


# =================Vehicle Details======================
sapcode = Label(TAB1, text="SAP Code",)
sapcode.grid(row=2, column=2, pady=10)
sapcodeentry = Entry(TAB1, width=27)
sapcodeentry.grid(row=2, column=3)

legendno = Label(TAB1, text="Ledger Number",)
legendno.grid(row=3, column=2, pady=10)
legendnoentry = Entry(TAB1, width=27)
legendnoentry.grid(row=3, column=3)




ttk.Label(TAB1, text="Manufacture", justify='left').grid(
    row=4, column=2, pady=10)
# Combobox creation
manufacturechoosen = ttk.Combobox(TAB1, width=27,)
manufacturechoosen['values'] = (' Mahindra & Mahindra Itd', ' Tata', ' BMW',)
manufacturechoosen.grid(row=4, column=3)
manufacturechoosen.current()

Modelno = Label(TAB1, text="Model",)
Modelno.grid(row=5, column=2, pady=10)
modelchoosen = ttk.Combobox(TAB1, width=27,)
modelchoosen['values'] = ('BOLERO CAMPER GOLD 2WD', 'Scarpio', 'Car',)
modelchoosen.grid(row=5, column=3)
modelchoosen.current()


vehicltyp = Label(TAB1, text="Vehicle Type",)
vehicltyp.grid(row=6, column=2, pady=10)

vechiletypechoosen = ttk.Combobox(TAB1, width=26,)
vechiletypechoosen['values'] = ('CAMPER', 'CAMPER1', 'CAMPER1',)
vechiletypechoosen.grid(row=6, column=3)
vechiletypechoosen.current()


base = Label(TAB1, text="Base KM",)
base.grid(row=7, column=2, pady=10)
baseentry = Entry(TAB1, width=27)
baseentry.grid(row=7, column=3)




rto = Label(TAB1, text="RTO",)
rto.grid(row=8, column=2, pady=10)

rtochoosen = ttk.Combobox(TAB1, width=26,)
rtochoosen['values'] = ('BARBIL,ODISHA', 'NOIDA,UP', 'NCR,DELHI',)
rtochoosen.grid(row=8, column=3)
rtochoosen.current()


ttk.Separator(TAB1, orient='horizontal').place(relx=0, rely=0.60, relwidth=1, relheight=1)
# ===================Engine Details============================
engineDetai = Label(TAB1, text="Engine Details", foreground='orange', font=25)
engineDetai.grid(row=9, column=0, pady=10)

Modelyear = Label(TAB1, text="Model Year",)
Modelyear.grid(row=10, column=2, pady=10)
yearchoosen = ttk.Combobox(TAB1, width=27,)
yearchoosen['values'] = ('1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
                         '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',)
yearchoosen.grid(row=10, column=3)
yearchoosen.current()

chassisno = Label(TAB1, text="Chassis No.",)
chassisno.grid(row=11, column=2, pady=10)
chassisnoentry = Entry(TAB1, width=27)
chassisnoentry.grid(row=11, column=3)


fuel = Label(TAB1, text="Fuel Type",)
fuel.grid(row=12, column=2, pady=10)
fuelchoosen = ttk.Combobox(TAB1, width=27,)
fuelchoosen['values'] = ('PETROL', 'DIESEL')
fuelchoosen.grid(row=12, column=3)
fuelchoosen.current()

oldvehicleno = Label(TAB1, text="Old Vehicle No.",)
oldvehicleno.grid(row=13, column=2, pady=10)
oldvehiclenoentry = Entry(TAB1, width=27)
oldvehiclenoentry.grid(row=13, column=3)


root.mainloop()
