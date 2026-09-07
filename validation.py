def is_positive_float(n):
    try :
        float_n = float(n)
        if float_n > 0 :
            vaild = True
        else:
            vaild = False
    except ValueError:
        vaild = False 
    return vaild

