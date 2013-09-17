
import re
import time
import dictionary
import sys
import parser_init
import numbers
import prod_mod
import flags
import semantics2
flag1 = 0
global queue
queue = []
global stack
stack = []
global handle
handle = []
global handle_num
handle_num = []
global stack_num
stack_num = []
global queue_num
queue_num = []
global ss
global redns
redns = []
global strg
strg = ''
#Beginning of Lexical Analyser Function
def lexan(line):
    global strg
    global stack
    #s1=open('output.txt','a')        
    def string():
        #print("Token: {}".format(f.group(1)).rjust(100),"code:{}".format('78'))
        queue.append(f.group(1))
        queue_num.append(78)
        #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..',f.group(1))
    def negreal(a): #Function to check Negative Real Numbers
        a=(a.split('0'))
        length1 = len(a[0])-1
        if (length1>7):                
            print("\t\t\t\t\tInvalid negative real: {}".format(f.group(5)),"(The number has more than 7 significant digits)")
        else:
                                  
            #print("Token: {}".format(f.group(5)).rjust(100),"code:{}".format('102'))
            queue.append(f.group(5))
            queue_num.append(102)
        
    def posreal(b): #Function to check Positive Real Numbers
        b = (b.split('0'))                    
        length2 = len(b[0])            
        if (length2>7):                
           print("\t\t\t\t\tInvalid real: {}".format(f.group(6)),"(The number has more than 7 significant digits)")
        else:
            #print("Token: {}".format(f.group(6)).rjust(100),"code:{}".format('102'))
            queue.append(f.group(6))
            queue_num.append(102)
        
    def neginteger(length): #Function to check Negative Integers
        if ((length-1)>32):
          print("\t\t\t\t\tInvalid integer: {}".format(f.group(7)),"(The number has more than 9 significant digits)")
        else:
            #print("Token: {}".format(f.group(7)).rjust(100),"code:{}".format('61'))
            queue.append(f.group(7))
            queue_num.append(61)
    def integer(length):  #Function to check Integers
        if (length>32):
           print("\t\t\t\t\tInvalid integer: {}".format(f.group(8)),"(The number has more than 9 significant digits)")
        else:
    
            #print("Token: {}".format(f.group(8)).rjust(100),"code:{}".format('61'))
            queue.append(f.group(8))
            queue_num.append(61)
    
    def specialcharacters(): #Function to check Special Characters
        if(f.group(9) in dictionary.dict):            
            #print("Token: {}".format(f.group(9)).rjust(100),"code:{}".format(dictionary.dict.get(f.group(9))))
            queue.append(f.group(9))
            queue_num.append(numbers.numbers.get(f.group(9)))
    
        if (f.group(9) not in dictionary.dict):
            num = ord(f.group(9))
            #print("\t\t\t\t\tInvalid ASCII character: {}".format(f.group(9)),"(Its ASCII value :",num,")")    
    def reservewords(): #Function to read Reserve words
        if(f.group(10) in dictionary.dict): 
           #print("Token: {}".format(f.group(10)).rjust(100),"code:{}".format(dictionary.dict.get(f.group(10))))
           queue.append(f.group(10))
           queue_num.append(numbers.numbers.get(f.group(10)))
    
        if(f.group(10) not in dictionary.dict):
           print("\t\t\t\t\tInvalid Reserve Word: {}".format(f.group(10)))
    def invidentifiers(): #Function to check Invalid Identifiers
        print("\t\t\t\t\tInvalid identifier: {}",f.group(11))
    def identlength(): #Function to check Identifier Length
        idlength = len(f.group(12))
        if idlength>24:
          print("\t\t\t\t\t Invalid length identifiers: {}".format(f.group(12)),"(Identifiers should be at most 24 characters.)")
        else:
    
            #print("Token: {}".format(f.group(12)).rjust(100),"code:{}".format('56'))
            queue.append(f.group(12))
            queue_num.append(56)
                                               
   #Regular Expression 
    reg = re.compile(r"""(".+?")|(//.+)|
([#][#][\d\w\s+-/.*()\[\]+<>\\:"'&]*[#][#])|
([/][*].+[*][/])|
([\-][0-9]+[.][0-9]+)|
([0-9]+[.][0-9]+)|
([\-][0-9]+)|
([0-9]+)|
([=][=]|[!][=]|[<][=]|[>][=]|[<][-]|[&][&]|[|][|]|[\;]|[\:]|[\,]|[\[]|[\]]|[\(]|[\)]|[\<]|[\>]|[\!]|[\+]|[\-]|[\*]|[\/]|[\{]|[\}]|[\=]|[.]|[~])|
([A-Z]+)|
([A-Z]+[a-z0-9]+)|
([a-z][a-zA-Z0-9_]*)""",re.VERBOSE)    
               
    
    for f in re.finditer(reg, line):
        if f.group(1):
            string();
            
        if f.group(2):
            continue
        
        if f.group(3):           
            continue
        if f.group(4):           
            continue
           
        if f.group(5):
            a = (f.group(5))  
            negreal(a);          
            
        if f.group(6):
            b = (f.group(6))           
            posreal(b);
                              
        if f.group(7):
            length = len(f.group(7))
            neginteger(length);          
        
        if f.group(8):
            length = len(f.group(8))
            integer(length);       
            '''if (length>32):
                print("\t\t\t\t\tInvalid integer: {}".format(f.group(8)),"(The number has more than 9 significant digits)")
            else:
                print("Token: {}".format(f.group(8)).rjust(100),"code:{}".format(dictionary.dict1.get(f.group(8))))
                queue.append(f.group(8))'''   
        
        if f.group(9):
            specialcharacters();
        
        if f.group(10):
            reservewords();
        
        if f.group(11):
            invidentifiers();
        
        if f.group(12):           
            identlength();
           

                                      
