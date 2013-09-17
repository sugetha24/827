'''
Created on Oct 14, 2012

@author: sugethk
'''
import semantics_dict
import flags
import re
import pragmatics
global_sym = []  #global sumbol table
local_sym = []   #local symbol table
sym_dict = {}    #global symbol dictionary
sym_dict_local = {}   #local symbol dictionary
local_var = 0    #local variable to find whether local or global scope is set
integercounter = 0
realcounter = 0
labelcounter = 0
bcounter = 0
ircounter = 0
errorcheck = 0
five = ''
la = 0

def convert(var):
    reg1 = re.compile(r"""(^[0-9][.][0-9]+)|(^[0-9]+)|(['#'])""",re.VERBOSE)
    
    for f in re.finditer(reg1, var):
        if f.group(1):
            return 'REAL'
        if f.group(2):
            #print('var',var)
            return 'INTEGER'
        if f.group(3):
            return '#'
    

def chck(v):
    
    reg = re.compile(r"""(['R'])|(['I'])|(^[0-9][.][0-9]+)|(^[0-9]+)|(['#'])""",re.VERBOSE)
    for f in re.finditer(reg, v):
        if f.group(1):
            return 'REAL'
        if f.group(2):
            return 'INTEGER'
        if f.group(3):
            return 'REAL'
        if f.group(4):
            return 'INTEGER'
        if f.group(5):
            return '#'
        chck_type(v)
        
def chck_type(var):
    global local_var
    global local_sym
    global global_sym
    
    type = 'not set'
    #print('local var is ',local_var)
    if(local_var):
            for i in range(len(local_sym)):
                    v=local_sym[i][0]
                    if v == var:
                        type = local_sym[i][1]
                        
            if type == 'not set':
                
                for i in range(len(global_sym)):
                        v=global_sym[i][0]
                        if v == var:
                            type = global_sym[i][1]
    else:
            for i in range(len(global_sym)):
                    v=global_sym[i][0]
                    if v == var:
                        type = global_sym[i][1]
    #print('type of '+var+' is',type)
    if type == 'not set':
        type = chck(var)
        #print('returning type of '+var+' as',type)
        return type
    else:
        return type

def error3(pos,stack):
    type = chck(stack[pos])
    if type == 'REAL' or type == 'INTEGER':
        return
    elif stack[pos] not in sym_dict and stack[pos] not in sym_dict_local:
        print('ERROR3 :'+stack[pos]+' IS USED BUT NOT DECLARED')

def prnt(one,two,three,four):
    global five
    tuples = '('+one+','+two+','+three+','+four+')'
    x = convert(four)
    if x == 'INTEGER':
        four = int(four)
    if x == 'REAL':
        four = float(four)
    x = convert(three)
    if x == 'INTEGER':
        three = int(three)
    if x == 'REAL':
        three = float(three)
    prag_tup = [one, two, three, four,five]
    #print('type of '+one+' is:',five)
    print('The Tuple is: {}'.format(tuples).rjust(100))
    pragmatics.tuples(prag_tup,local_var)

    #print('prag tuples is',prag_tup) 
    
     
def line2(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt(str(stack[-1]),'PROGRAMBEGIN','#','#')
    
    if local_var:
        if stack[-1] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-1], '#', '#', '#','#']
            sym_dict_local[stack[-1]] = 2
            local_sym.append(sym_list)
    else:
        if stack[-1] not in sym_dict:
            sym_list=[stack[-1], '#', '#', '#','#']
            sym_dict[stack[-1]] = 2
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    sym_list = []
    temp = stack[-1]
    stack[-2] = temp
    stack.pop()
    #print('semantics stack is',stack)
def line18(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    stack[-1] = 'INTEGER'
    for i in range(length-1):
        stack.pop()
    
def line14(stack,length):
            
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five
    

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-1]),'{},'.format(stack[-2]), '1, #)')
        five = stack[-2]
        prnt(str(stack[-1]),'MEMORY','1','0')
        
        
    if local_var:
        if stack[-1] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-1], stack[-2], 'SCALAR', '1' ,'0']
            sym_dict_local[stack[-1]] = 14
            local_sym.append(sym_list)
    else:
        if stack[-1] not in sym_dict:
            sym_list=[stack[-1], stack[-2], 'SCALAR', '1' ,'0']
            sym_dict[stack[-1]] = 14
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    temp = stack[-1]
    stack[-2] = temp
    stack.pop()
    #print('semantics stack is',stack)
    #sem[-1] = sym_list[1][2]
    
