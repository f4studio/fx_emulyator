# -*- coding: utf-8 -*-
# open csv, read, visualise, create mask decision tree,
#python --version      Python 2.7.12

import matplotlib as mpl #визуализация - библиотека построения графиков
import matplotlib.pyplot as plt  #визуализация - библиотека построения графиков
import math
import csv
from datetime import datetime, date, time
#%matplotlib   #график выводится в отдельном окне
from sklearn import tree

#test git commit

timestamp1=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

testV=[['0.8414709848078965'], ['0.9092974268256817'], ['0.1411200080598672'], ['-0.7568024953079282'], ['-0.9589242746631385'], ['-0.27941549819892586'], ['0.6569865987187891'], ['0.9893582466233818'], ['0.4121184852417566']]

testV2=[['11'], ['13'], ['15'], ['17'], ['19'], ['21'], ['23'], ['25'], ['27']]

'''==============================================================================='''

'''
На входе
  maskln длина маски, funcdata массив значения функции, xmult на сколько умножить для работы с целыми числами    
На выхлоде
  masks[n][xxxx,xxxx,xxxx,xxxx,xxxx,xxxx]
  maskLastOne[n][xxx]
  [n][массив движений(значений)][движение(значение) которое мы будем учиться предсказывать] 
'''  
def Masker(maskln, funcdata,xmult):
  masks=[ [0]*maskln for x in range(0,(len(funcdata)-maskln) )]  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
  maskLastOne=[0]*(len(funcdata)-maskln)    # [0, 0, 0, 0, 0, 0, 0]
  i=0
  k=0
  muskNumber = 0

  #print masks   
  
  while k<=len(funcdata)-maskln-1:
    #print(k)
    #print(masks)
    #print(maskLastOne)
    
    coefficient=(funcdata[k+maskln-1][0])
    while (i < maskln+1):
      if (i==maskln):
        maskLastOne[ muskNumber ]=int( (     ( (funcdata[k][0])-coefficient )*xmult    )//1)
      else:  
        masks[ muskNumber ][i]=int( (     ( (funcdata[k][0])-coefficient )*xmult      )//1)       
      i+=1
      k+=1
    k=k-maskln
    muskNumber = k
    i=0 
  
  #print('-----------')
  #print(masks)
  #print(maskLastOne)
  return masks, maskLastOne  

#функция потом (данные, длина маски) 
#Помните, что списки передаются как ссылки, не как глубокая копия.
def MakeMaskForEnding(dataset1,maskLn,xmult):
   
  coeff  =  (dataset1[-1][0])  
  #print coeff
  index=0
  konchik=[]
  while index<maskLn:

    konchik.append(  int(   ( (dataset1[index-maskLn][0])   - coeff  )*xmult )   )  # да отрицательные индексы
    index+=1
  t=[]
  t.append( konchik )
  #print('---')  
  #print coeff
  #print('---')
  return coeff,t


'''==============================================================================='''
'''==============================================================================='''
'''==============================================================================='''


funcvalues=[] #массив под значения функции

print('Hello world')
dpi = 80    #число точек на дюйм в изображении
fig = plt.figure(dpi = dpi, figsize = (1012 / dpi, 484 / dpi) )#размер судя по всему в дюймах
plt.rcParams.update({'font.size': 10})

plt.axis([0, 150000, 55, 65])
##plt.axis([0, 140, 0, 140])

#ofile  = open('test1122.csv', "rb",0)
ofile  = open('logfile_log1_cut.txt', "rb",0)

x = 0  #будем считать число значений
count =0 # не знаю зачем это тут, напишите кто знает
xs=[]; 
maskLn=150
xMult=1
xMult2=10000
newValWeNeed=400


reader = csv.reader(ofile, lineterminator='\n')#csv.reader(csvfile, delimiter=' ', quotechar='|')
for row in reader: 
  #print row, reader 
  funcvalues.append(row)
  xs += [x]  #оказывается так можно, добавлять в массив     
  x+=1
  if x>10000: #ограничитель тестируем
    break



##print funcvalues 
#print funcvalues  # [ ['0.8414709848078965'], ['0.9092974268256817'], ['0.1411200080598672'] ]
            
#print xs  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(xs, funcvalues, color = 'green', linestyle = 'solid', label = 'funcvalues')
plt.legend(loc = 'upper right')
fig.savefig('dataset_input_'+timestamp1+'.png')

testV2=[]
for cc in funcvalues:  
  
  #print ('=')
  testV2.append(  [ int(float(cc[0])*xMult2) ]  )
#print testV2   


 #логика стратегии класификатор#

print('Masker...')
# моё творчество
features,labels = Masker(maskLn,testV2,xMult)
##print(features)
##print(labels)
'''
#sklearn example
from sklearn import tree
features=[[4,2,1],[7,3,0],[5,7,0],[5,4,1],[5,4,0],[5,4,1]]
labels=[1,0,0,1,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print clf.predict([[2,1,5]])
'''
print('TreeClassifier...');
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)   #(данные - последовательность, реакция - следующее число последовательности)
#print clf.predict([[-3.0, -2.0, -1.0, 0.0]]) # передаём новые неведаные данные и получаем предсказание следующего число последовательности

print('Looking for new values...')

m=0
while m<newValWeNeed:
  m+=1
  coeff, konchikMask= MakeMaskForEnding(testV2,maskLn,xMult)
  newOne=clf.predict(konchikMask)  # передаём новые неведаные данные и получаем предсказание следующего число последовательности
  nO=newOne[0]+coeff
  testV2.append( [nO] )
  xs += [x]  #оказывается так можно, добавлять в массив     
  x+=1


##print testV2

  #конец логика стратегии класификатор#

#написовать новый графих с новыми значениями
plt.axis([0, 150000, 550000, 650000])
plt.plot(xs, testV2, color = 'red', linestyle = 'solid', label = 'funcvalues')
plt.legend(loc = 'upper right')
fig.savefig('dataset_output_sklearn_'+timestamp1+'.png')


ofile  = open('dataset_output_sklearn_'+timestamp1+'.csv', "wb",0)
writer = csv.writer(ofile, lineterminator='\n')
writer.writerows(testV2)



''' у данных в основной задаче не более 4 знаков после запятой, 
буду умножать на 1000 и резать, 
чтоб работать с натуральными числами потом в sklearn,
как оказалось оно плохо с float

синус просто пример для теста, так что и так сойдёт, потеряется точность с ним
'''




