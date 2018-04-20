
class Automata:
    pila = ['#']
    tabla = [
        ['f:', 'a', 'b', '~'],
        [['p','#'], ['p','#a'], ['p','#b'], ['','']],
        [['p','a'], [['p','aa','ID2102'], ['q','~','ID2112']], ['p','ab'], ['','']],
        [['p','b'], ['p','ba'], [['p','bb','ID3202'], ['q','~','ID3212']], ['','']],
        [['q','#'], ['',''], ['',''], ['r','#']],
        [['q','a'], ['q','~'], ['',''], ['','']],
        [['q','b'], ['',''], ['q','~'], ['','']],
    ]
    estadoActual = 'p'

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop()
        for l in apilar:
            if l != '~' :
                self.pila.append(l)     

    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        i = 0
        restorePoint = []
        
        def createRestorePoint(i, pila, estado, usadas):
            restorePoint.append(
                {
                    'i' : i,
                    'pila' : pila,
                    'estado' : estado,
                    'usadas' : usadas
                }
            )
        #createRestorePoint(i=2, pila=['#','a','b'], estado='p', usadas=['ID3202'])

        noHayMasTransiciones = False
        while i < len(expresion) :            
            cont = cont + 1 
            if self.estadoActual == 'p':            
                for f in range(1, 4):
                    if self.tabla[f][0][1] == self.top() :
                        for c in range(1,3):
                            if self.tabla[0][c] == expresion[i]:
                                if type(self.tabla[f][c][0]) != list : 
                                    self.estadoActual = self.tabla[f][c][0]
                                    self.popPush(self.tabla[f][c][1])
                                    #print ('letra',expresion[i],'- estado',self.tabla[f][c][0],'- pila',self.pila)
                                    nTransiciones = nTransiciones + 1
                                else:
                                    print('letra',expresion[i],'- pos',i,'- newState',self.tabla[f][c][0])
                                    if restorePoint : 
                                        seEncontroNuevo = False
                                        for elem in self.tabla[f][c]:
                                            if elem[2] not in restorePoint[-1]['usadas']:
                                                print ('Ahora utilizare ',elem[2])
                                                restorePoint[-1]['usadas'].append(elem[2])
                                                self.estadoActual = elem[0]
                                                print('pila es ',self.pila)
                                                self.popPush(elem[1])
                                                nTransiciones = nTransiciones + 1
                                                seEncontroNuevo = True
                                                print('newState',self.estadoActual,'- apilo',elem[1])
                                                print('pila queda ',self.pila)
                                                break
                                                
                                        if not seEncontroNuevo :
                                            print('No hay mas estados')
                                            noHayMasTransiciones = True                                        
                                    else:
                                        print('se creara un punto para',self.tabla[f][c][0][2],'- pila',self.pila)
                                        createRestorePoint(i=i, pila=self.pila, estado=self.estadoActual, usadas=[self.tabla[f][c][0][2]])
                                        self.estadoActual = self.tabla[f][c][0][0]
                                        self.popPush(self.tabla[f][c][0][1])
                                        nTransiciones = nTransiciones + 1
                        #endfor              
                        if nTransiciones == cont : break
                            
            elif self.estadoActual == 'q':
                print('ahora estoy en ',self.estadoActual,'l',expresion[i],' - pila',self.pila)
                for f in range(4, 7):
                    if self.tabla[f][0][1] == self.top() :
                        for c in range(1,4):
                            if self.tabla[0][c] == expresion[i]:
                                print('entre papu f',f,'c',c,'l',expresion[i],self.tabla[0][c])
                                self.estadoActual = self.tabla[f][c][0]
                                self.popPush(self.tabla[f][c][1])
                                print ('letra',expresion[i],'- estado',self.tabla[f][c][0],'- pila',self.pila)
                                nTransiciones = nTransiciones + 1
                        if nTransiciones == cont: break

            
            if restorePoint and self.estadoActual == 'p' and not noHayMasTransiciones:
                self.estadoActual = restorePoint[-1]['estado']
                print('se restablecera la pila',restorePoint[-1]['pila'])
                self.pila = restorePoint[-1]['pila']
                i = int(restorePoint[-1]['i'])-1
                cont = restorePoint[-1]['i']
                nTransiciones = restorePoint[-1]['i']
                print('Se resteblecera el punto',restorePoint[-1])
                print('i=',i)
            

            i = i + 1
            if i < len(expresion) :print('Se volvera a leer la ',expresion[i],' en la pos',i)
            
        #endwhile
        if self.estadoActual == 'q' and self.top() == '#' and nTransiciones == len(expresion) :
            self.popPush('#')
            self.estadoActual = 'r'
        
        print('automata final: estado',self.estadoActual,'- pila',self.pila)

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
print(automata.validar("abba"))
"""
while True:
    expresion = input("Ingrese una expresion : ")
    if expresion != '' :
        print ('A continuacion evaluara la expresion "'+expresion+'"')
        print (automata.validar(expresion))
        print ('Pila resultante ',automata.pila)
    else:
        break
"""
"""
import expresiones
print ('A continuacion se evaluaran las expresiones aceptadas')
for e in expresiones.expresionesCorrectas :
    print ('La expresion',e,'es aceptada?',automata.validar(e))

print ('A continuacion se evaluaran las expresiones NO aceptadas')
for e in expresiones.expresionesIncorrectas :
    print ('La expresion',e,'es aceptada?',automata.validar(e))
"""

