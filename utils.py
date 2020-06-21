
def find_max(list):
    hght = max(list)
    return hght


def runmax(xk):
    nht=xk[0]
    for nm in xk:
        if nht<nm:
            nht=nm
    return nht