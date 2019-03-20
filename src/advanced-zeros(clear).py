number = 71398757
base = 12
#должно получиться 35699370

def getZerosCount(number, base):
    #находим простые делители системы счисления
    i = 2
    b = base
    dividers = []
    degrees = []
    ps_i = 0
    step = 0 #степень - т.е. количество раз повторения делителя
    
    while i <= base:   
        if b % i == 0:
            if i > ps_i:
                degrees.append(step)
                dividers.append(i)
                ps_i = i
                step = 0
                
            print('b = ', b, 'i = ', i)
            b /= i
            step += 1                
        else:
            i +=1
    degrees.append(step)
    del degrees[0]
    print(dividers, degrees)
    
    def countdel(delit, stepen):
        temp = number
        count = 0
        i = delit
        
        while temp // i > 1:
            count += temp // i
            print('c', count, 'i = ', i)
            i *= delit
        count = count // stepen
        return count


    variants = []
    for i in range(0, len(dividers)):
        variants.append(countdel(dividers[i],degrees[i]))
        
    #print(variants)
    res = min(variants)
    print('result = ', res)



    # #находим количество разложений числа number на делители base
    # temp = number
    # count1 = 0
    # #step = 0
    # i = dividers[1]
    # while temp // i > 1:
    #     count1 += temp // i
    #     print('c1', count1, 'i = ', i)
    #     i *= dividers[1]
    #     #step += 1
    # #if step > 1:
    # #   step +=1
    # count1 = count1 // dividers[2]
    # print('count1', count1)
    
    
    # if len(dividers) > 3:
    #     temp = number
    #     count2 = 0
    #     step = 0
    #     i = dividers[3]
    #     while temp // i > 1:
    #         count2 += temp // i
    #         print('c2 = ', count2, 'i = ', i)
    #         i *= dividers[3]
    #         step += 1
    #         count2 = count2 // dividers[4]
    #     #if step > 1:
    #     #    step += 1
    #     #    count2
    #     print('count2', count2)  
    
    
    #     if count1 < count2:
    #         print('Количество нулей: ', count1)
    #     else:
    #         print('Количество нулей: ', count2)
    # else:        
    #     print('Количество нулей: ', count1)    
            

getZerosCount(number, base)