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

import copy
#test git commit

timestamp1=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
logger=1 #вести лог
log=[["Журналы."]]

#####

testV=[['0.8414709848078965'], ['0.9092974268256817'], ['0.1411200080598672'], ['-0.7568024953079282'], ['-0.9589242746631385'], ['-0.27941549819892586'], ['0.6569865987187891'], ['0.9893582466233818'], ['0.4121184852417566']]

originalData=[['11'], ['13'], ['15'], ['17'], ['19'], ['21'], ['23'], ['25'], ['27']]

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
  #print dataset1  
  coeff  =  (dataset1[-1][0])  
  #print coeff
  index=0
  konchik=[]
  while index<maskLn:
    #print dataset1[index-maskLn][0]  
    konchik.append(  int(   ( (dataset1[index-maskLn][0])   - coeff  )*xmult )   )  # берём с конца через отрицательные индексы питона
    index+=1
  maska=[]
  maska.append( konchik )
  #print('---')  
  #print coeff
  #print('---')
  return coeff,maska


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
ofile  = open('testovaya_data1.txt', "rb",0)  #logfile_log1_cut.txt

x = 0  #будем считать число значений
count =0 # не знаю зачем это тут, напишите кто знает
xs=[]; # сколько у нас будет чисел считано из файла, а дальнейшем возможно длина массива + новые значения
#print xs  # [0, 1, 2, 3, 4, 5, 6, 7, 8]  в таком виде чтоб скормить рисовалке графика
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
            


plt.plot(xs, funcvalues, color = 'green', linestyle = 'solid', label = 'funcvalues')
plt.legend(loc = 'upper right')
fig.savefig(timestamp1+'dataset_input.png')


#сделать всё целыми числами, множим на xMult2  ~10000
originalData=[]
#print funcvalues
#print("-----------------")
for cc in funcvalues:  
  originalData.append(  [ int( round(float(cc[0])*xMult2,0) )  ]  )
 
# (pyton2,7) Сегодня я потратил 8 часов чтоб в итоге всплыло вот это
# int(100117.99999) = 100117
# int(round(100117.99999, 0)) = 100118


#######
# функции GoogleTraTrend


def MaskCheckMatch(maskFromHistory
               ,maska
               ,pogreshnosT
               ,maskLn
  ):
  #сравнниваем нашу и из истории, сравнивая каждое значение
  jindeX=1    
  while jindeX<maskLn:  #  
    #print maskFromHistory
    #print("nextValuE "+str(nextValuE)+" stroka № "+str(len(newdataset)+indeX-maskLn-sdviG) )
    #print maska
    #print("==============")
    #print maskLn
    #print -jindeX
    #print maskFromHistory
    maskFromHistory[-jindeX]
    maska[-jindeX]
    if( (maskFromHistory[-jindeX]-pogreshnosT <= maska[-jindeX]) and (maskFromHistory[-jindeX]+pogreshnosT >= maska[-jindeX]) ):
      #log.append( "match "+str(maskFromHistory[-jindeX])+ " = " +str(maska[-jindeX]))   
      flag=flag=1  
      #print("flag="+str(flag) )    
    else:
      flag=flag=0
      #log.append( "not m "+str(maskFromHistory[-jindeX])+ " = "+ str(maska[-jindeX]))
      #print("flag="+str(flag) )    
      break
    jindeX+=1 #следующие значение в маске
  #print("flag last="+str(flag) )    
  #сравнниваем нашу и из истории, сравнивая каждое значение КОНЕЦ
  return flag    



def MaskFromHistory(newdataset # дата из которой делаем маску
                   ,sdviG # до какой позиции с конца, конец маски дудет эта позиция в дате
                   ,maskLn
                   ,maskFromHistory
  ):# грустный смайлик
  #maskFromHistory=[0]*maskLn
  #сделали маску из истории и сохранили значение за ней
  coeff  =  (newdataset[-1-sdviG][0])  
  indeX=0
  while indeX<maskLn:
    maskFromHistory[indeX] = newdataset[indeX-maskLn-sdviG][0] - coeff  # идём с конца через отрицательные индексы питона
    indeX+=1  
  nextValuE=newdataset[indeX-maskLn-sdviG][0]-coeff #следующие маско-значение после найденой маски
  #сделали маску из истории и созранили значение за ней КОНЕЦ
  #print("nextValuE "+str(nextValuE)+" stroka № "+str(len(newdataset)+indeX-maskLn-sdviG) )
  return nextValuE,coeff  




