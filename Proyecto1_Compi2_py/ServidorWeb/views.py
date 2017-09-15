from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import os
import zipfile

from . import Datos

import Sintactico
import ply.lex





def index(request):
    return render(request, 'index.html')    

def Envio(cadena):

    transport = TSocket.TSocket('localhost', 8080)
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Datos.Client(protocol)

    transport.open()

    
    
    respuesta=client.Paquete(cadena)
    
    transport.close()

    return respuesta


    
def inicio(request):
    if(request.method=='POST'):
        nombre = request.POST['txtNombre']
        contra = request.POST['txtContra']

        
        
        cadena= "SELECCIONAR * DE usuarios DONDE usuario == "+nombre+" && password == \""+contra+"\";"
        
        analisis=Sintactico.analizar(cadena)
        
        if analisis!="ERROR":
            cadena="[\n \"validar\":1500,\n \"login\":[\n \"comando\": \"" + cadena+"\"\n]\n]" 

            recibo=Envio(cadena)       

            paquete = Sintactico.analizar(recibo)

            if paquete!="ERROR":
                respuesta=paquete
            else:
                respuesta="ERROR"
        
        else:
            respuesta="ERROR"
        
        try:
            valores = respuesta.split(";")
        
            if valores[1]=="true":
                respuesta="Login Exitoso" 
                documentos = str(valores[0]).split(",")
                user =str(documentos[0]).split(":")
                name =str(documentos[1]).split(":")
           
                
                return HttpResponseRedirect('Mesa.html?usuario='+user[1]+'&nombre='+name[1])
                #return mesa(request)
                #return HttpResponseRedirect('Mesa')
                 
                 
            else:
                respuesta= "login fallido"
                return render(request, 'index.html')
        except:
            respuesta= "login fallido"
            
            return render(request, 'index.html')
        
    
    else:
         
        cadena="[\n \"paquete\" : \"fin\" \n]"                 
        Envio(cadena)
        return render(request, 'index.html')

def mesa(request):
    return render(request, 'Mesa.html')


def ejec(request):
    if(request.method=='POST'):
       entrada = request.POST['entrada']
       analisis=Sintactico.analizar(entrada)

       if analisis!="ERROR":
          entrada="[\n \"paquete\" : \"usql\" ,\n \"instruccion\": \"" + entrada+"\",\n]" 
          recibo=Envio(entrada)
          paquete = Sintactico.analizar(recibo)

          if paquete!="ERROR":
                try:
                    Crear_carpeta()
                    back=paquete.split("#")
                    if back[0]=='"Backup General" ':
                        print "hola"
                        ruta="C:\\Archivos-Base\\"+back[2][2:-1]+".zip"
                        comprimdio=zipfile.ZipFile(ruta,'w')

                        archivos=str(back[1]).split("-.-")
                        
                        for x in range(len(archivos)):
                            archivo=str(archivos[x]).split("\o/")
                            subruta="C:\\Archivos-Base\\"+archivo[0][2:-1]+".usac"
                            f = open (subruta,'w')
                            f.write(archivo[1])
                            f.close()
                            comprimdio.write(subruta, compress_type=zipfile.ZIP_DEFLATED)
                            os.remove(subruta)
                            print x    

                        comprimdio.close() 

                    else:
                        print "Hola"
                        ruta="C:\\Archivos-Base\\"+back[1][2:-1]+".udmp"
                        f = open (ruta,'w')
                        f.write(back[0])
                        f.close()
                    
                    respuesta=back[0];
                except:
                    respuesta=paquete
          else:
                respuesta="ERROR"  


       else:
          respuesta="ERROR"   

       return HttpResponseRedirect( 'Mesa.html?respuesta='+respuesta)
        
    else: 
       
       return render(request, 'Mesa.html')
    
def Crear_carpeta():
    try:
        os.makedirs("C:\Archivos-Base")
    except:
        pass

def reporte(request):
    return render(request, 'Reportes.html')