def line19(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    stack[-1] = 'REAL'
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line16(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-4]),'{},'.format(stack[-5]), '{},'.format(stack[-2]),' #)')
        five = stack[-5]
        prnt(str(stack[-4]),'MEMORY',str(stack[-2]),'0')
        

        
    if local_var:
        if stack[-4] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-4], stack[-5], 'VECTOR', stack[-2] ,'0']
            sym_dict_local[stack[-4]] = 16
            local_sym.append(sym_list)
    else:
        if stack[-4] not in sym_dict:
            sym_list=[stack[-4], stack[-5], 'VECTOR', stack[-2] ,'0']
            sym_dict[stack[-4]] = 16
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    temp = stack[-4]
    stack[-5] = temp
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line17(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-6]),'{},'.format(stack[-7]), '{},'.format(stack[-4]),'{})'.format(stack[-2]),')')
        five = stack[-7]
        prnt(str(stack[-6]),'MEMORY',str(stack[-4]),str(stack[-2]))
        
        
    if local_var:
        if stack[-6] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-6], stack[-7], 'MATRIX',stack[-4],stack[-2]]
            sym_dict_local[stack[-6]] = 17
            local_sym.append(sym_list)
            
    else:
        if stack[-6] not in sym_dict:
            sym_list=[stack[-6], stack[-7], 'MATRIX',stack[-4],stack[-2]]
            sym_dict[stack[-6]] = 17
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    if flags.flags[15] == 1:
        print(sym_list)
    temp = stack[-6]
    stack[-7] = temp
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line5(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    

    if flags.flags[13] == 1:
        #print('Tuple is :( #, ENDDECLARATIONS, #, #)')
        prnt('#','ENDDECLARATIONS','#','#')

    #local_var = 0
    for i in range(length-1):
        stack.pop()

def line1(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    

    if flags.flags[13] == 1:
        #print('Tuple is :({}'.format(stack[-3]),', ENDPROGRAM, #, #)')
        prnt(str(stack[-3]),'ENDPROGRAM','#','#')

    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    if flags.flags[16] == 1:
        print('GLOBAL SYMBOL TABLE')
        for each in range(len(global_sym)):
            print(global_sym[each])
    #print(stack)
    
def line11(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-3]),'INTEGERASSIGN,', '{},'.format(stack[-1]),'#)')
        prnt(str(stack[-3]),'INTEGERASSIGN',str(stack[-1]),'#')

        
    if local_var:
        if stack[-3] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-3], stack[-5], 'SCALAR','1','0']
            sym_dict_local[stack[-3]] = 11
            local_sym.append(sym_list)
            
    else:
        if stack[-1] not in sym_dict:
            sym_list=[stack[-3], stack[-5], 'SCALAR','1','0']
            sym_dict[stack[-3]] = 11
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    for i in range(length-1):
        stack.pop()

def line12(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-4]),'{},'.format(stack[-6]), '{},'.format(stack[-2]),'#)')
        prnt(str(stack[-4]),str(stack[-6]),str(stack[-2]),'#')

        
    if local_var:
        if stack[-4] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-4], stack[-6], 'VECTOR',stack[-2],'0']
            sym_dict_local[stack[-4]] = 12
            local_sym.append(sym_list)
    else:
        if stack[-4] not in sym_dict:
            sym_list=[stack[-4], stack[-6], 'VECTOR',stack[-2],'0']
            sym_dict[stack[-4]] = 12
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    for i in range(length-1):
        stack.pop()
        
def line10(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-1]),'{},'.format(stack[-3]), '1,#)')
        prnt(str(stack[-1]),str(stack[-3]),'1','#')

        
    if local_var:
        if stack[-1] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-1], stack[-3], 'SCALAR','1','0']
            sym_dict_local[stack[-1]] = 10
            local_sym.append(sym_list)
    else:
        if stack[-1] not in sym_dict:
            sym_list=[stack[-1], stack[-3], 'SCALAR','1','0']
            sym_dict[stack[-1]] = 10
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    for i in range(length-1):
        stack.pop()
        
def line13(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({}'.format(stack[-6]),',{}'.format(stack[-8]), ',{}'.format(stack[-4]),',{})'.format(stack[-2]),')')
        prnt(str(stack[-6]),str(stack[-8]),str(stack[-4]),str(stack[-2]))

        
    if local_var:
        if stack[-6] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-6], stack[-8], 'MATRIX',stack[-4],stack[-2]]
            sym_dict_local[stack[-6]] = 13
            local_sym.append(sym_list)
            
    else:
        if stack[-6] not in sym_dict:
            sym_list=[stack[-6], stack[-8], 'MATRIX',stack[-4],stack[-2]]
            sym_dict[stack[-6]] = 13
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    temp = stack[-6]
    stack[-8] = temp
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line15(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({}'.format(stack[-3]),',INTEGERASSIGN,', '1, #)')
        prnt(str(stack[-1]),str(stack[-2]),'1','#')

        
    if local_var:
        if stack[-3] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
        else:
            sym_list=[stack[-3], stack[-4], 'SCALAR', '1' ,'0']
            sym_dict_local[stack[-3]] = 15
            local_sym.append(sym_list)
    else:
        if stack[-3] not in sym_dict:
            sym_list=[stack[-3], stack[-4], 'SCALAR', '1' ,'0']
            sym_dict[stack[-3]] = 15
            global_sym.append(sym_list)
        else:
            print('DOUBLY DECLARED ERROR')
    
    temp = stack[-3]
    stack[-4] = temp
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line23(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-4]),' ENDPROCEDURE, #, #)')
        prnt(str(stack[-4]),'ENDPROCEDURE','#','#')

    if flags.flags[14] == 1:
        print('LOCAL SYMBOL TABLE')
        for each in range(len(local_sym)):
            print(local_sym[each])
    local_var = 0
    local_sym = []
    sym_dict_local = {}
    """if stack[-4] not in sym_dict:
        sym_list=[stack[-4], '#', '#','#','#']
        sym_dict[stack[-4]] = 23
        global_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR'.rjust(100))"""
        
    #print(local_sym)
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)    

