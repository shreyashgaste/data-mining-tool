from sre_constants import MIN_UNTIL
from tkinter import *
from tkinter import filedialog
import pandas as pd
import math
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import operator
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import itertools
import numpy as np
from sklearn.tree import _tree
from sklearn import metrics
from tkinter import messagebox as mb
from sklearn.neighbors import KNeighborsClassifier
from joblib.numpy_pickle_utils import xrange
from numpy import log,dot,exp,shape
from sklearn.datasets import make_classification
import random
import sys
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse

def browseDataset():
    filename = filedialog.askopenfilename(initialdir="/",title="Select dataset", filetypes=(("CSV files", "*.csv*"), ("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    newfilename = ''
    print(filename)
    for i in filename:
        if i == "/":
            newfilename = newfilename + "/"
        newfilename = newfilename + i
    print(newfilename)
    data = pd.read_csv(filename)
    d = pd.read_csv(filename)
    w = Tk()
    w.title("2019BTECS00025-Data Analysis Tool")
    w.geometry("600x500")
    
    tv1 = ttk.Treeview(w)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = Scrollbar(w, orient="vertical", command=tv1.yview) 
    treescrollx = Scrollbar(w, orient="horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y") 
    tv1["column"] = list(data.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) 

    df_rows = data.to_numpy().tolist() 
    for row in df_rows:
        tv1.insert("", "end", values=row)
    
    # Creating Menubar
    menubar = Menu(w)
    
    # Adding File Menu and commands
    assignements = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Assignment', menu = assignements)
    assignements.add_command(label ='Assignment 1', command = lambda: GoToAssignment("Assignment1"))
    assignements.add_command(label ='Assignment 2', command = lambda: GoToAssignment("Assignment2"))
    assignements.add_command(label ='Assignment 3', command = lambda: GoToAssignment("Assignment3"))
    assignements.add_command(label ='Assignment 4', command = lambda: GoToAssignment("Assignment4"))
    assignements.add_command(label ='Assignment 5', command = lambda: GoToAssignment("Assignment5"))
    assignements.add_command(label ='Assignment 6', command = lambda: GoToAssignment("Assignment6"))
    assignements.add_command(label ='Assignment 7', command = lambda: GoToAssignment("Assignment7"))
    
    # display Menu
    w.config(menu = menubar,bg='#18253f')
    
    def GoToAssignment(assignment):          
        if assignment == "Assignment1":
            window1 = Tk()
            window1.title("Assignment1")
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='Data Display', command = lambda: SolveQuestion("Data Display"))
            questions.add_command(label ='Measure of central tendencies', command = lambda: SolveQuestion("Measure of central tendencies"))
            questions.add_command(label ='Dispersion of data', command = lambda: SolveQuestion("Dispersion of data"))
            questions.add_command(label ='Plots', command = lambda: SolveQuestion("Plots"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "Data Display":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    tv1 = ttk.Treeview(window2)
                    tv1.place(relheight=1, relwidth=1)

                    treescrolly = Scrollbar(w, orient="vertical", command=tv1.yview) 
                    treescrollx = Scrollbar(w, orient="horizontal", command=tv1.xview)
                    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
                    treescrollx.pack(side="bottom", fill="x")
                    treescrolly.pack(side="right", fill="y") 
                    tv1["column"] = list(data.columns)
                    tv1["show"] = "headings"
                    for column in tv1["columns"]:
                        tv1.heading(column, text=column) 

                    df_rows = data.to_numpy().tolist() 
                    for row in df_rows:
                        tv1.insert("", "end", values=row)
                    
                    window2.mainloop()
                elif question == "Measure of central tendencies":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute = StringVar(window2)
                    clickedAttribute.set("Select Attribute")
                    dropCols = OptionMenu(window2, clickedAttribute, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    measureOfCentralTendancies = ["Mean","Mode","Median","Midrange","Variance","Standard Deviation"]
                    clickedMCT = StringVar(window2)
                    clickedMCT.set("Select MCT")
                    dropMCT = OptionMenu(window2, clickedMCT, *measureOfCentralTendancies)
                    dropMCT.grid(column=2,row=5)
                    Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30)

                    def computeOperation():
                        attribute = clickedAttribute.get()
                        operation = clickedMCT.get()
                        if operation == "Mean":
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute]
                            avg = sum/len(data)
                            res = "Mean of given dataset is ("+attribute+") "+str(avg)
                            Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                        elif operation == "Mode": 
                            freq = {}
                            for i in range(len(data)):
                                freq[data.loc[i, attribute]] = 0
                            maxFreq = 0
                            maxFreqElem = 0
                            for i in range(len(data)):
                                freq[data.loc[i, attribute]] = freq[data.loc[i, attribute]]+1
                                if freq[data.loc[i, attribute]] > maxFreq:
                                    maxFreq = freq[data.loc[i, attribute]]
                                    maxFreqElem = data.loc[i, attribute]
                            res = "Mode of given dataset is ("+attribute+") "+str(maxFreqElem)
                            Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                        elif operation == "Median":
                            n = len(data)
                            i = int(n/2)
                            j = int((n/2)-1)
                            arr = []
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute])
                            arr.sort()
                            if n%2 == 1:
                                res = "Median of given dataset is ("+attribute+") "+str(arr[i])
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                            else:
                                res = "Median of given dataset is ("+attribute+") "+str((arr[i]+arr[j])/2)
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                        elif operation == "Midrange":
                            n = len(data)
                            arr = []
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute])
                            arr.sort()
                            res = "Midrange of given dataset is ("+attribute+") "+str((arr[n-1]+arr[0])/2)
                            Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                        elif operation == "Variance" or operation == "Standard Deviation":
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute]
                            avg = sum/len(data)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute]-avg)*(data.loc[i, attribute]-avg)
                            var = sum/(len(data))
                            if operation == "Variance":
                                res = "Variance of given dataset is ("+attribute+") "+str(var)
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                            else:
                                res = "Standard Deviation of given dataset is ("+attribute+") "+str(math.sqrt(var)) 
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)  
                    window2.mainloop()
                elif question == "Dispersion of data":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute = StringVar(window2)
                    clickedAttribute.set("Select Attribute")
                    dropCols = OptionMenu(window2, clickedAttribute, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    dispersionOfData = ["Range","Quartiles","Inetrquartile range","Minimum","Maximum"]
                    clickedDispersion = StringVar(window2)
                    clickedDispersion.set("Select Dispersion Operation")
                    dropDisp = OptionMenu(window2, clickedDispersion, *dispersionOfData)
                    dropDisp.grid(column=2,row=5)
                    Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30)
                    
                    def computeOperation():
                        attribute = clickedAttribute.get()
                        operation = clickedDispersion.get()
                        if operation == "Range":
                            arr = []
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute])
                            arr.sort()
                            res = "Range of given dataset is ("+attribute+") "+str(arr[len(data)-1]-arr[0])
                            Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                        elif operation == "Quartiles" or operation == "Inetrquartile range": 
                            arr = []
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute])
                            arr.sort()
                            if operation == "Quartiles": 
                                res1 = "Lower quartile(Q1) is ("+attribute+") "+str(arr[int((len(arr)+1)/4)])
                                res2 = "Middle quartile(Q2) is ("+attribute+") "+str(arr[int((len(arr)+1)/2)])
                                res3 = "Upper quartile(Q3) is ("+attribute+") "+str(arr[int(3*(len(arr)+1)/4)])
                                Label(window2,text=res1,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                                Label(window2,text=res2,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=8)
                                Label(window2,text=res3,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=9)
                            else:
                                res = "Interquartile range(Q3-Q1) of given dataset is ("+attribute+") "+str(arr[int(3*(len(arr)+1)/4)]-arr[int((len(arr)+1)/4)])
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=8)
                                
                        elif operation == "Minimum" or operation == "Maximum":
                            arr = []
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute])
                            arr.sort()
                            if operation == "Minimum":
                                res = "Minimum value of given dataset is ("+attribute+") "+str(arr[0])
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                            else:
                                res = "Maximum value of given dataset is ("+attribute+") "+str(arr[len(data)-1])
                                Label(window2,text=res,width=80,height=3,fg='green',font=('Verdana', 12)).grid(column=1,row=7)
                    window2.mainloop()
                elif question == "Plots":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute1 = StringVar(window2)
                    clickedAttribute1.set("Select Attribute 1")
                    clickedAttribute2 = StringVar(window2)
                    clickedAttribute2.set("Select Attribute 2")
                    clickedClass = StringVar(window2)
                    clickedClass.set("Select class")
                    plots = ["Quantile-Quantile Plot","Histogram","Scatter Plot","Boxplot"]
                    clickedPlot = StringVar(window2)
                    clickedPlot.set("Select Plot")
                    dropPlots = OptionMenu(window2, clickedPlot, *plots)
                    dropPlots.grid(column=1,row=6,padx=20,pady=30)
                    Button(window2,text="Select Attributes",command= lambda:selectAttributes()).grid(column=2,row=6,padx=20,pady=30)
                    
                    def computeOperation():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get()
                        
                        operation = clickedPlot.get()
                        if operation == "Quantile-Quantile Plot": 
                            arr = []
                            sum = 0
                            for i in range(len(data)):
                                arr.append(data.loc[i, attribute1])  
                                sum += data.loc[i, attribute1]
                            avg = sum/len(arr)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute1]-avg)*(data.loc[i, attribute1]-avg)
                            var = sum/(len(data))
                            sd = math.sqrt(var)
                            z = (arr-avg)/sd
                            stats.probplot(z, dist="norm", plot=plt)
                            plt.title("Normal Q-Q plot")
                            plt.show()
                            
                        elif operation == "Histogram": 
                            sns.set_style("whitegrid")
                            sns.FacetGrid(data, hue=clickedClass.get(), height=5).map(sns.histplot, attribute1).add_legend()
                            plt.title("Histogram")
                            plt.show(block=True)
                        elif operation == "Scatter Plot":
                            sns.set_style("whitegrid")
                            sns.FacetGrid(data, hue=clickedClass.get(), height=4).map(plt.scatter, attribute1, attribute2).add_legend()
                            plt.title("Scatter plot")
                            plt.show(block=True)
                        elif operation == "Boxplot":
                            sns.set_style("whitegrid")
                            sns.boxplot(x=attribute1,y=attribute2,data=data)
                            plt.title("Boxplot")
                            plt.show(block=True)
                        
                    def selectAttributes():
                        operation = clickedPlot.get()
                        if operation == "Quantile-Quantile Plot":
                            dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                            dropCols.grid(column=3,row=8,padx=20,pady=30)  
                            Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=4,row=6)
                        
                        elif operation == "Histogram":   
                            dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                            dropCols.grid(column=3,row=8,padx=20,pady=30)  
                            dropCols = OptionMenu(window2, clickedClass, *cols)
                            dropCols.grid(column=5,row=8,padx=20,pady=30) 
                            Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=4,row=6)
                    
                        elif operation == "Scatter Plot":
                            dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                            dropCols.grid(column=2,row=8,padx=20,pady=30)
                            dropCols = OptionMenu(window2, clickedAttribute2, *cols)
                            dropCols.grid(column=3,row=8,padx=20,pady=30)
                            dropCols = OptionMenu(window2, clickedClass, *cols)
                            dropCols.grid(column=5,row=8)
                            Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=4,row=6)

                        elif operation == "Boxplot":
                            dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                            dropCols.grid(column=2,row=8,padx=20,pady=30)
                            dropCols = OptionMenu(window2, clickedAttribute2, *cols)
                            dropCols.grid(column=3,row=8,padx=20,pady=30)
                            Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=4,row=6)
                    window2.mainloop()
            window1.config(menu = menubar)
            window1.mainloop()
        
        elif assignment == "Assignment2":
            window1 = Tk()
            window1.title("Assignment2")
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='Chi-Square Test', command = lambda: SolveQuestion("Chi-Square Test"))
            questions.add_command(label ='Correlation(Pearson) Coefficient', command = lambda: SolveQuestion("Correlation(Pearson) Coefficient"))
            questions.add_command(label ='Normalization Techniques', command = lambda: SolveQuestion("Normalization Techniques"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "Chi-Square Test":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute1 = StringVar(window2)
                    clickedAttribute1.set("Select Attribute1")
                    dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    clickedAttribute2 = StringVar(window2)
                    clickedAttribute2.set("Select Attribute2")
                    dropCols = OptionMenu(window2, clickedAttribute2, *cols)
                    dropCols.grid(column=2,row=5)
                    clickedClass = StringVar(window2)
                    clickedClass.set("Select Class")
                    dropCols = OptionMenu(window2, clickedClass, *cols)
                    dropCols.grid(column=3,row=5)
                    Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30) 
                    
                    def computeOperation():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get()
                        category = clickedClass.get()
                        arrClass = data[category].unique()
                        g = data.groupby(category)
                        f = {
                        attribute1: 'sum',
                        attribute2: 'sum'
                        }
                        v1 = g.agg(f)
                        print(v1)
                        v = v1.transpose()
                        print(v)
                        
                        tv1 = ttk.Treeview(window2,height=3)
                        tv1.grid(column=1,row=8,padx=5,pady=8)
                        tv1["column"] = list(v.columns)
                        tv1["show"] = "headings"
                        for column in tv1["columns"]:
                            tv1.heading(column, text=column)

                        df_rows = v.to_numpy().tolist()
                        for row in df_rows:
                            tv1.insert("", "end", values=row)

                        total = v1[attribute1].sum()+v1[attribute2].sum()
                        chiSquare = 0.0
                        for i in arrClass:
                            chiSquare += (v.loc[attribute1][i]-(((v[i].sum())*(v1[attribute1].sum()))/total))*(v.loc[attribute1][i]-(((v[i].sum())*(v1[attribute1].sum()))/total))/(((v[i].sum())*(v1[attribute1].sum()))/total)
                            chiSquare += (v.loc[attribute2][i]-(((v[i].sum())*(v1[attribute2].sum()))/total))*(v.loc[attribute2][i]-(((v[i].sum())*(v1[attribute2].sum()))/total))/(((v[i].sum())*(v1[attribute2].sum()))/total)
                        
                        degreeOfFreedom = (len(v)-1)*(len(v1)-1)
                        Label(window2,text="Chi-square value is "+str(chiSquare), justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=9,padx=5,pady=8) 
                        Label(window2,text="Degree of Freedom is "+str(degreeOfFreedom), justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=10,padx=5,pady=8) 
                        res = ""
                        if chiSquare > degreeOfFreedom:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are strongly correlated."
                        else:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are not correlated."
                        Label(window2,text=res, justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=11,padx=5,pady=8)
                    window2.mainloop()
                elif question == "Correlation(Pearson) Coefficient":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute1 = StringVar(window2)
                    clickedAttribute1.set("Select Attribute1")
                    dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    clickedAttribute2 = StringVar(window2)
                    clickedAttribute2.set("Select Attribute2")
                    dropCols = OptionMenu(window2, clickedAttribute2, *cols)
                    dropCols.grid(column=2,row=5)
                    Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30) 
                    
                    def computeOperation():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get()
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += data.loc[i, attribute1]
                        avg1 = sum/len(data)
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute1]-avg1)
                        var1 = sum/(len(data))
                        sd1 = math.sqrt(var1)
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += data.loc[i, attribute2]
                        avg2 = sum/len(data)
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute2]-avg2)*(data.loc[i, attribute2]-avg2)
                        var2 = sum/(len(data))
                        sd2 = math.sqrt(var2)
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute2]-avg2)
                        covariance = sum/len(data)
                        pearsonCoeff = covariance/(sd1*sd2)    
                        Label(window2,text="Covariance value is "+str(covariance), justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=8,padx=5,pady=8) 
                        Label(window2,text="Correlation coefficient(Pearson coefficient) is "+str(pearsonCoeff), justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=9,padx=5,pady=8) 
                        res = ""
                        if pearsonCoeff > 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are positively correlated."
                        elif pearsonCoeff < 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are negatively correlated."
                        elif pearsonCoeff == 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are independant."
                        Label(window2,text=res, justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=11,padx=5,pady=8)
                    window2.mainloop()
                elif question == "Normalization Techniques":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute1 = StringVar(window2)
                    clickedAttribute1.set("Select Attribute1")
                    dropCols = OptionMenu(window2, clickedAttribute1, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    clickedAttribute2 = StringVar(window2)
                    clickedAttribute2.set("Select Attribute2")
                    dropCols = OptionMenu(window2, clickedAttribute2, *cols)
                    dropCols.grid(column=2,row=5)
                    clickedClass = StringVar(window2)
                    clickedClass.set("Select class")
                    dropCols = OptionMenu(window2, clickedClass, *cols)
                    dropCols.grid(column=3,row=5)
                    normalizationOperations = ["Min-Max normalization","Z-Score normalization","Normalization by decimal scaling"]
                    clickedOperation = StringVar(window2)
                    clickedOperation.set("Select Normalization Operation")
                    dropOperations = OptionMenu(window2, clickedOperation, *normalizationOperations)
                    dropOperations.grid(column=4,row=5)
                    Button(window2,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30) 
                    
                    def computeOperation():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get() 
                        operation = clickedOperation.get()
                        if operation == "Min-Max normalization":
                            n = len(data)
                            arr1 = []
                            for i in range(len(data)):
                                arr1.append(data.loc[i, attribute1])
                            arr1.sort()
                            min1 = arr1[0]
                            max1 = arr1[n-1]
                            
                            arr2 = []
                            for i in range(len(data)):
                                arr2.append(data.loc[i, attribute2])
                            arr2.sort()
                            min2 = arr2[0]
                            max2 = arr2[n-1]
                            
                            for i in range(len(data)):
                                d.loc[i, attribute1] = ((data.loc[i, attribute1]-min1)/(max1-min1))
                            
                            for i in range(len(data)):
                                d.loc[i, attribute2] = ((data.loc[i, attribute2]-min2)/(max2-min2))
                        elif operation == "Z-Score normalization":
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute1]
                            avg1 = sum/len(data)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute1]-avg1)
                            var1 = sum/(len(data))
                            sd1 = math.sqrt(var1)
                            
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute2]
                            avg2 = sum/len(data)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute2]-avg2)*(data.loc[i, attribute2]-avg2)
                            var2 = sum/(len(data))
                            sd2 = math.sqrt(var2)
                            
                            for i in range(len(data)):
                                d.loc[i, attribute1] = ((data.loc[i, attribute1]-avg1)/sd1)
                            
                            for i in range(len(data)):
                                d.loc[i, attribute2] = ((data.loc[i, attribute2]-avg2)/sd2)
                        elif operation == "Normalization by decimal scaling":        
                            j1 = 0
                            j2 = 0
                            n = len(data)
                            arr1 = []
                            for i in range(len(data)):
                                arr1.append(data.loc[i, attribute1])
                            arr1.sort()
                            max1 = arr1[n-1]
                            
                            arr2 = []
                            for i in range(len(data)):
                                arr2.append(data.loc[i, attribute2])
                            arr2.sort()
                            max2 = arr2[n-1]
                            
                            while max1 > 1:
                                max1 /= 10
                                j1 += 1
                            while max2 > 1:
                                max2 /= 10
                                j2 += 1
                            
                            for i in range(len(data)):
                                d.loc[i, attribute1] = ((data.loc[i, attribute1])/(pow(10,j1)))
                            
                            for i in range(len(data)):
                                d.loc[i, attribute2] = ((data.loc[i, attribute2])/(pow(10,j2)))
                        
                        Label(window2,text="Normalized Attributes", justify='center',height=2,fg='green',font=('Verdana', 12)).grid(column=1,row=8,padx=5,pady=8)         
                        tv1 = ttk.Treeview(window2,height=15)
                        tv1.grid(column=1,row=9,padx=5,pady=8)
                        tv1["column"] = [attribute1,attribute2]
                        tv1["show"] = "headings"
                        for column in tv1["columns"]:
                            tv1.heading(column, text=column)
                        i = 0
                        while i < len(data):
                            tv1.insert("", "end", iid=i, values=(d.loc[i, attribute1],d.loc[i, attribute2]))
                            i += 1
                        sns.set_style("whitegrid")
                        sns.FacetGrid(d, hue=clickedClass.get(), height=4).map(plt.scatter, attribute1, attribute2).add_legend()
                        plt.title("Scatter plot")
                        plt.show(block=True)
                    window2.mainloop()
            window1.config(menu = menubar)
            window1.mainloop()
        
        elif assignment == "Assignment3" or assignment == "Assignment4":
            window1 = Tk()
            window1.title(assignment)
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='Information Gain & Gain Ratio', command = lambda: SolveQuestion("Information Gain & Gain Ratio"))
            questions.add_command(label ='Gini Index', command = lambda: SolveQuestion("Gini Index"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "Information Gain & Gain Ratio":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    print(data)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute = StringVar(window2)
                    clickedAttribute.set("Select Attribute")
                    dropCols = OptionMenu(window2, clickedAttribute, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    
                    dropAttribute = StringVar(window2)
                    dropAttribute.set("Drop Attribute")
                    dropCols = OptionMenu(window2, dropAttribute, *cols)
                    dropCols.grid(column=2,row=5,padx=20,pady=30)
                    
                    d = {}
                    split_i = {}
                    Button(window2,text="Compute",command= lambda:compute()).grid(column=1,row=6,padx=20,pady=30) 
                    Button(window2,text="Drop Column",command= lambda:dropCol()).grid(column=2,row=6,padx=20,pady=30) 
                    
                    def dropCol():
                        print(dropAttribute.get())
                        cols.remove(dropAttribute.get())
                        
                    def compute():
                        cols.remove(clickedAttribute.get())
                        print(clickedAttribute.get())
                        print(cols)
                        arrClass = data[clickedAttribute.get()].unique()
                        g = data.groupby(clickedAttribute.get())
                        print(arrClass, g)
                        f = {
                        clickedAttribute.get() : 'count'
                        }
                        v = g.agg(f)
                        total = 0
                        for category in arrClass:
                            total += v.transpose()[category]
                            
                        info_d = 0
                        for category in arrClass:
                            info_d += calcEntropy(float(v.transpose()[category]), total)
                            
                        for i in cols:
                            arrAttribute = data[i].unique()
                            g1 = data.groupby(i)
                            print(arrAttribute, i)
                            f1 = {
                            i : 'count'
                            }
                            v1 = g1.agg(f1)
                            
                            total1 = 0
                            for eachValue in arrAttribute:
                                total1 += v1.transpose()[eachValue]
                                
                                    
                            info_d1 = 0
                            split_info = 0
                            for eachValue in arrAttribute:
                                for k in arrClass:
                                    num = 0
                                    for j in range(len(data)):
                                        if data.loc[j, clickedAttribute.get()] == k and data.loc[j, i] == eachValue:
                                            num += 1
                                    info_d1 += calcEntropy(num, float(v1.transpose()[eachValue]))
                                info_d1 *= float(v1.transpose()[eachValue])/total1
                                split_info += calcEntropy(float(v1.transpose()[eachValue]), total1)    
                            d[i] = float(info_d1)
                            split_i[i] = float(split_info)
                        
                        sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
                        print(d)
                        print(sorted_d)
                        columns = ('Attributes', 'Info', 'Gain', 'Gain ratio')
                        tv1 = ttk.Treeview(window2, columns=columns, show='headings')
                        tv1.grid(column=1,row=8,padx=5,pady=8)
                        
                        tv1.heading('Attributes', text='Attributes')
                        tv1.heading('Info', text='Info')
                        tv1.heading('Gain', text='Gain')
                        tv1.heading('Gain ratio', text='Gain ratio')
                        
                        tuples = []
                        for n in sorted_d:
                            tuples.append((f'{n}', f'{sorted_d[n]}', f'{float(info_d-sorted_d[n])}', f'{(float(info_d-sorted_d[n])/float(split_i[n]))}'))
                        for tuple in tuples:
                            tv1.insert('', END, values=tuple)
                        tv1.grid(row=7, column=1, sticky='nsew')
                        
                        
                        f_names = []
                        c_names = []
                        f_names = cols
                        print(f_names)
                        for c in arrClass:
                            c_names.append(str(c))
                        print(type(c_names))
                        le_class = LabelEncoder()
                        df = data
                        df[clickedAttribute.get()] = le_class.fit_transform(df[clickedAttribute.get()])
                        dft = data.drop(clickedAttribute.get(), axis=1)
                        print(dft)
                        X_train, X_test, Y_train, Y_test = train_test_split(dft, df[clickedAttribute.get()], test_size=0.2, random_state=1)
                        clf = DecisionTreeClassifier(max_depth = 3, random_state = 0,criterion="entropy")
                        model = clf.fit(X_train, Y_train)
                        Y_predicted = clf.predict(X_test)
                        Y_test = Y_test.to_numpy()
                        print(type(Y_predicted),type(Y_test))
                        print(Y_predicted, "predicted", len(Y_predicted), Y_test, "Y_test", len(Y_test))
                        c_matrix = confusion_matrix(Y_test,Y_predicted)
                        
                        print(c_matrix)
                        print(classification_report(Y_test,Y_predicted))
                        ax = plt.subplot()
                        sns.heatmap(c_matrix, annot=True, fmt='g', ax=ax)
                        ax.set_xlabel('Predicted labels')
                        ax.set_ylabel('True labels') 
                        ax.set_title('Confusion Matrix')
                        ax.xaxis.set_ticklabels(c_names)
                        ax.yaxis.set_ticklabels(c_names)
                        
                        
                        text_representation = tree.export_text(clf)
                        # print(text_representation)
                        print(f_names,c_names)
                        print(type(f_names),type(c_names))
                        fig = plt.figure(figsize=(25,20))
                        _ = tree.plot_tree(clf, feature_names=f_names, class_names=c_names,filled=True)
                        if assignment == "Assignment4":
                            accuracy = "Accuracy " + str(metrics.accuracy_score(Y_test,Y_predicted))
                            Label(window1, text=accuracy).grid(row=10,column=1,padx=20,pady=5)
                        plt.show()
                        
                        if assignment == "Assignment4":
                            def get_rules(tree, feature_names, class_names):
                                tree_ = tree.tree_
                                feature_name = [
                                    feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
                                    for i in tree_.feature
                                ]

                                paths = []
                                path = []
                                
                                def recurse(node, path, paths):
                                    
                                    if tree_.feature[node] != _tree.TREE_UNDEFINED:
                                        name = feature_name[node]
                                        threshold = tree_.threshold[node]
                                        p1, p2 = list(path), list(path)
                                        p1 += [f"({name} <= {np.round(threshold, 3)})"]
                                        recurse(tree_.children_left[node], p1, paths)
                                        p2 += [f"({name} > {np.round(threshold, 3)})"]
                                        recurse(tree_.children_right[node], p2, paths)
                                    else:
                                        path += [(tree_.value[node], tree_.n_node_samples[node])]
                                        paths += [path]
                                        
                                recurse(0, path, paths)

                                # sort by samples count
                                samples_count = [p[-1][1] for p in paths]
                                ii = list(np.argsort(samples_count))
                                paths = [paths[i] for i in reversed(ii)]
                                
                                rules = []
                                for path in paths:
                                    rule = "if "
                                    
                                    for p in path[:-1]:
                                        if rule != "if ":
                                            rule += " and "
                                        rule += str(p)
                                    rule += " then "
                                    if class_names is None:
                                        rule += "response: "+str(np.round(path[-1][0][0][0],3))
                                    else:
                                        classes = path[-1][0][0]
                                        l = np.argmax(classes)
                                        rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
                                    rule += f" | based on {path[-1][1]:,} samples"
                                    rules += [rule]
                                    
                                return rules 
                            
                            rules = get_rules(clf, f_names, c_names)
                            win = Tk()
                            win.title("Extracted Rules")
                            win.geometry("500x500")
                            win.config(background="white")
                            i=0
                            for r in rules:
                                Label(win, text=r, justify='center',font=('Verdana', 12), fg="#fff",bg="#555",height=2).grid(row=i,column=1,padx=20,pady=5)
                                i=i+1
                            
                            win.mainloop()
                            for r in rules:
                                print(r)
                            
                    def calcEntropy(c,n):
                        if c <= 0:
                            return 0.0 
                        return -(c*1.0/n)*math.log(c*1.0/n, 2)
                    
                    window2.mainloop()
                    
                elif question == "Gini Index":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("500x500")
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    clickedAttribute = StringVar(window2)
                    clickedAttribute.set("Select Attribute")
                    dropCols = OptionMenu(window2, clickedAttribute, *cols)
                    dropCols.grid(column=1,row=5,padx=20,pady=30)
                    
                    dropAttribute = StringVar(window2)
                    dropAttribute.set("Drop Attribute")
                    dropCols = OptionMenu(window2, dropAttribute, *cols)
                    dropCols.grid(column=2,row=5,padx=20,pady=30)
                    
                    d = {}
                    Button(window2,text="Compute",command= lambda:compute()).grid(column=1,row=6,padx=20,pady=30) 
                    Button(window2,text="Drop Column",command= lambda:dropCol()).grid(column=2,row=6,padx=20,pady=30) 
                    
                    def dropCol():
                        print(dropAttribute.get())
                        cols.remove(dropAttribute.get())
                        # window.mainloop()
                        
                    def compute():
                        cols.remove(clickedAttribute.get())
                        print(clickedAttribute.get())
                        print(cols)
                        arrClass = data[clickedAttribute.get()].unique()
                        g = data.groupby(clickedAttribute.get())
                        print(arrClass, g)
                        f = {
                        clickedAttribute.get() : 'count'
                        }
                        v = g.agg(f)
                        total = 0
                        for category in arrClass:
                            total += v.transpose()[category]
                            
                        gini_d = 1
                        for category in arrClass:
                            gini_d -= ((float(v.transpose()[category])/total)*(float(v.transpose()[category])/total))
                            
                        print(gini_d, "gini_d")
                        
                            
                        
                        for i in cols:
                            arrAttribute = data[i].unique()
                            g1 = data.groupby(i)
                            # print(arrAttribute, i)
                            f1 = {
                            i : 'count'
                            }
                            v1 = g1.agg(f1)
                            list1 = []            
                            total1 = 0
                            for eachValue in arrAttribute:
                                total1 += v1.transpose()[eachValue]
                                print(v1.transpose()[eachValue], i)
                                list1.append(eachValue)
                            print(total1, "total1", i) 
                            list_combinations = []
                            for r in range(len(list1)+1):
                                for combination in itertools.combinations(list1, r):
                                    list_combinations.append(combination)
                            
                            list_combinations = list_combinations[1:-1]
                            # prob = 1
                            for t in list_combinations:
                                gini_di = 0
                                for l in t:
                                    prob = 1
                                    for k in arrClass:
                                        num = 0
                                        for j in range(len(data)):
                                            if data.loc[j, clickedAttribute.get()] == k and data.loc[j, i] == l:
                                                num += 1
                                        prob -= ((float(num)/float(v1.transpose()[l]))*(float((num)/float(v1.transpose()[l]))))
                                    print(v1.transpose()[l], total1)
                                    gini_di += ((float(v1.transpose()[l])/float(total1))*float(prob))
                                key = 'Gini '+str(i)+str(t)
                                d[key] = float(gini_di)
                                    
                        dictionary_keys = list(d.keys())
                        sorted_d = {dictionary_keys[i]: sorted(
                            d.values())[i] for i in range(len(dictionary_keys))}
                        
                        columns = ('Criteria', 'Gini Index')
                        tv1 = ttk.Treeview(window2, columns=columns, show='headings')
                        tv1.grid(column=1,row=8,padx=5,pady=8)
                        
                        tv1.heading('Criteria', text='Criteria')
                        tv1.heading('Gini Index', text='Gini Index')
                        
                        tuples = []
                        for n in sorted_d:
                            tuples.append((f'{n}', f'{sorted_d[n]}'))
                        for tuple in tuples:
                            tv1.insert('', END, values=tuple)
                        tv1.grid(row=7, column=1, sticky='nsew')      
                        
                        f_names = []
                        c_names = []
                        f_names = cols
                        print(f_names)
                        for c in arrClass:
                            c_names.append(str(c))
                        print(type(c_names))
                        le_class = LabelEncoder()
                        df = data
                        df[clickedAttribute.get()] = le_class.fit_transform(df[clickedAttribute.get()])
                        dft = data.drop(clickedAttribute.get(), axis=1)
                        print(dft)
                        X_train, X_test, Y_train, Y_test = train_test_split(dft, df[clickedAttribute.get()], test_size=0.2, random_state=1)
                        clf = DecisionTreeClassifier(max_depth = 3, random_state = 0,criterion="gini")
                        model = clf.fit(X_train, Y_train)
                        Y_predicted = clf.predict(X_test)
                        Y_test = Y_test.to_numpy()
                        print(type(Y_predicted),type(Y_test))
                        print(Y_predicted, "predicted", len(Y_predicted), Y_test, "Y_test", len(Y_test))
                        c_matrix = confusion_matrix(Y_test,Y_predicted)
                        
                        print(c_matrix)
                        print(classification_report(Y_test,Y_predicted))
                        ax = plt.subplot()
                        sns.heatmap(c_matrix, annot=True, fmt='g', ax=ax)
                        ax.set_xlabel('Predicted labels')
                        ax.set_ylabel('True labels') 
                        ax.set_title('Confusion Matrix')
                        ax.xaxis.set_ticklabels(c_names)
                        ax.yaxis.set_ticklabels(c_names)
                        
                        
                        text_representation = tree.export_text(clf)
                        # print(text_representation)
                        print(f_names,c_names)
                        print(type(f_names),type(c_names))
                        fig = plt.figure(figsize=(25,20))
                        _ = tree.plot_tree(clf, feature_names=f_names, class_names=c_names,filled=True)
                        if assignment == "Assignment4":
                            accuracy = "Accuracy " + str(metrics.accuracy_score(Y_test,Y_predicted))
                            Label(window1, text=accuracy).grid(row=10,column=1,padx=20,pady=5)
                        plt.show()

                        if assignment == "Assignment4":
                            def get_rules(tree, feature_names, class_names):
                                tree_ = tree.tree_
                                feature_name = [
                                    feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
                                    for i in tree_.feature
                                ]

                                paths = []
                                path = []
                                
                                def recurse(node, path, paths):
                                    
                                    if tree_.feature[node] != _tree.TREE_UNDEFINED:
                                        name = feature_name[node]
                                        threshold = tree_.threshold[node]
                                        p1, p2 = list(path), list(path)
                                        p1 += [f"({name} <= {np.round(threshold, 3)})"]
                                        recurse(tree_.children_left[node], p1, paths)
                                        p2 += [f"({name} > {np.round(threshold, 3)})"]
                                        recurse(tree_.children_right[node], p2, paths)
                                    else:
                                        path += [(tree_.value[node], tree_.n_node_samples[node])]
                                        paths += [path]
                                        
                                recurse(0, path, paths)

                                # sort by samples count
                                samples_count = [p[-1][1] for p in paths]
                                ii = list(np.argsort(samples_count))
                                paths = [paths[i] for i in reversed(ii)]
                                
                                rules = []
                                for path in paths:
                                    rule = "if "
                                    
                                    for p in path[:-1]:
                                        if rule != "if ":
                                            rule += " and "
                                        rule += str(p)
                                    rule += " then "
                                    if class_names is None:
                                        rule += "response: "+str(np.round(path[-1][0][0][0],3))
                                    else:
                                        classes = path[-1][0][0]
                                        l = np.argmax(classes)
                                        rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
                                    rule += f" | based on {path[-1][1]:,} samples"
                                    rules += [rule]
                                    
                                return rules 
                            
                            rules = get_rules(clf, f_names, c_names)
                            win = Tk()
                            win.title("Extracted Rules")
                            win.geometry("500x500")
                            win.config(background="white")
                            i=0
                            for r in rules:
                                Label(win, text=r, justify='center',font=('Verdana', 12), fg="#fff",bg="#555",height=2).grid(row=i,column=1,padx=20,pady=5)
                                i=i+1
                            
                            win.mainloop()
                            for r in rules:
                                print(r)
                        
                    window2.mainloop()
                    
            window1.config(menu = menubar)
            window1.mainloop()
        
        elif assignment == "Assignment5":
            window1 = Tk()
            window1.title(assignment)
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='k-NN Classifier', command = lambda: SolveQuestion("k-NN Classifier"))
            questions.add_command(label ='ANN Classifier', command = lambda: SolveQuestion("ANN Classifier"))
            questions.add_command(label ='Naive Bayes', command = lambda: SolveQuestion("Naive Bayes"))
            questions.add_command(label ='Logistic Regression', command = lambda: SolveQuestion("Logistic Regression"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "k-NN Classifier":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("800x500")
                    Label(window2, text="k",font=('Verdana', 12)).grid(row=1,column=1,padx=20,pady=30)
                    answer1 = Entry(window2)
                    answer1.grid(row=1,column=2,padx=20,pady=30)
                    Label(window2, text="Unknown Pattern(Enter comma separated values)",font=('Verdana', 12)).grid(row=2,column=1,padx=20,pady=30)
                    answer2 = Entry(window2)
                    answer2.grid(row=2,column=2,padx=20,pady=30)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:findClass(int(answer1.get()), answer2.get())).grid(column=1,row=6,padx=20,pady=30) 
                    def findClass(k,unknownPattern):
                        ls = unknownPattern.split(",")
                        targetLS = []
                        
                        for s in ls:
                            targetLS.append(float(s))
                        
                        le_class = LabelEncoder()
                        df = data
                        print(data.iloc[:,-1] )
                        df.iloc[: , -1] = le_class.fit_transform(df.iloc[: , -1])
                        print(data.iloc[:,-1] )
                        labelClasses = {}
                        for i in range(len(df)):
                            print(data.iloc[i,-1], type(d.iloc[i,-1]))
                            labelClasses[df.iloc[i,-1]] = d.iloc[i,-1]
                        print(labelClasses)
                        dft = data.iloc[: , :-1] #dropping target column
                        
                        # manual classification

                        uP = tuple(targetLS)
                        allClassPoints = {}
                        for i in range(len(dft)):
                            value = allClassPoints.get(df.iloc[i,-1])
                            if value == None:
                                allClassPoints[df.iloc[i,-1]] = []
                            allClassPoints[df.iloc[i,-1]].append(tuple(dft.iloc[i]))
                        distArray = []
                        for eachClass in allClassPoints:
                            for eachTuple in allClassPoints[eachClass]:
                                sum = 0
                                t = 0
                                while t < (len(eachTuple)):
                                    sum += ((eachTuple[t]-uP[t])**2)
                                    t += 1
                                euclideanDistance = math.sqrt(sum)
                                distArray.append((euclideanDistance,eachClass))
                        
                        distFrequencyDict = {} 
                        maxFreqClass = 0      
                        distArray = sorted(distArray)[:k]
                        for distance in distArray:
                            if distFrequencyDict.get(distance[1]) == None:
                                distFrequencyDict[distance[1]] = 0
                            distFrequencyDict[distance[1]] = distFrequencyDict[distance[1]] + 1
                            if maxFreqClass < distFrequencyDict[distance[1]]:
                                maxFreqClass = distance[1]
                        print(labelClasses[maxFreqClass],"Class Manual")
                        
                        # using in built fn classifier
                        targetLS = [targetLS]
                        X_train, X_test, y_train, y_test = train_test_split(
                        dft, df.iloc[: , -1], test_size = 0.2, random_state=42)
            
                        knn = KNeighborsClassifier(k)
            
                        knn.fit(X_train, y_train)
                        u_pattern = pd.DataFrame(targetLS, columns=list(dft.columns))
                        print(u_pattern,"u_pattern\n")
                        # Predict on dataset which model has not seen before
                        print(knn.predict(u_pattern),type(knn.predict(u_pattern)), "class")

                        Label(window2, text="Predicted Class manually",fg='green',font=('Verdana', 12)).grid(row=7,column=1,padx=20,pady=30)
                        Label(window2, text=labelClasses[maxFreqClass],bg='green',fg='#fff',font=('Verdana', 12)).grid(row=7,column=2,padx=20,pady=30)
                        Label(window2, text="Predicted Class using in built function",fg='green',font=('Verdana', 12)).grid(row=8,column=1,padx=20,pady=30)
                        Label(window2, text=labelClasses[knn.predict(u_pattern)[0]],bg='green',fg='#fff',font=('Verdana', 12)).grid(row=8,column=2,padx=20,pady=30)
                        
                    window2.mainloop()
                elif question == "ANN Classifier":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("800x500")
                    # Label(window2, text="k",font=('Verdana', 12)).grid(row=1,column=1,padx=20,pady=30)
                    # answer1 = Entry(window2)
                    # answer1.grid(row=1,column=2,padx=20,pady=30)
                    Label(window2, text="Unknown Pattern(Enter comma separated values)",font=('Verdana', 12)).grid(row=2,column=1,padx=20,pady=30)
                    answer2 = Entry(window2)
                    answer2.grid(row=2,column=2,padx=20,pady=30)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:findClass(answer2.get())).grid(column=1,row=6,padx=20,pady=30) 
                    def findClass(unknownPattern):
                        errors = []
                        def calcSigmoid(x):
                            return (1 / (1 + np.exp(-x)))
                    
                        def sigmoidDerivative(x):
                            return (x * (1 - x))
                        
                        def learnModel(allClassPoints,wtMatrix):
                            return calcSigmoid(np.dot(allClassPoints, wtMatrix))
                    
                        def trainModel(allClassPoints, features, iterations, wtMatrix):
                            for iteration in xrange(iterations):
                                output = learnModel(allClassPoints,wtMatrix)
                                error = features - output
                                for er in error:
                                    errors.append(er)
                                # Adjusting the weights by a factor
                                factor = np.dot(allClassPoints.T, error * sigmoidDerivative(output))
                                wtMatrix += factor
                    
                        
                        ls = unknownPattern.split(",")
                        targetLS = []
                        
                        for s in ls:
                            targetLS.append(float(s))
                        df = data
                        

                        le_class = LabelEncoder()
                        
                        # print(data.iloc[:,-1] )
                        df.iloc[: , -1] = le_class.fit_transform(df.iloc[: , -1])
                        # print(data.iloc[:,-1] )
                        labelClasses = {}
                        features = []
                        tmpList = []
                        for i in range(len(df)):
                            labelClasses[df.iloc[i,-1]] = d.iloc[i,-1]
                            tmpList.append(df.iloc[i,-1])
                        features.append(tmpList)
                        print(labelClasses)
                        dft = data.iloc[: , :-1] #dropping target column
                        
                        # manual classification
                        allClassPoints = []
                        for i in range(len(dft)):
                            allClassPoints.append(list(dft.iloc[i]))
                        # print(features)
                        # print(allClassPoints)
                        
                        np.random.seed(4)
                        wtMatrix = 2*np.random.random((len(allClassPoints[0]),1))-1
                        print(len(wtMatrix),"st")
                        print(wtMatrix)
                        allClassPoints = np.array(allClassPoints)
                        features = np.array(features).T
                        trainModel(allClassPoints,features,10000,wtMatrix)
                        print(learnModel(np.array([13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]),wtMatrix),"B")
                        print(learnModel(np.array([17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]),wtMatrix),"M")
                        plt.title('Error Graph')
                        plt.plot(errors)
                        plt.xlabel('Epoch')
                        plt.ylabel('Error')
                        plt.show()
                        # print("hello",type(learnModel(np.array([17.99, 10.38, 122.8, 1001]),wtMatrix)))
                        # print(len(allClassPoints[0]))
                        # using in built fn classifier
                        targetLS = [targetLS]
                        # X_train, X_test, y_train, y_test = train_test_split(
                        # dft, df.iloc[: , -1], test_size = 0.2, random_state=42)
            
                        
                        # Label(window2, text="Predicted Class manually",fg='green',font=('Verdana', 12)).grid(row=7,column=1,padx=20,pady=30)
                        # Label(window2, text=labelClasses[maxFreqClass],bg='green',fg='#fff',font=('Verdana', 12)).grid(row=7,column=2,padx=20,pady=30)
                        # Label(window2, text="Predicted Class using in built function",fg='green',font=('Verdana', 12)).grid(row=8,column=1,padx=20,pady=30)
                        # Label(window2, text=labelClasses[knn.predict(u_pattern)[0]],bg='green',fg='#fff',font=('Verdana', 12)).grid(row=8,column=2,padx=20,pady=30)
                    
                    window2.mainloop()
                elif question == "Naive Bayes":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("800x500")
                    Label(window2, text="Unknown Pattern(Enter comma separated values)",font=('Verdana', 12)).grid(row=1,column=1,padx=20,pady=30)
                    answer1 = Entry(window2)
                    answer1.grid(row=1,column=2,padx=20,pady=30)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:findClass(answer1.get())).grid(column=1,row=6,padx=20,pady=30) 
                    def findClass(unknownPattern):
                        ls = unknownPattern.split(",")
                        targetLS = []
                        
                        for s in ls:
                            targetLS.append(float(s))        
                        train = data.sample(frac = 0.7, random_state = 1)
                        test = data.drop(train.index)
                        cols = list(data.columns)
                        y_train = train[cols[len(cols)-1]]
                        x_train = train.drop(cols[len(cols)-1], axis = 1)

                        y_test = test[cols[len(cols)-1]]
                        x_test = test.drop(cols[len(cols)-1], axis = 1)
                        
                        means = train.groupby([cols[len(cols)-1]]).mean() 
                        var = train.groupby([cols[len(cols)-1]]).var() 
                        prior = (train.groupby(cols[len(cols)-1]).count() / len(train)).iloc[:,1] # prior probabilities
                        classes = np.unique(train[cols[len(cols)-1]].tolist()) # all possible classes
                        
                        def Normal(n, mu, var):
                            sd = np.sqrt(var)
                            pdf = (np.e ** (-0.5 * ((n - mu)/sd) ** 2)) / (sd * np.sqrt(2 * np.pi))                           
                            return pdf

                        def Predict(X):
                            Predictions = []
                            for i in X.index: 
                                
                                ClassLikelihood = []
                                instance = X.loc[i]
                                
                                for cls in classes: 
                                    FeatureLikelihoods = []
                                    FeatureLikelihoods.append(np.log(prior[cls])) 
                                    
                                    for col in x_train.columns: 
                                        
                                        data = instance[col]
                                        
                                        mean = means[col].loc[cls] 
                                        variance = var[col].loc[cls] 
                                        
                                        Likelihood = Normal(data, mean, variance)
                                        
                                        if Likelihood != 0:
                                            Likelihood = np.log(Likelihood)
                                        else:
                                            Likelihood = 1/len(train) 
                                        
                                        FeatureLikelihoods.append(Likelihood)
                                        
                                    TotalLikelihood = sum(FeatureLikelihoods) # posterior
                                    ClassLikelihood.append(TotalLikelihood)
                                    
                                MaxIndex = ClassLikelihood.index(max(ClassLikelihood)) 
                                Prediction = classes[MaxIndex]
                                Predictions.append(Prediction)
                                
                            return Predictions
                        
                        PredictTrain = Predict(x_train)
                        PredictTest = Predict(x_test)
                        targetLS = [targetLS]
                        u_pattern = pd.DataFrame(targetLS, columns=list(x_train.columns))
                        
                        def Accuracy(y, prediction):
                            y = list(y)
                            prediction = list(prediction)
                            score = 0
                            
                            for i, j in zip(y, prediction):
                                if i == j:
                                    score += 1
                                    
                            return score / len(y)
                        Label(window2, text="Predicted Class",fg='green',font=('Verdana', 12)).grid(row=7,column=1,padx=20,pady=30)
                        Label(window2, text=Predict(u_pattern)[0],bg='green',fg='#fff',font=('Verdana', 12)).grid(row=7,column=2,padx=20,pady=30)
                        Label(window2, text="Accuracy",fg='green',font=('Verdana', 12)).grid(row=8,column=1,padx=20,pady=30)
                        Label(window2, text=Accuracy(y_test,PredictTest),bg='green',fg='#fff',font=('Verdana', 12)).grid(row=8,column=2,padx=20,pady=30)
                elif question == "Logistic Regression":
                    le_class = LabelEncoder()
                    df = data
                    df.iloc[: , -1] = le_class.fit_transform(df.iloc[: , -1])
                    labelClasses = {}
                    for i in range(len(df)):
                        labelClasses[df.iloc[i,-1]] = d.iloc[i,-1]
                    print(labelClasses)
                    dft = data.iloc[: , :-1] #dropping target column
                    X_tr,X_te,y_tr,y_te = train_test_split(dft, df.iloc[: , -1],test_size=0.2)
                    # def standardize(X_tr):
                    #     for i in range(shape(X_tr)[1]):
                    #         X_tr[:,i] = (X_tr[:,i] - np.mean(X_tr[:,i]))/np.std(X_tr[:,i])
                    def F1_score(y,y_hat):
                        tp,tn,fp,fn = 0,0,0,0
                        for i in range(len(y)):
                            if y[i] == 1 and y_hat[i] == 1:
                                tp += 1
                            elif y[i] == 1 and y_hat[i] == 0:
                                fn += 1
                            elif y[i] == 0 and y_hat[i] == 1:
                                fp += 1
                            elif y[i] == 0 and y_hat[i] == 0:
                                tn += 1
                        precision = tp/(tp+fp)
                        recall = tp/(tp+fn)
                        f1_score = 2*precision*recall/(precision+recall)
                        return f1_score
                    class LogidticRegression:
                        def sigmoid(self,z):
                            sig = 1/(1+exp(-z))
                            return sig
                        def initialize(self,X):
                            weights = np.zeros((shape(X)[1]+1,1))
                            X = np.c_[np.ones((shape(X)[0],1)),X]
                            return weights,X
                        def fit(self,X,y,alpha=0.001,iter=400):
                            weights,X = self.initialize(X)
                            def cost(theta):
                                z = dot(X,theta)
                                cost0 = y.T.dot(log(self.sigmoid(z)))
                                cost1 = (1-y).T.dot(log(1-self.sigmoid(z)))
                                cost = -((cost1 + cost0))/len(y)
                                return cost
                            cost_list = np.zeros(iter,)
                            for i in range(iter):
                                weights = weights - alpha*dot(X.T,self.sigmoid(dot(X,weights))-np.reshape(y,(len(y),1)))
                                cost_list[i] = cost(weights)
                            self.weights = weights
                            return cost_list
                        def predict(self,X):
                            z = dot(self.initialize(X)[1],self.weights)
                            lis = []
                            for i in self.sigmoid(z):
                                if i>0.5:
                                    lis.append(1)
                                else:
                                    lis.append(0)
                            return lis
                    # standardize(X_tr)
                    # standardize(X_te)
                    obj1 = LogidticRegression()
                    model= obj1.fit(X_tr,y_tr)
                    y_pred = obj1.predict(X_te)
                    y_train = obj1.predict(X_tr)
                    #Let's see the f1-score for training and testing data
                    f1_score_tr = F1_score(y_tr,y_train)
                    f1_score_te = F1_score(y_te,y_pred)
                    print(f1_score_tr)
                    print(f1_score_te)     
            window1.config(menu = menubar)
            window1.mainloop()
    
        elif assignment == "Assignment6":
            window1 = Tk()
            window1.title(assignment)
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='k-Means', command = lambda: SolveQuestion("k-Means"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "k-Means":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("800x500")
                    Label(window2, text="k",font=('Verdana', 12)).grid(row=1,column=1,padx=20,pady=30)
                    answer1 = Entry(window2)
                    answer1.grid(row=1,column=2,padx=20,pady=30)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:makeCluster(int(answer1.get()))).grid(column=1,row=6,padx=20,pady=30) 
                    def makeCluster(k):
                        dft = data.iloc[: , :-1] #dropping target column
                        randomIndex = []
                        currMeans = []
                        for i in range(k):
                            randomIndex.append(random.randint(0, len(data)-1))
                        for r in randomIndex:
                            currMeans.append(dft.iloc[r])
                            print(type(dft.iloc[r]))
                        
                        prevMeans = []
                        print(currMeans)
                        while(currMeans != prevMeans):
                            for i in range(len(dft)):
                                sumDict = dict()
                                for t in currMeans:
                                    sumDict[t] = 0
                                print(sumDict)
                                for cm in  currMeans:
                                    for c in dft.columns:
                                        sumDict[cm] += abs(dft.iloc[i, c]-cm.iloc[i, c])
                                minTuple = pd.Series()
                                minSum = sys.maxint
                                for j in sumDict.keys():
                                    if(sumDict[j] < minSum):
                                        minSum = sumDict[j]
                                        minTuple = j  
                                print(minTuple)
                            if 1:
                                break
                                
                    window2.mainloop()

            window1.config(menu = menubar)
            window1.mainloop()

        elif assignment == "Assignment7":
            window1 = Tk()
            window1.title(assignment)
            window1.geometry("300x300")
            menubar = Menu(window1)
            questions = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Topics', menu = questions)
            questions.add_command(label ='Apriori Algo', command = lambda: SolveQuestion("Apriori Algo"))
            Label(window1,text="Select Topic from Menu", font=('Verdana', 14), fg="#fff",bg="#555",height=4).grid(row=0,column=0,padx=20,pady=30)
            def SolveQuestion(question):
                if question == "Apriori Algo":
                    window2 = Tk()
                    window2.title(question)
                    window2.geometry("800x500")
                    Label(window2, text='''Minimum support(Don't put '%' sign)''',font=('Verdana', 12)).grid(row=1,column=1,padx=20,pady=30)
                    answer1 = Entry(window2)
                    answer1.grid(row=1,column=2,padx=20,pady=30)
                    Label(window2, text='''Threshold Confidence(Don't put '%' sign)''',font=('Verdana', 12)).grid(row=2,column=1,padx=20,pady=30)
                    answer2 = Entry(window2)
                    answer2.grid(row=2,column=2,padx=20,pady=30)
                    cols = []
                    for i in data.columns:
                        cols.append(i)
                    Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:findClass(int(answer1.get()), int(answer2.get()))).grid(column=1,row=6,padx=20,pady=30) 
                    def findClass(min_support,threshold_confidence):
                        print(min_support,threshold_confidence)

                        # Reading Excel file 
                        bread = data
                        bread = bread.drop_duplicates()

                        bread = bread.drop('DateTime', axis=1)
                        print(len(set(bread['Items'])))
                        print(bread.head)

                        transaction = pd.crosstab(index= bread['TransactionNo'], columns= bread['Items'])
                        print(transaction)


                        def APRIORI_MY(data, min_support=0.04,  max_length = 4):
                            from itertools import combinations
                            # Step 1:
                            # Creating a dictionary to stored support of an itemset.
                            support = {} 
                            L = list(data.columns)
                            
                            # Step 2: 
                            #generating combination of items with len i in ith iteration
                            for i in range(1, max_length+1):
                                c = set(combinations(L,i))
                                
                            # Reset "L" for next ith iteration
                                L =set()     
                            # Step 3: 
                                #iterate through each item in "c"
                                for j in list(c):
                                    #print(j)
                                    sup = data.loc[:,j].product(axis=1).sum()/len(data.index)
                                    if sup > min_support:
                                        #print(sup, j)
                                        support[j] = sup
                                        
                                        # Appending frequent itemset in list "L", already reset list "L" 
                                        L = list(set(L) | set(j))
                                
                            # Step 4: data frame with cols "items", 'support'
                            result = pd.DataFrame(list(support.items()), columns = ["Items", "Support"])
                            return(result)

                        ## finding frequent itemset with min support = 4% 0.04
                        my_freq_itemset = APRIORI_MY(transaction, float(min_support/100), 3)
                        my_freq_itemset.sort_values(by = 'Support', ascending = False)

                        print(my_freq_itemset)

                        def ASSOCIATION_RULE_MY(df, min_threshold=0.5):
                            from itertools import permutations
                            
                            # STEP 1:
                            #creating required varaible
                            support = pd.Series(df.Support.values, index=df.Items).to_dict()
                            data = []
                            L= df.Items.values
                            
                            # Step 2:
                            #generating rule using permutation
                            p = list(permutations(L, 2))
                            
                            # Iterating through each rule
                            for i in p:
                                
                                # If LHS(Antecedent) of rule is subset of RHS then valid rule.
                                if set(i[0]).issubset(i[1]):
                                    conf = support[i[1]]/support[i[0]]
                                    #print(i, conf)
                                    if conf > min_threshold:
                                        #print(i, conf)
                                        j = i[1][not i[1].index(i[0][0])]
                                        lift = support[i[1]]/(support[i[0]]* support[(j,)])
                                        leverage = support[i[1]] - (support[i[0]]* support[(j,)])
                                        convection = (1 - support[(j,)])/(1- conf)
                                        data.append([i[0], (j,), support[i[0]], support[(j,)], support[i[1]], conf, lift, leverage, convection])

                                
                            # STEP 3:
                            result = pd.DataFrame(data, columns = ["antecedents", "consequents", "antecedent support", "consequent support",
                                                                "support", "confidence", "Lift", "Leverage", "Convection"])
                            return(result)

                        ## Rule with minimun confidence = 50%
                        my_rule = ASSOCIATION_RULE_MY(my_freq_itemset, float(threshold_confidence/100))
                        print(my_rule)  
                        print(type(my_rule))
                        window3 = Tk()
                        window3.title("2019BTECS00025-Data Analysis Tool")
                        window3.geometry("600x500")
                        
                        tv1 = ttk.Treeview(window3)
                        tv1.place(relheight=1, relwidth=1)

                        treescrolly = Scrollbar(window3, orient="vertical", command=tv1.yview) 
                        treescrollx = Scrollbar(window3, orient="horizontal", command=tv1.xview)
                        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
                        treescrollx.pack(side="bottom", fill="x")
                        treescrolly.pack(side="right", fill="y") 
                        tv1["column"] = list(my_rule.columns)
                        tv1["show"] = "headings"
                        for column in tv1["columns"]:
                            tv1.heading(column, text=column) 

                        df_rows = my_rule.to_numpy().tolist() 
                        for row in df_rows:
                            tv1.insert("", "end", values=row)
                        window3.mainloop()
                    window2.mainloop()
            window1.config(menu = menubar)
            window1.mainloop()
    w.mainloop()                  
       
