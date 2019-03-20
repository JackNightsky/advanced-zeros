number = 46899647
base = 232
#должно получиться 1674985

def getZerosCount(number, base):
    #находим простые делители системы счисления
    i = 2
    b = base
    deliteli = []
    ps_i = 0
    while i <= base:   
        
        if b % i == 0:
            print(b, 'i = ', i)
            b /= i
            if i > ps_i:
                deliteli.append(i)
            ps_i = i
        else:
            i +=1
    print(deliteli)
    
    #находим количество разложений числа number на делители base
    temp = number
    count1 = 0
    step = 0
    i = deliteli[0]
    while temp // i > 1:
        count1 += temp // i
        print('c1', count1, 'i = ', i)
        i *= deliteli[0]
        step += 1
    if step > 1:
        step +=1
    count1 = count1 // step
    print('count1', count1, step)
    
    
    if len(deliteli) > 1:
        temp = number
        count2 = 0
        step = 0
        i = deliteli[1]
        while temp // i > 1:
            count2 += temp // i
            print('c2 = ', count2, 'i = ', i)
            i *= deliteli[1]
            step += 1
        if step > 1:
            step += 1
            count2 = count2 // step
        print('count2', count2, step)  
    
    
        if count1 < count2:
            print('Количество нулей: ', count1)
        else:
            print('Количество нулей: ', count2)
    else:        
        print('Количество нулей: ', count1)    
            

getZerosCount(number, base)
            
#это решение проходит два