def line24(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-3]),' ENDPROCEDURE, #, #)')
        prnt(str(stack[-3]),'ENDPROCEDURE','#','#')

    local_var = 0
    local_sym = []
    sym_dict_local = {}
    if flags.flags[14] == 1:
        print('LOCAL SYMBOL TABLE IS')
        for each in range(len(local_sym)):
            print(local_sym[each])
    local_sym = []        
    if local_var:
        if stack[-3] in sym_dict_local:
            print('DOUBLY DECLARED ERROR')
    """elif stack[-3] not in sym_dict:
        sym_list=[stack[-3], '#', '#','#','#']
        sym_dict[stack[-3]] = 24
        global_sym.append(sym_list)"""
    
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line27(stack,length):
    
        
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var

    if flags.flags[13] == 1:
        #print('Tuple is :({},'.format(stack[-1]),'PROCEDUREBEGIN,','#, #)')
        prnt(str(stack[-1]),'PROCEDUREBEGIN','#','#')

    local_var = 1
    #local_sym = []
    if stack[-1] not in sym_dict:
        sym_list=[stack[-1], 'PROCEDURE', '#', '0' ,'0']
        sym_dict[stack[-1]] = 27
        sym_dict_local[stack[-1]] = 27
        global_sym.append(sym_list)
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    temp = stack[-1]
    stack[-2] = temp
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
"""def semantics(line_num,stack,length):
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    global labelcounter
    global bcounter
    global ircounter
    global type
    global type1
    global type2
    global type23
    global type33
    global errorcheck
    global set
    
    if line_num == 7 or line_num == 8 or line_num == 3 or line_num == 4 or line_num == 9 or line_num == 20 or line_num == 21 or line_num == 22 or line_num == 25 or line_num == 26:
        for i in range(length-1):
            stack.pop()
        #print('semantics stack is',stack)
    
    if line_num == 38 or line_num ==40 or  line_num == 41 or line_num == 42 or line_num == 43 or line_num == 44 or line_num == 45 or line_num == 46 or line_num == 47 or line_num ==  48 or line_num == 86 or line_num == 87 or line_num == 91 or line_num == 93 or line_num == 94 or line_num == 96 or line_num == 98 or line_num == 105 or line_num == 106 or line_num == 110 or line_num == 111 or line_num == 114 or line_num == 116 or line_num == 117 or line_num == 120 or line_num ==121:
        for i in range(length-1):
            stack.pop()"""

