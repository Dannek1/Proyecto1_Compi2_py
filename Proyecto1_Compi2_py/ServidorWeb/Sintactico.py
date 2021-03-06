import ply.yacc as yacc

from Analizador import tokens
from Semantico import *


precendia = (
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV'),
    ('right','POW'),
    ('nonassoc','IGUAL','DISTINTO','MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL'),
    ('left','OR'),
    ('left','AND'),
    ('left','NOT'),
    ('nonassoc','PAR_IZ','PAR_DER'),
    )

def p_programa1(p):
    '''programa : inicio'''
    print "programa1"

def p_programa2(p):
    '''programa : ABRIR paquete CERRAR'''
    p[0]=programa2(p[2],"programa")
    print "programa2"

def p_programa3(p):
    '''programa : R_AHTML html R_CHTML'''
    p[0]=programa3(p[2],"programa")
    print "programa2"

#primer analizador (SQL)
def p_inicio(p):
    '''inicio : sentencias'''
    print "inicio"

#Se debe de hacer un "metodo " por cada opcion de la produccion
# sentencias := sentencias sentencia
#             | sentencia   

def p_sentencias1(p):
    '''sentencias : sentencias sentencia'''
    print "sentencias1"

def p_sentencias2(p):
    '''sentencias : sentencia'''
    print "sentencias2"

def p_sentencia1(p):
    '''sentencia : usar'''
    print "sentencia1"

def p_sentencia2(p):
    '''sentencia : crear'''
    print "sentencia2"

def p_sentencia3(p):
    '''sentencia : imprimir'''
    print "sentencias3"

def p_sentencia4(p):
    '''sentencia : insertar'''
    print "sentencias4"

def p_sentencia5(p):
    '''sentencia : actualizar'''
    print "sentencias5"

def p_sentencia6(p):
    '''sentencia : borrar'''
    print "sentencias6"

def p_sentencia7(p):
    '''sentencia : seleccionar'''
    print "sentencias7"

def p_sentencia8(p):
    '''sentencia : otorgar'''
    print "sentencias8"

def p_sentencia9(p):
    '''sentencia : denegar'''
    print "sentencias9"

def p_sentencia10(p):
    '''sentencia : back'''
    print "sentencias10"

def p_sentencia11(p):
    '''sentencia : restaurar'''
    print "sentencia11"

def p_sentencia12(p):
    '''sentencia : alterar'''
    print "sentencia12"

def p_sentencia13(p):
    '''sentencia : eliminar'''
    print "sentencia13"

def p_sentencia14(p):
    '''sentencia : declarar'''
    print "sentencia14"

def p_sentencia15(p):
    '''sentencia : contar'''
    print "sentencia15"

def p_sentencia16(p):
    '''sentencia : procedimiento'''
    print "sentencia16"

def p_usar(p):
    '''usar : R_USAR ID PUNTO_COMA'''
    print "usar"

def p_crear(p):
    '''crear : R_CREAR opcionescrear'''
    print "crear"

def p_opcionescrear1(p):
    '''opcionescrear : crearbase'''
    print "opcionescrear1"

def p_opcionescrear2(p):
    '''opcionescrear : creartabla'''
    print "opcionescrear2"

def p_opcionescrear3(p):
    '''opcionescrear : crearobjeto'''
    print "opcionescrear3"

def p_opcionescrear4(p):
    '''opcionescrear : crearpro'''
    print "opcionescrear4"

def p_opcionescrear5(p):
    '''opcionescrear : crearfun'''
    print "opcionescrear5"

def p_opcionescrear6(p):
    '''opcionescrear : crearusuario'''
    print "opcionescrear6"

def p_crearbase(p):
    ''' crearbase : R_BASE ID PUNTO_COMA'''
    print "crear base"

def p_creartabla(p):
    '''creartabla : R_TABLA ID PAR_IZ campostabla PAR_DER PUNTO_COMA'''
    print "creartabla"

def p_campostabla1(p):
    '''campostabla : campostabla COMA campotabla'''
    print "campostabla1"

def p_campostabla2(p):
    '''campostabla : campotabla'''
    print "campostabla2"

def p_campotabla1(p):
    ''' campotabla : tipodato ID complemento'''
    print "campotabla1"

def p_campotabla2(p):
    ''' campotabla : tipodato ID'''
    print "campotabla2"

def p_complemento1(p):
    '''complemento : R_NO R_NULO'''
    print "complemento1"

def p_complemento2(p):
    '''complemento : R_NULO'''
    print "complemento2"

def p_complemento3(p):
    '''complemento : R_AUTOINCREMENTABLE'''
    print "complemento3"