global ss
ss=' '            
print("\nName : Sugetha Kalyanaraman Chandhrasekar , Sakti Aishwarya Arunachalam")
print("Email : sugethk@clemson.edu , sarunac@clemson.edu")
t1 = time.localtime() #prints the current time
print("Time stamp : ",time.asctime(t1))
print("\nSTARTING FILE SCAN\n")
inputfile=open('Sorting.txt','r')
print("\n")    
 #setting flags       
for line in inputfile.readlines():
     flag=line.find('##')
     x=re.compile(r"""([+][0-9]+)""",re.VERBOSE)
     x1=re.compile(r"""([\-][0-9]+)""",re.VERBOSE)
     for f in x.findall(line):
         for i in range(1,32):
             if(f=='+{}'.format(i)):
                 flags.set_flags(i,1)
             continue       
     for f in x1.findall(line):
         for i in range(1,32):
             if(f=='-{}'.format(i)):
                 flags.set_flags(i,0)
             continue   
         
         
     if(flags.flags[1]==1):
      print(line)
      #Checking Multi Line Comments     
     if(flag1==0):
        l1=line.find('/*')
        if(l1==0):
                flag1=1
                line1=line[0:l1]
                l12=line.find('*/')
                if(l12!=-1):
                    flag1=0
                    line2=line[(l12+2):80]
                    line=line1+line2
                else:
                    continue       
             
     if(flag1==1):
        l2=line.find('*/')
        if(l2==-1):
            continue
        elif(l2>=80):
            flag1=0
            break
        elif(l2<80):
            line=line[(l2+2):80]
            flag1=0
        continue 
              
     lexan(line)
     if queue_num:
          parser_init.parse(queue,queue_num,stack,stack_num,handle,handle_num,line)
#print(stack_num)
if line[-1]:
    handle_num=stack_num
    for x in handle_num:
        strg+=str(x)
        strg+='   '
    strg=strg.strip()
    if (strg in prod_mod.productions):
        prod_num=prod_mod.productions.get(strg)
    if (strg in prod_mod.reductions):
        line_num=prod_mod.reductions.get(strg)
    
    #print(prod_num)
    if flags.flags[7] == 1:
        for key,val in numbers.numbers.items():
            if val==prod_num:
                print('Reduction # {}'.format(line_num).rjust(100),'',key+'---->')
        for each in handle_num:
            for key,val in numbers.numbers.items():
                if val==each:
                    print(key+' ')
        print()
    
    if line_num == 1:
        getattr(semantics2, 'line%d' %line_num)(stack,3)
    
#print('FLAGGGSSSS',flags.flags)    
print("END OF FILE SCAN.")