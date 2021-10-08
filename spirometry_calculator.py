
import tkinter as tk
from tkinter import *
from tkinter import Text
# --- functions --- #
#Main root:
root = tk.Tk()
root.title("Spirometry Calculator")

#Imput variables:
height_get = tk.DoubleVar()
weight_get = tk.DoubleVar()
age_get = tk.DoubleVar()
patient_id = tk.StringVar()
measured_fvc = tk.DoubleVar()
measured_fev1 = tk.DoubleVar()
measured_fev1fvc = tk.DoubleVar()
measured_fef2575 = tk.DoubleVar()

#Output variables:
predicted_fvc_boys = tk.DoubleVar()
predicted_fvc_girls = tk.DoubleVar()
predicted_fev1_boys = tk.DoubleVar()
predicted_fev1_girls = tk.DoubleVar()
predicted_fef2575_boys = tk.DoubleVar()
predicted_fef2575_girls = tk.DoubleVar()
predicted_fev1fvc_boys = tk.DoubleVar()
predicted_fev1fvc_girls = tk.DoubleVar()

percent_predicted_fvc_boys = tk.DoubleVar()
percent_predicted_fvc_girls = tk.DoubleVar()
percent_predicted_fev1_boys = tk.DoubleVar()
percent_predicted_fev1_girls = tk.DoubleVar()
percent_predicted_fef2575_boys = tk.DoubleVar()
percent_predicted_fef2575_girls = tk.DoubleVar()
percent_predicted_fev1fvc_boys = tk.DoubleVar()
percent_predicted_fev1fvc_girls = tk.DoubleVar()

lln_predicted_fvc_boys = tk.DoubleVar()
lln_predicted_fvc_girls = tk.DoubleVar()
lln_predicted_fev1_boys = tk.DoubleVar()
lln_predicted_fev1_girls = tk.DoubleVar()
lln_predicted_fef2575_boys = tk.DoubleVar()
lln_predicted_fef2575_girls = tk.DoubleVar()
lln_predicted_fev1fvc_boys = tk.DoubleVar()
lln_predicted_fev1fvc_girls = tk.DoubleVar()

zscore_predicted_fvc_boys = tk.DoubleVar()
zscore_predicted_fvc_girls = tk.DoubleVar()
zscore_predicted_fev1_boys = tk.DoubleVar()
zscore_predicted_fev1_girls = tk.DoubleVar()
zscore_predicted_fef2575_boys = tk.DoubleVar()
zscore_predicted_fef2575_girls = tk.DoubleVar()
zscore_predicted_fev1fvc_boys = tk.DoubleVar()
zscore_predicted_fev1fvc_girls = tk.DoubleVar()

#------FUNCTION TO CALCULATE PREDICTED VALUES------#
#FVC functions:
#FVC boys functions:
def fvc_boys():
    try:
        result_fvc_boys = -2.322603 + (0.030837*float(height_get.get())) + (0.00305*float(weight_get.get())) + (0.009612*float(age_get.get()))
    except Exception as ex:
        print(ex)
        result_fvc_boys = 'error'
    result_fvc_boys = round(result_fvc_boys, 2)
    predicted_fvc_boys.set(result_fvc_boys)
    
#FVC girls functions:
def fvc_girls():
    try:
        result_fvc_girls = -3.897335 + (0.040381*float(height_get.get())) - (0.02474*float(weight_get.get())) + (0.06740*(float(weight_get.get())/((float(height_get.get())/100)*float(height_get.get())/100)))
    except Exception as ex:
        print(ex)
        result_fvc_girls = 'error'
    result_fvc_girls = round(result_fvc_girls, 2)
    predicted_fvc_girls.set(result_fvc_girls)

#FEV1 boys functions:
def fev1_boys():
    try:
        result_fev1_boys = -2.03101 + (0.02710*float(height_get.get())) + (0.02203*float(age_get.get()))
    except Exception as ex:
        print(ex)
        result_fev1_boys = 'error'
    result_fev1_boys = round(result_fev1_boys, 2)
    predicted_fev1_boys.set(result_fev1_boys)

#FEV1 girls functions:
def fev1_girls():
    try:
        result_fev1_girls = -3.012830 + (0.030310*float(height_get.get())) - (0.015603*float(weight_get.get())) + (0.035593*float(age_get.get())) + (0.049651*(float(weight_get.get())/((float(height_get.get())/100)*float(height_get.get())/100)))
    except Exception as ex:
        print(ex)
        result_fev1_girls = 'error'
    result_fev1_girls = round(result_fev1_girls, 2)
    predicted_fev1_girls.set(result_fev1_girls)

