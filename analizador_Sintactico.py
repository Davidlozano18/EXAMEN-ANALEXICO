import ply.yacc as yacc

from analizador_lexico import tokens

def p_program(p):
    '''
    program : programa_1
    '''
    p[0] = "Programa Scala lista"

def p_programa_1(p):
    '''
    programa_1 : USING SYSTEM SEMICOLON object_declaration  
    '''
    p[0] = "Declaración de objeto para programa 1 valida."

def p_object_declaration(p):
    '''
    object_declaration : NAMESPACE ID LBRACE main_declaration RBRACE 
    '''
    p[0] = "Declaración de objetos funcional"

def p_main_declaration(p):
    '''
    main_declaration : CLASS ID LBRACE args RBRACE 
    '''
    p[0] = "Declaramos el método main para que sea correcto"

def p_args(p):
    '''
    args : STATIC VOID MAIN LPAREN STRING_TYPE LEFT_BRACKET RIGHT_BRACKET ARGS RPAREN LBRACE statements RBRACE 
    '''
    p[0] = "Los argumentos de main son correctos"

""" def p_block(p):
    '''
    block : LBRACE statements RBRACE
    '''
    p[0] = "Este bloque es valido"
 """

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

def p_statement(p):
    '''
    statement : expression SEMICOLON
              | println_statement
              | assignment
    '''

def p_println_statement(p):
    '''
    println_statement : SYSTEM DOT CONSOLE DOT WRITELINE LPAREN STRING_LITERAL RPAREN SEMICOLON
    '''
    p[0] = "Declaración de impresión válida."

def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
    '''


def p_factor(p):
    '''
    factor : NUMBER
           | ID
           | LPAREN expression RPAREN

    '''


def p_term(p):
    '''
    term : factor
         | term TIMES factor
         | term DIVIDE factor
    '''

def p_error(p):
    if p is not None:
        mensaje_error = f"Error al colocar el token '{p.value}', tipo '{p.type}' en la línea {p.lineno}"
        raise SyntaxError(mensaje_error)
    else:
        raise SyntaxError(
            "Error en la sintaxis= No se puede crear el arbol sintactico")

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = "Asignación válida."



parser = yacc.yacc(errorlog=yacc.NullLogger())

def parse_code(code, debug=None):
    try:
        parser.parse(code, debug=debug)
        resultado_sintactico = {"status": "success",
                                "message": "Felicidades el analizador sintactico funciona"}
    except SyntaxError as e:
        resultado_sintactico = {"status": "error", "message": str(e)}
        if debug:
            debug.append(resultado_sintactico)

    return resultado_sintactico