def p_complemento4(p):
    '''complemento : R_PK'''
    print "complemento4"

def p_complemento5(p):
    '''complemento : R_FK ID'''
    print "complemento5"

def p_complemento6(p):
    '''complemento : R_UNICO'''
    print "complemento6"

def p_crearobjeto1(p):
    '''crearobjeto : R_OBJETO ID PAR_IZ parametros PAR_DER PUNTO_COMA'''
    print "crearobjeto"

def p_crearobjeto2(p):
    '''crearobjeto : R_OBJETO ID PAR_IZ PAR_DER PUNTO_COMA'''
    print "crearobjeto"

def p_parametros1(p):
    '''parametros : parametros COMA parametro'''
    print "parametros"

def p_parametros2(p):
    '''parametros : parametro'''
    print "parametros2"

def p_parametro(p):
    '''parametro : tipodato ID'''
    print "parametro"

def p_crearpro1(p):
    '''crearpro : R_PROCEDIMIENTO ID PAR_IZ parametros PAR_DER COR_IZ subsentencias COR_Der'''
    print "crearpro1"

def p_crearpro2(p):
    '''crearpro : R_PROCEDIMIENTO ID PAR_IZ PAR_DER COR_IZ subsentencias COR_Der'''
    print "crearpro2"

def p_subsentencias1(p):
    '''subsentencias : subsentencias subsentencia'''
    print "subsentencias1"

def p_subsentencias2(p):
    '''subsentencias : subsentencia'''
    print "subsentencias2"

def p_subsentencia1(p):
    '''subsentencia : asignacion'''
    print "subsentencia1"

def p_subsentencia2(p):
    ''' subsentencia : if'''
    print "subsentencia2"

def p_subsentencia3(p):
    ''' subsentencia : switch'''
    print "subsentencia3"

def p_subsentencia4(p):
    ''' subsentencia : for'''
    print "subsentencia4"

def p_subsentencia5(p):
    '''subsentencia : while'''
    print "subsentencia5"

def p_subsentencia6(p):
    '''subsentencia : fecha'''
    print "subsentencia6"

def p_subsentencia7(p):
    '''subsentencia : fecha_hora'''
    print "subsentencia7"

def p_subsentencia8(p):
    '''subsentencia : sentencia'''
    print "subsentencia8"

def p_crearfun1(p):
    '''crearfun : R_FUNCION ID PAR_IZ parametros PAR_DER tipodato COR_IZ sentencias_retorno COR_Der'''
    print "crearfun1"

def p_crearfun2(p):
    '''crearfun : R_FUNCION ID PAR_IZ PAR_DER tipodato COR_IZ sentencias_retorno COR_Der'''
    print "crearfun2"

def p_sentencias_retorno(p):
    '''sentencias_retorno : subsentencias retorno'''
    print "sentencias_retorno"

def p_retorno(p):
    '''retorno : R_RETORNO aritmetica PUNTO_COMA'''
    print "retorno"

def p_crearusuario(p):
    '''crearusuario : R_USUARIO ID R_COLOCAR R_PAS I_ASIG expresion PUNTO_COMA'''
    print "Crearususario"

def p_imprimir(p):
    '''imprimir : R_IMPRIMIR PAR_IZ expresion PAR_DER PUNTO_COMA'''
    print "imprimir"

def p_insertar(p):
    '''insertar : R_INSERTAR R_EN R_TABLA ID PAR_IZ tipoins'''
    print "insertar"

def p_tipoins1(p):
    '''tipoins : campos PAR_DER R_VALORES PAR_IZ valor PAR_DER PUNTO_COMA'''
    print "tipoins1"

def p_tipoins2(p):
    '''tipoins : valor PAR_DER PUNTO_COMA'''
    print "tipoins2"

def p_campos1(p):
    '''campos : campos COMA campo'''
    p[0]=campos1(p[1],p[3],"campos1")
    print "campos1"

def p_campos2(p):
    '''campos : campo'''
    p[0]=campos2(p[1],"campos2")
    print "campos2"

def p_campo1(p):
    '''campo : ID'''
    p[0]=campo1(ID(p[1]),"campo1")
    print "campo1"

def p_campo2(p):
    '''campo : R_USUARIO'''
    p[0]=campo2("campo2")
    print "campo2"

def p_valor1(p):
    '''valor : valor COMA aritmetica'''
    print "valor1"

def p_valor2(p):
    '''valor : aritmetica'''
    print "valor2"

