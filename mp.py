import random
import os

def getP():
    with open('Lists/p.txt') as f:
        lines = f.read().splitlines()
    return lines
def getA():
    with open('Lists/a.txt') as f:
        lines = f.read().splitlines()
    return lines
def getO():
    with open('Lists/o.txt') as f:
        lines = f.read().splitlines()
    return lines
def getE():
    with open('Lists/e.txt') as f:
        lines = f.read().splitlines()
    return lines
def getC():
    with open('Lists/c.txt') as f:
        lines = f.read().splitlines()
    return lines

def randNo():
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                Cuantos numeros generar:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            >>>""")
    
    show = ''
    i=0
    while i < many:
        i += 1
        rando = random.randint(0,99)
        show = show + str(rando)

    
    
    return show
 
def rand3():
    
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            Cuantos pares de 3 generar:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            >>>""")
    j = 0
    showall ='' 
    while j < many:
        j+=1
        i=0
        show = ''
        while i < 3:
            i+=1
            rando = random.randint(0,99)
            show = show + str(rando) + '-'
        showall = showall + show + '||'

    
    
    return showall
 
def nameG():
    
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
       Adivina el numero!! Cuantos intentos?:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                >>> """)

    plines = getP()
    i = 0
    s = 0
    while i < many:
        i += 1
        rando = random.randint(0,99)
        print('|||||'+ str(plines[rando])+'|||||')
        ans = input('::::::')
        if (ans == rando):
            s +=1
            print('+1 = ' + str(rando))
        else:
            print('+0 = ' + str(rando))
    
    print('Total:'+str(many))
    print('Correct:'+str(s))
    print('%:'+str((s*100)/many))
    return "..."
 
def noG():
    
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        Adivina el nombre!! Cuantos intentos?:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                >>> """)

    plines = getP()
    i = 0
    s = 0
    while i < many:
        i += 1
        rando = random.randint(0,99)
        print('|||||  '+ str(rando)+'  |||||')
        ans = raw_input('::::::')
        if (ans == plines[rando]):
            s +=1
            print('+1 = ' + str(plines[rando]))
        else:
            print('+0 = ' + str(plines[rando]))
    
    print('Total:'+str(many))
    print('Correct:'+str(s))
    print('%:'+str((s*100)/many))
    return "..."
 
 
def eG():
    
    many = input("""\

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    Adivina el elemento!! Cuantos intentos?:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            >>>""")

    elines = getE()
    i = 0
    s = 0
    while i < many:
        i += 1
        rando = random.randint(0,99)
        print('|||||  '+ str(rando)+'  |||||')
        ans = raw_input('::::::')
        if (ans == elines[rando]):
            s +=1
            print('+1 = ' + str(elines[rando]))
        else:
            print('+0 = ' + str(elines[rando]))
    
    print('Total:'+str(many))
    print('Correct:'+str(s))
    print('%:'+str((s*100)/many))
    return "..."
def cG():
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    Adivina el nombre!! Cuantos intentos?:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            >>>""")

    clines = getC()
    plines = getP()
    i = 0
    s = 0
    while i < many:
        i += 1
        rando = random.randint(0,52)
        print('|||||  '+ str(clines[rando])+'  |||||')
        ans = raw_input('::::::')
        if (ans == plines[rando]):
            s +=1
            print('+1 = ' + str(clines[rando])+':'+str(rando)+':'+str(plines[rando])+'\n')
        else:
            print('+0 = ' + str(clines[rando])+':'+str(rando)+':'+str(plines[rando])+'\n')
    
    print('Total:'+str(many))
    print('Correct:'+str(s))
    print('%:'+str((s*100)/many))
    return "..."
 
def showL():
    
    print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    Lista CPAOE:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < 99:
        i += 1
        show = show +'['+ clines[i] +']\n   ' + str(i) + ' : ' + plines[i] + '\n   '+ str(i) + ' : ' + elines[i] + '     ' + alines[i] +' -> '+ olines[i] + ' \n\n'

    return show

def showPE():
    
    print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    Lista CPAOE:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::: """)
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < 99:
        i += 1
        show = show +'['+ elines[i] +']'+' : [' + plines[i] + ']['+str(i) + ']  \n   '

    return show
def showPC():
    
    print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    Lista CPAOE:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < 99:
        i += 1
        show = show +'['+ clines[i] +']'+' : [' + plines[i] + ']['+str(i) + ']  \n   '

    return show
    
def randL():
    
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            Cuantos elementos desea ver?:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                >>> """)
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < many:
        rando = random.randint(0,99)
        i += 1
        show = show +'['+ clines[rando] +']\n   ' + str(rando) + ' : ' + plines[rando] + '\n   '+ str(rando) + ' : ' + elines[rando] + '     ' + alines[rando] +' -> '+ olines[rando] + ' \n\n'

    return show
    
def randLM():
    
    many = input("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
             Cuantos ejemplos desea ver:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            >>> """)
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < many:
        rando = random.randint(0,99)
        rando2 = random.randint(0,99)
        rando3 = random.randint(0,99)
        i += 1
        show = show +'['+ clines[rando] +'] '+ '#: ' +str(rando)+'--'+str(rando2)+'--'+str(rando3)+'\n   ' + str(rando) + ' : ' + plines[rando] + '\n   '+ str(rando) + ' : ' + elines[rando] + '     ' +str(rando2) +' : ' + alines[rando2] +' -> ' +str(rando3) +' : ' + olines[rando3] + ' \n\n'

    return show
    
def seq():
    
    many = input("""\

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        Cuantos ejemplos desea crear:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
             >>> """)
    clines = getC()
    plines = getP()
    alines = getA()
    olines = getO()
    elines = getE()
    i = 0
    show = ''
    while i < many:
        p = input('P:') 
        a = input('A:') 
        o = input('O:')
        print('# : '+str(p)+'--'+str(a)+'--'+str(o)+'\n')
        print('# : '+plines[p]+'--'+alines[a]+'--'+ olines[o])
        print('\n')
    return show
    
def sexit():
    exit()
    return "Bye"
    
def sixnine():
    return """\
       _(((,|         ?    
      /  _-\ \      ?                 
     / C o\o  \   ?                  
   _/_    __\  \     
  /   \ \___/  )   
  |    |\_|\  /   
  |    |#  #|/          
  (   /     | 
   |  |#  # | 
   |  |    #|                      
   |  | #___n_,_                  
,-/   7-' .     `\                 
`-\...\-_   -  o /                 
   |#  # `---U--'                  
   `-v-^-'\/                       
     \  |_|_                 
     (_____"_"_"
        """
    
def whatmp(argument):
    switcher = {
        1: randNo,
        2: rand3,
        3: nameG,
        4: noG,
        5: eG,
        55: cG,
        6: showL,
        7: randL,
        8: randLM,
        9: seq,
        10: sexit,
        66: showPC,
        666: showPE,
        69: sixnine
    }
    func = switcher.get(argument, lambda: "Invalid")
    lala = func()
    print (lala)
    starter()


def starter():  
    argument = input("""\   
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 
1)Numeros Aleatorios     2)Numeros Aleatorios de 3 en 3 
             
3)# Guess            4)P Guess              5-55)E Guess   

 6-6-666)Show List            7)Show Random List 

 8)List Randon Random             9) Make Sequence
                                
                     10) Salir
                                                69)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::


""")
    whatmp(argument)

starter()
