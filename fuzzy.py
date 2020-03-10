import csv
import numpy as np
import pandas as pd
data = []
batas1 = 35
batas2 = 62
batas3 = 80
batas4 = 100

batas5 = 59
batas6 = 63
batas7 = 70
batas8 = 85

with open('dataTest.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
def low_linguistik(batas1, batas2, x):
    if (x<batas1) : return 1
    elif (x<batas2) :
        return ((batas2 - x)/(batas2 - batas1))
    else : return 0
def average_linguistik(batas1, batas2, batas3, batas4, x):
    if (x<batas1) : return 0
    elif (x<batas2) :
        return ((x - batas1)/(batas2 - batas1))
    elif (x<batas3) : return 1
    elif (x<batas4) : return ((batas4 - x)/(batas4 - batas3))
    else : return 0
def high_linguistik(batas1, batas2, x) :
    if (x<batas1) : return 0
    elif (x<batas2) : return ((x - batas1)/(batas2 - batas1))
    else : return 1
def fuzzification(data) : 
	data.append(low_linguistik(batas1, batas2, float(data[1])))
	data.append(average_linguistik(batas1, batas2, batas3, batas4, float(data[1])))
	data.append(high_linguistik(batas3, batas4, float(data[1])))
	data.append(low_linguistik(batas5, batas6, float(data[2])))
	data.append(average_linguistik(batas5, batas6, batas7, batas8, float(data[2])))
	data.append(high_linguistik(batas7, batas8, float(data[2])))
	return data

def accepted(row):
	return max(min(float(row[4]),float(row[8])),min(float(row[4]),float(row[9])), min(float(row[5]),float(row[8])), min(float(row[5]),float(row[9])), min(float(row[6]),float(row[8])), min(float(row[6]),float(row[9])))
def rejected(row):
	return max(min(float(row[4]),float(row[7])), min(float(row[5]),float(row[7])),min(float(row[6]),float(row[7])))
def inference(row):
	row.append(accepted(row))
	row.append(rejected(row))
	return row
def  deffuzification(row):
	no = [1,1,1,1,1,0.583,0.167,0,0,0]
	yes  = [0,0,0,0,0,0.417,0.833,1,1,1]
	a = []
	for x in range(0,10) :
		yes[x] = min(yes[x], row[10])
		no[x] = min(no[x], row[11])
		a.append(max(yes[x], no[x]))
	row.append(((a[0]*10)+(a[1]*20)+(a[2]*30)+(a[3]*40)+(a[4]*50)+(a[5]*60)+(a[6]*70)+(a[7]*80)+(a[8]*90)+(a[9]*100)) / np.sum(a))
	return row    
def kelas(x):
    if x > 50:
        return 'Ya'
    else:
        return 'Tidak'
    
data.pop(0)
def get(element):
	return element[12]
clas = []
idp = []
at1 = []
at2 = []
clas1 = []
defuzz = []
for i in range(0,10):
	data[i] = fuzzification(data[i])
	data[i] = inference(data[i])
	data[i] = deffuzification(data[i])
	clas.append(kelas(data[i][12]))
	idp.append(data[i][0])
	at1.append(data[i][1])
	at2.append(data[i][2])
	clas1.append(data[i][3])
	defuzz.append(data[i][12])
#kalo mau ngetest data.csv rangenya 0-20
def akurasi(data1, data2):
    sum = 0
    for i in range(0, len(data1)):
        if data1[i] == data2[i]:
            sum = sum + 1
    return sum * 100 / len(data1)
                
print(clas)
#print("Nilai Akurasi : ", akurasi(clas, clas1), "%") #buat test data.csv
dataBaru = {'ID':idp, 'Tes Kompetensi':at1, 'Tes Keprbadian':at2, 'Keputusan':clas, 'Nilai Fuzzy':defuzz}
df = pd.DataFrame(dataBaru)
df.to_csv("TebakanTugas3.csv", index=False)