def line28(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    if flags.flags[13] == 1:
        #print('Tuple is :(#,NOFORMALDECLARATION ,#, #)')
        prnt('#','NOFORMALDECLARATION','#','#')

    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line29(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is :(#,ENDFORMALPARAMETERLIST ,#, #)')
        prnt('#','ENDFORMALPARAMETERLIST','#','#')

    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line30(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is :({}'.format(stack[-1]),'FORMAL{}'.format(stack[-2]),'PARAMETER, 1,0 )')
        prnt(stack[-1],stack[-2],'1','0',1)
    if stack[-1] not in sym_dict_local:
        sym_list=[stack[-1], stack[-2],'SCALAR',1,0,stack[-3]]
        sym_dict_local[stack[-1]] = 30
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line31(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five
    
    if flags.flags[13] == 1:
        #print('Tuple is :({}'.format(stack[-4]),'FORMAL{}'.format(stack[-5]),'PARAMETER, 1,0 )')
        five = stack[-5]
        prnt(str(stack[-4]),'MEMORY',str(stack[-2]),'0')
        prnt(str(stack[-4]),'FORMAL'+str(stack[-6])+'VALUE',str(stack[-2]),'#')
        
        
    if stack[-4] not in sym_dict_local:
        sym_list=[stack[-4], stack[-5],'VECTOR',stack[-2],0,stack[-6]]
        sym_dict_local[stack[-4]] = 31
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line32(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five
    
    if flags.flags[13] == 1:
        
        five = stack[-7]
        prnt(str(stack[-6]),'MEMORY',str(stack[-4]),str(stack[-2]))
        prnt(str(stack[-6]),'FORMAL'+str(stack[-8])+'PARAMETER', str(stack[-4]),str(stack[-2]))
        
    if stack[-6] not in sym_dict_local:
        sym_list=[stack[-6], stack[-7],'MATRIX',stack[-4],stack[-2],stack[-8]]
        sym_dict_local[stack[-6]] = 32
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line33(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global five
    
    if flags.flags[13] == 1:
        five = stack[-2]
        prnt('#','BEGINFORMALPARAMETERLIST','#',' #')
        #prnt(str(stack[-1]),'MEMORY','1','0')
        prnt(str(stack[-1]),'FORMAL'+str(stack[-3])+'PARAMETER', str(1),str(0))
        

        #print('Tuple is :(#,BEGINFORMALPARAMETERLIST ,#, #)')
    if stack[-1] not in sym_dict_local:
        sym_list=[stack[-1], stack[-2],'SCALAR',1,0,stack[-3]]
        sym_dict_local[stack[-1]] = 33
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line34(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        print('#','BEGINFORMALPARAMETERLIST ','#', '#',0)
        #print('Tuple is :({},'.format(stack[-4]),'FORMAL ,','{},'.format(stack[-5]),'PARAMETER,',stack[-2], '0)')
        prnt(str(stack[-4]),str(stack[-5]),str(stack[-2]),'0')

        #print('Tuple is :(#,BEGINFORMALPARAMETERLIST ,#, #)')
    if stack[-4] not in sym_dict_local:
        sym_list=[stack[-4], stack[-5],'VECTOR',stack[-2],0,stack[-6]]
        sym_dict_local[stack[-4]] = 34
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line35(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','BEGINFORMALPARAMETERLIST','#','#')
        prnt(str(stack[-6]),str(stack[-7]),str(stack[-4]),str(stack[-2]))
        #print('Tuple is :({},'.format(stack[-6]),'FORMAL{}'.format(stack[-7]),'PARAMETER', stack[-4],stack[-2],')' )

    if stack[-6] not in sym_dict_local:
        sym_list=[stack[-6], stack[-7],'MATRIX',stack[-4],stack[-2],stack[-8]]
        sym_dict_local[stack[-6]] = 35
        local_sym.append(sym_list)
    else:
        print('DOUBLY DECLARED ERROR')
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line36(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    stack[-1] = 'VALUE'
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line37(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    stack[-1] = 'REFERENCE'
    for i in range(length-1):
        stack.pop()
    #print('semantics stack is',stack)
    
def line39(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: (MAIN,LABEL,#,#)')
        prnt('MAIN','LABEL','#','#')

    for i in range(length-1):
        stack.pop()
                     
def line49(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: ("scanf",ENDPROCEDURECALL,#,#)')
        prnt('scanf','ENDPROCEDURE','#','#')
    local_var = 0

    for i in range(length-1):
        stack.pop()
                            
def line50(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: (#,ACTUALscanfSUBPARAMETER,{}'.format(stack[-1]),',#)')
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-1]),'#')

    for i in range(length-1):
        stack.pop()
    
def line51(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-4]),str(stack[-2]))        
    for i in range(length-1):
        stack.pop()
    
def line52(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    
    if flags.flags[13] == 1:
        
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-6]:
                    x = local_sym[i][4] 
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-6]:
                    x = global_sym[i][4]
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),x)
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-2]))
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-6]),'I$'+str(integercounter+1))     
    for i in range(length-1):
        stack.pop()
    integercounter+=1
           
def line53(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: (#,ACTUALscanfSUBPARAMETER,{}'.format(stack[-1]),',#)')
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-1]),'#')        

    for i in range(length-1):
        stack.pop()
    
def line54(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: (#,ACTUALscanfSUBPARAMETER,{}'.format(stack[-4]),',{})'.format(stack[-2]))
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-4]),str(stack[-2]))        

    for i in range(length-1):
        stack.pop()
    
def line55(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    
    if flags.flags[13] == 1:
        
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-8]:
                    x = local_sym[i][4] 
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-8]:
                    x = global_sym[i][4]
                    
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),x)
        prnt('I$'+str(integercounter+1),'IADD',str(integercounter),str(stack[-2]))
        prnt('#','ACTUALSCANFSUBPARAMETER',str(stack[-6]),'I$'+str(integercounter+1))     
    for i in range(length-1):
        stack.pop()
    integercounter+=1
        
def line56(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        #print('Tuple is: ("scanf",BEGINPROCEDURECALL,#,#)')
        prnt('scanf','BEGINPROCEDURECALL','#','#')        
        prnt(str(stack[-1]),'ACTUALSCANFPARAMETER','#','#')
    for i in range(length-1):
        stack.pop()
        
def line57(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('printf','ENDPROCEDURECALL','#','#')
    for i in range(length-1):
        stack.pop()
        
def line58(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('printf','ENDPROCEDURECALL','#','#')
    for i in range(length-1):
        stack.pop()

def line59(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALPRINTFPARAMETER',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()

def line60(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()

def line61(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('ACTUALPRINTFSUBPARAMETER',str(stack[-4,]),str(stack[-2]))
    for i in range(length-1):
        stack.pop()
        
def line62(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter

    
    if flags.flags[13] == 1:
        print(stack)
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-6]:
                    x = local_sym[i][4]
            
            
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-6]:
                    x = global_sym[i][4]
                    
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),str(x))
        prnt('I$'+str(integercounter+1),',IADD','I$'+str(integercounter),str(stack[-2]))
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-6]),'I$'+str(integercounter+1))    
    for i in range(length-1):
        stack.pop()
    integercounter+=1
    
def line63(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-1]),'#')    
    for i in range(length-1):
        stack.pop()
            
def line64(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-1]),'#') 
    for i in range(length-1):
        stack.pop()


def line65(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-4]),str(stack[-2]))
    for i in range(length-1):
        stack.pop()
     
def line66(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    #global x
    #x = ''
    print(stack)
    if flags.flags[13] == 1:
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-6]:
                    x = local_sym[i][4]
                               
            
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-6]:
                    x = global_sym[i][4]
                                
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),x)
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-2]))
        prnt('#','ACTUALPRINTFSUBPARAMETER',str(stack[-6]),'I$'+str(integercounter+1))    
    for i in range(length-1):
        stack.pop()
    integercounter+=1
    
