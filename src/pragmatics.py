
import re
#import semantics2
find1 = re.compile('([a-z][a-zA-Z0-9]*)|([0-9]+)|([IR$]+[0-9]+)')
vic = re.compile('[a-z][a-zA-Z0-9]+')
assem=[]
vari = {}
local = []
globa = []
realno = []
integerno = []
integernol = []
mixer = ''
frp =[]
frpc = []
reals = []
data1 = ['SECTION .data\nformati:\tdb "%d",10,0,\nformatr:\tdb "%f",10,0']
bss = ['SECTION .bss\nz1:    resd    1']
v1 = ''
v2 = ''
prime = 0
reg = {'eax':'','ebx':'','ecx':'','edx':'','esp':'','ebp':'','esi':'','edi':''}
register = ['ebx','ecx','esi','edi','ebp','esp']
jumphere = ''



def printdata(name):
    if name in local :
        if name in integerno or name in integernol :
            data='push\tdword [z1]'
            assem.append(data)
            prin(data)
            data='push formati'
            assem.append(data)
            prin(data)
            data='call printf'
            assem.append(data)
            prin(data)
        elif name in realno :
            data='push formatr'
    elif name in globa :
        if name in integerno or name in integernol :
            data='push\tdword ['+ name +']'
            assem.append(data)
            prin(data)
            data='push formati'
            assem.append(data)
            prin(data)
            data='call printf'
            assem.append(data)
            prin(data)
        elif name in realno :
            data='push formatr'
    else :
        if name in integerno or name in integernol :
            data='push\t[z1]'
            assem.append(data)
            prin(data)
            data='push formati'
            assem.append(data)
            prin(data)
            data='call printf'
            assem.append(data)
            prin(data)
        elif name in realno :
            data='push formatr'
            
                        
def printdata_sub(name,index):
    
    if name in globa :
        if name in integerno or name in integernol :
            if index in local :
                data='mov\teax,'+ reg[vari[index]]
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data)
            elif index in globa :
                data='mov\teax,['+index+']'
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data) 
            else :
                data='mov\teax,' + index
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data)  
            data='push\tdword ['+ name +' + eax]'
            assem.append(data)
            prin(data)
            data='push formati'
            assem.append(data)
            prin(data)
            data='call printf'
            assem.append(data)
            prin(data)
        elif name in realno :
            data='push formatr'
            

def prin(data):
    print (data)
 
 
def rclear():
    global vari
    vari = {}
    global local
    local = []
    global reg
    reg = {'eax':'','ebx':'','ecx':'','edx':'','esi':'','edi':'','ebp':'','esp':''}    


def assign_value(name):
    if name in local :
        #print('reg',vari)
        data='mov\t'+ reg[vari[name]] + ',eax'
        assem.append(data)
        prin(data)
    elif name in globa :
        data='mov\tdword ['+ name + '],eax'
        assem.append(data)
        prin(data)
    else :
        z = assign(name,'0000')
        data='mov\t'+ z + ',eax'
        assem.append(data)
        prin(data)
        
        
def assign(nam,var):
    #print('assign')
    for e in register:

        if reg[e] == '':
            #print('vari inside assign',vari)
            reg[e] = var
            vari[nam] = e
            return e
    print ('no register vacant')
      
      
def remove(nam,var):
    #print('vari',vari)
    reg[vari[nam]] = ''
    vari.pop(nam)


def in_global(var):
    data = 'mov\teax,'+'['+var+']'
    assem.append(data)
    prin(data)


