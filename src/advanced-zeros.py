#написать функцию которая берет в себя два числа и возвращает количество нулей получаемое в конфце числа
# которое получается если вычислить факториал числа nimber в base системе 
# number 1 <= number <= 10^7
# 2 <= base <= 256
# факториал числа вычисляться не должен
number = 761288
number = number - (number % 5)
print('number = ', number )
base = 152
count = 0


def getZerosCount(number, base):
    if True:# <= number <= 10^7 and 2 <= base <= 256:
        deliteli = []
        stat = []
        
        i = 5
        while i < number:
            deliteli.append(i)
            i *=5
            
        
        
        print('alright, going on')
        
        print("deliteli = ", deliteli)
        fiveCount = 0
        n = 0
        
        for i in deliteli:
            if i < number:
                fiveCount += number // i # подсчет всего делителей 5к числа number
        
        
        
        for i in range(2, base):
            if base % i == 0:
                while base % i == 0:
                    n += 1
                    base /= i
                print('n = ', n)
                
                n1 = 0
                temp = number
                while temp / i > 0:
                    n1 += temp / i
                    temp /=i
                print('n1 = ', n1)
                
        mun = n1 / n
        print('mun', mun)
        if n < n1: # присваивание значения результата
            res = n
        else:
            res = n1
            
        print('Res = ', res)
            
            
        
        print('fiveСount = ', fiveCount)
        
getZerosCount(number, base)