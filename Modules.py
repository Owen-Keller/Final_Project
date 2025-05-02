"""
Modules used to calculate sqrt of primes

this project is not truely infinite I ran out of ram, and python is not 
so good at allowing the general user to do garbage clean up themselves

but here is the psuedo library of babbel
"""
#imports
from decimal import Decimal, getcontext



primer = 10 ** 8 # used to set context for decimal placement going over 10 causes issues.. ie editor crash

class modules:


    #
    def __init__(self):

        self.n = 1
    

    
    def get_ascii(self, s :str):
        backTostring = ''
        for _ in range(0,len(s), 3):
            converterHundreds = int(s[_: _+3])


            if converterHundreds >=126:
                converter_01 = int(s[_: _+2])
                converter_10 = int(s[_+1:_+3])

                if converter_01 < 32 and converter_10 >= 32:
                    backTostring+=chr(converter_10)

                elif converter_10 < 32 and converter_01 >= 32:
                    backTostring+=chr(converter_01)

                elif converter_01 >= 32 and converter_10 >=32:
                    backTostring+=chr(converter_01)
                    backTostring+=chr(converter_10)
                
                elif converter_01 == 10 or converter_10 == 10:
                    backTostring+=chr(10)

                else:
                    continue

            
            elif converterHundreds >= 32:
                backTostring+=chr(converterHundreds)
            else:
                continue
                
            
        return backTostring
    

    #44 * 8 = 352 chunks
    
    def write_file(self, n:int):
            
        get_prime = n 
        string_val = get_sqrt(get_prime, (get_prime -1), 5)
        True_book = self.get_ascii(string_val)
        babbel = open("book {}.txt".format(n),"w")

        babbel.write(True_book)
            
        babbel.close

        return 1


#using this method you can aproximate alot more values
# and  
def get_sqrt( x:int, aprox:float, iter:int):
    global primer
    getcontext().prec = primer

    x0 = aprox

    x1 = Decimal((x0 + (x/x0)) / 2)

    if iter == 1:
        return str(Decimal(x1)).replace('.','')
        
    return get_sqrt(x, x1, iter-1)
        

#tried applying Taylors serries, but found that the aproxamtion led to an over flow for stored value and 
# was alot slower than heros method refer below

def test_1(x:int):
    d = 1

    n = 0.5


    d = n
    n-=1

    a = d * (x ** n)

    return a



# heros method
"""def test_2(x:int, aprox:float, iter:int):
    getcontext().prec = 10**9

    x0 = aprox

    x1 = Decimal((x0 + (x/x0)) / 2)

    if iter == 1:
        return str(Decimal(x1))


    return test_2(x, x1, iter-1)






sqrt = test_2(2,1 ,10)
print(sqrt)"""