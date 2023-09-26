import customtkinter as ctk

WINDOW_WIDTH=280
WINDOW_HEIGTH=382

root = ctk.CTk()
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGTH}')
root.minsize(WINDOW_WIDTH,WINDOW_HEIGTH)
root.maxsize(WINDOW_WIDTH,WINDOW_HEIGTH)
root.title('CTk Calculator')

calc_screen = ctk.CTkLabel(root, text='', height=40, width=260, font=('Arial', 24, 'bold'), fg_color='grey80', corner_radius=20, anchor='e', padx=5, text_color='black')
calc_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

calc = ''

def add_to_calc(char):
    global calc
    calc += str(char)
    calc_screen.configure(text=calc)

def eval_calc():
    global calc
    if calc=='':
        calc='0'
    try:
        calc = str(eval(calc))
        calc_screen.configure(text=calc)
    except ZeroDivisionError:
        calc_screen.configure(text='ERROR')
        calc=''

def clear_field():
    global calc
    calc=''
    calc_screen.configure(text='')


key1 = ctk.CTkButton(root, text='1', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('1'))
key1.grid(row=5, column=0, padx=2, pady=2)
key2 = ctk.CTkButton(root, text='2', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('2'))
key2.grid(row=5, column=1, padx=2, pady=2)
key3 = ctk.CTkButton(root, text='3', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('3'))
key3.grid(row=5, column=2, padx=2, pady=2)
key4 = ctk.CTkButton(root, text='4', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('4'))
key4.grid(row=4, column=0, padx=2, pady=2)
key5 = ctk.CTkButton(root, text='5', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('5'))
key5.grid(row=4, column=1, padx=2, pady=2)
key6 = ctk.CTkButton(root, text='6', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('6'))
key6.grid(row=4, column=2, padx=2, pady=2)
key7 = ctk.CTkButton(root, text='7', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('7'))
key7.grid(row=3, column=0, padx=2, pady=2)
key8 = ctk.CTkButton(root, text='8', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('8'))
key8.grid(row=3, column=1, padx=2, pady=2)
key9 = ctk.CTkButton(root, text='9', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('9'))
key9.grid(row=3, column=2, padx=2, pady=2)
key0 = ctk.CTkButton(root, text='0', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('0'))
key0.grid(row=6, column=0, padx=2, pady=2)
keyC = ctk.CTkButton(root, text='C', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=clear_field)
keyC.grid(row=2, column=0, padx=2, pady=2)
keyopen = ctk.CTkButton(root, text='(', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('('))
keyopen.grid(row=2, column=1, padx=2, pady=2)
keyclose = ctk.CTkButton(root, text=')', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc(')'))
keyclose.grid(row=2, column=2, padx=2, pady=2)
keydiv = ctk.CTkButton(root, text='/', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='cyan4', corner_radius=20, command=lambda: add_to_calc(' / '))
keydiv.grid(row=2, column=3, padx=2, pady=2)
keymult = ctk.CTkButton(root, text='*', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='cyan4', corner_radius=20, command=lambda: add_to_calc(' * '))
keymult.grid(row=3, column=3, padx=2, pady=2)
keymin = ctk.CTkButton(root, text='-', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='cyan4', corner_radius=20, command=lambda: add_to_calc(' - '))
keymin.grid(row=4, column=3, padx=2, pady=2)
keyplus = ctk.CTkButton(root, text='+', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='cyan4', corner_radius=20, command=lambda: add_to_calc(' + '))
keyplus.grid(row=5, column=3, padx=2, pady=2)
keydot = ctk.CTkButton(root, text='.', height= 60, width=60, font=('Arial', 24, 'bold'), fg_color='grey30', corner_radius=20, command=lambda: add_to_calc('.'))
keydot.grid(row=6, column=1, padx=2, pady=2)
keyresult = ctk.CTkButton(root, text='=', height= 60, width=130, font=('Arial', 24, 'bold'), fg_color='cyan4', corner_radius=20, command=eval_calc)
keyresult.grid(row=6, column=2, padx=2, pady=2, columnspan=2)


root.mainloop()