def sub_assign(name,value,index):
    value = str(value)
    name = str(name)
    index = str(index)
    #print('name ',name, value, index)
    #print('local',local)
    #print('global',globa)
    if index == '#' :
        if name in local :
            if value in local :
                data='mov\t'+reg[vari[name]]+','+ reg[vari[value]]
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],'+ reg[vari[value]]
                assem.append(data)
                prin(data)
            elif value in globa :
                data='mov\t'+reg[vari[name]]+',['+value+']'
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],['+value+']'
                assem.append(data)
                prin(data)
            else :
                data='mov\t'+reg[vari[name]]+','+ str(value)
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],'+ value
                assem.append(data)
                prin(data)
        elif name in globa :
            if value in local :
                data='mov\tdword ['+name+'],'+ reg[vari[value]]
                assem.append(data)
                prin(data)
            elif value in globa :
                in_global(value)
                data='mov\tdword ['+name+'],eax'
                assem.append(data)
                prin(data)
            else :
                data='mov\tdword ['+name+'],'+ value
                assem.append(data)
                prin(data)
        else :
            z=assign(name,'0000')
            if value in local :
                data='mov\t'+z+','+ reg[vari[value]]
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],'+ reg[vari[value]]
                assem.append(data)
                prin(data)
            elif value in globa :
                in_global(value)
                data='mov\t'+z+',eax'
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],eax'
                assem.append(data)
                prin(data)
            else :
                data='mov\t'+z+','+ value
                assem.append(data)
                prin(data)
                data='mov\tdword [z1],'+ value
                assem.append(data)
                prin(data)
    else :
        if name in globa :
            if index in local :
                data='mov\teax,'+ reg[vari[index]]
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data) 
            elif index in globa :
                data='mov\teax,['+index+']'
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data)
            else :
                data='mov\teax,' + index
                assem.append(data)
                prin(data)
                data='imul\teax,4'
                assem.append(data)
                prin(data)
                
            if value in local :
                data='mov\tdword ['+name+' + eax],'+ reg[vari[value]]
                assem.append(data)
                prin(data)
            elif value in globa :
                data='mov\tedx,['+value+']'
                assem.append(data)
                prin(data)
                data='mov\tdword ['+name+' + eax],edx'
                assem.append(data)
                prin(data)
            else :
                data='mov\tdword ['+name+' + eax],'+ str(value)
                assem.append(data)
                prin(data)    
                
                
def sub_load(name,index) :
    #print('local ',local)
    #print('global',globa)
    if name in globa :
        #print('inside sub_load')
        if index in local :
            data='mov\teax,'+ reg[vari[index]]
            assem.append(data)
            prin(data)
            data='imul\teax,4'
            assem.append(data)
            prin(data)
            data='mov\teax,['+ name +' + eax]'
            assem.append(data)
            prin(data)
        elif index in globa :
            data='mov\teax,['+index+']'
            assem.append(data)
            prin(data)
            data='imul\teax,4'
            assem.append(data)
            prin(data)
            data='mov\teax,['+ name +' + eax]'
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,' + index
            assem.append(data)
            prin(data)
            data='imul\teax,4'
            assem.append(data)
            prin(data)
            data='mov\teax,['+ name + ' + eax]'
            assem.append(data)
            prin(data)
        
        
