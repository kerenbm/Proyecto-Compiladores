
# Analizador lexico


tokens = [
            "INICIO_OP", "NUMERO", "A_PAR", "C_PAR", "SUMA", "RES", "MULT", "DIV", "POT", "DEC", "A_COR", "C_COR", "FINAL"
         ]

t_INICIO_OP = "INICIO_OP"
t_A_PAR = r'\('
t_C_PAR = r'\)'
t_A_COR = r'\['
t_C_COR = r'\]'
t_SUMA = r'\+'
t_RES = r'-'
t_MULT = r'\*'   
t_DIV = r'/'
t_POT = r'\^' 
t_FINAL = r'\$'
t_ignore = " \t"



def t_DEC(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error en: %d", t.value)
        t.value = 0
    return t

def t_NUMERO( t ):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Error en: %d", t.value)
        t.value = 0
    return t




def t_error( t ):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


