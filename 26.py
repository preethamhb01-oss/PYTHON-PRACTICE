'''
Create a Decorator That Times a Function

Use time module to record how long a function takes to run.
Apply it to a long_task() function that sleeps for 2 seconds.
'''

import time
import wikipedia
try :
    
    start_at = time.perf_counter()

    def get_details(func):
        def wrapper (name):
            
            print(f"\n{func.__name__} is called ...\n")
            func(name)
            
        return wrapper

    @get_details
    def biodata(name):
        print(wikipedia.summary(name))
        

        
   
    
except Exception :
    print("ERROR :  ")
    
else:
    name = input("\nEnter name to get Biodata :   ")
    
    biodata(name)
    
finally :
    


    end_at=time.perf_counter()

    execution_time = end_at -start_at

    print(f"\nTIME TAKEN TO RUN CODE IS : {execution_time} S\n")