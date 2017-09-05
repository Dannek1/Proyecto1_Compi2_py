from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from django.http import HttpResponse
from django.http import HttpResponseRedirect

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
                return HttpResponseRedirect( 'index.html?respuesta='+respuesta)
        except:
            respuesta= "login fallido"
            
            return HttpResponseRedirect( 'index.html?respuesta='+respuesta)
        
    
    else:
        return render(request, 'index.html')

def mesa(request):
    return render(request, 'Mesa.html')

def salir(request):
    if(request.method=='GET'):
       
        nuewvorequest= HttpRequest()
        nuewvorequest.user = request.user
        nuewvorequest.method= 'GET'    
        
        return inicio(nuewvorequest)
    else:
        return render(request, 'Mesa.html')
    
