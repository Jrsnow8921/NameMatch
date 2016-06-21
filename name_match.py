class Check(object): 


  def __init__(self, word): 
     self.word = word 

  def abbr(self): 
     e = self.word 
     w = self.word[:1] 
     lens = len(self.word) 
     last = self.word[-1:] 
     all = '%s%s%s' %(w, lens, last) 
  
     self.check_fn(e, all) 
     

  def check_fn(self, my_name, intials): 
     a = my_name 
     b = intials 

     list_a = [] 
     list_b = [] 

     aa = list_a.append(a) 
     bb = list_b.append(b) 

     dictonary = dict(zip(list_a, list_b))
  
     for k, v in dictonary.items():
     
       #if (v[:1] == k[:1] and v[1] == len(k) and v[-1:] == k[-1:]):
       if (v[:1] == k[:1] and v[1] == str(len(k)) and v[-1:] == k[-1:]):
         print True          
       else:
         print False
         print v[:1], k[:1], v[1], str(len(k)), v[-1:], k[-1:]
        


Check.abbr(Check("test"))


