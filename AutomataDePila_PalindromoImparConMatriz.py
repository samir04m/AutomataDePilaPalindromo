
class Automata:
    pila = ['#']
    tabla = [
        ['f:', 'a', 'b', 'c', '~'],
        [['p','#'], ['p','#a'], ['p','#b'], ['q','#'], ['','']],
        [['p','a'], ['p','aa'], ['p','ab'], ['q','a'], ['','']],
        [['p','b'], ['p','ba'], ['p','bb'], ['q','b'], ['','']],
        [['q','#'], ['',''], ['',''], ['',''], ['r','#']],
        [['q','a'], ['q','~'], ['',''], ['',''], ['','']],
        [['q','b'], ['',''], ['q','~'], ['',''], ['','']],
    ]
    estadoActual = 'p'

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop(-1)
        for l in apilar:
            if l != '~' :
                self.pila.append(l)      

    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        for w in expresion :
            cont = cont + 1
            if self.estadoActual == 'p':            
                for f in range(1, 4):
                    if self.tabla[f][0][1] == self.top() :
                        for c in range(1,4):
                            if self.tabla[0][c] == w:
                                self.estadoActual = self.tabla[f][c][0]
                                self.popPush(self.tabla[f][c][1])
                                #print ('letra',w,'- estado',self.tabla[f][c][0],'- pila',self.pila)
                                nTransiciones = nTransiciones + 1
                        if nTransiciones == cont: break
            elif self.estadoActual == 'q':
                for f in range(4, 7):
                    if self.tabla[f][0][1] == self.top() :
                        for c in range(1,5):
                            if self.tabla[0][c] == w:
                                self.estadoActual = self.tabla[f][c][0]
                                self.popPush(self.tabla[f][c][1])
                                #print ('letra',w,'- estado',self.tabla[f][c][0],'- pila',self.pila)
                                nTransiciones = nTransiciones + 1
                        if nTransiciones == cont: break
        #endfor
        if self.estadoActual == 'q' and self.top() == '#' and nTransiciones == len(expresion) :
            self.popPush('#')
            self.estadoActual = 'r'
            #print(',#/#', self.pila)

        if self.estadoActual == 'r' : 
            self.returnToInitialState()
            return True
        else:
            self.returnToInitialState()
            return False
     
    def returnToInitialState(self):
        self.estadoActual = 'p'
        self.pila = ['#']

    def getTabla(self):
        f = False
        for fila in self.tabla:
            for columna in fila:
                if not f : print (columna, end='\t\t')
                else : print (columna, end='\t')    
            print()
            f = True

automata = Automata()
import expresiones
print ('A continuacion se evaluaran las expresiones aceptadas')
for e in expresiones.expresionesCorrectas :
    print ('La expresion',e,'es aceptada?',automata.validar(e))

print ('A continuacion se evaluaran las expresiones NO aceptadas')
for e in expresiones.expresionesIncorrectas :
    print ('La expresion',e,'es aceptada?',automata.validar(e))

"""
white True:
    expresion = input("Ingrese una expresion : ")
    if expresion != '' :
        print ('A continuacion evaluara la expresion "'+expresion+'"')
        print (automata.validar(expresion))
        print ('Pila resultante ',automata.pila)
    else:
        break
"""
