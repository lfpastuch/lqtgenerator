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
    'baradas',
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
    'Ó',
    'EU SOU O LUQUITOOO AHHHH',
    'tá na jungle farmando hard',
    'vou aplicar a lei do solinho',
    'que se foda catequese',
    'pai tá chato',
    'pai tá chato, né?',
    'dalhe na narguilheira',
    'o cara é um mamute',
    'o cara é um mamute, né?',
    'ADURIANO NEH',
    'Boneco de posto'
    'tá maluco, tá doidão',
    'piá, é isso piá',
    'tem que ver isso aí',
]

adjetivo_dmais = [
    'gordo',
    'carinhas',
    'gado',
    'badaras',
    'baradas',
    'pipinhas léguas',
]

adjetivo_do = [
    'baby',
    'xesk',
    'bresk',
    'chesque',
    'bait',
]

adicional_final = [
    'papai',
    'meu papai',
    'pai',
    'meu pai',
    'primo',
    'meu primo',
    'papebas',
    'meu papebas',
    'tá ligado',
]

adicional_inicio = [
    'piá',
]

jogos = [
    'Dota 2 (Lion mid)',
    'Dota 2 (Pudge mid)',
    'Dota 2 (Legion jungle)',
    'Poketibia',
    'CoD',
    'Grand Chase',
]


def gera_jogo():
    r = random.randint(0, len(jogos) - 1)
    s = jogos[r]
    return str(s)


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
    return str(frase_adicional_ambas(s))


def frase_especial():
    r = random.randint(0, len(especial) - 1)
    s = especial[r]
    return str(s)


def frase_do():
    r = random.randint(0, len(adjetivo_do) - 1)
    s = adjetivo_do[r]
    s = str(s) + ' do ' + str(s)
    return str(frase_adicional_ambas(s))


def frase_adicional_final(s):
    r = random.randint(0, 100)
    if r <= 50:
        return s
    else:
        r = random.randint(0, len(adicional_final) - 1)
        return str(s) + ', ' + str(adicional_final[r])


def frase_adicional_inicial(s):
    r = random.randint(0, 100)
    if r <= 50:
        return s
    else:
        r = random.randint(0, len(adicional_inicio) - 1)
        return str(adicional_inicio[r]) + ', ' + str(s)


def frase_adicional_ambas(s):
    return str(frase_adicional_final(frase_adicional_inicial(s)))


def frase():
    r = random.randint(0, 140)
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
    elif r >= 101 and r <= 120:
        return str(frase_pior_que())
    elif r >= 121 and r <= 140:
        return str(frase_especial())


def gera_frase():
    s = frase()
    return s[0].upper() + s[1:]
