import csv
import geopy
from geopy.geocoders import Nominatim
import pandas as pd
import sys

values=[]
col=5
df1 = pd.read_csv("awards.csv",delimiter=',')
df2 = pd.read_csv("contracts.csv",delimiter=',')
df = pd.merge(df1, df2, how='outer', on=['contractname'])
df.to_csv("merged.csv", index=False)
saved_column=df.contractname
print(saved_column)


with open('merged.csv', 'r') as csv:
    cols=[4]
    for line in csv.readlines():
        content = list(line[i] for i in cols)
        print(content)
      
        elements = line.strip().split(',')
        try:
             if int(elements[col]) == Amount:
                 values.append(int(elements[col]))
                 break
        except ValueError:
             csum = sum(values)
print("Sum of column %d: %f" % (col, csum))


def geolocator():
        table_string = ""
        listAddress=[]
        geolocator = Nominatim()
        locationsList=['Banke','Makwanpur','Lalitpur']
        for i in locationsList:
            table_string += "<tr>" + \
                          "<td>" + \
                              "".join(i) + \
                          "</td>" + \
                        "</tr>\n"
    
            sys.stdout.write( table_string )
          
            location = geolocator.geocode(i)
            #here we pass the values of latitude and longitudes in a javascript function 
            "<html><td>"
            "<tr>"
            "< a href="" onclick=javascript:loadMap({{location.latitude , location.longitude}});>{{location}}</a>"
            "</tr>"
            "</td>"
            "</html>"
            a=print(location.latitude, location.longitude)
            listAddress.append(a)
        return listAddress

geolocator()

def merge():
     df=pd.read_csv('merged.csv')
     df['latlon']=df['Amount']
     df.to_csv("mergedWithLatlon.csv", index=False)
     return(df)

merge()







    





