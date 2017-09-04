import ply.lex


tokens = ['SUMA','RESTA','MULTI','DIV','POW','INCR','DECR','I_ASIG',
          'PUNTO_COMA','COMA','PUNTO','IGUAL','DISTINTO','MENOR',
          'MAYOR','MENOR_IGUAL','MAYOR_IGUAL','OR','AND','NOT',
          'PAR_IZ','PAR_DER','COR_IZ','COR_Der','ID','ENTERO','DECIMAL',
          'CADENA','FECHA','FECHA_HORA','DOS_PUNTO','BOOLEAN','ABRIR',
          'CERRAR',#'COMILLAS', 
           'XML','IPAQUETE'
]

reservadas = {
    
    'USAR':'R_USAR',
    'CREAR':'R_CREAR',
    'BASE_DATOS':'R_BASE',
    'TABLA':'R_TABLA',
    'OBJETO':'R_OBJETO',
	'PROCEDIMIENTO':'R_PROCEDIMIENTO',
	'FUNCION':'R_FUNCION',
	'RETORNO':'R_RETORNO',
	'USUARIO':'R_USUARIO',
	'COLOCAR':'R_COLOCAR',
	'password':'R_PAS',
	'IMPRIMIR':'R_IMPRIMIR',
	'INSERTAR':'R_INSERTAR',
	'EN':'R_EN',
	'VALORES':'R_VALORES',
	'ACTUALIZAR':'R_ACTUALIZAR',
	'DONDE':'R_DONDE',
	'BORRAR': 'R_BORRAR',
	'SELECCIONAR':'R_SELECCIONAR',
	'DE': 'R_DE',
	'ORDENAR_POR':'R_ORDENAR',
	'ASC':'R_ASC',
	'DESC': 'R_DESC',
	'OTORGAR': 'R_OTORGAR',
	'PERMISOS': 'R_PERMISOS',
	'DENEGAR': 'R_DENEGAR',
	'BACKUP': 'R_BACKUP',
	'USQLDUMP': 'R_USQLDUMP',
	'COMPLETO': 'R_COMPLETO',
	'RESTAURAR': 'R_RESTAURAR',
	'ALTERAR': 'R_ALTERAR',
	'AGREGAR': 'R_AGREGAR',
	'QUITAR': 'R_QUITAR',
	'CAMBIAR': 'R_CAMBIAR',
	'ELIMINAR': 'R_ELIMINAR',
	'DECLARAR': 'R_DECLARAR',
	'SI': 'R_SI',
	'SINO': 'R_SINO',
	'SELECCIONA': 'R_SELECCIONA',
	'CASO': 'R_CASO',
	'DEFECTO': 'R_DEFECTO',
	'PARA': 'R_PARA',
	'MIENTRAS': 'R_MIENTRAS',
	'DETENER': 'R_DETENER',
	'CONTAR': 'R_CONTAR',
    
    'FECHA':'R_FECHA',
    'FECHA_HORA':'R_FECHA_HORA',

    
    'TEXT': 'R_TEXT',
	'INTEGER': 'R_INTEGER',
    'DOUBLE': 'R_DOUBLE',
	'BOOL': 'R_BOOL',
	'DATE': 'R_DATE',
	'DATETIME': 'R_DATETIME',

    '\"validar\"':'R_VALIDAR',
    '\"login\"':'R_LOGIN',
    '\"paquete\"':'R_PAQUETE',
     '\"tipo\"':'R_TIPO_PAQUETE',
    '\"error\"':'R_ERROR',
    '\"lenguaje\"':'R_LENGUAJE',
    '\"otro\"':'R_OTRO',
    '\"msg\"':'R_MSG',
    '\"datos\"':'R_DATOS',
    '\"Lexico\"':'R_LEXICO',
    '\"Archivo\"':'R_ARCHIVO',
    '\"col\"':'R_COL',
    '\"fila\"':'R_FILA',
    '\"usql\"':'R_USQL',
    '\"reporte\"':'R_REPORTE',
    'true':'R_TRUE',
    'false':'R_FALSE',

    'No': 'R_NO',
	'Nulo':'R_NULO',
	'Autoincrementable': 'R_AUTOINCREMENTABLE',
	'Llave_Primaria': 'R_PK',
	'Llave_Foranea': 'R_FK',
	'Unico': 'R_UNICO',
}

tokens = tokens+list(reservadas.values())

t_ignore = '\t| '
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_MULTI   = r'\*'
t_DIV    = r'/'
t_POW   = r'\^'
t_INCR = r'\+\+'
t_DECR = r'--'
t_I_ASIG  = r'='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_OR = r'\|\|'
t_AND = r'&&'   
t_NOT = r'!'
t_PAR_IZ  = r'\('
t_PAR_DER  = r'\)'
t_PUNTO_COMA = r';'
t_COMA = r','
t_PUNTO = r'\.'
t_DOS_PUNTO = r':'
t_ABRIR = r'\['
t_CERRAR = r'\]'
#t_COMILLAS= r'\"'
t_IPAQUETE= r'=>'
t_XML = r'(<.*>)'
t_FECHA = r'[1-3][0-9][-][0-1][0-9][-][1-9][0-9][0-9][0-9]'
t_FECHA_HORA = r'[1-3][0-9][-][0-1][0-9][-][1-9][0-9][0-9][0-9][" "][0-2]*[0-9][:][0-5][0-9][:][0-5][0-9]'

def t_CADENA(t):
    r'("[^"]*")'
    t.type = reservadas.get(t.value,'CADENA')    # Check for reserved words
    return t


def t_code_lbrace(t):
    r'\{'
    return t

def t_code_rbrace(t):
    r'\}'
    return t

def t_ID(t):
    r'[a-zA-Z_@][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    return t

def t_ENTERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    print (t.value)
    return t

def t_double(t):
    r'[0-9]+([.][0-9]+)?'
    t.value = float(t.value)
    print (t.value)
    return t

def t_COMENTARIO_S(t):
    r'\#.*'
    pass

def t_COMENTARIO_M(t):
    r'\#\*(.*| \n) \*\#'
    pass


def t_newline(t):
    "\\n+"
    #t.lexer.lineno += len(t.value)
    #t.lexer.linestart = t.lexer.lexpos
    pass

def t_error(t):
    print "ERROR Caracter Invalido: '%s'" % t.value[0]
    global flag_error
    flag_error = "ERROR"
    t.lexer.skip(1)    
    

analizador =ply.lex.lex()    
