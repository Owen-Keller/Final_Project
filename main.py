"""
The Babbel Library

"""

#imports
from Modules import *

#main function
def main():

    make_primeFile()

#function that has the list of primes. and calls module for generating files
def make_primeFile():
    md = modules()
    list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
                      101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                      151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 
                      199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 
                      263, 269, 271, 277, 281, 283, 293]
    print("Generating : {} books of unknown length".format(len(list_of_primes)))
    count = 0
    for _ in list_of_primes:
        md.write_file(_)
        count +=1
        print("{} book completed".format(count))
    
  
#calls main
if __name__ == "__main__":
    main()


#if x >= 32 ok
# if char 
#if x > 126 bad
