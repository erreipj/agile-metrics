import pandas as pd
import matplotlib.pyplot as plt
import yaml

# Chargement de la configuration
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

# Raccourcis pour la lisibilité
cols = config['columns']
dataset = config['dataset']

# Chargement des données
df_sprints = pd.read_csv(dataset['sprints_file'])

# Calcul du Throughput en tickets par semaine
df_sprints['throughput'] = (
    df_sprints[cols['completed_issues_count']] / df_sprints[cols['sprint_length']] * 7
).round(1)

# On garde les colonnes utiles
throughput = df_sprints[[cols['sprint_name'], 'throughput']].dropna()

# Moyenne globale
avg_throughput = throughput['throughput'].mean()

print("=== THROUGHPUT PAR SPRINT ===")
print(throughput)
print(f"\nThroughput moyen : {avg_throughput:.1f} tickets/semaine")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(throughput[cols['sprint_name']], throughput['throughput'], color='steelblue')
ax.axhline(y=avg_throughput, color='red', linestyle='--', label=f'Moyenne : {avg_throughput:.1f} tickets/semaine')
ax.set_title('Throughput par sprint', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Tickets livrés par semaine')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/throughput.png')
plt.show()

print("\nGraphique sauvegardé dans charts/throughput.png")