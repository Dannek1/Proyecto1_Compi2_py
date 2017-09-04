import ply.yacc as yacc

from Analizador import tokens


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
    print "campos1"

def p_campos2(p):
    '''campos : campo'''
    print "campos2"

def p_campo1(p):
    '''campo : ID'''
    print "campo1"

def p_campo2(p):
    '''campo : R_USUARIO'''
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
    print "condicionar"

def p_borrar(p):
    '''borrar : R_BORRAR R_EN R_TABLA ID condicionar PUNTO_COMA'''
    print "borrar"

def p_seleccionar1(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID condicionar ordenamiento PUNTO_COMA'''
    print "seleccionar1"

def p_seleccionar2(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID condicionar PUNTO_COMA'''
    print "seleccionar2"

def p_seleccionar3(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID  ordenamiento PUNTO_COMA'''
    print "seleccionar3"

def p_seleccionar4(p):
    '''seleccionar : R_SELECCIONAR camposSelect R_DE ID  PUNTO_COMA'''
    print "seleccionar4"

def p_camposSelect1(p):
    '''camposSelect : MULTI'''
    print "camposSelect1"

def p_camposSelect2(p):
    '''camposSelect : campos'''
    print "camposSelect2"

def p_ordenamiento(p):
    '''ordenamiento : R_ORDENAR ID modoorden'''
    print "ordenamiento"

def p_modoorden1(p):
    '''modoorden : R_ASC'''
    print "modoorden1"

def p_modoorden2(p):
    '''modoorden : R_DESC'''
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
    print "logica"

def p_logor1(p):
    '''logor : logand OR logand'''
    print "logor1"

def p_logor2(p):
    '''logor : logand'''
    print "logor2"

def p_logand1(p):
    '''logand : relacional AND logica'''
    print "logand1"

def p_logand2(p):
    '''logand : NOT relacional '''
    print "logand2"

def p_logand3(p):
    '''logand : relacional '''
    print "logand3"

def p_logand4(p):
    '''logand : PAR_IZ logica  PAR_DER '''
    print "logand4"

def p_relacional1(p):
    '''relacional : subrelacional relacionalprima'''
    print "relacional1"

def p_relacional2(p):
    '''relacional : subrelacional '''
    print "relacional2"

def p_relacionalprima1(p):
    '''relacionalprima : IGUAL  subrelacional relacionalprima'''
    print "relacionalprima1"

def p_relacionalprima2(p):
    '''relacionalprima : IGUAL  subrelacional'''
    print "relacionalprima2"

def p_relacionalprima3(p):
    '''relacionalprima : DISTINTO  subrelacional relacionalprima'''
    print "relacionalprima3"

def p_relacionalprima4(p):
    '''relacionalprima : DISTINTO  subrelacional'''
    print "relacionalprima4"

def p_relacionalprima5(p):
    '''relacionalprima : MENOR  subrelacional relacionalprima'''
    print "relacionalprima5"

def p_relacionalprima6(p):
    '''relacionalprima : MENOR  subrelacional'''
    print "relacionalprima6"

def p_relacionalprima7(p):
    '''relacionalprima : MAYOR  subrelacional relacionalprima'''
    print "relacionalprima7"

def p_relacionalprima8(p):
    '''relacionalprima : MAYOR  subrelacional'''
    print "relacionalprima8"

def p_relacionalprima9(p):
    '''relacionalprima : MENOR_IGUAL  subrelacional relacionalprima'''
    print "relacionalprima9"

def p_relacionalprima10(p):
    '''relacionalprima : MENOR_IGUAL  subrelacional'''
    print "relacionalprima10"

def p_relacionalprima11(p):
    '''relacionalprima : MAYOR_IGUAL  subrelacional relacionalprima'''
    print "relacionalprima9"

def p_relacionalprima12(p):
    '''relacionalprima : MAYOR_IGUAL  subrelacional'''
    print "relacionalprima10"

def p_subrelacional1(p):
    '''subrelacional : aritmetica'''
    print "subrelacional1"

def p_subrelacional2(p):
    '''subrelacional : PAR_IZ relacional  PAR_DER'''
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
    print "inicio1"

def p_inicio2(p):
    '''paquete : paquetes'''
    print "inicio2"

def p_login(p):
    '''login : validar COMA logins'''
    print "login"

def p_validar(p):
    ''' validar : R_VALIDAR DOS_PUNTO ENTERO'''
    print "validar"

def p_logins1(p):
    ''' logins : R_LOGIN DOS_PUNTO ABRIR datosl COMA validacionl CERRAR'''
    print "logins1"

def p_logins2(p):
    ''' logins : R_LOGIN DOS_PUNTO ABRIR validacionl CERRAR'''
    print "logins2"

def p_datosl1(p):
    '''datosl : datosl COMA datol'''
    print "datosl1"

def p_datosl2(p):
    '''datosl : datol '''
    print "datosl2"

def p_datol(p):
    '''datol : CADENA DOS_PUNTO CADENA'''
    print "datol"

def p_validacionl1(p):
    '''validacionl : R_LOGIN DOS_PUNTO R_TRUE'''
    print "validacionl1"

def p_validacionl2(p):
    '''validacionl : R_LOGIN DOS_PUNTO R_FALSE'''
    print "validacionl2"

def p_paquetes(p):
    '''paquetes : R_PAQUETE DOS_PUNTO tipopaquete'''
    print "paquetes"

def p_tipopaquete1(p):
    '''tipopaquete : usql'''
    print "tipopaquete1"

def p_tipopaquete2(p):
    '''tipopaquete : reporte'''
    print "tipopaquete2"

def p_tipopaquete3(p):
    '''tipopaquete : paqueteerror'''
    print "tipopaquete3"

def p_usql(p):
    ''' usql : R_USQL COMA R_DATOS DOS_PUNTO ABRIR  datosusql CERRAR'''
    print "usql"

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

def p_error(p):
    global flag_error
    flag_error = "ERROR"
    print "Error de sintaxis ", p


def analizar(cadena):
   parser = yacc.yacc()
   result = parser.parse(cadena)
    
   try:
       result=flag_error
   except:
       pass
    
   return result
       