#FEF25/75 boys functions:
def fef2575_boys():
    try:
        result_fef2575_boys = 0.4493680  - (0.0001922*float(height_get.get())) + (0.0510957*float(age_get.get())) + (0.6790825*float(measured_fvc.get()))
    except Exception as ex:
        print(ex)
        result_fef2575_boys = 'error'
    result_fef2575_boys = round(result_fef2575_boys, 2)
    predicted_fef2575_boys.set(result_fef2575_boys)

#FEF25/75 girls fucntions:
def fef2575_girls():
    try:
        result_fef2575_girls = -1.23855 + (0.01240*float(height_get.get())) - (0.01284*float(weight_get.get())) + (0.74267*float(measured_fvc.get())) + (0.04417*(float(weight_get.get())/((float(height_get.get())/100)*float(height_get.get())/100)))
    except Exception as ex:
        print(ex)
        result_fef2575_girls = 'error'
    result_fef2575_girls = round(result_fef2575_girls, 2)
    predicted_fef2575_girls.set(result_fef2575_girls)

#FEV1/FVC boys functions:
def fev1fvc_boys():
    try:
        result_fev1fvc_boys = "89.96 (85.31-94.61)"
    except Exception as ex:
        print(ex)
        result_fev1fvc_boys = 'error'
    predicted_fev1fvc_boys.set(result_fev1fvc_boys)

#FEV1/FVC girls functions:
def fev1fvc_girls():
    try:
        result_fev1fvc_girls = "90.81 (86.18-95.44)"
    except Exception as ex:
        print(ex)
        result_fev1fvc_girls = 'error'
    predicted_fev1fvc_girls.set(result_fev1fvc_girls)

#------FUNCTIONS TO CALCULATE PERCENT %%PREDICTED VALUES------#
#FVC boys functions
def percent_fvc_boys():
    try:
        result_percent_fvc_boys = (float(measured_fvc.get())/float(predicted_fvc_boys.get()))*100
    except Exception as ex:
        print(ex)
        result_percent_fvc_boys = 'error'
    result_percent_fvc_boys = round(result_percent_fvc_boys, 2)
    percent_predicted_fvc_boys.set(result_percent_fvc_boys)

#FVC girls functions:
def percent_fvc_girls():
    try:
        result_percent_fvc_girls = (float(measured_fvc.get())/float(predicted_fvc_girls.get()))*100
    except Exception as ex:
        print(ex)
        result_percent_fvc_girls = 'error'
    result_percent_fvc_girls = round(result_percent_fvc_girls, 2)
    percent_predicted_fvc_girls.set(result_percent_fvc_girls)

#FEV1 boys functions:
def percent_fev1_boys():
    try:
        result_percent_fev1_boys = (float(measured_fev1.get())/float(predicted_fev1_boys.get()))*100
    except Exception as ex:
        print(ex)
        result_percent_fev1_boys = 'error'
    result_percent_fev1_boys = round(result_percent_fev1_boys, 2)
    percent_predicted_fev1_boys.set(result_percent_fev1_boys)

#FEV1 girls functions:
def percent_fev1_girls():
    try:
        result_percent_fev1_girls = (float(measured_fev1.get())/float(predicted_fev1_girls.get()))*100
    except Exception as ex:
        print(ex)
        result_percent_fev1_girls = 'error'
    result_percent_fev1_girls = round(result_percent_fev1_girls, 2)
    percent_predicted_fev1_girls.set(result_percent_fev1_girls)

#FEF25/75 boys functions:
def percent_fef2575_boys():
    try:
        result_percent_fef2575_boys = (float(measured_fef2575.get())/float(predicted_fef2575_boys.get()))*100
    except Exception as ex:
        print(ex)
        result__percent_fef2575_boys = 'error'
    result_percent_fef2575_boys = round(result_percent_fef2575_boys, 2)
    percent_predicted_fef2575_boys.set(result_percent_fef2575_boys)

#FEF25/75 girls fucntions:
def percent_fef2575_girls():
    try:
        result_percent_fef2575_girls = (float(measured_fef2575.get())/float(predicted_fef2575_girls.get()))*100
    except Exception as ex:
        print(ex)
        result_percent_fef2575_girls = 'error'
    result_percent_fef2575_girls = round(result_percent_fef2575_girls, 2)
    percent_predicted_fef2575_girls.set(result_percent_fef2575_girls)