def assignment8():
    w = Tk()
    w.title("2019BTECS00025-Data Analysis Tool")
    w.geometry("400x400")
    
    # Creating Menubar
    menubar = Menu(w)
    
    # Adding File Menu and commands
    topics = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Topics', menu = topics)
    topics.add_command(label ='Crawler', command = lambda: GoToAssignment("Crawler"))  
    topics.add_command(label ='PageRank Algorithm', command = lambda: GoToAssignment("PageRank Algorithm"))  
    topics.add_command(label ='HITS Algorithm', command = lambda: GoToAssignment("HITS Algorithm"))  
    
    label1 = Label(w,text="Select Topic from Menu",  justify='center', font=('Verdana', 14), fg="#fff",bg="#555",height=4) #.grid(row=0,column=0,padx=20,pady=30)
    label1.place(relx=0.5, rely=0.1, anchor=CENTER)

    label2 = Label(w, text="URL",  justify='center', font=('Verdana', 12)) #.grid(row=1,column=0,padx=20,pady=30)
    label2.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    answer1 = Entry(w, justify='center')
    # answer1.grid(row=1,column=2,padx=20,pady=30)      
    answer1.place(relx=0.5, rely=0.5, anchor=CENTER)
    # display Menu
    w.config(menu = menubar)
    
    def GoToAssignment(topic):
        if topic == "Crawler":
            window2 = Tk()
            window2.title(topic)
            window2.geometry("600x500")
            cols = ['BFS', 'DFS']
            clickedAttribute = StringVar(window2)
            clickedAttribute.set("Select Procedure")
            dropCols = OptionMenu(window2, clickedAttribute, *cols)
            dropCols.grid(column=1,row=5,padx=20,pady=30)
            Button(window2,text="Compute",font=('Verdana', 12), width=15, height=5,command= lambda:getURLs(answer1.get(),clickedAttribute.get())).grid(column=1,row=6,padx=20,pady=30) 
            def getURLs(inputURL, procedure):
                # Set for storing urls with same domain
                links_intern = set()
                input_url = inputURL
                
                # Set for storing urls with different domain
                links_extern = set()
                
                
                # Method for crawling a url at next level
                def level_crawler(input_url):
                    temp_urls = set()
                    current_url_domain = urlparse(input_url).netloc
                
                    # Creates beautiful soup object to extract html tags
                    beautiful_soup_object = BeautifulSoup(
                        requests.get(input_url).content, "lxml")

                    # Access all anchor tags from input 
                    # url page and divide them into internal
                    # and external categories
                    for anchor in beautiful_soup_object.findAll("a"):
                        href = anchor.attrs.get("href")
                        if(href != "" or href != None):
                            href = urljoin(input_url, href)
                            href_parsed = urlparse(href)
                            href = href_parsed.scheme
                            href += "://"
                            href += href_parsed.netloc
                            href += href_parsed.path
                            final_parsed_href = urlparse(href)
                            is_valid = bool(final_parsed_href.scheme) and bool(
                                final_parsed_href.netloc)
                            if is_valid:
                                if current_url_domain not in href and href not in links_extern:
                                    print("{}".format(href))
                                    links_extern.add(href)
                                if current_url_domain in href and href not in links_intern:
                                    print("{}".format(href))
                                    links_intern.add(href)
                                    temp_urls.add(href)
                    return temp_urls
                
                #BFS
                if procedure == 'BFS':
                    queue = []
                    queue.append(input_url)
                    for count in range(len(queue)):
                        url = queue.pop(0)
                        urls = level_crawler(url)
                        for i in urls:
                            queue.append(i)
                
                if procedure == 'DFS':
                    def get_links_recursive(base, path, visited, max_depth=3, depth=0):
                        if depth < max_depth:
                            try:
                                soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

                                for link in soup.find_all("a"):
                                    href = link.get("href")
                                    href = urljoin(input_url, href)
                                    href_parsed = urlparse(href)
                                    href = href_parsed.scheme
                                    href += "://"
                                    href += href_parsed.netloc
                                    href += href_parsed.path
                                    
                                    if href not in visited:
                                        visited.add(href)
                                        print("{}".format(href))

                                        if href.startswith("http"):
                                            get_links_recursive(href, "", visited, max_depth, depth + 1)
                                        else:
                                            get_links_recursive(base, href, visited, max_depth, depth + 1)
                            except:
                                pass
                    get_links_recursive(input_url, "", set([input_url]))
               
            window2.mainloop()
        
    w.mainloop()
