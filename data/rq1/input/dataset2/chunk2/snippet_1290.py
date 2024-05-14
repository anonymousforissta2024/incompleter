#Source: https://stackoverflow.com/questions/51684913/typeerror-int-object-is-not-iterable-using-python-3
import json
import csv

with open('leap_data.json') as f:
    data = json.load(f)
#print(data)
cnt=0
final_list={}

for k,v in data.items():
    for m,n in v.items():
        #print n
        cnt=cnt+1
        #print cnt
        if cnt==6:
            #print n
            for data1 in n:
                for a,b in data1.items():
                    final_list[a]=b    
                with open('output4.json', 'a') as outfile:  
                    json.dump(final_list,outfile)

            my_list = "["+open('output4.json').read().replace("}{","},{")+"]"
            data_1 = json.loads(my_list)
            print(data_1)


with open(r'samp.csv', 'w+') as csvfile:
  output = csv.writer(csvfile)
  output.writerow(data_1[0].keys())
  for row in data_1:
        output.writerow(row.values())