
class Nodo():
    pass
    
class programa2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1   

class paquete(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        son1 = self.son1.imprimir()

        
        return son1   

class paquete2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        return son1   

class login(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        global respuesta
        son1 = self.son1.imprimir() 
        
        return son1   

class validar(Nodo):
    ''' validar : R_VALIDAR DOS_PUNTO ENTERO'''
    print "validar"

class logins1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       

    def imprimir(self):
       
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1 + ";"+ son2   

class logins2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1          

    def imprimir(self):
        son1 = self.son1.imprimir()
                
        return son1  

class datosl1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       

    def imprimir(self):
       
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
       
        
        return son1 + ","+ son2  



class datosl2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1          

    def imprimir(self):
        
        son1 = self.son1.imprimir()
      
        
        return son1  

class datol(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        
        return son1 + ":"+ son2
    

class validacionl1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1          

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        return son1  

class validacionl2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1  

class paquetes(Nodo):   
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1  

class tipopaquete1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class tipopaquete2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class tipopaquete3(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class usql1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class usql2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1    

class mensajear(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1  

class datosusql1(Nodo):
    '''datosusql : datosusql datousql'''
    print "datosusql1"

class datosusql2(Nodo):
    '''datosusql : datousql'''
    print "datosusql2"

class datousql(Nodo):
    '''datousql : ABRIR valorespaquete CERRAR'''
    print "datousql"

class valorespaquete1(Nodo):
    '''valorespaquete : valorespaquete valorpaquete '''
    print "valorespaquete1"

class valorespaquete2(Nodo):
    '''valorespaquete :  valorpaquete '''
    print "valorespaquete2"

class valorpaquete(Nodo):
    '''valorpaquete : CADENA  IPAQUETE   CADENA'''
    print "valorpaquete"

class reporte(Nodo):
    ''' reporte : R_REPORTE COMA R_DATOS DOS_PUNTO ABRIR  XML CERRAR'''
    print "reporte"

class paqueteerror(Nodo):
    '''paqueteerror : R_ERROR COMA R_TIPO_PAQUETE DOS_PUNTO tipoerror COMA R_MSG DOS_PUNTO CADENA COMA  R_DATOS DOS_PUNTO cuerpoerrorpack '''
    print "paqueteerror"

class cuerpoerrorpack(Nodo):
    ''' cuerpoerrorpack : ABRIR R_ERROR DOS_PUNTO R_LEXICO COMA R_ARCHIVO DOS_PUNTO CADENA COMA R_COL DOS_PUNTO ENTERO  COMA R_FILA DOS_PUNTO ENTERO  CERRAR '''
    print "cuerpoerrorpack"

class tipoerror1(Nodo):
    '''tipoerror : R_LEXICO '''
    print "tipoerror1"

class tipoerror2(Nodo):
    '''tipoerror : R_OTRO '''
    print "tipoerror2"

class cadena(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name   

class verdadero(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name    

class falso(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name   