#FEV1/FVC boys functions:
def percent_fev1fvc_boys():
    try:
        result_percent_fev1fvc_boys = (((float(measured_fev1.get()))/(float(measured_fvc.get()))/89.96)*100)*100
    except Exception as ex:
        print(ex)
        result_percent_fev1fvc_boys = 'error'
    result_percent_fev1fvc_boys = round(result_percent_fev1fvc_boys, 2)
    percent_predicted_fev1fvc_boys.set(result_percent_fev1fvc_boys)

#FEV1/FVC girls functions:
def percent_fev1fvc_girls():
    try:
        result_percent_fev1fvc_girls = (((float(measured_fev1.get()))/(float(measured_fvc.get()))/90.81)*100)*100
    except Exception as ex:
        print(ex)
        result_percent_fvc_girls = 'error'
    result_percent_fev1fvc_girls = round(result_percent_fev1fvc_girls, 2)
    percent_predicted_fev1fvc_girls.set(result_percent_fev1fvc_girls)

#------FUNCTIONS TO CALCULATE LLN VALUES------#
#FVC boys functions
def lln_fvc_boys(): 
    try:
        result_lln_fvc_boys = float(predicted_fvc_boys.get())-(1.64*0.34)
    except Exception as ex:
        print(ex)
        result_lln_fvc_boys = 'error'
    result_lln_fvc_boys = round(result_lln_fvc_boys, 2)
    lln_predicted_fvc_boys.set(result_lln_fvc_boys)

#FVC girls functions:
def lln_fvc_girls():
    try:
        result_lln_fvc_girls = float(predicted_fvc_girls.get())-(1.64*0.33)
    except Exception as ex:
        print(ex)
        result_lln_fvc_girls = 'error'
    result_lln_fvc_girls = round(result_lln_fvc_girls, 2)
    lln_predicted_fvc_girls.set(result_lln_fvc_girls)

#FEV1 boys functions:
def lln_fev1_boys():
    try:
        result_lln_fev1_boys = float(predicted_fev1_boys.get())-(1.64*0.29)
    except Exception as ex:
        print(ex)
        result_lln_fev1_boys = 'error'
    result_lln_fev1_boys = round(result_lln_fev1_boys, 2)
    lln_predicted_fev1_boys.set(result_lln_fev1_boys)

#FEV1 girls functions:
def lln_fev1_girls():
    try:
        result_lln_fev1_girls = float(predicted_fev1_girls.get())-(1.64*0.30)
    except Exception as ex:
        print(ex)
        result_lln_fev1_girls = 'error'
    result_lln_fev1_girls = round(result_lln_fev1_girls, 2)
    lln_predicted_fev1_girls.set(result_lln_fev1_girls)

#FEF25/75 boys functions:
def lln_fef2575_boys():
    try:
        result_lln_fef2575_boys = float(predicted_fef2575_boys.get())-(1.64*0.53)
    except Exception as ex:
        print(ex)
        result__lln_fef2575_boys = 'error'
    result_lln_fef2575_boys = round(result_lln_fef2575_boys, 2)
    lln_predicted_fef2575_boys.set(result_lln_fef2575_boys)

#FEF25/75 girls fucntions:
def lln_fef2575_girls():
    try:
        result_lln_fef2575_girls = float(predicted_fef2575_girls.get())-(1.64*0.53)
    except Exception as ex:
        print(ex)
        result_lln_fef2575_girls = 'error'
    result_lln_fef2575_girls = round(result_lln_fef2575_girls, 2)
    lln_predicted_fef2575_girls.set(result_lln_fef2575_girls)

#FEV1/FVC boys functions:
def lln_fev1fvc_boys():
    try:
        result_lln_fev1fvc_boys = 82.334
    except Exception as ex:
        print(ex)
        result_lln_fev1fvc_boys = 'error'
    result_lln_fev1fvc_boys = round(result_lln_fev1fvc_boys, 2)
    lln_predicted_fev1fvc_boys.set(result_lln_fev1fvc_boys)