def Usage():
    mb.showinfo("Product Information", "1.Browse dataset .csv file from file explorer \n2.First select assignment number from menu dropdown \n3.Perform data analysis of your choice from menu\n")


window = Tk()
window.title("2019BTECS00025-Data Analysis Tool")
window.geometry("600x500")
labelHead = Label(window,text="Data Analysis Tool",justify='center',font=("Verdana", 34),background='#c345fc',foreground='#fff')
label_file_explorer = Label(window,text="Choose Dataset from File Explorer",justify='center',font=("Verdana", 14),height=4,fg="blue")
button_explore = Button(window,text="Browse Dataset", justify='center', width=20, height=4, font=("Verdana", 8),command=browseDataset)
button_skip = Button(window,text="Skip to assignment8", justify='center', width=20, height=2, font=("Verdana", 8),command=assignment8)
labelHead.place(relx=0.5, rely=0.1, anchor=CENTER)
label_file_explorer.place(relx=0.5, rely=0.3, anchor=CENTER)
button_explore.place(relx=0.5, rely=0.5, anchor=CENTER)
button_skip.place(relx=0.5, rely=0.7, anchor=CENTER)

# labelHead.grid(row=1,column=1,padx=15,pady=20)
# label_file_explorer.grid(column=1,row=2,padx=20,pady=30)
# button_explore.grid(column=1,row=3,padx=20,pady=30)
# display Menu
menubar = Menu(window)
helps = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Usage', menu = helps)
helps.add_command(label ='HowToUse?', command = Usage)
window.config(menu = menubar,bg='#18253f')
window.config(bg='#18253f')
window.mainloop()