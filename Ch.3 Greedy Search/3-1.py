#Page 87

def coin_counter(received):
        coins=0
        coins += received/500
        coins += (received//500)/100
        coins += ((received//500)//100)
        coins += (((received//500)//100)//50)
        coins += ((((received//500)//100)//50)//10)
        return coins

coin_counter(1260)
