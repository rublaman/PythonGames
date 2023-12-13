import tkinter


def button_clicked():
    result = int(input_miles.get()) * 1.60934
    result = round(result, 2)
    label_km_result.config(text=result)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_is_equal_to = tkinter.Label(text="is equal to")
label_is_equal_to.grid(column=0, row=1)

label_km_result = tkinter.Label(text="0")
label_km_result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)

button_calculate = tkinter.Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=2)





window.mainloop()
