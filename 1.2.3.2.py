def hitting_time_ask(LAM_PLUS, LAM_MINUS, Q_ASK):
    L = Q_ASK
    t = 0
    rate = LAM_PLUS + LAM_MINUS
    p_up = LAM_PLUS / rate
    while L > 0:
        t += np.random.exponential(1.0 / rate)
        L += 1 if np.random.random() < p_up else -1
    return t

taus_ask = [hitting_time_ask(LAM_PLUS, LAM_MINUS, Q_ASK) for _ in range(N2)]
plt.hist(taus_ask, bins=50, density=True, alpha=0.5, label="Simulation Poisson",color='purple')

def bm_hitting_sample(x, mu, sigma):
    mu_ig  = x / (-mu)
    lam_ig = x**2 / sigma**2
    v = np.random.normal()
    y = v**2
    r = (mu_ig + mu_ig**2*y/(2*lam_ig)
         - mu_ig/(2*lam_ig)*np.sqrt(4*mu_ig*lam_ig*y + mu_ig**2*y**2))
    return r if np.random.random() <= mu_ig/(mu_ig+r) else mu_ig**2/r

taus_bm = [bm_hitting_sample(Q_ASK, mu, sigma) for _ in range(N2)]
plt.hist(taus_bm, bins=50, density=True, alpha=0.5, label="Simulation BM",color='pink')

t_grid = np.linspace(0.1, max(taus)*1.1, 500)
pdf    = (Q_ASK / (sigma * np.sqrt(2*np.pi*t_grid**3))) \
         * np.exp(-(Q_ASK + mu*t_grid)**2 / (2*sigma**2*t_grid))
plt.plot(t_grid, pdf, color="blue", lw=2, label="Densité théorique BM")

plt.xlabel("Temps d'atteinte en 0")
plt.ylabel("Densité")
plt.title("Distribution du temps d'atteinte de 0")
plt.legend()
plt.show()
