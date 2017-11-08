def descodifica(pals, ordem):
    pals_new=pals[:]
    for i in range(len(pals)):
        pals_new.pop(ordem[i])
        pals_new.insert(ordem[i], pals[i])
    print(pals_new)