#сделать маску, искать , увеличить маску, не нашли взять последнюю найденую
def GoogleTraRek(howFar #длина истории в которой ищем
                  ,rekDeep #глубина рекурсии
                  ,maskLn #начальная ширина маски
                  ,maska
                  ,rekStop #регулятор 
                  ,pogreshnosT #величина погрешности, рекомендуемые значения 1-100
                  ,newdataset
                                                                                      ):
  #func code
  log.append( [ "Рекурсивный поиск. Уровень рекурсии "+str(rekDeep)] )
  #print("in rek "+str(rekDeep))


  #получить маску и следующее за ней маско-значение
  sdviG=1 # ++
  flag=1
  flagS=0 #надо понять не нашлось значений или закончилась рекурсия, будет 0 или 1 
  nextValuE=99999
  ReValuE=99999
  reFlaG=0
  maskFromHistory=[0]*maskLn
  while sdviG<(howFar-maskLn):#ищем совпадение маски двигаясь взад
    
    nextValuE,coeff=MaskFromHistory(newdataset,sdviG,maskLn,maskFromHistory)
    log.append( [ "С позиции "+str(-1*sdviG)+" взята маска "+ str(maskFromHistory)+" coef "+str(coeff)] )   
    
    #log.append( ["maskLn"+str(maskLn)])
    #print("maskLn"+str(maskLn))
    
    flag=MaskCheckMatch(maskFromHistory,maska,pogreshnosT,maskLn)
    log.append( [ "Сравнение последних "+str(maskLn)+" значений. Совпало="+str(flag)+" В масках "+ str(maskFromHistory) + " и " +str(maska) ])   
    
    #if(rekStop<=rekDeep):
    #  print("GoogleTraRek skipped: rekStop<rekDeep")
    #  log.append("GoogleTraRek skipped: rekStop<rekDeep")
    
    #реагируем на совпадение или несопадение масок из истории и нашей
    if((flag==1)):#если маски совпали
      flagS=1  
      log.append( [ "Реагируем по случаю находки, запускаем GoogleTraRek, ищем маску шире" ] )  
      
      if(rekStop<=rekDeep):
        print("GoogleTraRek skipped: rekStop<rekDeep")
        log.append(["GoogleTraRek skipped: rekStop<rekDeep"])      
      else:
        ReValuE,reFlaG=GoogleTraRek(howFar,rekDeep+1,maskLn+1,maska,rekStop,pogreshnosT,newdataset)
      
      log.append( [ "Куда-то упёрлись. Возврат назад внутри рекурсии. "])
      break
    #реагируем на совпадение или несопадение масок из истории и нашей КОНЕЦ  
    
    
    sdviG+=1 #сдвигаемся в глубь истории
  #предупреждения      
  #if(rekDeep<5):
    #print("GoogleTraRek() не эфективно, rekDeep не достиг хотябы 5. Need increase pogreshnosT or dataset.")  
    
  if((flagS==1)and(reFlaG==1)):
    nextValuE=ReValuE
    
  return nextValuE,flagS  


def zzz(a):
  return a


#                  длина истории в которой ищем, сколько новых значений нам надо, глубина рекурсии, начальная ширина маски 
#def GoogleTraTrend(howFar                       ,newValWeNeed                   ,rekDeep           ,startWidth           ):

