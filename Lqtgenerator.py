import random

verbo_sem_obj = {
    0: 'trollou',
    1: 'feedou',
    2: 'farmou',
    3: 'fodeu',
}

verbo_clan_uva = {
    0: 'matar',
    1: 'mutar',
}

moios = {
    0: 'moios',
    1: 'broios',
    2: 'troios',
    3: 'droios',
    4: 'trodos',
    5: 'trotos',
}

clan_uva = {
    0: 'o Adriano',
    1: 'o Adriano',
    2: 'o Adriano',
    3: 'o Adriano',
    4: 'o Adriano',
    5: 'o Kibe',
    6: 'o Pastuch',
    7: 'o Caio',
}

especial = {
    0: 'ó',
    1: 'EU SOU O LUQUITOOO AHHHH',
    2: 'tá na jungle farmando hard',
    3: 'vou aplicar a lei do solinho',
}

adjetivo_dmais = {
    0: 'gordo',
    1: 'carinhas',
    2: 'gado',
}

adjetivo_do = {
    0: 'baby',
    1: 'xesk',
    2: 'bresk',
    3: 'chesque',
}

adicional = {
    0: 'papai',
    1: 'meu papai',
    2: 'pai',
    3: 'meu pai',
}


def frase_ai_1():
    # aí (VERBO SEM OBJETO)
    r = random.randint(0, len(verbo_sem_obj) - 1)
    s = verbo_sem_obj.get(r)
    return str('Aí ') + str(s)


def frase_ai_2():
    # aí é (MOIOS)
    r = random.randint(0, len(moios) - 1)
    s = moios.get(r)
    return str('Aí é ') + str(s)


def frase_eu_vou():
    # eu vou (VERBO CLAN UVA) (CLAN UVA)
    r1 = random.randint(0, len(verbo_clan_uva) - 1)
    r2 = random.randint(0, len(clan_uva) - 1)
    s1 = verbo_clan_uva.get(r1)
    s2 = clan_uva.get(r2)
    return str('Eu vou ') + str(s1) + ' ' + str(s2)


def frase_dmais():
    # (ADJETIVO) d+
    r = random.randint(0, len(adjetivo_dmais) - 1)
    s = adjetivo_dmais.get(r)
    s = str(s) + ' d+'
    return str(frase_adicional(s))


def frase_especial():
    r = random.randint(0, len(especial) - 1)
    s = especial.get(r)
    return str(s)


def frase_do():
    r = random.randint(0, len(adjetivo_do) - 1)
    s = adjetivo_do.get(r)
    s = str(s) + ' do ' + str(s)
    return str(frase_adicional(s))


def frase_adicional(s):
    r = random.randint(0, 100)
    if r <= 99:
        return s
    else:
        r = random.randint(0, len(adicional) - 1)
        return str(s) + ' ' + str(adicional.get(r))


def gera_frase():
    r = random.randint(0, 100)
    if r <= 20:
        return str(frase_ai_1())
    elif r >= 21 and r <= 40:
        return str(frase_ai_2())
    elif r >= 41 and r <= 60:
        return str(frase_eu_vou())
    elif r >= 61 and r <= 80:
        return str(frase_dmais())
    elif r >= 81 and r <= 99:
        return str(frase_do())
    elif r >= 100:
        return str(frase_especial())


for i in range(0, 1000):
    s = gera_frase()
    s = s[0].upper() + s[1:]
    print(s)
