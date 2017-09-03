from django.shortcuts import render, redirect

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
            respuesta=Envio(cadena)       
        else:
            respuesta="ERROR"



       # cadena="[\n \"validar\":1500,\n \"login\":[\n \"comando\": \"SELECCIONAR * DE usuarios DONDE usuario == "+nombre+" && password == \""+contra+"\";\"\n]\n]"


          
        return HttpResponse(respuesta)

    else:
        return render(request, 'index.html')