def line67(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('printf','BEGINPROCEDURECALL','#','#')
        prnt(str(stack[-1]),'ACTUALVALPARAMETER','#','#')    
    for i in range(length-1):
        stack.pop()

def line68(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt(str(stack[-2]),'ENDNOPARAMETERSPROCEDURECALL','#','#')    
    for i in range(length-1):
        stack.pop()
        
        
def line69(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt(str(stack[-2]),'ENDPROCEDURECALL','#','#')    
    for i in range(length-1):
        stack.pop()
        
        
def line70(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt(str(stack[-1]),'CALL','#','#')
        stack[-2]=stack[-1]
    for i in range(length-1):
        stack.pop()
        
def line71(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ENDACTUALPARAMETERLIST','#','#')
    for i in range(length-1):
        stack.pop()
def line72(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
       prnt('#','ACTUAL'+str(stack[-2])+'PARAMETERLIST',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()

def line73(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUALVALPARAMETER',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()


def line74(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','ACTUAL'+str(stack[-5]),'SUBPARAMTER',str(stack[-4]),str(stack[-2]))
    for i in range(length-1):
        stack.pop()

def line75(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    
    if flags.flags[13] == 1:
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-8]:
                    x = local_sym[i][4]
            
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-8]:
                    x = global_sym[i][4]
                    
        prnt('I$'+str(integercounter),'IMULT'+str(stack[-4]),x)
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-2]))
        prnt('#','ACTUAL'+str(stack[-7]),'SUBPARAMETER'+str(stack[-6]),'I$'+str(integercounter+1))     
    for i in range(length-1):
        stack.pop()
    integercounter+=1 

def line76(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','BEGINACTUALPARAMETER','#','#')
        prnt('#','ACTUAL'+str(stack[-2])+'SUBPARAMETER',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()

    
def line77(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','BEGINACTUALPARAMETER','#','#')
        prnt('#','ACTUALSUBPARAMETER',str(stack[-1]),'#')
    for i in range(length-1):
        stack.pop()
         
        
def line78(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    
    if flags.flags[13] == 1:
        prnt('#','BEGINACTUALPARAMETER','#','#')
        print('#','ACTUAL'+str(stack[-5]),'SUBPARAMTER'+str(stack[-4]),str(stack[-2]))
    for i in range(length-1):
        stack.pop()
                            
def line79(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    if flags.flags[13] == 1:
        prnt('#','BEGINACTUALPARAMETER','#','#')
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),str(stack[-6]))
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-2]))
        prnt('#','ACTUAL'+str(stack[-7]),'SUBPARAMETER'+str(stack[-6]),'I$'+str(integercounter+1))     
    for i in range(length-1):
        stack.pop()
    integercounter+=1
    
def line80(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    
    if flags.flags[13] == 1:
        print(stack)
        print('80')
        
        #print('REDUCTION NUMMMMMMM',line_num)
        prnt('L$'+str(la),'LABEL','#','#')    
    for i in range(length-1):
        stack.pop()
    labelcounter+=1
   
def line81(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    
    if flags.flags[13] == 1:
        #print('REDUCTION NUMMMMMMM',line_num)
        print(stack)
        prnt('L$'+str(labelcounter),'LABEL','#','#')
        #stack[-1] = '{}'.format(labelcounter)  
        labelcounter+=1     
    for i in range(length-1):
        stack.pop()
        
def line82(stack,length):
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    
    if flags.flags[13] == 1:
        prnt('L$'+str(labelcounter+1),'JUMP','#','#')
        prnt('L$'+str(labelcounter),'LABEL','#','#')
        
    for i in range(length-1):
        stack.pop()
    labelcounter+=1 
    
def line83(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    global la
    #print(stack)
    #print('REDUCTION NUMMMMM {}'.format(line_num))
    #print(stack)
    bexpr=''
    
    if flags.flags[13] == 1:
        labelcounter+=1
        #reg = re.compile(r"""[a-zA-Z0-9]([>]|[<]|[>][=]|[<][=]|[=][=])[a-zA-Z0-9]""",re.VERBOSE)
        #for f in reg.findall(bexpr):
         #   if f.group(1):
        #prnt('L$'+str(labelcounter),'LABEL','#','#')
        stack[-1]=labelcounter
        la = labelcounter
        prnt('L$'+str(labelcounter),'CJUMP',str(stack[-3]),'#')
          #  else:
    #bexpr=stack[-3][0]
    if stack[-3][0] != "B":
        print('ERROR1 : A NON-LOGICAL EXPRESSION IN AN IF OR LOOPING STATEMENT CONDITION')
                    
    for i in range(length-1):
        stack.pop()  

def line84(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    
    #print(stack)
    if flags.flags[13] == 1:
        #print('REDUCTION NUMMMMMMMMMM',line_num)
        prnt('L$'+str(stack[-5]),'CJUMP',str(stack[-2]),'#')            
        #prnt('L$'+str(stack[-5]+1),'LABEL','#','#')
        #print('CHANGEEEE{}'.format(stack[-5]),',CJUMP,{}'.format(stack[-3]),',#')
    #print(stack[-2])
    labelcounter+=1
    if stack[-2][0] != 'B':
            print('ERROR1 : A NON-LOGICAL EXPRESSION IN AN IF OR LOOPING STATEMENT CONDITION')
    for i in range(length-1):
        stack.pop()
    
def line85(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global labelcounter
    if flags.flags[13] == 1:
        labelcounter+=1
        stack[-1]=labelcounter
        prnt('L$'+str(labelcounter),'LABEL','#','#')
        
        #prnt('L$'+str(labelcounter+1),'JUMP','#','#')
    for i in range(length-1):
        stack.pop()
    
              
def line88(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    global five
    
    if flags.flags[13] == 1: 
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])
        #print('type 1 '+stack[-1], type1)
        #print('type 2 '+stack[-3], type2)
        if type1 == type2:
            five = chck_type(str(stack[-1]))
            prnt(str(stack[-3]),'STORE',str(stack[-1]),'#')
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-1] = 'I$'+str(integercounter)
            prnt(str(stack[-3]),'STORE',str(stack[-1]),'#')
            integercounter = integercounter + 1
        elif type1 != type2 and type2 == 'REAL':
            stack[-1] = 'R$'+str(realcounter)
            prnt(str(stack[-3]),'STORE',str(stack[-1]),'#')
            realcounter = realcounter + 1
        
    for i in range(length-1):
        stack.pop()
       

def line89(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    global five
    print(stack)
    if flags.flags[13] == 1:
        type3 = chck_type(stack[-4])
        if type3 == 'REAL':
            print('ERROR : SUBSCRIPT IS NOT AN INTEGER')
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-6])
        five = type2
        if type1 == type2:
            
            prnt(str(stack[-6]),'SUBSTORE',str(stack[-1]),str(stack[-4]))
        elif type1 != type2 and type2 == 'INTEGER':
            
            prnt(str(stack[-6]),'SUBSTORE',str(stack[-1]),str(stack[-4]))
            integercounter = integercounter + 1
        elif type1 != type2 and type2 == 'REAL':
            prnt(str(stack[-6]),'SUBSTORE',str(stack[-1]),str(stack[-4]))
            realcounter = realcounter + 1
    for i in range(length-1):
        stack.pop()
       
    print(stack)        
 
def line90(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    #global type1
    #global type2
    
    #print(stack)
    if flags.flags[13] == 1:
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-8]:
                    x = local_sym[i][4]
            
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-8]:
                    x = global_sym[i][4]
        #prnt('I$'+str(integercounter),'IMULT',str(stack[-6]),x) 
        #prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-4]))
        type1 = chck_type(stack[-4])
        type2 = chck_type(stack[-6])
        if type1 == 'REAL':
            print('ERROR: SUBSCRIPT NOT AN INTEGER')
        if type2 == 'REAL':
            print('ERROR: SUBSCRIPT NOT AN INTEGER')
        prnt('I$'+str(integercounter),'IMULT',str(stack[-6]),x) 
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-4]))
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-8])
        if type1 == type2:
            prnt(str(stack[-8]),'SUBSTORE',str(stack[-1]),'I$'+str(integercounter+1))
            integercounter = integercounter + 2
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-1]='I$'+str(integercounter)
            prnt(str(stack[-8]),'SUBSTORE',str(stack[-1]),'I$'+str(integercounter+1))
            integercounter = integercounter + 2
        elif type1 != type2 and type2 == 'REAL':
            stack[-1]='R$'+str(realcounter)
            prnt(str(stack[-8]),'SUBSTORE',str(stack[-1]),'I$'+str(integercounter+1))
            integercounter = integercounter + 2
            realcounter = realcounter + 1
        
    for i in range(length-1):
        stack.pop()
   
