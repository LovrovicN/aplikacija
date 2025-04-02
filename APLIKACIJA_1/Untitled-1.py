for year in range(1,2025):
    if(year >= 1584):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print (str(year)+ " prijestupna godina")
        else:
            if (year % 4 == 0):
                print (str(year)+ " prijestupna godina")