#FEV1/FVC girls functions:
def lln_fev1fvc_girls():
    try:
        result_lln_fev1fvc_girls = 83.2168
    except Exception as ex:
        print(ex)
        result_lln_fvc_girls = 'error'
    result_lln_fev1fvc_girls = round(result_lln_fev1fvc_girls, 2)
    lln_predicted_fev1fvc_girls.set(result_lln_fev1fvc_girls)

#------FUNCTIONS TO CALCULATE Z-Score VALUES------#
#FVC boys functions
def zscore_fvc_boys(): 
    try:
        result_zscore_fvc_boys = (float(measured_fvc.get())-float(predicted_fvc_boys.get()))/0.34
    except Exception as ex:
        print(ex)
        result_zscore_fvc_boys = 'error'
    result_zscore_fvc_boys = round(result_zscore_fvc_boys, 2)
    zscore_predicted_fvc_boys.set(result_zscore_fvc_boys)

#FVC girls functions:
def zscore_fvc_girls():
    try:
        result_zscore_fvc_girls = (float(measured_fvc.get())-float(predicted_fvc_girls.get()))/0.33
    except Exception as ex:
        print(ex)
        result_zscore_fvc_girls = 'error'
    result_zscore_fvc_girls = round(result_zscore_fvc_girls, 2)
    zscore_predicted_fvc_girls.set(result_zscore_fvc_girls)

#FEV1 boys functions:
def zscore_fev1_boys():
    try:
        result_zscore_fev1_boys = (float(measured_fev1.get())-float(predicted_fev1_boys.get()))/0.29
    except Exception as ex:
        print(ex)
        result_zscore_fev1_boys = 'error'
    result_zscore_fev1_boys = round(result_zscore_fev1_boys, 2)
    zscore_predicted_fev1_boys.set(result_zscore_fev1_boys)

#FEV1 girls functions:
def zscore_fev1_girls():
    try:
        result_zscore_fev1_girls = (float(measured_fev1.get())-float(predicted_fev1_girls.get()))/0.30
    except Exception as ex:
        print(ex)
        result_zscore_fev1_girls = 'error'
    result_zscore_fev1_girls = round(result_zscore_fev1_girls, 2)
    zscore_predicted_fev1_girls.set(result_zscore_fev1_girls)

#FEF25/75 boys functions:
def zscore_fef2575_boys():
    try:
        result_zscore_fef2575_boys = (float(measured_fef2575.get())-float(predicted_fef2575_boys.get()))/0.53
    except Exception as ex:
        print(ex)
        result__zscore_fef2575_boys = 'error'
    result_zscore_fef2575_boys = round(result_zscore_fef2575_boys, 2)
    zscore_predicted_fef2575_boys.set(result_zscore_fef2575_boys)

#FEF25/75 girls fucntions:
def zscore_fef2575_girls():
    try:
        result_zscore_fef2575_girls = (float(measured_fef2575.get())-float(predicted_fef2575_girls.get()))/0.53
    except Exception as ex:
        print(ex)
        result_zscore_fef2575_girls = 'error'
    result_zscore_fef2575_girls = round(result_zscore_fef2575_girls, 2)
    zscore_predicted_fef2575_girls.set(result_zscore_fef2575_girls)

#FEV1/FVC boys functions:
def zscore_fev1fvc_boys():
    try:
        result_zscore_fev1fvc_boys = ((float(measured_fev1.get())/float(measured_fvc.get())*100)-89.96)/4.65
    except Exception as ex:
        print(ex)
        result_zscore_fev1fvc_boys = 'error'
    result_zscore_fev1fvc_boys = round(result_zscore_fev1fvc_boys, 2)
    zscore_predicted_fev1fvc_boys.set(result_zscore_fev1fvc_boys)

#FEV1/FVC girls functions:
def zscore_fev1fvc_girls():
    try:
        result_zscore_fev1fvc_girls = ((float(measured_fev1.get())/float(measured_fvc.get())*100)-90.81)/4.63
    except Exception as ex:
        print(ex)
        result_zscore_fvc_girls = 'error'
    result_zscore_fev1fvc_girls = round(result_zscore_fev1fvc_girls, 2)
    zscore_predicted_fev1fvc_girls.set(result_zscore_fev1fvc_girls)

# --- main ---
#Imput values:
enter_patient_id = Label(root, text="Enter patient ID:").grid(row=0, column=0)
enter_height = Label(root, text="Enter height:").grid(row=1, column=0)
enter_weight = Label(root, text="Enter weight:").grid(row=2, column=0)
enter_age = Label(root, text="Enter age:").grid(row=3, column=0)

