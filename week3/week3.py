# import json
# with open("taipei-attractions-assignment.json",mode="r",encoding="utf-8") as file:
#     data = json.load(file)
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

main = data['result']['results']

import re

#attraction.csv
with open("attraction.csv", mode="w", encoding="utf-8") as file:
    for x in main:
        #find the end of first URL
        first_img = re.search("http.*?.jpg",x["file"],re.IGNORECASE).group()       
        #write
        file.write(x["stitle"] + "," + x["address"][5:8] + "," + x["longitude"] + "," + first_img +"\n")

#mrt.csv

#make a list of MRT station
mrt_station = []
for a in main:
    #陽明山國家公園 “MRT":null 
    #error will occur, so I check the type
    if type(a["MRT"]) is str:
        mrt_station.append(a["MRT"])
#remove duplicates in list
mrt_station = set(mrt_station)


with open("mrt.csv", mode="w", encoding="utf-8") as file:
    #write station name
    for b in mrt_station:
        #find out sites matches station
        several_sites = ""
        for c in main:
            if c["MRT"] == b:
                several_sites += ("," + c["stitle"])
        #write in file "mrt.csv" (combine station name with corresponding sites)
        file.write(b+ several_sites + "\n")


   