def line92(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    if flags.flags[13] == 1:
        prnt('B$'+str(bcounter),'OR',str(stack[-3]),str(stack[-1]))
        stack[-3] = 'B$'+str(bcounter)
        
    for i in range(length-1):
        stack.pop()
    bcounter+=1
           
def line95(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    if flags.flags[13] == 1:
        prnt('B$'+str(bcounter),'AND',str(stack[-3]),str(stack[-1]))
        stack[-3] = 'B$'+str(bcounter)
    for i in range(length-1):
        stack.pop()
    bcounter+=1
        
def line97(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    if flags.flags[13] == 1:
        prnt('B$'+str(bcounter),'NOT',str(stack[-1]),'#')
        stack[-2] = 'B$'+str(bcounter)
    for i in range(length-1):
        stack.pop()
    bcounter+=1

def line99(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    global realcounter
    
    
    if flags.flags[13] == 1:
        error3(-1,stack)
        error3(-3,stack)
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-1])
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'ILESSTHAN',str(stack[-3]),str(stack[-1]))
        if type1 == type2 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'RLESSTHAN',str(stack[-3]),str(stack[-1]))
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RLESSTHAN',str(stack[-3]),str(stack[-1])) 
            realcounter = realcounter + 1
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RLESSTHAN',str(stack[-3]),str(stack[-1])) 
            realcounter = realcounter + 1
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1

    for i in range(length-1):
        stack.pop()

