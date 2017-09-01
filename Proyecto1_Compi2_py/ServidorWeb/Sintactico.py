import ply.yacc

import Analizador


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
    p[0] = programa(p[1],"programa")

def p_inicio(p):
    '''inicio : sentencias'''
    p[0] = inicio(p[1],"inicio")
    

def p_sentencias1(p):
    '''sentencias : sentencias sentencia
    '''
    p[0] = p
    
    

