
'''
healthchecking 
The status of the Arduino boards, which are mqtt publishers,
are checked every 30 seconds by default and the information is sent to kafka.
healthcheck.py can change the default time of 30 seconds as requested by the web server
'''
class Healthcheck :
    
    
 # default time    
    def __init__(self) :

        self.time = 30
        self.ping_message= "ping time:" + str(self.time) 
    
     
    def set_time(self,time) :
        self.time = time 

    def get_time(self) :
        return self.time  
                  
    
        


        
  