def line100(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    global realcounter
    
    if flags.flags[13] == 1:
        
        error3(-1,stack)
        error3(-3,stack)
        type1 = chck_type(stack[-1])
        #print('type1 ',type1)
        type2 = chck_type(stack[-3])
        #print('type2 ',type2)
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'ILESSTHANEQUALS',str(stack[-3]),str(stack[-1]))
        elif type2 == type1 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'RLESSTHANEQUALS',str(stack[-3]),str(stack[-1]))
        
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RLESSTHANEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-3] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RLESSTHANEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
                     
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1
    for i in range(length-1):
        stack.pop()
    
        
def line101(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    global realcounter
    
    if flags.flags[13] == 1:
        
        error3(-1,stack)
        error3(-3,stack)
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])
    
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'IGREATERTHAN',str(stack[-3]),str(stack[-1]))
        elif type2 == type1 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'RGREATERTHAN',str(stack[-3]),str(stack[-1]))
            
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RGREATERTHAN',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1      
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-3] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RGREATERTHAN',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
        
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1
    for i in range(length-1):
        stack.pop()
            
def line102(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    if flags.flags[13] == 1:
        
        error3(-1,stack)
        error3(-3,stack)
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])
        
            
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'IGREATERTHANEQUALS',str(stack[-3]),str(stack[-1]))
        elif type2 == type1 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'RGREATERTHANEQUALS',str(stack[-3]),str(stack[-1]))
            
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RGREATERTHANEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
            
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-3] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RGREATERTHANEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
                     
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1
    for i in range(length-1):
        stack.pop()
            
            
        
def line103(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    #print(stack)
    if flags.flags[13] == 1:
        
        error3(-1,stack)
        error3(-3,stack)
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])
        
            
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'IEQUALS',str(stack[-3]),str(stack[-1]))
        elif type2 == type1 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'REQUALS',str(stack[-3]),str(stack[-1])) 
        
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'REQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
            
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-3] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'REQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1   
    
    
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1
    
    for i in range(length-1):
        stack.pop()
                    
def line104(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global bcounter
    
    if flags.flags[13] == 1:
        
        #error3(-1,stack)
        #error3(-3,stack)
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])
        
        if type1 == type2 and type1 == 'INTEGER':
            prnt('B$'+str(bcounter),'INOTEQUALS',str(stack[-3]),str(stack[-1]))
        elif type2 == type1 and type1 == 'REAL':
            prnt('B$'+str(bcounter),'RNOTEQUALS',str(stack[-3]),str(stack[-1]))   
        elif type1 != type2 and type1 == 'INTEGER':
            stack[-1] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RNOTEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
            
        elif type1 != type2 and type2 == 'INTEGER':
            stack[-3] = 'R$'+str(realcounter)
            prnt('B$'+str(bcounter),'RNOTEQUALS',str(stack[-3]),str(stack[-1]))
            realcounter = realcounter + 1
            
        
           
    stack[-3] = 'B$'+str(bcounter)
    bcounter+=1
    for i in range(length-1):
        stack.pop()
            
def line107(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    #global type1
    #global type2
    
    if flags.flags[13] == 1:            
        
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])

        if type1 == type2 and type1 == 'INTEGER':
            prnt('I$'+str(integercounter+1),'IADD',str(stack[-3]),str(stack[-1]))     
            stack[-3]= 'I$'+str(integercounter+1)
            integercounter+=2
        elif type1 == type2 and type1 == 'REAL':
            prnt('R$'+str(realcounter+1),'RADD',str(stack[-3]),str(stack[-1]))
            stack[-3]= 'R$'+str(realcounter+1)     
            realcounter+=2
        elif type1 != type2 and type1 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-1]),'#')
            stack[-1]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RADD',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
        elif type1 != type2 and type2 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-3]),'#')
            stack[-3]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RADD',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
                              
                               
    
   
        
    for i in range(length-1):
        stack.pop()
        
def line108(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    #global type1
    #global type2
    
    if flags.flags[13] == 1:
        
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])

        if type1 == type2 and type1 == 'INTEGER':
            prnt('I$'+str(integercounter+1),'ISUB',str(stack[-3]),str(stack[-1]))     
            stack[-3]= 'I$'+str(integercounter+1)
            integercounter+=2
        elif type1 == type2 and type1 == 'REAL':
            prnt('R$'+str(realcounter+1),'RSUB',str(stack[-3]),str(stack[-1]))
            stack[-3]= 'R$'+str(realcounter+1)     
            realcounter+=2
        elif type1 != type2 and type1 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-1]),'#')
            stack[-1]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RSUB',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
        elif type1 != type2 and type2 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-3]),'#')
            stack[-1]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RSUB',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
      
    for i in range(length-1):
        stack.pop()

