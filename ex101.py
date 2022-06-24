print('-' * 30)
b_year = int(input('Em que ano você nasceu? '))

def voto(b_year):
    from datetime import date
    age = date.today().year - b_year
    strAge = 'Com ' + str(age) + ' anos: '
    
    if age < 16:
        return strAge + 'VOTO NEGADO'
    elif age < 18:
        return strAge + 'VOTO OPCIONAL'
    elif age >= 18 and age < 60:
        return strAge + 'VOTO OBRIGATÓRIO'
    else:
        return strAge + 'VOTO OPCIONAL'

print(voto(b_year))