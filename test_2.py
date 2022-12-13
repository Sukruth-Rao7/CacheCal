import math
from tabulate import tabulate

class cacheCalc:
    #@staticmethod
    def cacheCalc_1(x, System_Architecture_bits, Numberofwords, block_size, Associativity):    
    
        x = str(input("Enter the hex address: "))
        #take user inputs
        
        scale = 16 ## equals to hexadecimal

        num_of_bits = 32

        a = bin(int(x, scale))[2:].zfill(num_of_bits)
        print(a)

        ##byte offset 2 bits
        b=(a[:-2]) ##30bits data
        print(b)
        byteoffset=2
        
        System_Architecture_bits = int(input("Enter the system architecture bits: "))
        Numberofwords = int(input("Enter Number of words: "))
        block_size = int(input("Enter Size of each block: "))
        Associativity = int(input("Enter the degree of associativity: "))
        
        # print("System_architecture_bits=",System_Architecture_bits, "\n")
        # print("block_size=",block_size,"\n")
        print("Numberofwords=",Numberofwords, "\n")

        if(Associativity == 0):#Direct mapped cache       
            
        #Direct mapped cache with any block size
            block_offset = int(math.log(block_size,2))
            Numberofsets = int(Numberofwords / block_size)
            print("Numberofsets: ",Numberofsets, "\n")
            Number_of_set_bits = int(math.log(Numberofsets,2))
            print("Number of set bits: ",Number_of_set_bits, "\n")
            set_bits = b[System_Architecture_bits - byteoffset - Number_of_set_bits:]
            print("Set bits: ", set_bits,"\n")
            Tag_field = System_Architecture_bits - Number_of_set_bits - block_offset - byteoffset
            print("Tag field: ", Tag_field, "\n")
            size_cache = Numberofsets*((System_Architecture_bits*block_size)+Tag_field+1)
            print("size_cache = Numberofsets*((System_Architecture_bits*block_size)+Tag_field+1): ",size_cache)


        if(Associativity == 1): #Fully set associative cache for any block size 
            Numberofsets = int(Numberofwords / block_size)
            Numberofblocks = Numberofsets
            block_offset = int(math.log(Numberofblocks,2)) 
            block_offset_bits = b[System_Architecture_bits-byteoffset-block_offset:]
            print("Number of sets = NA")
            print("Set bits = NA")
            print("block offset = ",block_offset,"\n")
            print("block offsets bits = ",block_offset_bits,"\n")
            Tag_field = System_Architecture_bits - block_offset - byteoffset
            print("Tag field for Fully set associative cache", Tag_field,"\n")
            Number_of_set_bits = null
            
            set_bits = null
            print("Number_of_set_bits=",Number_of_set_bits, "\n")
            print("set_bits=",set_bits, "\n")
            Tag_field = System_Architecture_bits - block_offset - byteoffset
            print("Tag field for", Associativity , "-way set associative cache", Tag_field, "\n")


            size_cache = Numberofblocks*((System_Architecture_bits*block_size)+ Tag_field + 1)
            print("size_cache = Numberofblocks*((System_Architecture_bits*block_size)+ Tag_field + 1)= ",size_cache, "\n")

        #if(Associativity == 1 and block_size > 1):#fully set associative cache with block size > 1
        if(Associativity > 1):
            Numberofsets = int(Numberofwords / (Associativity * block_size))
            print("Number of sets= ", Numberofsets,"\n")
            block_offset = block_offset = block_offset = int(math.log(block_size,2))
            print("block offset = ", block_offset,"\n")
            #block_offset_bits = b[System_Architecture_bits-byteoffset-block_offset:]
            Number_of_set_bits = int(math.log(Numberofsets,2))
            set_bits = b[System_Architecture_bits-byteoffset-Number_of_set_bits:]
            print("Number_of_set_bits=",Number_of_set_bits, "\n")
            print("set_bits=",set_bits, "\n")
            Tag_field = System_Architecture_bits - Number_of_set_bits - block_offset - byteoffset
            print("Tag field for", Associativity , "-way set associative cache", Tag_field, "\n")
            size_cache = Numberofsets*Associativity*((System_Architecture_bits*block_size)+Tag_field+1)
            print("Cache size = Numberofsets*Associativity((System_Architecture_bits*block_size)+Tag_field+1)= ", size_cache,"\n")


        return x, System_Architecture_bits, Numberofwords, block_size, Associativity, Numberofsets, block_offset, Number_of_set_bits,set_bits, Tag_field, size_cache

    cacheCalc_1(x, System_Architecture_bits, Numberofwords, block_size, Associativity)

def main():
    mydata = [[Numberofsets, Number_of_set_bits, set_bits, Tag_field, block_offset, byteoffset, size_cache]]
 
# display table
    head = ["No. of sets", "Number of Set bits", "Set Bits", "Tag field", "Block offset", "byte offset", "size_cache"]
 
# display table
    print(tabulate(mydata, headers=head, tablefmt="grid"))

if __name__=="__main__":
    main()
    cacheCalc.cacheCalc_1()