def line109(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    
    if flags.flags[13] == 1:
        type1 = chck_type(stack[-1])
        if type1 == 'INTEGER':              
            prnt('I$'+str(integercounter),'ISUB','#',str(stack[-1]))
            stack[-2]='I$'+str(integercounter)
            integercounter+=1
        else:
            prnt('R$'+str(realcounter),'RSUB','#',str(stack[-1]))
            stack[-2]='R$'+str(realcounter)
            realcounter+=1
    for i in range(length-1):
        stack.pop()


def line112(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter

    
    if flags.flags[13] == 1:  
        #print(stack)  
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])

        if type1 == type2 and type1 == 'INTEGER':
            prnt('I$'+str(integercounter+1),'IMUL',str(stack[-3]),str(stack[-1]))     
            stack[-3]= 'I$'+str(integercounter+1)
            integercounter+=2
        elif type1 == type2 and type1 == 'REAL':
            prnt('R$'+str(realcounter+1),'RMUL',str(stack[-3]),str(stack[-1]))
            stack[-3]= 'R$'+str(realcounter+1)     
            realcounter+=2
        elif type1 != type2 and type1 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-1]),'#')
            stack[-1]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RMUL',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
        elif type1 != type2 and type2 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-3]),'#')
            stack[-3]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RMUL',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
            
    for i in range(length-1):
        stack.pop()

                          
def line113(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    #global type1
    #global type2

    if flags.flags[13] == 1:
        type1 = chck_type(stack[-1])
        type2 = chck_type(stack[-3])

        if type1 == type2 and type1 == 'INTEGER':
            prnt('I$'+str(integercounter+1),'IDIV',str(stack[-3]),str(stack[-1]))     
            stack[-3]= 'I$'+str(integercounter+1)
            integercounter+=2
        elif type1 == type2 and type1 == 'REAL':
            prnt('R$'+str(realcounter+1),'RDIV',str(stack[-3]),str(stack[-1]))
            stack[-3]= 'R$'+str(realcounter+1)     
            realcounter+=2
        elif type1 != type2 and type1 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-1]),'#')
            stack[-1]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RDIV',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
        elif type1 != type2 and type2 == 'INTEGER':
            prnt('R$'+str(realcounter),'CONVERTIR',str(stack[-3]),'#')
            stack[-3]='R$'+str(realcounter)
            prnt('R$'+str(realcounter+1),'RDIV',str(stack[-3]),str(stack[-1]))
            stack[-3]='R$'+str(realcounter+1)
            realcounter+=2
                                    
    for i in range(length-1):
        stack.pop()
 
def line115(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    #print(stack)
    if flags.flags[13] == 1:
        stack[-3] = stack[-2]
    for i in range(length-1):
        stack.pop()

def line118(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    global type
    global five
    
    if flags.flags[13] == 1:
        type = chck_type(stack[-2])
        if type == 'REAL':
            print('ERROR: SUBSCRIPT IS NOT INTEGER')
        type = chck_type(stack[-4])
        five = type
        if type =='INTEGER':
            
            prnt('I$'+str(integercounter+1),'SUBLOAD',str(stack[-4]),str(stack[-2]))
            stack[-4] = 'I$'+str(integercounter+1)
            integercounter+=2    
        elif type =='REAL':
            prnt('R$'+str(realcounter+1),'SUBLOAD',str(stack[-4]),str(stack[-2]))
            stack[-4] = 'R$'+str(realcounter+1)
            realcounter+=2
    for i in range(length-1):
        stack.pop()
                        
        

def line119(stack,length):
    
    global global_sym
    global local_sym
    global sym_dict
    global sym_dict_local
    global local_var
    global integercounter
    global realcounter
    global type
    global t
    global t1
    global type23
    global type33
    
    #print(stack)
    t=''
    t1=''
    integercounter+=1
    if flags.flags[13] == 1:
        if local_var:
            for i in range(len(local_sym)):
                v=local_sym[i][0]
                if v == stack[-6]:
                    x = local_sym[i][4] 
        else:
            for i in range(len(global_sym)):
                v=global_sym[i][0]
                if v == stack[-6]:
                    x = global_sym[i][4] 
                    
        type1 = chck_type(stack[-2])
        type2 = chck_type(stack[-4])
        if type1 == 'REAL':
            print('ERROR: SUBSCRIPT ARE NOT INTEGER')
        if type2 == 'REAL':
            print('ERROR: SUBSCRIPT ARE NOT INTEGER')
            
        prnt('I$'+str(integercounter),'IMULT',str(stack[-4]),x)
        prnt('I$'+str(integercounter+1),'IADD','I$'+str(integercounter),str(stack[-2]))
        
        
        type = chck_type(stack[-6])
        
        if type =='REAL':
            prnt('R$'+str(realcounter+2),'SUBLOAD',str(stack[-6]),'I$'+str(integercounter+1))
            stack[-6]='R$'+str(realcounter+2)
            realcounter+=2
        elif type =='INTEGER':
            prnt('I$'+str(integercounter+2),'SUBLOAD',str(stack[-6]),'I$'+str(integercounter+1))
            stack[-6]='I$'+str(integercounter+2)
            integercounter+=2  
        
    if local_var:
        for i in range(len(local_sym)):
            v=local_sym[i][0]
            if v == stack[-6]:
                t = local_sym[i][4] 
                 
    else:
        for i in range(len(global_sym)):
            v=global_sym[i][0]
            if v == stack[-6]:
                t1 = global_sym[i][4]
    print(t,t1)
    if t == '0' or t1 == '0':
        print('ERROR2 :A VARIABLE USED DIFFERENTLY THAN IT IS DECLARED, ETC')

    
    for i in range(length-1):
        stack.pop()
    