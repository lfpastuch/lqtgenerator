import random

verbo_sem_obj = [
    'trollou',
    'feedou',
    'farmou',
    'fodeu',
]

verbo_clan_uva = [
    'matar',
    'mutar',
]

moios = [
    'moios',
    'broios',
    'troios',
    'droios',
    'trodos',
    'trotos',
    'badaras',
]

clan_uva = [
    'o Adriano',
    'o Adriano',
    'o Adriano',
    'o Adriano',
    'o Adriano',
    'o Kibe',
    'o Pastuch',
    'o Caio',
    'o Sebben',
    'o Pedro',
    'o Dezzo',
]

especial = [
    'ó',
    'EU SOU O LUQUITOOO AHHHH',
    'tá na jungle farmando hard',
    'vou aplicar a lei do solinho',
    'Que se foda catequese'
]

adjetivo_dmais = [
    'gordo',
    'carinhas',
    'gado',
    'badaras',
]

adjetivo_do = [
    'baby',
    'xesk',
    'bresk',
    'chesque',
]

adicional = [
    'papai',
    'meu papai',
    'pai',
    'meu pai',
    'primo',
    'meu primo',
]


def frase_pior_que():
    # pior que daí é (MOIOS)
    r = random.randint(0, len(moios) - 1)
    s = moios[r]
    return str('Pior que daí é ') + str(s)


def frase_ai_1():
    # aí (VERBO SEM OBJETO)
    r = random.randint(0, len(verbo_sem_obj) - 1)
    s = verbo_sem_obj[r]
    return str('Aí ') + str(s)


def frase_ai_2():
    # aí é (MOIOS)
    r = random.randint(0, len(moios) - 1)
    s = moios[r]
    return str('Aí é ') + str(s)


def frase_eu_vou():
    # eu vou (VERBO CLAN UVA) (CLAN UVA)
    r1 = random.randint(0, len(verbo_clan_uva) - 1)
    r2 = random.randint(0, len(clan_uva) - 1)
    s1 = verbo_clan_uva[r1]
    s2 = clan_uva[r2]
    return str('Eu vou ') + str(s1) + ' ' + str(s2)


def frase_dmais():
    # (ADJETIVO) d+
    r = random.randint(0, len(adjetivo_dmais) - 1)
    s = adjetivo_dmais[r]
    s = str(s) + ' d+'
    return str(frase_adicional(s))


def frase_especial():
    r = random.randint(0, len(especial) - 1)
    s = especial[r]
    return str(s)


def frase_do():
    r = random.randint(0, len(adjetivo_do) - 1)
    s = adjetivo_do[r]
    s = str(s) + ' do ' + str(s)
    return str(frase_adicional(s))


def frase_adicional(s):
    r = random.randint(0, 100)
    if r <= 99:
        return s
    else:
        r = random.randint(0, len(adicional) - 1)
        return str(s) + ' ' + str(adicional[r])


def gera_frase():
    r = random.randint(0, 120)
    if r <= 20:
        return str(frase_ai_1())
    elif r >= 21 and r <= 40:
        return str(frase_ai_2())
    elif r >= 41 and r <= 60:
        return str(frase_eu_vou())
    elif r >= 61 and r <= 80:
        return str(frase_dmais())
    elif r >= 81 and r <= 100:
        return str(frase_do())
    elif r >= 101 and r <= 119:
        return str(frase_pior_que())
    elif r >= 120:
        return str(frase_especial())


for i in range(0, 1000):
    s = gera_frase()
    s = s[0].upper() + s[1:]
    print(s)