tk.Entry(root, textvariable=patient_id).grid(row=0, column=1)
tk.Entry(root, textvariable=height_get).grid(row=1, column=1)
tk.Entry(root, textvariable=weight_get).grid(row=2, column=1)
tk.Entry(root, textvariable=age_get).grid(row=3, column=1)

enter_patient_fvc = Label(root, text="Enter measured FVC:").grid(row=0, column=2)
enter_patient_fev1 = Label(root, text="Enter measured FEV1:").grid(row=1, column=2)
enter_patient_fev1fvc = Label(root, text="Enter measured FEV1/FVC (optional)").grid(row=2, column=2)
enter_patient_fef25775 = Label(root, text="Enter measured FEF25-75:").grid(row=3, column=2)

tk.Entry(root, textvariable=measured_fvc).grid(row=0, column=3)
tk.Entry(root, textvariable=measured_fev1).grid(row=1, column=3)
tk.Entry(root, textvariable=measured_fev1fvc).grid(row=2, column=3)
tk.Entry(root, textvariable=measured_fef2575).grid(row=3, column=3)

tk.Label(root, text="--------------------------------------------------------------").grid(row=4, column=0, columnspan=5)

#Presenting results:
#Labels:
#Boys:
tk.Label(root, text="Expected").grid(row=5, column=1)
tk.Label(root, text="% predicted").grid(row=5, column=2)
tk.Label(root, text="LLN").grid(row=5, column=3)
tk.Label(root, text="Z-Score").grid(row=5, column=4)

calculated_fvc_boys = Label(root, text="FVC").grid(row=6, column=0)
calculated_fev1_boys = Label(root, text="FEV1").grid(row=7, column=0)
calculated_fev1_fvc_boys = Label(root, text="FEV1/FVC").grid(row=8, column=0)
calculated_fef2575_boys = Label(root, text="FEF25-75").grid(row=9, column=0)

#Girls:
tk.Label(root, text="Expected").grid(row=10, column=1)
tk.Label(root, text="% predicted").grid(row=10, column=2)
tk.Label(root, text="LLN").grid(row=10, column=3)
tk.Label(root, text="Z-Score").grid(row=10, column=4)

tk.Label(root, text="FVC").grid(row=11, column=0)
tk.Label(root, text="FEV1").grid(row=12, column=0)
tk.Label(root, text="FEV1/FVC").grid(row=13, column=0)
tk.Label(root, text="FEF25-75").grid(row=14, column=0)

#Entries:
#FVC Boys:
tk.Entry(root, textvariable=predicted_fvc_boys).grid(row=6, column=1)
tk.Entry(root, textvariable=percent_predicted_fvc_boys).grid(row=6, column=2)
tk.Entry(root, textvariable=lln_predicted_fvc_boys).grid(row=6, column=3)
tk.Entry(root, textvariable=zscore_predicted_fvc_boys).grid(row=6, column=4)
#FVC Girls:
tk.Entry(root, textvariable=predicted_fvc_girls).grid(row=11, column=1)
tk.Entry(root, textvariable=percent_predicted_fvc_girls).grid(row=11, column=2)
tk.Entry(root, textvariable=lln_predicted_fvc_girls).grid(row=11, column=3)
tk.Entry(root, textvariable=zscore_predicted_fvc_girls).grid(row=11, column=4)
#FEV1 Boys:
tk.Entry(root, textvariable=predicted_fev1_boys).grid(row=7, column=1)
tk.Entry(root, textvariable=percent_predicted_fev1_boys).grid(row=7, column=2)
tk.Entry(root, textvariable=lln_predicted_fev1_boys).grid(row=7, column=3)
tk.Entry(root, textvariable=zscore_predicted_fev1_boys).grid(row=7, column=4)
#FEV1 Girls:
tk.Entry(root, textvariable=predicted_fev1_girls).grid(row=12, column=1)
tk.Entry(root, textvariable=percent_predicted_fev1_girls).grid(row=12, column=2)
tk.Entry(root, textvariable=lln_predicted_fev1_girls).grid(row=12, column=3)
tk.Entry(root, textvariable=zscore_predicted_fev1_girls).grid(row=12, column=4)
#FEF2575 Boys:
tk.Entry(root, textvariable=predicted_fef2575_boys).grid(row=9, column=1)
tk.Entry(root, textvariable=percent_predicted_fef2575_boys).grid(row=9, column=2)
tk.Entry(root, textvariable=lln_predicted_fef2575_boys).grid(row=9, column=3)
tk.Entry(root, textvariable=zscore_predicted_fef2575_boys).grid(row=9, column=4)
#FEF2575 Girls:
tk.Entry(root, textvariable=predicted_fef2575_girls).grid(row=14, column=1)
tk.Entry(root, textvariable=percent_predicted_fef2575_girls).grid(row=14, column=2)
tk.Entry(root, textvariable=lln_predicted_fef2575_girls).grid(row=14, column=3)
tk.Entry(root, textvariable=zscore_predicted_fef2575_girls).grid(row=14, column=4)
#FEV1/FVC Boys:
tk.Entry(root, textvariable=predicted_fev1fvc_boys).grid(row=8, column=1)
tk.Entry(root, textvariable=percent_predicted_fev1fvc_boys).grid(row=8, column=2)
tk.Entry(root, textvariable=lln_predicted_fev1fvc_boys).grid(row=8, column=3)
tk.Entry(root, textvariable=zscore_predicted_fev1fvc_boys).grid(row=8, column=4)
#FEV1/FVC Girls:
tk.Entry(root, textvariable=predicted_fev1fvc_girls).grid(row=13, column=1)
tk.Entry(root, textvariable=percent_predicted_fev1fvc_girls).grid(row=13, column=2)
tk.Entry(root, textvariable=lln_predicted_fev1fvc_girls).grid(row=13, column=3)
tk.Entry(root, textvariable=zscore_predicted_fev1fvc_girls).grid(row=13, column=4)


