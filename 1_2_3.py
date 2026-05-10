def deux_files(init, lam_plus, lam_minus):
    t = 0.0
    A = init
    V = init
    temps = [t]
    ventes = [A]
    achats = [V]

    while A > 0 and V > 0:
        t += np.random.exponential(1 / (2 * (lam_plus + lam_minus)))
        if np.random.rand() < 0.5:
            if np.random.rand() < lam_plus / (lam_plus + lam_minus):
                A += 1
            else:
                A -= 1
        else:
            if np.random.rand() < lam_plus / (lam_plus + lam_minus):
                V += 1
            else:
                V -= 1

        temps.append(t)
        ventes.append(A)
        achats.append(V)

    return t, temps, ventes, achats


