
def deux_files(init, lam_plus, lam_minus):
    t = 0
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


def une_file(init, lam_plus, lam_minus):
    t = 0.0
    q = init
    temps = [t]
    valeurs = [q]

    while q > 0:
        t += np.random.exponential(1 / (lam_plus + lam_minus))
        if np.random.rand() < lam_plus / (lam_plus + lam_minus):
            q += 1
        else:
            q -= 1
        temps.append(t)
        valeurs.append(q)

    return temps, valeurs, t


def moyenne_temps_atteinte(N, init, lam_plus, lam_minus):
    tt = []
    for _ in range(N):
        _, _, tau = une_file(init, lam_plus, lam_minus)
        tt.append(tau)
    tt = np.array(tt)
    m = np.mean(tt)
    s = np.std(tt, ddof=1)
    ic = 1.96 * s / np.sqrt(N)
    return m, m - ic, m + ic


def brownien(init, mu, sigma, dt=0.01, tmax=1000):
    t = 0.0
    x = init
    temps = [t]
    valeurs = [x]

    while x > 0 and t < tmax:
        x = x + mu * dt + sigma * np.sqrt(dt) * np.random.randn()
        t += dt
        temps.append(t)
        valeurs.append(x)

    return temps, valeurs

plt.figure() 
t, temps, valeur = une_file(10, 1.2, 1.5)
plt.bar(temps, valeur, label = 'loi experimentale')
temps2, valeurs2 = brownien(10, 1.2-1.5, np.sqrt(1.2+1.5), dt=0.01, tmax= t)
plt.stem(temps2, valeurs2, label = 'loi theorique', linefmt="r", markerfmt="ro", basefmt="None")