button_boys = Button(root, text="Calculate for Boys", command=lambda:[fvc_boys(), fev1_boys(), fef2575_boys(), fev1fvc_boys(), percent_fvc_boys(), percent_fev1_boys(), percent_fef2575_boys(), percent_fev1fvc_boys(), lln_fvc_boys(), lln_fev1_boys(), lln_fef2575_boys(), lln_fev1fvc_boys(), zscore_fvc_boys(), zscore_fev1_boys(), zscore_fef2575_boys(), zscore_fev1fvc_boys()])
button_boys.grid(row=5, column=0)
button_girls = Button(root, text="Calculate for Girls", command=lambda:[fvc_girls(),fev1_girls(),fef2575_girls(), fev1fvc_girls(), percent_fvc_girls(), percent_fev1_girls(), percent_fef2575_girls(), percent_fev1fvc_girls(), lln_fvc_girls(), lln_fev1_girls(), lln_fef2575_girls(), lln_fev1fvc_girls(), zscore_fvc_girls(), zscore_fev1_girls(), zscore_fef2575_girls(), zscore_fev1fvc_girls()])
button_girls.grid(row=10, column=0)

tk.Label(root, text="--------------------------------------------------------------").grid(row=15, column=0, columnspan=5)

#------AUTO REPORT FUNCTION------#
auto_report_text = tk.StringVar()
auto_report_result = tk.StringVar()

