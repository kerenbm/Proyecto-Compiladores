# Analizador sintactico


precedence = (
    ('left', 'SUMA', 'RES'),
    ('left','POT', 'MULT', 'DIV'),
    ('right','U_MENOS'),
    ('left', 'A_PAR', 'C_PAR'),
    ('left', 'A_COR', 'C_COR')
)

resultados = []
operacion = {}

def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''   


def p_instrucciones_operar(t):
    
    'instruccion : INICIO_OP A_COR expresion C_COR FINAL'
    resultados.append([t[3]])
    operacion[t[1]] = t[3]

    print('El resultado de la expresión es: ' + str(t[3]))

def p_instrucciones_expr(t):
    'instruccion : expresion'
    print(t[1])

def p_expresion_binaria(t):
    '''expresion : expresion SUMA expresion
                  | expresion RES expresion
                  | expresion MULT expresion
                  | expresion DIV expresion
                  | expresion POT expresion'''
                  
    


    try:
        if t[2] == '+'  : t[0] = t[1] + t[3]
        elif t[2] == '-': t[0] = t[1] - t[3]
        elif t[2] == '*': t[0] = t[1] * t[3]
        elif t[2] == '/': t[0] = t[1] / t[3]
        elif t[2] == '^': t[0] = pow(t[1] , t[3])
    except ZeroDivisionError:
        error = "Error, División por cero"
        print(error)


def p_expresion_unaria(t):
    
    'expresion : RES expresion %prec U_MENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    
    'expresion : A_PAR expresion C_PAR'
    t[0] = t[2]


def p_expresion_number(t):
    '''expresion    : NUMERO
                    | DEC'''
   
    t[0] = t[1]

def p_error(t):
    operacion["INICIO_OP"] = 0

    print("Error sintáctico en '%s'" % t.value)