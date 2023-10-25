import tkinter


BMI_dictionary = { "Underweight": 18.4, 
                   "Normal weight": 24.9, 
                   "Overweight": 29.9, 
                   "Obesity": 39.9, 
                   "Extreme obesity": 40 }


def check_validation():
    
    global weight
    global length

    try:

        weight = int(kg_entry.get())
        length = int(cm_entry.get())
        return True
         
    except:
        
        result_label.config(text="It is not a valid value")
        return False
    


def BMI_calculator():

    if check_validation():

        length_m = length/100
        BMI_value = weight/(length_m ** 2)

        for key, value in BMI_dictionary.items():

            print(f"key: {key}, value: {value}")
            
            if BMI_value < value:
                 
                result_label.config(text=f"BMI value: {BMI_value:.2f}\n You are {key}")
                break

            elif BMI_value > BMI_dictionary.get("Extreme obesity"):

                result_label.config(text=f"BMI value: {BMI_value:.2f}\n You are Extreme obesity")
                break
                
        
            


def button_clicked():
    
    # result_label.config(text="button clicked")

    BMI_calculator()



def start_widow():
    

    #Window

    window = tkinter.Tk()
    window.title("BMI Calculator")
    window.minsize(width=250, height=160)
    window.config(padx=20,pady=20)


    #Widget
    
    global kg_label
    global cm_label
    global kg_entry
    global cm_entry 
    global result_label 

    kg_label = tkinter.Label(text="Enter Your Weight (kg)", fg="black", font=("",11,""))
    cm_label = tkinter.Label(text="Enter Your Height (cm)", fg="black", font=("",11,""))
    kg_entry = tkinter.Entry(width=20)
    cm_entry = tkinter.Entry(width=20)
    result_label = tkinter.Label(font=("",11,""))
    

    # button

    calculation_button = tkinter.Button(text="Calculate", width=15,bg="orange", command= button_clicked)


    # packing wiindow

    kg_label.pack()
    kg_entry.pack()
    cm_label.pack()
    cm_entry.pack()
    calculation_button.pack()
    result_label.pack()

    tkinter.mainloop()


start_widow()
