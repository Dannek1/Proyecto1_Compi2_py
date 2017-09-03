import ply.yacc

from Analizador.py import tokens


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

def p_programa(p):
    '''programa : inicio'''
    print "programa"

def p_inicio(p):
    '''inicio : sentencias'''
    print "inicio"

def p_sentencias1(p):
    '''sentencias : sentencias sentencia'''
    print "sentencias1"

def p_sentencias2(p):
    '''sentecias : sentecia'''
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
    '''usar: R_USAR ID PUNTO_COMA'''
    print "usar"

def p_crear(p):
    '''crear: R_CREAR opcionescrear'''
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
    '''complemento: R_NO R_NULO'''
    print "complemento1"

def p_complemento2(p):
    '''complemento: R_NULO'''
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
    '''parametro: tipodato ID'''
    print "parametro"

def p_crearpro1(p):
    '''crearpro: R_PROCEDIMIENTO ID PAR_IZ parametros PAR_DER COR_IZ subsentencias COR_Der'''
    print "crearpro1"

def p_crearpro2(p):
    '''crearpro: R_PROCEDIMIENTO ID PAR_IZ PAR_DER COR_IZ subsentencias COR_Der'''
    print "crearpro2"

def p_subsentencias1(p):
    '''subsentencias : subsentencias subsentencia'''
    print "subsentencias1"

def p_subsentencias2(p):
    '''subsentencias : subsentencia'''
    print "subsentencias2"

def p_subsentencia1(p):
    '''subsentencia: asignacion'''
    print "subsentencia1"

def p_subsentencia2(p):
    ''' subsentencia : if'''
    print "subsentencia2"

def p_subsentencia3(p):
    ''' subsentencia:switch'''
    print "subsentencia3"

def p_subsentencia4(p):
    ''' subsentencia: for'''
    print "subsentencia4"

def p_subsentencia5(p):
    '''subsentencia :while'''
    print "subsentencia5"

def p_subsentencia6(p):
    '''subsentencia: fecha'''
    print "subsentencia6"

def p_subsentencia7(p):
    '''subsentencia: fecha_hora'''
    print "subsentencia7"

def p_subsentencia8(p):
    '''subsentencia: sentencia'''
    print "subsentencia8"

def p_crearfun1(p):
    '''crearfun: R_FUNCION ID PAR_IZ parametros PAR_DER tipodato COR_IZ sentencias_retorno COR_Der'''
    print "crearfun1"

def p_crearfun2(p):
    '''crearfun: R_FUNCION ID PAR_IZ PAR_DER tipodato COR_IZ sentencias_retorno COR_Der'''
    print "crearfun2"

def p_sentencias_retorno(p):
    '''sentencias_retorno: subsentencias retorno'''
    print "sentencias_retorno"

def p_retorno(p):
    '''retorno: R_RETORNO aritmetica PUNTO_COMA'''
    print "retorno"

def p_crearusuario(p):
    '''crearusuario : R_USUARIO ID R_COLOCAR R_PAS I_ASIG expresion PUNTO_COMA'''
    print "Crearususario"

def p_imprimir(p):
    '''imprimir : R_IMPRIMIR PAR_IZ expresion PAR_DER PUNTO_COMA'''
    print "imprimir"

def p_insertar(p):
    '''insertar: R_INSERTAR R_EN R_TABLA ID PAR_IZ tipoins'''
    print "insertar"

def p_tipoins1(p):
    '''tipoins : campos PAR_DER R_VALORES PAR_IZ valor PAR_DER PUNTO_COMA'''
    print "tipoins1"

def p_tipoins2(p):
    '''tipoins : valor PAR_DER PUNTO_COMA'''
    print "tipoins2"

def p_campos1(p):
    '''campos: campos COMA campo'''
    print "campos1"

def p_campos2(p):
    '''campos: campo'''
    print "campos2"

def p_campo1(p):
    '''campo: ID'''
    print "campo1"

def p_campo2(p):
    '''campo: R_USUARIO'''
    print "campo2"

def p_valor1(p):
    '''valor: valor COMA aritmetica'''
    print "valor1"

def p_valor2(p):
    '''valor: aritmetica'''
    print "valor2"

def p_actualizar1():
    '''actualizar: R_ACTUALIZAR R_TABLA ID PAR_IZ campos PAR_DER R_VALORES PAR_IZ valor PAR_DER condicionar PUNTO_COMA'''
    print "actualizar1"

def p_actualizar2():
    '''actualizar: R_ACTUALIZAR R_TABLA ID PAR_IZ campos PAR_DER R_VALORES PAR_IZ valor PAR_DER PUNTO_COMA'''
    print "actualizar2"

def p_condicionar(p):
    '''condicionar: R_DONDE logica'''
    print "condicionar"

def p_borrar(p):
    '''borrar:R_BORRAR R_EN R_TABLA ID condicionar PUNTO_COMA'''
    print "borrar"

def p_seleccionar1(p):
    '''seleccionar:R_SELECCIONAR camposSelect R_DE ID condicionar ordenamiento PUNTO_COMA'''
    print "seleccionar1"

