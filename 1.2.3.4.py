N4 = 500
Q_range=np.arange(1,21)
moyennes=np.zeros((len(Q_range),len(Q_range)))

for i, Q1 in enumerate(Q_range):
    for j, Q2 in enumerate(Q_range):
       taus=[]
       for _ in range(N4):
          times, ask_vals, bid_vals, T, ask_empty = Queues(LAM_PLUS, LAM_MINUS, Q1, Q2)
          taus.append(T)
          moyennes[i,j]=np.mean(taus)
          

plt.imshow(moyennes, origin='lower',
           extent=[Q_range[0], Q_range[-1], Q_range[0], Q_range[-1]])
plt.colorbar(label="E[min(τ₁, τ₋₁)]")
plt.xlabel("Q₋₁(0)")
plt.ylabel("Q₁(0)")
plt.title("Temps moyen d'atteinte de 0")
plt.show()       

