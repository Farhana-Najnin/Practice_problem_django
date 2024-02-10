from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author':'Rahim', 'age':20, 'author':"nivedika",'age':25,'lst' : ['python','is','best'],'birthday':datetime.datetime.now(),'val':'','value':'5',
       'value1': [
            {'name': 'Mosh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        'st':'I Am Master Yoda',
        'value2':['Banana', 'Mango', 'Orange'],
        'na':'ABCDEF'
  }
    
    return render(request,'home.html',d )