import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yaml

# Chargement de la configuration
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

cols = config['columns']
dataset = config['dataset']
mc_config = config['monte_carlo']

# Chargement des données
df_sprints = pd.read_csv(dataset['sprints_file'])

# Historique du throughput (tickets livrés par sprint)
throughput_history = df_sprints[cols['completed_issues_count']].dropna().values

# Paramètres de la simulation
backlog_size = mc_config['backlog_size']
n_simulations = mc_config['simulations']

print(f"Simulation Monte Carlo — Backlog : {backlog_size} tickets, {n_simulations} simulations")

# Simulation
sprints_needed = []

for _ in range(n_simulations):
    delivered = 0
    sprints = 0
    while delivered < backlog_size:
        # On tire aléatoirement un throughput depuis l'historique
        delivered += np.random.choice(throughput_history)
        sprints += 1
    sprints_needed.append(sprints)

sprints_needed = np.array(sprints_needed)

# Calcul des percentiles
p50 = int(np.percentile(sprints_needed, 50))
p85 = int(np.percentile(sprints_needed, 85))
p95 = int(np.percentile(sprints_needed, 95))

print(f"\nPour livrer {backlog_size} tickets :")
print(f"  50% de chances en {p50} sprints ou moins")
print(f"  85% de chances en {p85} sprints ou moins")
print(f"  95% de chances en {p95} sprints ou moins")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(sprints_needed, bins=range(min(sprints_needed), max(sprints_needed) + 1),
        color='steelblue', edgecolor='white', alpha=0.8)
ax.axvline(x=p50, color='green', linestyle='--', label=f'50% → {p50} sprints')
ax.axvline(x=p85, color='orange', linestyle='--', label=f'85% → {p85} sprints')
ax.axvline(x=p95, color='red', linestyle='--', label=f'95% → {p95} sprints')
ax.set_title(f'Monte Carlo — Nombre de sprints pour livrer {backlog_size} tickets', fontsize=14)
ax.set_xlabel('Nombre de sprints')
ax.set_ylabel('Nombre de simulations')
ax.legend()
plt.tight_layout()
plt.savefig('charts/monte_carlo.png')
plt.show()

print("\nGraphique sauvegardé dans charts/monte_carlo.png")