def isub(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in local :
        if var2 in local :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='sub\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='sub\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='sub\teax,'+ var2
            assem.append(data)
            prin(data)
    elif var1 in globa :
        if var2 in local :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='sub\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,['+var1+']'
            assem.append(data)
            prin(data)
            data='sub\teax,['+ var2 +']'
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='sub\teax,'+ var2
            assem.append(data)
            prin(data)
    else :
        if var2 in local :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='sub\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='sub\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='sub\teax,'+ var2
            assem.append(data)
            prin(data)                

        
def imul(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in local :
        if var2 in local :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='imul\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='imul\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='imul\teax,'+ var2
            assem.append(data)
            prin(data)
    elif var1 in globa :
        if var2 in local :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='imul\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,['+var1+']'
            assem.append(data)
            prin(data)
            data='imul\teax,['+ var2 +']'
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='imul\teax,'+ var2
            assem.append(data)
            prin(data)
    else :
        if var2 in local :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='imul\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='imul\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='imul\teax,'+ var2
            assem.append(data)
            prin(data)        
        

def iadd(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in local :
        if var2 in local :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='add\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='add\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ reg[vari[var1]]
            assem.append(data)
            prin(data)
            data='add\teax,'+ var2
            assem.append(data)
            prin(data)
    elif var1 in globa :
        if var2 in local :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='add\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,['+var1+']'
            assem.append(data)
            prin(data)
            data='add\teax,['+ var2 +']'
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            assem.append(data)
            prin(data)
            data='add\teax,'+ var2
            assem.append(data)
            prin(data)
    else :
        if var2 in local :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='add\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='add\teax,['+var2+']' 
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='add\teax,'+ var2
            assem.append(data)
            prin(data)
        
           
def finder(name):
    if name in local :
        #print('inside local')
        1234
    elif name in globa :
        #print('inside global')
        1234
    else :
        local.append(name)
        #print('inside ')
        z = assign(name,'0000')
        remove(name,'')
        assign(name,z)
        #print('z',z,name)


def compare(var1,var2) :
    var1 = str(var1)
    var2 = str(var2)
    if var1 in local :
        if var2 in local :
            #print('var1 in local and var2 in local',var2)
            data='cmp\t'+reg[vari[var1]]+','+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            #print('var1 in local and var2 in global',var2)
            data='cmp\t'+reg[vari[var1]]+',['+var2+']' 
            assem.append(data)
            prin(data)
            remove(var2,'')
        else :
            data='cmp\t'+reg[vari[var1]]+','+ var2
            assem.append(data)
            prin(data)
    elif var1 in globa :
        if var2 in local :
            #print('var1 in global and var2 in local',var2)
            data='cmp\t['+var1+'],'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            #print('var1 in global and var2 in global',var2)
            data='mov\teax,['+var1+']'
            assem.append(data)
            prin(data)
            data='cmp\teax,['+ var2 +']'
            assem.append(data)
            prin(data)
        else :
            data='cmp\tdword ['+var1+'],'+ var2
            assem.append(data)
            prin(data)
    else :
        if var2 in local :
            #print('var2 in local',var2)
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='cmp\teax,'+ reg[vari[var2]]
            assem.append(data)
            prin(data)
        elif var2 in globa :
            #print('var2 in global',var2)
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='cmp\teax,['+ var2+']'
            assem.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            assem.append(data)
            prin(data)
            data='cmp\teax,'+ var2
            assem.append(data)
            prin(data)
    
    zzz = find1.findall(var1)
    if zzz[0][2] != '' :
        remove(var1,'')
    zzz = find1.findall(var2)
    if zzz[0][2] != '' :
        remove(var2,'')
        
 
def actual_parameter(name):
    if name in local :
        data='push\t'+ reg[vari[name]]
        assem.append(data)
        prin(data)
    elif name in globa :
        z = assign(name,'0000')
        data='mov\t'+z+','+ name
        assem.append(data)
        prin(data)
        data='mov\teax,['+z+']'
        assem.append(data)
        prin(data)
        data='push\teax'
        assem.append(data)
        prin(data)
        remove(name,'')
    else :
        data='mov\teax,'+ name
        assem.append(data)
        prin(data)
        data='push\teax'
        assem.append(data)
        prin(data)
        
        
def end_actual_parameter():
    for ee in range(len(frpc)) :
        xx = frpc[len(frpc)-1-ee]
        if xx in local :
            data='pop\tdword '+ reg[vari[xx]]
            assem.append(data)
            prin(data)
        elif xx in globa :
            z = assign(xx,'0000')
            data='mov\t'+z+','+ xx
            assem.append(data)
            prin(data)
            data='pop\tdword ['+z+']'
            assem.append(data)
            prin(data) 
            

def r_sub_assign(name,value) :
    if name in globa :
        z = assign(name, '0000')
        remove(name,'')
        assign(name,z)
        data = 'mov\t'+z+','+name
        assem.append(data)
        prin(data)        
        if value in local :
            11111
        else :
            data = 'mov\tqword ['+z+'],'+ value
            assem.append(data)
            prin(data)
        remove(name,'')
            
   
def r_add(var1,var2,var3) :
    if var1 in globa :
        data = 'fld\tdword ['+var1+']'
        assem.append(data)
        prin(data)
    data = 'fld\tdword ['+var2+']'
    assem.append(data)
    prin(data)
    data = 'faddp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\npush\tformatr\ncall\tprintf\nadd\tesp,12'
    assem.append(data)
    prin(data)
            
   
def r_sub(var1,var2,var3) :
    if var1 in globa :
        data = 'fld\tdword ['+var1+']'
        assem.append(data)
        prin(data)
    data = 'fld\tdword ['+var2+']'
    assem.append(data)
    prin(data)
    data = 'fsubp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\npush\tformatr\ncall\tprintf\nadd\tesp,12'
    assem.append(data)
    prin(data)

        
def tuples(list1,globe):
    #print('register',reg)
    #print('vari inside tup',vari)
    #print('assem',assem)
    if list1[1]=='PROGRAMBEGIN':
        name=list1[0]+'.asm'
        assem.append(name)
        prin(name)
        
        
    elif list1[1]=='ENDPROGRAM':
        data = 'mov esp, ebp\npop dword ebp'
        assem.append(data)
        prin(data) 
        data = 'ret\n'
        assem.append(data)
        prin(data)
        prag=open(assem[0],'w+')
        assem.pop(0)
        prag.write('global main\nextern printf\n')
        for e in reals :
            e = e + ':\tresd\t1'
            bss.append(e)
        for e in data1 :
            e = e + '\n'
            prag.write(e)
        for e in bss :
            e = e + '\n'
            prag.write(e)
        for e in assem :
            e = e + '\n'
            prag.write(e)
        prag.close()
    
    
    elif list1[1] == 'ENDDECLARATIONS' and globe == 0 :
        assem.append('SECTION .text\n')
        prin('SECTION .text\n')
        
        
    elif list1[1]=='STARTDECLARATIONS':
        assem.append('SECTION .data')
        prin('SECTION .data')
        
        
    elif list1[1]=='MEMORY' and globe == 0 and list1[4] == 'INTEGER':
        global globa
        integerno.append(list1[0])
        if list1[2] == 1:
            data = list1[0]+':\tresd\t'+str(list1[2])
            globa.append(list1[0])
            bss.append(data)
            prin(data)
        elif list1[3] == 0:
            data = list1[0]+':\tresd\t'+str(int(list1[2]))
            globa.append(list1[0])
            bss.append(data)
            prin(data)
        else:
            data = list1[0]+':\tresd\t'+str(int(list1[2])*int(list1[3]))
            globa.append(list1[0])
            bss.append(data)
            prin(data)
            
        
    elif list1[1]=='MEMORY' and globe == 1 and list1[4] == 'INTEGER':
        global local
        integernol.append(list1[0])
        if list1[2] == 1:
            z = assign(list1[0],'0000')
            remove(list1[0],'')
            assign(list1[0],z)
            local.append(list1[0])
            
            
    elif list1[1]=='MEMORY' and globe == 0 and list1[4] == 'REAL':
        global globa
        realno.append(list1[0])
        if list1[2] == 1:
            globa.append(list1[0])
            reals.append(list1[0])
        print (reals,realno)
    
    
    elif list1[1] == 'ENDPROCEDURE' :
        global frp
        for ee in frp :
            data = 'push\t'+reg[vari[ee]]
            assem.append(data)
            prin(data)
            remove(ee,'')
        frp = []
        rclear()
        data = 'mov esp, ebp\npop dword ebp'
        assem.append(data)
        prin(data) 
        data = 'ret'
        assem.append(data)
        prin(data)
    
    
    elif list1[1] == 'PROCEDUREBEGIN' :
        rclear()
        data = list1[0]+':\t'
        assem.append(data)
        prin(data)
        data = 'push ebp\nmov ebp, esp'
        assem.append(data)
        #print('assem',assem)
        prin(data) 
    
    
    elif list1[1] == 'LABEL' :
        if list1[0] == 'MAIN' :
            data = list1[0].lower()+':\t'
            assem.append(data)
            prin(data) 
            data = 'push ebp\nmov ebp, esp'
            assem.append(data)
            prin(data) 
        else :
            data = list1[0]+':\t'
            assem.append(data)
            prin(data)
    
    
    elif list1[1] == 'JUMP' :
        data = 'jmp\t'+list1[0]
        assem.append(data)
        prin(data)
    
    
    elif list1[1] == 'BEGINPROCEDURECALL' :
        if list1[0] == 'printf' :
            global prime
            prime  = 1
    
    elif list1[1] == 'CALL' :
            data ='call\t'+list1[0]
            assem.append(data)
            prin(data)
    
    
    elif list1[1] == 'ACTUALVALUEPARAMETER' :
        data =list1[1]+'\t'+list1[0]
        assem.append(data)
        prin(data)
        
    
    elif list1[1] == 'ISUB' :
        finder(list1[0])
        isub(list1[2],list1[3])
        assign_value(list1[0])
        zzz = find1.findall(str(list1[2]))
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(list1[3])
        if zzz[0][2] != '' :
            remove(list1[3],'')
    
    
    elif list1[1] == 'IADD' :
        finder(list1[0])
        #print('inside iadd the list is',list1)
        iadd(list1[2],list1[3])
        #print('after calling iadd the list is',list1)
        assign_value(list1[0])
        #print('after calling assign value the list is',list1)
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        #print('list3',list1[3])
        zzz = find1.findall(str(list1[3]))
        if zzz[0][2] != '' :
            remove(list1[3],'')
    
    
    elif list1[1] == 'IMUL' :
        finder(list1[0])
        imul(list1[2],list1[3])
        assign_value(list1[0])
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(list1[3])
        if zzz[0][2] != '' :
            remove(list1[3],'')
    
    
    elif list1[1] == 'IMULT' :
        finder(list1[0])
        list1[2] = str(list1[2])
        list1[3] = str(list1[3])
        imul(list1[2],list1[3])
        #print('vari',vari)
        assign_value(list1[0])
        #print('list',list1)
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(list1[3])
        if zzz[0][2] != '' :
            remove(list1[3],'')
            
        
    elif list1[1] == 'SUBSTORE' :
        finder(list1[0])
        sub_assign(list1[0],list1[2],list1[3])
        zzz = find1.findall(str(list1[2]))
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(str(list1[3]))
        if zzz[0][2] != '' :
            remove(list1[3],'')
    
    
    elif list1[1] == 'SUBLOAD' :
        if list1[4] == 'INTEGER':
            #print('inside integer')
            finder(list1[0])
            sub_load(list1[2],list1[3])
            assign_value(list1[0])
            zzz = find1.findall(str(list1[2]))
            if zzz[0][2] != '' :
                #print('zzzzz',zzz[0][2][2])
                remove(list1[2],'')
            zzz = find1.findall(str(list1[3]))
            if zzz[0][2] != '' :
                if zzz[0][2][1] == '$' :
                    #print('zzzzz',zzz[0][2][1])
                    remove(list1[3],'')
                    
        if list1[4] == 'REAL':
            #print('real')
            finder(list1[0])
            global v1
            global v2
            global mixer
            if mixer == 'radd' :
                r_add(v1,v2,list1[0])
            elif mixer == 'rsub' :
                r_sub(v1,v2,list1[0])
            zzz = find1.findall(list1[2])
            if zzz[0][2] != '' :
                remove(list1[2],'')
            
            
            
    elif list1[1] == 'ILESSTHAN' :
        global jumphere
        jumphere = 'lessthan'
        compare(list1[2],list1[3])
            
            
            
    elif list1[1] == 'IGREATERTHAN' :
        global jumphere
        jumphere = 'greaterthan'
        compare(list1[2],list1[3])
            
            
            
    elif list1[1] == 'ILESSTHANEQUALS' :
        global jumphere
        jumphere = 'lessthanequal'
        compare(list1[2],list1[3])
            
            
            
    elif list1[1] == 'IGREATERTHANEQUALS' :
        global jumphere
        jumphere = 'greaterthanequal'
        compare(list1[2],list1[3])
            
            
            
    elif list1[1] == 'IEQUALS' :
        global jumphere
        jumphere = 'equal'
        compare(list1[2],list1[3])
            
            
            
    elif list1[1] == 'INOTEQUALS' :
        global jumphere
        jumphere = 'notequal'
        compare(list1[2],list1[3])
    
    
    elif list1[1] == 'CJUMP' :
        global jumphere
        if jumphere == 'lessthan' :
            data = 'jl\t'+list1[0]
            assem.append(data)
            prin(data)
        elif jumphere == 'greaterthan' :
            data = 'jg\t'+list1[0]
            assem.append(data)
            prin(data)
        elif jumphere == 'lessthanequal' :
            data = 'jle\t'+list1[0]
            assem.append(data)
            prin(data)
        elif jumphere == 'greaterthanequal' :
            data = 'jge\t'+list1[0]
            assem.append(data)
            prin(data)
        elif jumphere == 'equal' :
            data = 'je\t'+list1[0]
            assem.append(data)
            prin(data)
        elif jumphere == 'notequal' :
            data = 'jne\t'+list1[0]
            assem.append(data)
            prin(data)
            
            
            
    elif list1[1] == 'FORMALVALUEPARAMETER' :
        #print('inside formal')
        z = assign(list1[0],'0000')
        remove(list1[0],'')
        assign(list1[0],z)
        local.append(list1[0])
        data = 'pop\tdword '+z
        assem.append(data)
        prin(data)
            
            
            
    elif list1[1] == 'ACTUALVALUEPARAMETER' :
        actual_parameter(list1[2]) 
            
            
            
    elif list1[1] == 'ACTUALRPARAMETER' :
        frpc.append(list1[2])
        actual_parameter(list1[2])

            
                        
    elif list1[1] == 'BEGINFORMALPARAMETERLIST' :
        #assem.pop()
        1234              
            
    elif list1[1] == 'ENDACTUALPARAMETERLIST' :
        #data ='call\t'+list1[0]
        #assem.append(data)
        #prin(data)
        1111111
    elif list1[1] == 'FORMALREFERENCEPARAMETER' :
        zzz = find1.findall(str(list1[0]))
        if zzz[0][2] != '' :
            remove(list1[0],'')
        
        
        
    elif list1[1] == 'RADD' :
        finder(list1[0])
        global v1
        global v2
        global mixer
        mixer = 'radd'
        v1 = list1[2]
        v2 = list1[3]
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(list1[3])
        if zzz[0][2] != '' :
            remove(list1[3],'')
        
        
    elif list1[1] == 'RSUB' :
        finder(list1[0])
        global v1
        global v2
        global mixer
        mixer = 'rsub'
        v1 = list1[2]
        v2 = list1[3]
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        zzz = find1.findall(list1[3])
        if zzz[0][2] != '' :
            remove(list1[3],'')
        
        
    elif list1[1] == 'RSUBASSIGN' and list1[2][1] == '$' :
        finder(list1[0])
        global v1
        global v2
        global mixer
        if mixer == 'radd' :
            r_add(v1,v2,list1[0])
        elif mixer == 'rsub' :
            r_sub(v1,v2,list1[0])
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
        
        
    elif list1[1] == 'RSUBASSIGN' :
        finder(list1[0])
        if list1[0] in reals :
            data = list1[0]+':\t dd\t'+list1[2]
            data1.append(data)
            for eac in range(len(reals)) :
                if reals[eac] == list1[0] :
                    mm = eac
            reals.pop(mm)
        zzz = find1.findall(list1[2])
        if zzz[0][2] != '' :
            remove(list1[2],'')
            
    elif list1[1] == 'STORE' :
        #print(list1)
#        print('x',semantics2.chck(list1[0]))
#        x = semantics2.chck(str(list1[2]))
        #x = ''
        if list1[4] == 'REAL':
            list1[2] = str(list1[2])
            if list1[2][1] == '$':
                
                #print('real')
                finder(str(list1[0]))
                global v1
                global v2
                global mixer
                if mixer == 'radd' :
                    r_add(str(v1),str(v2),str(list1[0]))
                elif mixer == 'rsub' :
                    r_sub(str(v1),str(v2),str(list1[0]))
                zzz = find1.findall(str(list1[2]))
                if zzz[0][2] != '' :
                    remove(list1[2],'')
            else:
                finder(list1[0])
                if list1[0] in reals :
                    data = list1[0]+':\t dd\t'+list1[2]
                    data1.append(data)
                    for eac in range(len(reals)) :
                        if reals[eac] == list1[0] :
                            mm = eac
                    reals.pop(mm)
                zzz = find1.findall(list1[2])
                if zzz[0][2] != '' :
                    remove(list1[2],'')
                
        elif list1[4] == 'INTEGER':
            #print('list',list1)
            finder(list1[0])
            sub_assign(list1[0],list1[2],list1[3])
            zzz = find1.findall(str(list1[2]))
            if zzz[0][2] != '' :
                remove(list1[2],'')
    
    elif list1[1] == 'OUTPUTPARAMETER' :
        global prime
        if list1[2] != '" "' and prime == 1 :
            printdata(list1[2])
    
    
    elif list1[1] == 'ACTUALPRINTFSUBPARAMETER' :
        global prime
        
        if list1[2] != '" "' and prime == 1 :
            if list1[3] != '#':
                printdata_sub(list1[2],str(list1[3]))
            elif list1[3] == '#':
                printdata(list1[2])
    
    elif list1[1] == 'ENDPROCEDURECALL' :
        global prime
        prime = 0
