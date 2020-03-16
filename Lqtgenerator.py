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
    0: 'Ó',
    1: 'EU SOU O LUQUITOOO AHHHH',
    2: 'Tá na jungle farmando hard'
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


def frases_especiais():
    r = random.randint(0, len(especial) - 1)
    s = especial.get(r)
    return str(s)


def tipo_frase():
    r = random.randint(0, 100)
    if r >= 0 and r <= 25:
        return str(frase_ai_1())
    elif r >= 26 and r <= 80:
        return str(frase_ai_2())
    elif r >= 81 and r <= 99:
        return str(frase_eu_vou())
    elif r >= 100:
        return str(frases_especiais())


for i in range(0, 1000):
    print(tipo_frase())
