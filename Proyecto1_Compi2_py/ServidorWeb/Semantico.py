
class Nodo():
    pass
    
class programa2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1   

class programa3(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1  


class seleccionar1(Nodo):
    def __init__(self,son1,son2, son3,son4,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        self.son3 = son3       
        self.son4 = son4       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        son3 = self.son3.imprimir()
        son4 = self.son4.imprimir()
        
        return "SELECCIONAR " +son1 +" DE "+son2+" "+ son3 +" "+ son4+";" 

class seleccionar2(Nodo):
    def __init__(self,son1,son2, son3,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        self.son3 = son3       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        son3 = self.son3.imprimir()
                
        return "SELECCIONAR " +son1 +" DE "+son2+" "+ son3 +";" 

class seleccionar3(Nodo):
    def __init__(self,son1,son2, son3,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        self.son3 = son3       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        son3 = self.son3.imprimir()
                
        return "SELECCIONAR " +son1 +" DE "+son2+" "+ son3 +";" 

class seleccionar4(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        
    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
                        
        return "SELECCIONAR " +son1 +" DE "+son2+";" 

class camposSelect1(Nodo):
    def __init__(self,name):
        self.name = name
                
    def imprimir(self):
                                        
        return "*"

class camposSelect2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       
        
    def imprimir(self):
        
        son1 = self.son1.imprimir()
                                
        return son1

class ordenamiento(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        
    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
                        
        return "ORDENAR_POR " +son1 +" "+son2+";" 

class modoorden1(Nodo):
    def __init__(self,name):
        self.name = name
                
    def imprimir(self):
                                        
        return "ASC"    
    
class modoorden2(Nodo):
    def __init__(self,name):
        self.name = name
                
    def imprimir(self):
                                        
        return "DESC" 

class campos1(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2       
        
    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
                        
        return son1 +","+son2 

class campos2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       
                
    def imprimir(self):
        
        son1 = self.son1.imprimir()
                        
        return son1 

class campo1(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       
                
    def imprimir(self):
        
        son1 = self.son1.imprimir()
                        
        return son1 

class campo2(Nodo):
    def __init__(self,name):
        self.name = name
                
    def imprimir(self):
        
        return "usuario" 

class condicionar(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        
        return "Donde"+ son1 

class logica(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        
        return son1 

class logor1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1 +"||"+son2

class logor2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return son1

class logand1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1 +"&&"+son2

class logand2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "!"+son1

class logand3(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return son1

class logand4(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "("+son1+")"

class relacional1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1+ " "+son2

class relacional2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return son1

class relacionalprima1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return "=="+son1+ " "+son2

class relacionalprima2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "=="+son1

class relacionalprima3(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return "!="+son1+ " "+son2

class relacionalprima4(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "!="+son1

class relacionalprima5(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return "<"+son1+ " "+son2

class relacionalprima6(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "<"+son1

class relacionalprima7(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return ">"+son1+ " "+son2

class relacionalprima8(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return ">"+son1

class relacionalprima9(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return "<="+son1+ " "+son2

class relacionalprima10(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "<="+son1

class relacionalprima11(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2 
                
    def imprimir(self):

        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return ">="+son1+ " "+son2

class relacionalprima12(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return ">="+son1

class subrelacional1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return +son1

class paquete(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        son1 = self.son1.imprimir()

        
        return son1 

class subrelacional2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1 
                        
    def imprimir(self):

        son1 = self.son1.imprimir()
                
        return "("+son1+")"  

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

class usql3(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2             

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1+" # "+son2

class usql4(Nodo):
    def __init__(self,son1,son2,son3, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2             
        self.son3 = son3             

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        son3 = self.son3.imprimir()
        
        return son1+" # "+son2+" # "+son3           

class mensajear(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class archivo(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1  

class archivos1(Nodo):
    def __init__(self,son1,son2,son3, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2
        self.son3 = son3

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        son3 = self.son3.imprimir()

        
        return son1 +"-.-"+son2+"\o/"+son3 

class archivos2(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2
        

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        

        
        return son1+"\o/"+son2 

class nombrar(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class archivoback(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class archivosxml1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1 +son2

class archivosxml2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()

        
        return son1 

class archivoxml(Nodo):
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

class html(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return "<html>"+son1 +son2+"</html>"

class cabeza1(Nodo):
    def __init__(self, name):
        self.name = name
        

    def imprimir(self):

        return "<head></head>"

class cabeza2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<head>"+son1 +"</head>"

class cuerpo(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<body>"+son1 +"</body>"

class parteshtml1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1 +son2

class parteshtml2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml3(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml4(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml5(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml6(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml7(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class partehtml8(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class encabezado1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h1>"+son1+"<\h1>"

class encabezado2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h2>"+son1+"<\h2>"

class encabezado3(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h3>"+son1+"<\h3>"

class encabezado4(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h4>"+son1+"<\h4>"

class encabezado5(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h5>"+son1+"<\h5>"

class encabezado6(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h6>"+son1+"<\h6>"

class encabezado7(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<h7>"+son1+"<\h7>"

class encabezado8(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1       

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return "<USQL>#" +son1+"#<\USQL>"

class listaIDS1(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        self.son2 = son2

    def imprimir(self):
        
        son1 = self.son1.imprimir()
        son2 = self.son2.imprimir()
        
        return son1+" "+son2

class listaIDS2(Nodo):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1       
        
    def imprimir(self):
        
        son1 = self.son1.imprimir()
        
        return son1

class cadena(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name   

class entero(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name   

class DECIMAL(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name   

class ID(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self):
        return self.name  

class XML(Nodo):
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