LAM_PLUS    = 1.0
LAM_MINUS   = 1.1
ALPHA       = 0.5
BETA        = 0.5
Q_ASK       = 10
Q_BID       = 10
LAM_PLUS_2  = 1.2    
LAM_MINUS_2 = 1.5      
Q2_0        = 10     
N           = 2000

def Queues_Hawkes(lam_plus, lam_minus, alpha, beta, Q_ask, Q_bid):
    Q1, Qm1 = Q_ask, Q_bid
    t        = 0.0
    D1       = 0.0   
    DM1      = 0.0   

    while Q1 > 0 and Qm1 > 0:
        lm1  = max(0.0, lam_minus + D1)
        lmM1 = max(0.0, lam_minus + DM1)
        total = lam_plus + lm1 + lam_plus + lmM1

        dt    = np.random.exponential(1.0 / total)
        t    += dt
        decay = np.exp(-beta * dt)
        D1   *= decay;  DM1 *= decay

        lm1  = max(0.0, lam_minus + D1)
        lmM1 = max(0.0, lam_minus + DM1)
        total = lam_plus + lm1 + lam_plus + lmM1

        u = np.random.random() * total

        if   u < lam_plus:                    
            Q1  += 1;  D1  += alpha;  DM1 += alpha
        elif u < lam_plus + lm1:           
            Q1  -= 1;  D1  -= alpha;  DM1 -= alpha
        elif u < 2*lam_plus + lm1:           
            Qm1 += 1;  DM1 += alpha;  D1  += alpha
        else:                                   
            Qm1 -= 1;  DM1 -= alpha;  D1  -= alpha

    return t, (Q1 == 0)


def simulate_second_limit(lam_plus_2, lam_minus_2, Q2_0, T_stop):
    Q    = Q2_0
    t    = 0.0
    rate = lam_plus_2 + lam_minus_2
    p_up = lam_plus_2 / rate
    while True:
        dt = np.random.exponential(1.0 / rate)
        if t + dt > T_stop:
            break
        t += dt
        Q += 1 if np.random.random() < p_up else -1
        Q  = max(0, Q)  
    return Q


N2_vals_a = []
for _ in range(N):
    T, ask_empty = Queues_Hawkes(LAM_PLUS, LAM_MINUS, ALPHA, BETA, Q_ASK, Q_BID)
    if ask_empty:
        N2_vals_a.append(simulate_second_limit(LAM_PLUS_2, LAM_MINUS_2, Q2_0, T))


N2_marginal = []
for _ in range(N):
    T, _ = Queues_Hawkes(LAM_PLUS, LAM_MINUS, ALPHA, BETA, Q_ASK, Q_BID)
    N2_marginal.append(simulate_second_limit(LAM_PLUS_2, LAM_MINUS_2, Q2_0, T))

bins = np.arange(0, max(max(N2_vals_a), max(N2_marginal)) + 2) - 0.5
fig, ax = plt.subplots(figsize=(10, 5))
fig.suptitle("Simulation de N2+ sachant que N1+=0", fontweight="bold")

ax.hist(N2_marginal, bins=bins, density=True, color="gray",   alpha=0.5,
        rwidth=0.8, label="Marginale (sans cond.)")
ax.hist(N2_vals_a,   bins=bins, density=True, color="purple", alpha=0.5,
        rwidth=0.8, label="N+2 | N+1 touche 0")
ax.axvline(np.mean(N2_marginal), color="gray",   lw=2, ls="--",
           label=f"Moy. marginale = {np.mean(N2_marginal):.1f}")
ax.axvline(np.mean(N2_vals_a),   color="purple", lw=2,
           label=f"Moy. cond. = {np.mean(N2_vals_a):.1f}")
ax.set(xlabel="N+2 au temps τ", ylabel="Densité",
       title=f"Conditionnelle  vs Marginale ")
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