def auto_report_function():
    if ((float(zscore_predicted_fvc_boys.get()) != 0) and (float(zscore_predicted_fvc_girls.get()) != 0)): #only one gender at a time
        auto_report_text = "Please, calculate values for boys and girls separatly"
    elif ((float(zscore_predicted_fvc_boys.get()) >= -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fev1_boys.get()) >= -1.64 and float(zscore_predicted_fev1_girls.get()) == 0) and (float(zscore_predicted_fef2575_boys.get()) >= -1.64 and float(zscore_predicted_fef2575_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) >= -1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #normal spirometry for boys
        auto_report_text = "All parameters are within normal range."
    elif ((float(zscore_predicted_fvc_boys.get()) < -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fef2575_boys.get()) >= -1.64 and float(zscore_predicted_fef2575_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) >= -1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #restrictive pattern boys
        auto_report_text = "Forced Vital Capacity is bellow the 5th percentile. This suggests a restrictive pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_girls.get()) >= -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fev1_girls.get()) >= -1.64 and float(zscore_predicted_fev1_boys.get()) == 0) and (float(zscore_predicted_fef2575_girls.get()) >= -1.64 and float(zscore_predicted_fef2575_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) == 0 and float(zscore_predicted_fev1fvc_girls.get()) >= -1.64)): #normal spirometry for girls
        auto_report_text = "All parameters are within normal range."
    elif ((float(zscore_predicted_fvc_girls.get()) < -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fef2575_girls.get()) >= -1.64 and float(zscore_predicted_fef2575_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) == 0 and float(zscore_predicted_fev1fvc_girls.get()) >= -1.64)): #restrictive pattern girls
        auto_report_text = "Forced Vital Capacity is bellow the 5th percentile. This suggest a restrictive pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_boys.get()) >= -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fev1_girls.get()) == 0) and (float(zscore_predicted_fef2575_boys.get()) < -1.64 and float(zscore_predicted_fef2575_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) >= -1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #small airways obstruction boys
        auto_report_text = "FEF25-75 is bellow the 5th percentile. This suggests small airways obstruction and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_girls.get()) >= -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fev1_boys.get()) == 0) and (float(zscore_predicted_fef2575_girls.get()) < -1.64 and float(zscore_predicted_fef2575_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_girls.get()) >= -1.64 and float(zscore_predicted_fev1fvc_boys.get()) == 0)): #small airways obstruction girls
        auto_report_text = "FEF25-75 is bellow the 5th percentile. This suggests small airways obstruction and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_boys.get()) >= -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fev1_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) < -1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #obstructive pattern boys
        auto_report_text = "FEV1/FVC ratio is bellow the 5th percentile. This suggests an obstructive pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_girls.get()) >= -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fev1_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_girls.get()) < -1.64 and float(zscore_predicted_fev1fvc_boys.get()) == 0)): #obstructive pattern girls
        auto_report_text = "FEV1/FVC ratio is bellow the 5th percentile. This suggests an obstructive pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_boys.get()) < -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) <-1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #mixed pattern boys
        auto_report_text = "Forced Vital Capacity and FEV1/FVC ratio are bellow the 5th percentile. This suggests a mixed pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_girls.get()) < -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_girls.get()) <-1.64 and float(zscore_predicted_fev1fvc_boys.get()) == 0)): #mixed pattern girls
        auto_report_text = "Forced Vital Capacity and FEV1/FVC ratio are bellow the 5th percentile. This suggests a mixed pattern and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_boys.get()) >= -1.64 and float(zscore_predicted_fvc_girls.get()) == 0) and (float(zscore_predicted_fev1_boys.get()) < -1.64 and float(zscore_predicted_fev1_girls.get()) == 0) and (float(zscore_predicted_fef2575_boys.get()) >= -1.64 and float(zscore_predicted_fef2575_girls.get()) == 0) and (float(zscore_predicted_fev1fvc_boys.get()) >= -1.64 and float(zscore_predicted_fev1fvc_girls.get()) == 0)): #FEV1 not specific pattern boys
        auto_report_text = "Forced Expiratory Volume in the first second is bellow the 5th percentile. This is an unspecific finding and deserves further medical investigation."
    elif ((float(zscore_predicted_fvc_girls.get()) >= -1.64 and float(zscore_predicted_fvc_boys.get()) == 0) and (float(zscore_predicted_fev1_girls.get()) < -1.64 and float(zscore_predicted_fev1_boys.get()) == 0) and (float(zscore_predicted_fef2575_girls.get()) >= -1.64 and float(zscore_predicted_fef2575_boys.get()) == 0) and (float(zscore_predicted_fev1fvc_girls.get()) >= -1.64 and float(zscore_predicted_fev1fvc_boys.get()) == 0)): #FEV1 not specific pattern girls
        auto_report_text = "Forced Expiratory Volume in the first second is bellow the 5th percentile. This is an unspecific finding and deserves further medical investigation."
    else:
        auto_report_text = "--error--"
    auto_report_result.set(auto_report_text)


auto_report = Button(root, text="Auto Report", command=auto_report_function)
auto_report.grid(row=16, column=0, columnspan=5)
report_auto_text = Entry(root, textvariable=auto_report_result)
report_auto_text.grid(row=17, column=0, columnspan=5, ipadx=400, ipady=20)

#canvas = Canvas(root, width = 200, height = 200)
#canvas.grid(row=0, column=4, rowspan=4)      
#img = PhotoImage(file="/Users/pixel/Documents/tkinter_gui/spirometry_calculator/fmup.png")      
#canvas.create_image(100,100, image=img) 

tk.Label(root, text="Based on: Development and Validation of Predictive Equations for Spirometry in Portuguese Children, 2021 ").grid(row=18, column=0, columnspan=5)


root.mainloop()