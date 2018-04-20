
class Automata:
    pila = ['#']
    estados = { 
        'p': False, 
        'q': False, 
        'r': True
    }
    estadoActual = 'p'

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop(-1)
        for l in apilar:
            if l != '' :
                self.pila.append(l)      

    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        for w in expresion :
            cont = cont + 1
            if self.estadoActual == 'q':
                if w == 'b' and self.top() == 'b' :
                    self.popPush('')
                    nTransiciones =  nTransiciones + 1
                    print('b,b/', self.pila)
                elif w == 'a' and self.top() == 'a' :
                    self.popPush('')
                    nTransiciones =  nTransiciones + 1
                    print('a,a/', self.pila)
            elif self.estadoActual == 'p':
                if w == 'a' :
                    if self.top() == 'b' :
                        self.popPush('ba')
                        nTransiciones =  nTransiciones + 1
                        print('a,b/ba', self.pila)
                    elif self.top() == 'a' :
                        self.popPush('aa')
                        nTransiciones =  nTransiciones + 1
                        print('a,a/aa', self.pila)
                    elif self.top() == '#' :
                        self.popPush('#a')
                        nTransiciones =  nTransiciones + 1
                        print('a,#/#a', self.pila)
                elif w == 'b' :
                    if self.top() == 'b' :
                        self.popPush('bb')
                        nTransiciones =  nTransiciones + 1
                        print('b,b/bb', self.pila)
                    elif self.top() == 'a' :
                        self.popPush('ab')
                        nTransiciones =  nTransiciones + 1
                        print('b,a/ab', self.pila)
                    elif self.top() == '#' :
                        self.popPush('#b')
                        nTransiciones =  nTransiciones + 1
                        print('b,#/#b', self.pila)
                elif w == 'c' :
                    if self.top() == '#' :
                        self.popPush('#')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,#/#', self.pila)
                    elif self.top() == 'b' :
                        self.popPush('b')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,b/b', self.pila)
                    elif self.top() == 'a' :
                        self.popPush('a')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,a/a', self.pila)
            
            if nTransiciones != cont : break
        #endfor
        if self.estadoActual == 'q' and self.top() == '#' and nTransiciones == len(expresion) :
            self.popPush('#')
            self.estadoActual = 'r'
            print(',#/#', self.pila)

        if self.estadoActual == 'r' : 
            self.returnToInitialState()
            return True
        else:
            self.returnToInitialState()
            return False
    
    def returnToInitialState(self):
        self.estadoActual = 'p'
        self.pila = ['#']

automata = Automata()
while True:
    expresion = input("Ingrese una expresion : ")
    if expresion != '' :
        print ('A continuacion evaluara la expresion "'+expresion+'"')
        print (automata.validar(expresion))
        print ('Pila resultante ',automata.pila)
    else:
        break