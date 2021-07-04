import math

class active():
    def __init__(self) -> None:
        pass

    #def given(self, t1=None, t2=None, temp=None, temp2=None, act_en=None):
        

    def data(self,time1=None, time2=None, temp=None, temp2=None, act_eng=None):
        
        if time1 is None :
	            time1 = "omkar"
        elif 'h' in time1:
            time1 = int(time1.strip("h"))
            self.time1 = time1 * 60 * 60
        elif 'm' in time1:
            time1 = int(time1.strip("m"))
            self.time1 = time1 * 60 
        elif 's' in time1:
            time1 = int(time1.strip("s"))
            self.time1 = time1 
        else:
            print("wrong unit of time one")
            

        if time2 is None :
	            time2 = "omkar"
        elif 'h' in time2:
            time2 = int(time2.strip("h"))
            self.time2 = time2 * 60 * 60
        elif 'm' in time2:
            time23 = int(time2.strip("m"))
            self.time2 = time23 * 60 

        elif 's' in time2:
            time2 = int(time2.strip("s"))
            self.time2 = time2 
        else:
            print("wrong unit of time two")
            

        if temp is None :
	        temp = "omkar"
        elif 'k' in temp:
            temp = int(temp.strip("k"))
            self.temp = temp
        elif 'c' in temp:
            temp = int(temp.strip("c"))
            self.temp = temp + 273
        else:
            print("wrong unit of temp")
        

        if temp2 is None :
	            temp2 = "omkar"
        elif 'k' in temp2:
            temp2 = int(temp2.strip("k"))
            self.temp2 = temp2
        elif 'c' in temp2:
            temp2 = int(temp2.strip("c"))
            self.temp2 = temp2 + 273
        else:
            print("wrong unit of temp two")
        

        if act_eng is None :
	            act_eng = "omkar"
        elif 'j/mol' in act_eng:
            act_eng =  int(act_eng.strip("j/mol"))
            self.act_eng = act_eng
        elif 'k' in act_eng:
            act_eng =  int(act_eng.strip("kj/mol"))
            self.act_eng = act_eng * 1000
        else:
            print("wrong unit of activation energy")
            

    def ans(self):
        
        sel_for = input("1) activation energy 2) time 3) rate:- ")
        if '1' in sel_for:
            time_log = math.log(self.time1) - math.log(self.time2)
            ans = str((((time_log*8.314)*(self.temp2*self.temp))/(self.temp2-self.temp)))
            print(ans +" j/mol")
        
        if '3' or '2' in sel_for:
            ans = str(((self.temp2-self.temp)*(self.act_eng))/((8.3214*self.temp2)*(self.temp)))
            print(ans +" ")

at = active()
at.data(temp="792 k", temp2="800 k", act_eng="175 kjmol")

at.ans()  

      