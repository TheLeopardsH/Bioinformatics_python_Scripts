#The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs
def RabbitCount(months,offspring):
    if (months==1):
        return 1
    elif (months==2):
        return offspring
    oneOffspring=RabbitCount(months-1,offspring)
    twoOffspring=RabbitCount(months-2,offspring)

    if(months <=4):
        return (oneOffspring+twoOffspring)
    return (oneOffspring+(twoOffspring*offspring))

print(RabbitCount(35,4))
