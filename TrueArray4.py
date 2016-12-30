import math

def same(Strok):
    if (Strok.count(1)>0 and Strok.count(-1)==0) or\
    (Strok.count(-1)>0 and Strok.count(1)==0) or\
    (Strok.count(0)==3):
        return True
    else:
        return False

def differ(Strok1,Strok2,Strok3):
        vector=[sum(Strok1),sum(Strok2),sum(Strok3)]
        vector.sort()
        if (((int(vector[0]))<=0)and((int(vector[1]))<=0)and((int(vector[2]))>0)):    
            return True
        else:
            return False 

def answer(Strok1,Strok2,Strok3):
    vector=[sum(Strok1),sum(Strok2),sum(Strok3)]
    if (int(vector[0])>0):
        return(0)
    elif (int(vector[1])>0):
        return(1)
    else:
        return(2)
    
#Обьявим списки "заявлений", тоесть списки заполненные заявленимями о виновности подозреваемого другими подозреваемыми
#к примеру, statementB=[-1, -1, 1], потому что Браун заявил что он сам невиновен (первый элемент списка=-1),
#Джонс заявил, что Браун невиновен (второй элемент списка=-1), Смит заявил, что Браун невиновен (третий элемент списка=1)
statementB=[-1, -1, 1]
statementJ=[-1, 0, 0]
statementS=[0, 1, -1]
#Таким образом полученные три списка составляют как-бы "матрицу заявлений", заполненную заявлениями подозреваемых друг о друге
#Диагональ заполнена заявлениями подозреваемых относительно самих себя

#Обьявим список layer, составляющий полную выборку возможных вариантов относительно "правдивости" их заявлений
#Соответственно, первый элемент означает правдивость Брауна, второй Джонса, третий Смита
#0 означает, что человек один разсказал правду, а один раз соврал; 1 означает, что человек дважды сказал правду; -1 означает что человек дважды соврал
layer = [[-1, 1, 0],[-1, 0, 1],[0, 1, -1],[0, -1, 1],[1, 0, -1],[1, -1, 0]]
Bstrok1=[0,0,0]
Jstrok1=[0,0,0]
Sstrok1=[0,0,0]
Bstrok2=[0,0,0]
Jstrok2=[0,0,0]
Sstrok2=[0,0,0]
#Обьявим словарь, в котором и укажем для вывода позже, что первый столбец в матрицах и первый элемент в векторах соответстует Брауну и т.д.
dict2 = {0:'Браун',1:'Джонс',2:'Смит'}
#переберем варианты кто правдивости заявлений
for i in layer:
    #теперь умножим матрицу заявлений (наши списки statementB и т.д.) построчно на вектор правдивости i
    #результат записываем в две матрицы (в нашем случае просто группы строк Bstrok1,Jstrok1 и т.д.)
    #именно в две матрицы, так как один из подозреваемых один раз сказал правду, а один раз ложь, из-за чего возможны два варианта виновности
    #поэлементно переберем вектор правдивости
    for s in range(3):
        #проверим не равен ли элемент вектора правдивости 0, что значит, что для данного столбца матрицы правды будут иметь разные значения
        if i[s] == 0:
            #Если первый элемент столбца матрицы заявлений не равен нулю, один из следующих элементов столбца равен нулю, аа второй не равен нулю,
            #можем применить одни и те же действия умножения к обоим этим элементам, равный нулю так и останется нулем
            if statementB[0]!=0:
                Bstrok1[s] = statementB[s]
                Bstrok2[s] = -1*statementB[s]
                Jstrok1[s] = -1*statementJ[s]
                Jstrok2[s] =statementJ[s]
                Sstrok1[s] =statementS[s]
                Sstrok2[s] = -1*statementS[s]
            #Если первый элемент столбца матрицы заявлений равен нулю, то два другие не равны нулю
            else:
                Jstrok1[s] = -1*statementJ[s]
                Jstrok2[s] = statementJ[s]
                Sstrok1[s] = statementS[s]
                Sstrok2[s] = -1*statementS[s]
        #для случая 0 и 1 (полная неправда или правда) в векторе правдивости просто умножаем вектор правдивости на строки матрицы заявлений
        else:
            Bstrok1[s] = statementB[s]*i[s]
            Jstrok1[s] = statementJ[s]*i[s]
            Sstrok1[s] = statementS[s]*i[s] 
            Bstrok2[s] = statementB[s]*i[s]
            Jstrok2[s] = statementJ[s]*i[s]
            Sstrok2[s] = statementS[s]*i[s]
    #в функции same проверяем все ли значения в каждой строке матрице правды одинаковы (за исключением пустых, которые =0)
    #если условие не выполняется, то матрица противоречит себе самой

    #в функции differ делаем проверку чтобы три строки матрицы правды имели разное значение (один сказал правду, один солгал, один слегкаааа солгал) 
    if ((same(Bstrok1))and(same(Jstrok1))and(same(Sstrok1)))and((differ(Bstrok1,Jstrok1,Sstrok1))):
        print('Если ')
        print(dict2.get(i.index(1)),' сказал правду, ')
        print(dict2.get(i.index(0)),' соврал, ')
        print(dict2.get(i.index(-1)),' один раз сказал правду и один раз соврал, то ')
        print('Совершил преступление !!!',dict2.get(answer(Bstrok1,Jstrok1,Sstrok1)),'!!!')
        print()
    else:
        pass
    #в функции same проверяем все ли значения во второй матрице правды одинаковы (за исключением пустых, которые =0)
    #если условие не выполняется, то матрица противоречит себе самой

    #в функции differ делаем проверку чтобы три строки матрицы правды имели разное значение (один сказал правду, один солгал, один слегкаааа солгал) 
    if ((same(Bstrok2))and(same(Jstrok2))and(same(Sstrok2)))and((differ(Bstrok2,Jstrok2,Sstrok2))):
        print('Если ')
        print(dict2.get(i.index(1)),' сказал правду, ')
        print(dict2.get(i.index(-1)),' соврал, ')
        print(dict2.get(i.index(0)),' один раз сказал правду и один раз соврал, то ')
        print('Совершил преступление !!!',dict2.get(answer(Bstrok2,Jstrok2,Sstrok2)),'!!!')
        print()
    else:
        pass
##    print('i = ',i,'-----------------------------')
##    print('1')
##    print(Bstrok1)
##    print(Jstrok1)
##    print(Sstrok1)
##    print('2')
##    print(Bstrok2)
##    print(Jstrok2)
##    print(Sstrok2)
##    print('--------------')
