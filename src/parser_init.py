'''
Created on Oct 8, 2012

@author: sugethk
'''

import numbers
import re
import time
import dictionary
import sys
import matrix
import productions
import prod_mod
import flags
import semantics2
global strg
strg = " "
global count
count = 0
global syntax
syntax = []
global sem
sem = []


def parse(queue,queue_num,stack,stack_num,handle,handle_num,line):
    
    global line_num
    line_num = 0
    global syntax
    global sem
    
    def print_redns(number,redns,line_num):
        #global line_num
        for key,val in numbers.numbers.items():
            #count = count + 1
            if val==number:
                print('Reduction # {}'.format(line_num).rjust(100),'',key+' ---->')
        for each in redns:
            for key,val in numbers.numbers.items():
                if val==each:
                    print(key+' ')
        print()
        
    def greater(queue,queue_num,stack,stack_num,handle,handle_num):
        top_of_stack_num=stack_num.pop()
        #top_stack=stack.pop()
        handle_num.insert(0,top_of_stack_num)
        #handle.insert(0,top_stack)
        top=stack_num[-1]
        top_han=handle_num[0]
        rel=relations(top,top_han,queue,queue_num,stack,stack_num,handle,handle_num)
        while (rel==1) and stack_num:
            top_of_stack_num=stack_num.pop()
            #top_stack=stack.pop()
            handle_num.insert(0,top_of_stack_num)
            #handle.insert(0,top_stack)
            if not stack_num:
                break
            top=stack_num[-1]
            top_han=handle_num[0]
            rel=relations(top,top_han,queue,queue_num,stack,stack_num,handle,handle_num)
            
        if flags.flags[10]==1:
            for each in handle_num:
                for key,val in numbers.numbers.items():
                    if val==each:
                        print(key+' ')
            print()    
        single=tostring(handle_num,strg,queue,queue_num,stack,stack_num,handle,handle_num)
        redns = handle_num
        length = len(redns)
        handle_num=single
        prod,line_num=reduce(handle_num,queue,queue_num,stack,stack_num,handle,handle_num)
        if flags.flags[7]==1:
            print_redns(prod,redns,line_num)
        #print('line_num is ',line_num)
        
    
        #print(stack)
        if flags.flags[12] == 1:
            print('semantic stack before reduction',stack)
        
        if line_num == 7 or line_num == 8 or line_num == 3 or line_num == 4 or line_num == 6 or line_num == 9 or line_num == 20 or line_num == 21 or line_num == 22 or line_num == 25 or line_num == 26:
            for i in range(length-1):
                stack.pop()
    
        elif line_num == 38 or line_num ==40 or  line_num == 41 or line_num == 42 or line_num == 43 or line_num == 44 or line_num == 45 or line_num == 46 or line_num == 47 or line_num ==  48 or line_num == 86 or line_num == 87 or line_num == 91 or line_num == 93 or line_num == 94 or line_num == 96 or line_num == 98 or line_num == 105 or line_num == 106 or line_num == 110 or line_num == 111 or line_num == 114 or line_num == 116 or line_num == 117 or line_num == 120 or line_num ==121:
            for i in range(length-1):
                stack.pop()
        #semantics2.semantics(line_num,stack,length)
        else:
            
            getattr(semantics2, 'line%d' %line_num)(stack,length)
        
        if flags.flags[12] == 1:
            print('semantic stack after reduction',stack)
        
        
        
        #syntax.append(prod)
        
        if flags.flags[8]==1:
            print('stack before reductions    ')
            for each in stack_num:
                for key,val in numbers.numbers.items():
                    if val==each:
                        print(key+' ')
            print()
        
        stack_num.append(prod)
        
        if flags.flags[8]==1:
            print('stack after reduction is     ')
            for each in stack_num:
                for key,val in numbers.numbers.items():
                    if val==each:
                        print(key+' ')
            print()
        #return line_num
        
    def less_equal(queue,queue_num,stack,stack_num,handle,handle_num):
        stack.append(queue.pop(0))
        stack_num.append(queue_num.pop(0))
    
        
    def no_relation(queue,queue_num,stack,stack_num,handle,handle_num):
        print('no relation:ERROR')
                
            
    def tostring(to_s,strg,queue,queue_num,stack,stack_num,handle,handle_num):
        for x in to_s:
            strg+=str(x)
            strg+='   '
        strg=strg.strip()
        to_s = []
        to_s.insert(0, strg)
        return to_s            
                
    def reduce(somehandle,queue,queue_num,stack,stack_num,handle,handle_num):
        global line_num
        test=somehandle.pop()
        if (test in prod_mod.productions):
            prod_num=prod_mod.productions.get(test)
        if (test in prod_mod.reductions):
            line_num=prod_mod.reductions.get(test)
        return prod_num,line_num
            #return prod_num       
        
    def relations(a,b,queue,queue_num,stack,stack_num,handle,handle_num):
        if (matrix.matrix[a-1][b-1]==1):
            rel=1
            return rel
        if (matrix.matrix[a-1][b-1]==2):
            rel=2
            return rel
        if (matrix.matrix[a-1][b-1]==3):
            rel=3
            return rel
        if (matrix.matrix[a-1][b-1]==0):
            rel=0
            return rel
    
    
    
    
    
    global count
    count = 0
    #count=count+1
    global strg
    strg=" "
    global line_num

    while queue_num:
            global line_num
            if not stack_num:
                tt=queue_num.pop(0)
                stack_num.append(tt)
                stack.append(queue.pop(0))
            if handle_num:
                handle_num=tostring(handle_num,strg,queue,queue_num,stack,stack_num,handle,handle_num)
                handle_num.pop()
                handle=tostring(handle_num,strg,queue,queue_num,stack,stack_num,handle,handle_num)
                handle.pop()
            num_q=stack_num[-1]
            num_qnext=queue_num[0]
            rel=relations(num_q,num_qnext,queue,queue_num,stack,stack_num,handle,handle_num)
            if flags.flags[9]==1:
                print('top of stack: {}'.format(num_q).rjust(100))
                print('input symbol: {}'.format(num_qnext).rjust(100))
                print('relation : {}'.format(rel).rjust(100))
            if rel==0:
                print('char pair error at line between {}'.format(num_q).rjust(100),'and {}'.format(num_qnext).rjust(100))
                queue.pop(0)
                print('elements ignored in queue {}'.format(queue).rjust(100))
                for each in queue_num:
                    queue_num.pop()
                    queue.pop()
                print('elements ignored in the stack {}'.format(stack).rjust(100))
                for e in stack_num:
                    stack_num.pop()
                    stack.pop()                
                
            if rel==1 or rel==3:
                less_equal(queue,queue_num,stack,stack_num,handle,handle_num)
                
            if rel==2:
                greater(queue,queue_num,stack,stack_num,handle,handle_num)
            if not queue_num:
                break  
    
       