def p_seleccionar2(p):
    '''seleccionar:R_SELECCIONAR camposSelect R_DE ID condicionar PUNTO_COMA'''
    print "seleccionar2"

def p_seleccionar3(p):
    '''seleccionar:R_SELECCIONAR camposSelect R_DE ID  ordenamiento PUNTO_COMA'''
    print "seleccionar3"

def p_seleccionar4(p):
    '''seleccionar:R_SELECCIONAR camposSelect R_DE ID  PUNTO_COMA'''
    print "seleccionar4"

def p_camposSelect1(p):
    '''camposSelect: MULTI'''
    print "camposSelect1"

def p_camposSelect2(p):
    '''camposSelect: campos'''
    print "camposSelect2"

def p_ordenamiento(p):
    '''ordenamiento:R_ORDENAR ID modoorden'''
    print "ordenamiento"

def p_modoorden1(p):
    '''modoorden:R_ASC'''
    print "modoorden1"

def p_modoorden2(p):
    '''modoorden:R_DESC'''
    print "modoorden2"

def p_otorgar(P):
    '''otorgar:R_OTORGAR R_PERMISOS ID COMA ID PUNTO objeto PUNTO_COMA'''
    print "otorgar"

def p_objeto1(p):
    '''objeto: MULTI'''
    print "objeto1"

def p_objeto2(p):
    '''objeto: ID'''
    print "objeto2"

def p_denegar(p):
    '''denegar: R_DENEGAR R_PERMISOS ID COMA ID PUNTO objeto PUNTO_COMA'''
    print "denegar"

def p_back(p):
    '''back:R_BACKUP tipoback ID ID PUNTO_COMA'''
    print "backup"

def p_tipoback1(p):
    '''tipoback: R_USQLDUMP '''
    print "tipoback1"
 
def p_tipoback2(p):
    '''tipoback: R_COMPLETO '''
    print "tipoback2"   

def p_restaurar(p):
    '''restaurar: tipoback aritmetica PUNTO_COMA'''
    print "restaurar"

def p_alterar(p):
    '''alterar: R_ALTERAR alterado'''
    print "alterar"

def p_alterado1(p):
    '''alterado: R_TABLA ID accionalterartabla PUNTO_COMA'''
    print "alterado1"

def p_alterado2(p):
    '''alterado: R_OBJETO ID accionalterarobjeto PUNTO_COMA'''
    print "alterado2"

def p_alterado3(p):
    '''alterado: R_USUARIO ID R_CAMBIAR R_PAS I_ASIG expresion PUNTO_COMA'''
    print "alterado3"

def p_accionalterartabla1(p):
    '''accionalterartabla: R_AGREGAR PAR_IZ campostabla PAR_DER'''
    print "accionalterartabla1"

def p_accionalterartabla2(p):
    '''accionalterartabla: R_QUITAR campos'''
    print "accionalterartabla2"

def p_accionalterarobjeto1(p):
    '''accionalterarobjeto: R_AGREGAR PAR_IZ parametros PAR_DER'''
    print "accionalterarobjeto"

def p_accionalterarobjeto2(p):
    '''accionalterarobjeto: R_QUITAR campos'''
    print "accionalterarobjeto2"

def p_eliminar1(p):
    '''eliminar: R_ELIMINAR R_TABLA ID PUNTO_COMA'''
    print "eliminar1"

def p_eliminar2(p):
    '''eliminar: R_ELIMINAR R_BASE ID PUNTO_COMA'''
    print "eliminar2"

def p_eliminar3(p):
    '''eliminar: R_ELIMINAR R_OBJETO ID PUNTO_COMA'''
    print "eliminar3"

def p_eliminar4(p):
    '''eliminar: R_ELIMINAR R_USUARIO ID PUNTO_COMA'''
    print "eliminar"

def p_declarar1(p):
    '''declarar: R_DECLARAR listavar tipodato I_ASIG asigdecl PUNTO_COMA'''
    print"declarar1"

def p_declarar1(p):
    '''declarar: R_DECLARAR listavar tipodato PUNTO_COMA'''
    print"declarar1"

def p_listavar1(p):
    '''listavar: listavar COMA ID'''
    print "listavar1"

def p_listavar2(p):
    '''listavar: ID'''
    print "listavar2"

def p_asigdecl1(p):
    '''asigdecl: aritmetica PAR_IZ Valor PAR_DER'''
    print "asigdecl1"

def p_asigdecl2(p):
    '''asigdecl: aritmetica '''
    print "asigdecl2"

def p_asignacion(p):
    '''asignacion: ID I_ASIG aritmetica PUNTO_COMA'''
    print "asignacion"
 
def p_if1(p):
    '''if: R_SI PAR_IZ logica PAR_DER COR_IZ subsentencias COR_Der sinoelse'''
    print "if1"

def p_if2(p):
    '''if: R_SI PAR_IZ logica PAR_DER COR_IZ subsentencias COR_Der '''
    print "if2"