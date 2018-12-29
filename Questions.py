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
