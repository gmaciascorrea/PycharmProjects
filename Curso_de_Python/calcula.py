eq = input('Digite termo a ser calculado: ')

terms = {'^': 'e', 'v': 'ou', '⊻': 'ou_ou', '¬': 'negacao', '→': 'entao', '⇔': 'se_somente_se'}


def e(p, q):
    if p and q:
        return True
    else:
        return False


def ou(p, q):
    if p or q:
        return True
    else:
        return False


def ou_ou(p, q):
    if p and not q:
        return True
    if not p and q:
        return True
    else:
        return False


def negacao(param):
    if param:
        return False
    else:
        return True


def entao(p, q):
    if p and not q:
        return False
    else:
        return True


def se_somente_se(p, q):
    if p and q:
        return True
    if not p and not q:
        return True
    else:
        return False


var = ''

for i in eq:
    if i in terms:
        i = terms[i]

    var += i

print(var)
