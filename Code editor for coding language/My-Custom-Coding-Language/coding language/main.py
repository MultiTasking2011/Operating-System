import time
import turtle
import math
import random
import pygame
import re

#in case you don't realize, quiver is the name of the language, that means that everything including the print function is going to be inside quiver method

def read_file(filename):
    f = open(filename, "r")
    x = f.read()

    req_list = x.split("\n")
    req_list = [i for i in req_list if i != ""]
    return req_list
    
x = read_file("language.txt")

class fullcode:
    def __init__(self, code):
        self.code = code
        self.a = False
        self.b = False
        self.c = False
        self.d = False
        self.e = False
        self.f = False
        self.display_pattern = r'^display \.(.*?)\.'
        self.display_var_pattern = r'^display \|([^|]*)\|'
        self.display_list_pattern = r'^display \*([^|]*)\*'
        self.draw_forward = 0
        self.draw_left = 0
        self.draw_right = 0
        self.draw_square = 0
        self.draw_circle = 0
        self.draw_turn = 0
        self.draw_polygon = 0
        self.syntax_help = 0
        self.random_range = 0
        self.random_int = 0
        self.random_float = 0
        self.clock_tick = 0
        self.output_window = 0
        self.output_size = 0
        self.threedimension_square = 0
        self.loop_count = 0
        self.loop_infinite = 0
        self.loop_variable = 0
        self.function_define = r'^function:([^|]*):\*([^|]*)\* \~\>'
        self.function_call = r'[run]\:(.*?)\:\*(.*?)\*'
        self.define_variable = r'^var:(.*?): = (.*?):(.*?):'
        self.define_list = r'^list:(.*?): = ([^|]*)'
        self.list_append = r'^([^|]*)\|add\|\.(.*?)\.'
        self.list_remove = 0
        self.multiplication = 0
        self.addition = 0
        self.subtraction = 0
        self.division = 0
        self.exponentiation = 0
        self.string_conversion = 0
        self.ifstatement = 0
        self.ender = ':break:'
        self.break_turtle = 0
        self.liststorage = r'^(.*?):([^|]*):'
        self.listcalling = r'^(.*?)<([^|]*)>'

    def err(self):
        return "err"

    def importing(self):
        if "bring all from draw" in self.code:
            self.a = True
        if "bring all from quiver" in self.code:
            self.b = True
        if "bring all from rand" in self.code:
            self.c = True
        if "bring all from output" in self.code:
            self.d = True
        if "bring all from threedimensions" in self.code:
            self.e = True
        if "bring all from clock" in self.code:
            self.f = True
        if "bring all from math" in self.code:
            self.g = True

    def drawdot(self):
        if self.a:
            pass
        else:
            self.err()

    def quiver(self):
        self.importing()
        funcdisplaystore = list()
        store = list()
        varstore = dict() 
        funcvarstore = dict()
        funcliststore = list()
        funcliststorage = dict()
        liststore = list()
        liststorage = dict()
        parameterstore = dict()
        funccodestore = dict()

        if self.b:
            for i in self.code:
                # Display Pattern
                display = re.search(self.display_pattern, i)
                if display:
                    store.append(display.group(1))
                else:
                    self.err()

                # Variable
                variable = re.search(self.define_variable, i)
                if variable:
                    if variable.group(2) == "str":
                        varstore[variable.group(1)] = str(variable.group(3))
                    if variable.group(2) == "float":
                        varstore[variable.group(1)] = float(variable.group(3))
                    if variable.group(2) == "int":
                        varstore[variable.group(1)] = int(variable.group(3))
 
                # display variable
                display_variable = re.search(self.display_var_pattern, i)
                if display_variable:
                    store.append(varstore.get(display_variable.group(1)))

                #lists
                lists = re.search(self.define_list, i)
                if lists:
                    liststore.append(lists.group(2).split(', '))
                    listname = lists.group(1)
                    for item in liststore:
                        for a in item:
                            listchecker = re.search(self.liststorage, a)
                            itempos = int(item.index(a)+1)
                            dictkeyname = [listname+'_'+str(itempos)]
                            if listchecker:
                                if listchecker.group(1) == "str":
                                    liststorage[str(dictkeyname[0])] = str(listchecker.group(2))
                                if listchecker.group(1) == "float":
                                    liststorage[str(dictkeyname[0])] = float(listchecker.group(2))
                                if listchecker.group(1) == "int":
                                    liststorage[str(dictkeyname[0])] = int(listchecker.group(2)) 

                #display lists
                display_lists = re.search(self.display_list_pattern, i)
                if display_lists:
                    listcallingsyntax = display_lists.group(1)
                    listcall = re.search(self.listcalling, listcallingsyntax)
                    listnamecheck = listcall.group(1)
                    listindexcheck = listcall.group(2)
                    if listcall:
                        dictnamecheck = [listnamecheck+'_'+listindexcheck]
                        store.append(liststorage.get(str(dictnamecheck[0])))
                
                #functions
                functiontest = re.search(self.function_define, i)
                functioncallcheck = re.search(self.function_call, i)
                if functiontest:
                    if ',' in functiontest.group(2):
                        parameterstore[functiontest.group(1)] = list()
                        parameterstore[functiontest.group(1)].append(functiontest.group(2).split(', '))
                        for z in [j for j in parameterstore[functiontest.group(1)]]:
                            for a in z:
                                pass
                    
                
                    indexoffunction = self.code.index(f"function:{functiontest.group(1)}:*{functiontest.group(2)}* ~>")
                    funccodestore[functiontest.group(1)] = list()
                    funccodestore[functiontest.group(1)] = self.code[indexoffunction+1:self.code.index(self.ender)]
                    if functioncallcheck and functioncallcheck.group(1) == functiontest.group(1):
                        for codes in funccodestore[functiontest.group(1)]:
                            codes = codes.replace("-> ", "")
                            funcdisplay = re.search(self.display_pattern, codes)
                            if funcdisplay:
                                funcdisplaystore.append(funcdisplay.group(1))
                            else:
                                self.err()

                            # Variable
                            variablefunc = re.search(self.define_variable, codes)
                            if variablefunc:
                                if variablefunc.group(2) == "str":
                                    funcvarstore[variablefunc.group(1)] = str(variablefunc.group(3))
                                if variablefunc.group(2) == "float":
                                    funcvarstore[variablefunc.group(1)] = float(variablefunc.group(3))
                                if variablefunc.group(2) == "int":
                                    funcvarstore[variablefunc.group(1)] = int(variablefunc.group(3))

                            # display variable
                            display_variable_func = re.search(self.display_var_pattern, codes)
                            if display_variable_func:
                                funcdisplaystore.append(funcvarstore.get(display_variable_func.group(1)))

                            #lists
                            listsfunc = re.search(self.define_list, codes)
                            if listsfunc:
                                funcliststore.append(listsfunc.group(2).split(', '))
                                funclistname = listsfunc.group(1)
                                for everyitem in funcliststore:
                                    for afunc in everyitem:
                                        funclistchecker = re.search(self.liststorage, afunc)
                                        itemposition = int(everyitem.index(afunc)+1)
                                        funcdictkeyname = [funclistname+'_'+str(itemposition)]
                                        if funclistchecker:
                                            if funclistchecker.group(1) == "str":
                                                funcliststorage[str(funcdictkeyname[0])] = str(funclistchecker.group(2))
                                            if listchecker.group(1) == "float":
                                                funcliststorage[str(funcdictkeyname[0])] = float(funclistchecker.group(2))
                                            if listchecker.group(1) == "int":
                                                funcliststorage[str(funcdictkeyname[0])] = int(funclistchecker.group(2)) 

                            #display lists
                            display_lists_func = re.search(self.display_list_pattern, codes)
                            if display_lists_func:
                                funclistcallingsyntax = display_lists_func.group(1)
                                funclistcall = re.search(self.listcalling, funclistcallingsyntax)
                                funclistnamecheck = funclistcall.group(1)
                                funclistindexcheck = funclistcall.group(2)
                                if funclistcall:
                                    funcdictnamecheck = [funclistnamecheck+'_'+funclistindexcheck]
                                    funcdisplaystore.append(funcliststorage.get(str(funcdictnamecheck[0])))
                



            if functioncallcheck:
                return store, funcdisplaystore
            else:
                return store


    def rand(self):
        if self.c:
            pass
        else:
            self.err()

    def output(self):
        if self.d:
            pass
        else:
            self.err()

    def pthreedimension(self):
        if self.e:
            pass
        else:
            self.err()

    def clock(self):
        if self.f:
            pass
        else:
            self.err()
    
    def math(self):
        if self.g:
            pass
        else:
            self.err()
    
    def hehe(self):
        if self.b:
            pass
        else:
            self.err()
    
    def __str__(self) -> str:
        return "Do not print the class"

sourcecode = fullcode(x)
for i in sourcecode.quiver():
    for j in i:
        print(j)