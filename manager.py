import time
state_1 = True
state_2 = False
state_3 = False
state_4 = False

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def tf_manage(count_a, count_b, count_c, count_d):
    ##Fuzzy SISO
    start = a
    if (state_1):
        countdown(int(3))
    