def GoogleTraTrend(#howFar, #длина истории в которой ищем
                   newValWeNeed #сколько новых значений нам надо
                  ,rekStop #максимальная глубина рекурсии
                  ,maskLn #начальная ширина маски
                  ,pogreshnosT #величина погрешности, рекомендуемые значения 1-100
                  ,arrayln
                  ,newdataset
                  
                                                                                    ):
  if(rekStop+maskLn>len(newdataset)):
    print("Слишком мало входных данных, должны хотябы превышать rekStop+maskLn. Ничего не делаю.")
    log.append( [ "Слишком мало входных данных, должны хотябы превышать rekStop+maskLn. Ничего не делаю."])
  else:  
    #func code  
    m=0
    a=0
    b=0
    log.append( [ "Запуск GoogleTraTrend "] )
    x=len(arrayln)
    while m<newValWeNeed:
      coeff,maska=MakeMaskForEnding(newdataset,maskLn+rekStop,1)
      log.append( [ "Сделана маска для конца "+str(maska)+" coeff="+str(coeff)] )
      #print("Ending mask:")
      #print(maska)
      #print("coeff "+str(coeff))
      #функция предсказания следующего значения
      #depth=0 #отслеживать глубину вложесноти рекурсии чтоб если мы на ней уже были не терять время
    
      log.append( [ "Рекурсия GoogleTraRek"] )   
      #a,b=print 
      a,b=(GoogleTraRek(x,0,maskLn,maska[0],rekStop,pogreshnosT,newdataset))
      #print(type(a))
      #print(a[0])
      nO=coeff + a
      print("==========New= "+str(nO))
      newdataset.append( [nO] )
  
      m+=1
      arrayln += [x]  #оказывается так можно, добавлять в массив     
      x+=1 #размер массива с новым данным будет больше, нужен чтоб использовать для рисования потом 
 

############################################################################
 #логика стратегии GoogleTraTrend


arrayln=copy.deepcopy(xs)
newdataset=copy.deepcopy(originalData)


#print originalData
print("-=-=-=-=-=-=-=-")
GoogleTraTrend(    10 #сколько новых значений нам надо
                  ,18 #максимальная глубина рекурсии
                  ,3 #начальная ширина маски
                  ,0 #величина погрешности, рекомендуемые значения 1-100
                  ,arrayln
                  ,newdataset
                                                                            )

print newdataset 
############################################################################
 #логика стратегии класификатор#



'''
print('Masker...')
# моё творчество
features,labels = Masker(maskLn,originalData,xMult)
##print(features)
##print(labels)

##############sklearn example
#from sklearn import tree
#features=[[4,2,1],[7,3,0],[5,7,0],[5,4,1],[5,4,0],[5,4,1]]
#labels=[1,0,0,1,1,1]
#clf=tree.DecisionTreeClassifier()
#clf=clf.fit(features,labels)
#print clf.predict([[2,1,5]])
###############
print('TreeClassifier...');
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)   #(данные - последовательность, реакция - следующее число последовательности)
#print clf.predict([[-3.0, -2.0, -1.0, 0.0]]) # передаём новые неведаные данные и получаем предсказание следующего число последовательности

print('Looking for new values...')

m=0
while m<newValWeNeed:
  m+=1
  xs += [x]  #оказывается так можно, добавлять в массив     
  x+=1
  coeff, konchikMask= MakeMaskForEnding(originalData,maskLn,xMult)
  newOne=clf.predict(konchikMask)  # передаём новые неведаные данные и получаем предсказание следующего число последовательности
  nO=newOne[0]+coeff
  originalData.append( [nO] )



##print originalData

  #конец логика стратегии класификатор#

#написовать новый графих с новыми значениями
plt.axis([0, 150000, 550000, 650000])
plt.plot(xs, originalData, color = 'red', linestyle = 'solid', label = 'funcvalues')
plt.legend(loc = 'upper right')
fig.savefig('dataset_output_sklearn_'+timestamp1+'.png')


ofile  = open('dataset_output_sklearn_'+timestamp1+'.csv', "wb",0)
writer = csv.writer(ofile, lineterminator='\n')
writer.writerows(originalData)


'''






#написовать новый графих с новыми значениями
plt.axis([0, 150000, 550000, 650000])
plt.plot(xs, originalData, color = 'red', linestyle = 'solid', label = 'funcvalues')
plt.legend(loc = 'upper right')
fig.savefig(timestamp1+'originalData_output.png')

#logi
ofile  = open(timestamp1+'dataset_log.csv', "wb",0)
writer = csv.writer(ofile, lineterminator='\n')
writer.writerows(log)

#
ofile  = open(timestamp1+'dataset_output.csv', "wb",0)
writer = csv.writer(ofile, lineterminator='\n')
writer.writerows(originalData)

#
ofile  = open(timestamp1+'newdataset_output.csv', "wb",0)
writer = csv.writer(ofile, lineterminator='\n')
writer.writerows(newdataset)



''' у данных в основной задаче не более 4 знаков после запятой, 
буду умножать на 1000 и резать, 
чтоб работать с натуральными числами потом в sklearn,
как оказалось оно плохо с float

синус просто пример для теста, так что и так сойдёт, потеряется точность с ним
'''




