'''
Created on Oct 17, 2012

@author: sugethk
'''
sym_tab = {}
def semantics_dict(key,val):
    global sym_tab
    sym_tab[key] = val
    print(sym_tab)