def p_actualizar1(p):
    '''actualizar : R_ACTUALIZAR R_TABLA ID PAR_IZ campos PAR_DER R_VALORES PAR_IZ valor PAR_DER condicionar PUNTO_COMA'''
    print "actualizar1"

def p_actualizar2(p):
    '''actualizar : R_ACTUALIZAR R_TABLA ID PAR_IZ campos PAR_DER R_VALORES PAR_IZ valor PAR_DER PUNTO_COMA'''
    print "actualizar2"

def p_condicionar(p):
    '''condicionar : R_DONDE logica'''
    p[0]=condicionar(p[2],"condicionar")
    print "condicionar"

def p_borrar(p):
    '''borrar : R_BORRAR R_EN R_TABLA ID condicionar PUNTO_COMA'''
    print "borrar"

def p_seleccionar1(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID condicionar ordenamiento PUNTO_COMA'''
    p[0]=seleccionar1(p[2],ID(p[4]),p[5],p[6],"seleccionar1")
    print "seleccionar1"

def p_seleccionar2(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID condicionar PUNTO_COMA'''
    p[0]=seleccionar2(p[2],ID(p[4]),p[5],"seleccionar1")
    print "seleccionar2"

def p_seleccionar3(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID  ordenamiento PUNTO_COMA'''
    p[0]=seleccionar3(p[2],ID(p[4]),p[5],"seleccionar1")
    print "seleccionar3"

def p_seleccionar4(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID  PUNTO_COMA'''
    p[0]=seleccionar3(p[2],ID(p[4]),"seleccionar1")
    print "seleccionar4"

def p_camposSelect1(p):
    '''camposSelect : MULTI'''
    p[0]=camposSelect1("camposSelect1")
    print "camposSelect1"

def p_camposSelect2(p):
    '''camposSelect : campos'''
    p[0]=camposSelect2(p[1],"camposSelect2")
    print "camposSelect2"

def p_ordenamiento(p):
    '''ordenamiento : R_ORDENAR ID modoorden'''
    p[0]=ordenamiento(ID(p[2]),p[3],"ordenamiento")
    print "ordenamiento"

def p_modoorden1(p):
    '''modoorden : R_ASC'''
    p[0]=modoorden1("ASC")
    print "modoorden1"

def p_modoorden2(p):
    '''modoorden : R_DESC'''
    p[0]=modoorden2("DESC")
    print "modoorden2"

def p_otorgar(P):
    '''otorgar : R_OTORGAR R_PERMISOS ID COMA ID PUNTO objeto PUNTO_COMA'''
    print "otorgar"

def p_objeto1(p):
    '''objeto : MULTI'''
    print "objeto1"

def p_objeto2(p):
    '''objeto : ID'''
    print "objeto2"

def p_denegar(p):
    '''denegar : R_DENEGAR R_PERMISOS ID COMA ID PUNTO objeto PUNTO_COMA'''
    print "denegar"

def p_back(p):
    '''back : R_BACKUP tipoback ID ID PUNTO_COMA'''
    print "backup"

def p_tipoback1(p):
    '''tipoback : R_USQLDUMP '''
    print "tipoback1"
 
def p_tipoback2(p):
    '''tipoback : R_COMPLETO '''
    print "tipoback2"   

def p_restaurar(p):
    '''restaurar : R_RESTAURAR tipoback aritmetica PUNTO_COMA'''
    print "restaurar"

def p_alterar(p):
    '''alterar : R_ALTERAR alterado'''
    print "alterar"

def p_alterado1(p):
    '''alterado : R_TABLA ID accionalterartabla PUNTO_COMA'''
    print "alterado1"

def p_alterado2(p):
    '''alterado : R_OBJETO ID accionalterarobjeto PUNTO_COMA'''
    print "alterado2"

def p_alterado3(p):
    '''alterado : R_USUARIO ID R_CAMBIAR R_PAS I_ASIG expresion PUNTO_COMA'''
    print "alterado3"

def p_accionalterartabla1(p):
    '''accionalterartabla : R_AGREGAR PAR_IZ campostabla PAR_DER'''
    print "accionalterartabla1"

def p_accionalterartabla2(p):
    '''accionalterartabla : R_QUITAR campos'''
    print "accionalterartabla2"

def p_accionalterarobjeto1(p):
    '''accionalterarobjeto : R_AGREGAR PAR_IZ parametros PAR_DER'''
    print "accionalterarobjeto"

def p_accionalterarobjeto2(p):
    '''accionalterarobjeto : R_QUITAR campos'''
    print "accionalterarobjeto2"

def p_eliminar1(p):
    '''eliminar : R_ELIMINAR R_TABLA ID PUNTO_COMA'''
    print "eliminar1"

def p_eliminar2(p):
    '''eliminar : R_ELIMINAR R_BASE ID PUNTO_COMA'''
    print "eliminar2"

def p_eliminar3(p):
    '''eliminar : R_ELIMINAR R_OBJETO ID PUNTO_COMA'''
    print "eliminar3"

def p_eliminar4(p):
    '''eliminar : R_ELIMINAR R_USUARIO ID PUNTO_COMA'''
    print "eliminar"

def p_declarar1(p):
    '''declarar : R_DECLARAR listavar tipodato I_ASIG asigdecl PUNTO_COMA'''
    print"declarar1"

def p_declarar2(p):
    '''declarar : R_DECLARAR listavar tipodato PUNTO_COMA'''
    print"declarar2"

def p_listavar1(p):
    '''listavar : listavar COMA ID'''
    print "listavar1"

def p_listavar2(p):
    '''listavar : ID'''
    print "listavar2"

def p_asigdecl1(p):
    '''asigdecl : aritmetica PAR_IZ valor PAR_DER'''
    print "asigdecl1"

def p_asigdecl2(p):
    '''asigdecl : aritmetica '''
    print "asigdecl2"

def p_asignacion(p):
    '''asignacion : ID I_ASIG aritmetica PUNTO_COMA'''
    print "asignacion"
 
def p_if1(p):
    '''if : R_SI PAR_IZ logica PAR_DER COR_IZ subsentencias COR_Der sinoelse'''
    print "if1"

def p_if2(p):
    '''if : R_SI PAR_IZ logica PAR_DER COR_IZ subsentencias COR_Der '''
    print "if2"

def p_sinoelse(p):
    '''sinoelse : R_SINO COR_IZ subsentencias COR_Der'''
    print "sinoelse "

def p_switch1(p):
    '''switch : R_SELECCIONA PAR_IZ aritmetica PAR_DER COR_IZ casos defecto COR_Der'''
    print "switch1"

def p_switch2(p):
    '''switch : R_SELECCIONA PAR_IZ aritmetica PAR_DER COR_IZ casos COR_Der'''
    print "switch2"

def p_casos1(p):
    '''casos : casos caso'''
    print "casos1"

def p_casos2(p):
    '''casos : caso'''
    print "casos2"

def p_caso(p):
    '''caso : R_CASO expresion DOS_PUNTO sentenciasswitch '''
    print "caso"

def p_sentenciasswitch1(p):
    '''sentenciasswitch :  subsentencia sentenciasswitch'''
    print "sentenciasswitch1" 

def p_sentenciasswitch2(p):
    '''sentenciasswitch :  subsentencia '''
    print "sentenciasswitch2"

def p_sentenciasswitch3(p):
    '''sentenciasswitch :  R_DETENER  PUNTO_COMA'''
    print "sentenciasswitch2"

def p_defecto(p):
    '''defecto : R_DEFECTO DOS_PUNTO sentenciasswitch'''
    print "defecto"

def p_for(p):
    '''for : R_PARA PAR_IZ declaracionfor PUNTO_COMA logica PUNTO_COMA operadorfor PAR_DER COR_IZ sentenciasswitch COR_Der'''
    print "for"

def p_declaracionfor(p):
    '''declaracionfor : R_DECLARAR ID R_INTEGER I_ASIG aritmetica'''
    print "declaracionfor"

def p_operadorfor1(p):
    '''operadorfor : INCR'''
    print "operadorfor1"

def p_operadorfor2(p):
    '''operadorfor : DECR'''
    print "operadorfor2"

def p_while(p):
    '''while : R_MIENTRAS PAR_IZ logica PAR_DER COR_IZ sentenciasswitch COR_Der'''
    print "while"

def p_fecha(p):
    '''fecha : ID I_ASIG R_FECHA PAR_IZ  PAR_DER PUNTO_COMA'''
    print "fecha"

def p_fecha_hora(p):
    '''fecha_hora : ID I_ASIG R_FECHA_HORA PAR_IZ  PAR_DER PUNTO_COMA'''
    print "fecha_hora"

def p_contar(p):
    '''contar : R_CONTAR PAR_IZ MENOR MENOR seleccionar MAYOR MAYOR PAR_DER PUNTO_COMA'''
    print "contar"  

def p_tipodato1(p):
    '''tipodato : R_TEXT'''
    print "tipodato1"

def p_tipodato2(p):
    '''tipodato : R_INTEGER '''
    print "tipodato2"

def p_tipodato3(p):
    '''tipodato : R_DOUBLE '''
    print "tipodato3"

def p_tipodato4(p):
    '''tipodato : R_BOOL '''
    print "tipodato4"

def p_tipodato5(p):
    '''tipodato : R_DATE'''
    print "tipodato5"

def p_tipodato6(p):
    '''tipodato : R_DATETIME'''
    print "tipodato6"

def p_logica(p):
    '''logica : logor'''
    p[0]=logica(p[1],"logica")
    print "logica"

def p_logor1(p):
    '''logor : logand OR logand'''
    p[0]=logor1(p[1],p[3],"logor1")
    print "logor1"

def p_logor2(p):
    '''logor : logand'''
    p[0]=logor2(p[1],"logor2")
    print "logor2"

def p_logand1(p):
    '''logand : relacional AND logica'''
    p[0]=logand1(p[1],p[3],"logand1")
    print "logand1"

def p_logand2(p):
    '''logand : NOT relacional '''
    p[0]=logand2(p[2],"logand2")
    print "logand2"

def p_logand3(p):
    '''logand : relacional '''
    p[0]=logand3(p[1],"logand2")
    print "logand3"

def p_logand4(p):
    '''logand : PAR_IZ logica  PAR_DER '''
    p[0]=logand4(p[1],"logand2")
    print "logand4"

def p_relacional1(p):
    '''relacional : subrelacional relacionalprima'''
    p[0]=relacional1(p[1],p[2],"relacional1")
    print "relacional1"

def p_relacional2(p):
    '''relacional : subrelacional '''
    p[0]=relacional2(p[1],"relacional2")
    print "relacional2"

def p_relacionalprima1(p):
    '''relacionalprima : IGUAL  subrelacional relacionalprima'''
    p[0]=relacionalprima1(p[2],p[3],"relacionalprima1")
    print "relacionalprima1"

def p_relacionalprima2(p):
    '''relacionalprima : IGUAL  subrelacional'''
    p[0]=relacionalprima2(p[2],"relacionalprima2")
    print "relacionalprima2"

def p_relacionalprima3(p):
    '''relacionalprima : DISTINTO  subrelacional relacionalprima'''
    p[0]=relacionalprima3(p[2],p[3],"relacionalprima1")
    print "relacionalprima3"

def p_relacionalprima4(p):
    '''relacionalprima : DISTINTO  subrelacional'''
    p[0]=relacionalprima4(p[2],"relacionalprima2")
    print "relacionalprima4"

def p_relacionalprima5(p):
    '''relacionalprima : MENOR  subrelacional relacionalprima'''
    p[0]=relacionalprima5(p[2],p[3],"relacionalprima1")
    print "relacionalprima5"

def p_relacionalprima6(p):
    '''relacionalprima : MENOR  subrelacional'''
    p[0]=relacionalprima6(p[2],"relacionalprima2")
    print "relacionalprima6"

def p_relacionalprima7(p):
    '''relacionalprima : MAYOR  subrelacional relacionalprima'''
    p[0]=relacionalprima7(p[2],p[3],"relacionalprima1")
    print "relacionalprima7"

def p_relacionalprima8(p):
    '''relacionalprima : MAYOR  subrelacional'''
    p[0]=relacionalprima8(p[2],"relacionalprima2")
    print "relacionalprima8"

def p_relacionalprima9(p):
    '''relacionalprima : MENOR_IGUAL  subrelacional relacionalprima'''
    p[0]=relacionalprima9(p[2],p[3],"relacionalprima1")
    print "relacionalprima9"

def p_relacionalprima10(p):
    '''relacionalprima : MENOR_IGUAL  subrelacional'''
    p[0]=relacionalprima10(p[2],"relacionalprima2")
    print "relacionalprima10"

def p_relacionalprima11(p):
    '''relacionalprima : MAYOR_IGUAL  subrelacional relacionalprima'''
    p[0]=relacionalprima11(p[2],p[3],"relacionalprima1")
    print "relacionalprima9"

def p_relacionalprima12(p):
    '''relacionalprima : MAYOR_IGUAL  subrelacional'''
    p[0]=relacionalprima12(p[2],"relacionalprima2")
    print "relacionalprima10"

def p_subrelacional1(p):
    '''subrelacional : aritmetica'''
    p[0]=subrelacional1(p[1],"subrelacional1")
    print "subrelacional1"

def p_subrelacional2(p):
    '''subrelacional : PAR_IZ relacional  PAR_DER'''
    p[0]=subrelacional2(p[2],"subrelacional2")
    print "subrelacional2"

def p_aritmetica1(p):
    '''aritmetica : multidiv SUMA aritmetica'''
    print "aritmetica1"

def p_aritmetica2(p):
    '''aritmetica : multidiv RESTA aritmetica'''
    print "aritmetica2"

def p_aritmetica3(p):
    '''aritmetica : multidiv '''
    print "aritmetica3"

def p_multidiv1(p):
    '''multidiv : potenciar MULTI  multidiv '''
    print "multidiv1"

def p_multidiv2(p):
    '''multidiv : potenciar DIV  multidiv '''
    print "multidiv2"

def p_multidiv3(p):
    '''multidiv : potenciar'''
    print "multidiv3"

def p_potenciar1(p):
    '''potenciar : unario POW potenciar'''
    print "potenciar1"

def p_potenciar2(p):
    '''potenciar : unario'''
    print "potenciar2"

def p_unario1(p):
    ''' unario : RESTA expresion'''
    print "unario1"

def p_unario2(p):
    ''' unario : expresion'''
    print "unario2"

def p_unario3(p):
    ''' unario : PAR_IZ aritmetica  PAR_DER'''
    print "unario3"

def p_expresion1(p):
    '''expresion : ID'''
    print "expresion1"

def p_expresion2(p):
    '''expresion : ENTERO'''
    print "expresion2"

def p_expresion3(p):
    '''expresion : DECIMAL'''
    print "expresion3"

def p_expresion4(p):
    '''expresion : CADENA'''
    print "expresion4"

def p_expresion5(p):
    '''expresion : FECHA'''
    print "expresion5"

def p_expresion6(p):
    '''expresion : FECHA_HORA'''
    print "expresion6"

def p_expresion7(p):
    '''expresion : BOOLEAN'''
    print "expresion7"

def p_expresion8(p):
    '''expresion : R_USUARIO'''
    print "expresion8"

def p_expresion9(p):
    '''expresion : R_PAS'''
    print "expresion9"

def p_procedimiento1(p):
    '''procedimiento : ID PAR_IZ parametrosejec PAR_DER PUNTO_COMA'''
    print "procedimiento1"

def p_procedimiento2(p):
    '''procedimiento : ID PAR_IZ  PAR_DER PUNTO_COMA'''
    print "procedimiento2"

def p_parametrosejec1(p):
    '''parametrosejec : aritmetica COMA parametrosejec'''
    print "parametrosejec1"   

def p_parametrosejec2(p):
    '''parametrosejec : aritmetica '''
    print "parametrosejec2"     

#Paquete
def p_paquete(p):
    '''paquete : login'''
    p[0]=paquete(p[1],"paquete")
    print "inicio1"

def p_paquete2(p):
    '''paquete : paquetes'''
    p[0]=paquete2(p[1],"paquete")
    print "paquete2"

def p_login(p):
    '''login : validar COMA logins'''
    p[0]=login(p[3],"login")
    print "login"

def p_validar(p):
    ''' validar : R_VALIDAR DOS_PUNTO ENTERO'''
    print "validar"

def p_logins1(p):
    ''' logins : R_LOGIN DOS_PUNTO ABRIR datosl COMA validacionl CERRAR'''
    p[0]=logins1(p[4],p[6],"logins")
    print "logins1"

def p_logins2(p):
    ''' logins : R_LOGIN DOS_PUNTO ABRIR validacionl CERRAR'''
    p[0]=logins2(p[4],"logins")
    print "logins2"

def p_datosl1(p):
    '''datosl : datosl COMA datol'''
    p[0]=datosl1(p[1],p[3],"datosl1")
    print "datosl1"

def p_datosl2(p):
    '''datosl : datol '''
    p[0]=datosl2(p[1],"datosl2")
    print "datosl2"

def p_datol(p):
    '''datol : CADENA DOS_PUNTO CADENA'''
    p[0]=datol(cadena(p[1]),cadena(p[3]),datol)
    print "datol"

def p_validacionl1(p):
    '''validacionl : R_LOGIN DOS_PUNTO R_TRUE'''
    p[0]=validacionl1(verdadero(p[3]),"validacion")
    print "validacionl1"

def p_validacionl2(p):
    '''validacionl : R_LOGIN DOS_PUNTO R_FALSE'''
    p[0]=validacionl2(falso(p[3]),"validacion")
    print "validacionl2"

def p_paquetes(p):
    '''paquetes : R_PAQUETE DOS_PUNTO tipopaquete'''
    p[0]=paquetes(p[3],"paquetes")
    print "paquetes"

def p_tipopaquete1(p):
    '''tipopaquete : usql'''
    p[0]=tipopaquete1(p[1],"tipopaquete1")
    print "tipopaquete1"

def p_tipopaquete2(p):
    '''tipopaquete : reporte'''
    p[0]=tipopaquete2(p[1],"tipopaquete2")
    print "tipopaquete2"

def p_tipopaquete3(p):
    '''tipopaquete : paqueteerror'''
    p[0]=tipopaquete3(p[1],"tipopaquete3")
    print "tipopaquete3"

def p_usql1(p):
    ''' usql : R_USQL COMA R_DATOS DOS_PUNTO ABRIR  datosusql CERRAR'''
    p[0]=usql1(p[6],"usql1")
    print "usql1"

def p_usql2(p):
    ''' usql : R_USQL COMA mensajear'''
    p[0]=usql2(p[3],"usql2")
    print "usql2"    

def p_usql3(p):
    ''' usql : R_USQL COMA mensajear COMA archivo'''
    p[0]=usql3(p[3],p[5],"usql2")
    print "usql3"

def p_usql4(p):
    ''' usql : R_USQL COMA mensajear COMA archivos COMA archivo'''
    p[0]=usql4(p[3],p[5],p[7],"usql2")
    print "usql2"      

def p_mensajear(p):
    '''mensajear : R_MENSAJE DOS_PUNTO CADENA'''
    p[0]=mensajear(cadena(p[3]),"mensajear")
    print "mensajear"

def p_archivo(p):
    '''archivo : R_ARCHIVO DOS_PUNTO CADENA'''
    p[0]=archivo(cadena(p[3]),"archivo")
    print "archivo"

def p_archivos1(p):
    '''archivos : archivos COMA nombrar COMA archivoback'''
    p[0]=archivos1(p[1],p[3],p[5],"archivos1")
    print "archivos1"

def p_archivos2(p):
    '''archivos : nombrar COMA archivoback'''
    p[0]=archivos2(p[1],p[3],"archivos2")
    print "archivos2"

def p_nombrar(p):
    '''nombrar : CADENA DOS_PUNTO CADENA'''
    p[0]=nombrar(cadena(p[3]),"nombrar")
    print "nombrar"

def p_archivoback(p):
    '''archivoback : R_ARCHIVO DOS_PUNTO archivosxml'''
    p[0]=archivoback(p[3],"archivoback")
    print "archivoback"

def p_archivosxml1(p):
    '''archivosxml : archivosxml archivoxml'''
    p[0]=archivosxml1(p[1],p[2],"archivosxml")
    print "archivosxml"

def p_archivosxml2(p):
    '''archivosxml : archivoxml'''
    p[0]=archivosxml2(p[1],"archivosxml")
    print "archivosxml"


def p_archivoxml(p):
    '''archivoxml : XML'''
    p[0]=archivoxml(XML(p[1]),"archivoxml")
    print "archivoxml"


def p_datosusql1(p):
    '''datosusql : datosusql datousql'''
    print "datosusql1"

def p_datosusql2(p):
    '''datosusql : datousql'''
    print "datosusql2"

def p_datousql(p):
    '''datousql : ABRIR valorespaquete CERRAR'''
    print "datousql"

def p_valorespaquete1(p):
    '''valorespaquete : valorespaquete valorpaquete '''
    print "valorespaquete1"

def p_valorespaquete2(p):
    '''valorespaquete :  valorpaquete '''
    print "valorespaquete2"

def p_valorpaquete(p):
    '''valorpaquete : CADENA  IPAQUETE   CADENA'''
    print "valorpaquete"

def p_reporte(p):
    ''' reporte : R_REPORTE COMA R_DATOS DOS_PUNTO ABRIR  XML CERRAR'''
    print "reporte"

def p_paqueteerror(p):
    '''paqueteerror : R_ERROR COMA R_TIPO_PAQUETE DOS_PUNTO tipoerror COMA R_MSG DOS_PUNTO CADENA COMA  R_DATOS DOS_PUNTO cuerpoerrorpack '''
    print "paqueteerror"

def p_cuerpoerrorpack(p):
    ''' cuerpoerrorpack : ABRIR R_ERROR DOS_PUNTO R_LEXICO COMA R_ARCHIVO DOS_PUNTO CADENA COMA R_COL DOS_PUNTO ENTERO  COMA R_FILA DOS_PUNTO ENTERO  CERRAR '''
    print "cuerpoerrorpack"

def p_tipoerror1(p):
    '''tipoerror : R_LEXICO '''
    print "tipoerror1"

def p_tipoerror2(p):
    '''tipoerror : R_OTRO '''
    print "tipoerror2"

#HTML 

def p_html(p):
    ''' html : cabeza cuerpo '''
    p[0]=html(p[1],p[2],"html")
    print "html"

def p_cabeza1(p):
    ''' cabeza : R_AHEAD R_CHEAD '''
    p[0]=cabeza1("cabeza")
    print "cabeza"

def p_cabeza2(p):
    ''' cabeza : R_AHEAD parteshtml R_CHEAD '''
    p[0]=cabeza2(p[2],"cabeza")
    print "cabeza"

def p_cuerpo(p):
    ''' cuerpo : R_ABODY parteshtml R_CBODY '''
    p[0]=cuerpo(p[2],"cuerpo")
    print "cuerpo"

def p_parteshtml1(p):
    ''' parteshtml :  parteshtml partehmtl '''
    p[0]=parteshtml1(p[1],p[2],"parteshtml")
    print "parteshtml1"

def p_parteshtml2(p):
    ''' parteshtml :  partehmtl '''
    p[0]=parteshtml2(p[1],"parteshtml2")
    print "parteshtml2"

def p_partehtml1(p):
    ''' partehmtl : encabezado1'''
    p[0]=partehtml1(p[1],"partehtml1")
    print "partehmtl"

def p_partehtml2(p):
    ''' partehmt2 : encabezado2'''
    p[0]=partehtml2(p[1],"partehtml2")
    print "partehmtl"

def p_partehtml3(p):
    ''' partehmtl : encabezado3'''
    p[0]=partehtml3(p[1],"partehtml3")
    print "partehmtl"

def p_partehtml4(p):
    ''' partehmtl : encabezado4'''
    p[0]=partehtml4(p[1],"partehtml4")
    print "partehmtl"

def p_partehtml5(p):
    ''' partehmtl : encabezado5'''
    p[0]=partehtml5(p[1],"partehtml5")
    print "partehmtl"

def p_partehtml6(p):
    ''' partehmtl : encabezado6'''
    p[0]=partehtml6(p[1],"partehtml6")
    print "partehmtl"

def p_partehtml7(p):
    ''' partehmtl : encabezado7'''
    p[0]=partehtml7(p[1],"partehtml7")
    print "partehmtl"

def p_partehtml8(p):
    ''' partehmtl : htmlusql'''
    p[0]=partehtml8(p[1],"partehtml8")
    print "partehmtl"

def p_encabezado1(p):
    ''' encabezado1 : R_AH1  listaIDS R_CH1 '''
    p[0]=encabezado1(p[2],"encabezado1")
    print "encabezado11"

def p_encabezado2(p):
    ''' encabezado2 : R_AH2  listaIDS R_CH2 '''
    p[0]=encabezado2(p[2],"encabezado2")
    print "encabezado11"

def p_encabezado3(p):
    ''' encabezado3 : R_AH3  listaIDS R_CH3 '''
    p[0]=encabezado3(p[2],"encabezado3")
    print "encabezado11"

def p_encabezado4(p):
    ''' encabezado4 : R_AH4  listaIDS R_CH4 '''
    p[0]=encabezado4(p[2],"encabezado4")
    print "encabezado11"

def p_encabezado5(p):
    ''' encabezado5 : R_AH5  listaIDS R_CH5 '''
    p[0]=encabezado5(p[2],"encabezado5")
    print "encabezado11"

def p_encabezado6(p):
    ''' encabezado6 : R_AH6  listaIDS R_CH6 '''
    p[0]=encabezado6(p[2],"encabezado6")
    print "encabezado11"

def p_encabezado7(p):
    ''' encabezado7 : R_AH7  listaIDS R_CH7 '''
    p[0]=encabezado7(p[2],"encabezado7")
    print "encabezado11"

def p_encabezado8(p):
    ''' encabezado8 : R_AUSQL  seleccionar R_CUSQL '''
    p[0]=encabezado8(p[2],"encabezado8")
    print "encabezado11"

def p_listaIDS1(p):
    ''' listaIDS : listaIDS  ID'''
    p[0]=listaIDS1(p[1],ID(p[2]),"listaIDS1")
    print "listaIDS"

def p_listaIDS2(p):
    ''' listaIDS : ID'''
    p[0]=listaIDS2(ID(p[1]),"listaIDS2")
    print "listaIDS"

def p_error(p):
    global flag_error
    flag_error = "ERROR"
    print "Error de sintaxis ", p


def analizar(cadena):
   parser = yacc.yacc()
   parseo = parser.parse(cadena)
    
   try:
       result=flag_error
   except:
        result=parseo

   try :
        result = parseo.imprimir()
   except:
        result=parseo
    
   return result
       