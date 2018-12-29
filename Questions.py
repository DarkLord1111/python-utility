def askYN(question:str,default='')->bool:
    """
    Asks the user a yes/no question until a valid input is given.\n
    <question> : The question to ask\n
    <default>  : A default option to give
    """
    default=default.strip().lower()
    response='0'
    qText=(question+(' ['+default.lower().strip()+']') if default and default[0] in ('y','n') else question)+': '
    while response[0] not in ('y','n'):
        response=input(qText).strip().lower()
        if not response or response.isspace():
                response=default if default in ('y','n') else '0'

    return response[0]=='y'



def ask_option(question:str, options:list): # es ask_option('choose the box: ', boxes)
    """
    Asks the user to chose one of the provided options until exact input is given.\n
    <question> : The question to ask\n
    <options>  : Can use elements of a variable (suggestion: delete '[' ']: ') or hardcoded into the question (eg: 'a','b','c')
    """
    response='0'
    while response[0] not in options:
        response = input(question + '[ ' + str(options)+ ']: ')
        if not response or response.isspace():
            response = '0'
    return response[0] #True, return chosen option
