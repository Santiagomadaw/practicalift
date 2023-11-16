def check(lisp):
    
    '''Realiza la comprobación de que la orden recibida cumple las condiciones.
    En caso contrario, devuelve una excepción y devuelve True en caso de ser válida.
    
    Performs a check to verify that the received command meets the conditions.
    Raises an exception if it doesn't and returns True if valid.'''
    
    index = 0
    while index<len(lisp):
        if lisp[index] not in ('', ' ', '\t','\r','\n','(',')'):
            raise SyntaxError ('Comando incorrecto en la posicion [{}]: ({}) no es parametro aceptado'.format(index,lisp[index]))
        index+=1
        
    return True

def parse(lisp, checked=False):
    '''Esta función recibe una cadena y devuelve otra a la que elimina espacios en blanco, tabulaciones, saltos de línea, etc.
    Primero verifica que cumple el formato requerido. Si recibe una cadena que previamente
    ha sido chequeada, omite este paso.
    
    This function receives a string and returns another one after removing white spaces, tabs, newlines, etc.
    It first checks if it meets the required format. If it receives a string that has been previously checked, it skips this step.'''
    
    parse_lisp=''
    try:
        if checked or check(lisp):
            
            for comando in lisp:
                if comando not in ('', ' ', '\t','\r','\n'):
                    parse_lisp = parse_lisp + comando

    except SyntaxError as err:
        
      print('')
      print('\033[91m{}'.format(err))
      print('')
      print('\033[93mInstrucciones [(] suma 1, [)] baja 1 y [] es 0\033[0m')
      print('')
    return parse_lisp

def read(lisp):
    '''Recibe una cadena, la verifica y la pasa por parse. Devuelve la cadena verificada y parseada.
    
    Receives a string, checks it, and processes it through parse. Returns the checked and parsed string.'''
    
    parsed = ''
    try:
        parsed=parse(lisp, check(lisp))
        return parsed
    except SyntaxError as err:
      print('')
      print('\033[91m{}\033[0m"'.format(err))
      print('')
      print('\033[93mInstrucciones [(] suma 1, [)] baja 1 y [] es 0\033[0m')
      print('')


def eval_lisp (lisp):
    '''Traduce la cadena que recibe de read a un valor numérico.
    Translates the string received from read to a numeric value.'''
    move = 0
    
    checked_n_parsed = read(lisp)
    if checked_n_parsed ==0:
        move = 0
    else:
        
        for command in checked_n_parsed:
            
            if command == '(':
                move = move + 1
            else:
                move = move - 1
        
    return move

        
def run():
    '''Interfaz de usuario para recibir los comandos.
    User interface to receive commands.'''
    while True:
        print('\033[5mBIENVENIDO A -=L I S P=- LIFT EDITION\033[0m')
        print('')
        lisp = input('\033[1mIntroduzca una orden para el ascensor.\033[0m (X para salir) ')
        if lisp == 'X' or lisp =='x':
            break
        else:
            try:
                print('')
                print('\033[92mEl ascensor ira a la planta {}\033[0m'.format(eval_lisp(lisp)))
                print('')
            except TypeError as err:
                pass

if __name__ == '__main__':
    run()