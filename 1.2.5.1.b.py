N2_vals_b = []
for _ in range(N):
    T, ask_empty = Queues_Hawkes(LAM_PLUS, LAM_MINUS, ALPHA, BETA, Q_ASK, Q_BID)
    if not ask_empty:
        N2_vals_b.append(simulate_second_limit(LAM_PLUS_2, LAM_MINUS_2, Q2_0, T))


N2_marginal = []
for _ in range(N):
    T, _ = Queues_Hawkes(LAM_PLUS, LAM_MINUS, ALPHA, BETA, Q_ASK, Q_BID)
    N2_marginal.append(simulate_second_limit(LAM_PLUS_2, LAM_MINUS_2, Q2_0, T))

bins = np.arange(0, max(max(N2_vals_b), max(N2_marginal)) + 2) - 0.5
fig, ax = plt.subplots(figsize=(10, 5))
fig.suptitle("Simulation de N2+ sachant que N1-=0", fontweight="bold")

ax.hist(N2_marginal, bins=bins, density=True, color="yellow",   alpha=0.5,
        rwidth=0.8, label="Marginale (sans cond.)")
ax.hist(N2_vals_b,   bins=bins, density=True, color="brown", alpha=0.5,
        rwidth=0.8, label="N+2 | N+1 touche 0")
ax.axvline(np.mean(N2_marginal), color="yellow",   lw=2, ls="--",
           label=f"Moy. marginale = {np.mean(N2_marginal):.1f}")
ax.axvline(np.mean(N2_vals_b),   color="brown", lw=2,
           label=f"Moy. cond. = {np.mean(N2_vals_b):.1f}")
ax.set(xlabel="N+2 au temps τ", ylabel="Densité",
       title=f"Conditionnelle  vs Marginale ")
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
