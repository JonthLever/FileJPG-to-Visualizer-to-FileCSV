import pytesseract
import cv2 
import tkinter as tk
from tkinter import ttk

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Auxiliarconta\AppData\Local\Tesseract-OCR\tesseract.exe'

image = cv2.imread('Pana1857.jpg')
text = pytesseract.image_to_string(image, config='--psm 1 --oem 3') 

char = text.splitlines()
char_clean=[s for s in char if s !='']
subarray_size=25

def takes(arreglo):
    subarrays = []
    for i in range(0, len(arreglo), subarray_size):
        subarray = arreglo[i:i + subarray_size]
        subarrays.append(subarray) 
    return subarrays  
recuted=takes(char_clean)

def reorder(arreglo2):
    reorder_array=[]
    x_array=[]
    for x in range (len(arreglo2[0])):
        x_array=[str(arreglo2[0][x]),str(arreglo2[1][x]),str(arreglo2[2][x])]
        reorder_array.append(x_array)
    return reorder_array
reord=reorder(recuted)


#=======================================GUI=======================================#
root = tk.Tk()

root.geometry("600x600")
root.pack_propagate(0)
root.resizable(0, 0)



frame1 = tk.LabelFrame(root, text="This is a LabelFrame containing a Treeview")
frame1.place(height=300, width=600)


button1 = tk.Button(root, text="Refresh Table", command=lambda: Refresh_data())
button1.place(rely=0.65, relx=0.60)



tv1 = ttk.Treeview(frame1) 
column_list_account = ["Producto", "Cantidad", "Costo x Unidad"]  
tv1['columns'] = column_list_account  
tv1["show"] = "headings"  

for column in column_list_account:  
    tv1.heading(column, text=column)  
    tv1.column(column, width=50)  
tv1.place(relheight=1, relwidth=1)  
treescroll = tk.Scrollbar(frame1) 
treescroll.configure(command=tv1.yview) 
tv1.configure(yscrollcommand=treescroll.set)  
treescroll.pack(side="right", fill="y")  


def Load_data():
    for row in reord:
        tv1.insert("", "end", values=row)


def Refresh_data():
    tv1.delete(*tv1.get_children())

    Load_data()
    button2 = tk.Button(root, text="Export CSV", command=lambda: Export_data(recuted))
    button2.place(rely=0.65, relx=0.20)
    
def Export_data(recuteds):

    outfile = open("result-v2.csv", "w")
    for x in range (len(recuteds[0])):
        outfile.write(str(recuteds[0][x]) + '%' + str(recuteds[1][x]) + '%' + str(recuteds[2][x]))
        outfile.write('\n')
        frame2 = tk.Label(root, text="En tu aplicacion Excel, ve a Datos->Datos en Columnas->Delimitado->Otro \n y escribe el simbolo % para tener los datos tabulados")
        frame2.place(rely=0.75, relx=0.15)
    outfile.close()




root.mainloop()

#=======================================================================================#


