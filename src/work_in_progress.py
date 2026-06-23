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

# Calcul du WIP
wip = df_sprints[[cols['sprint_name'], cols['issues_not_completed']]].copy()
wip.columns = ['sprint_name', 'wip']

# Moyenne globale
avg_wip = wip['wip'].mean()

print("=== WORK IN PROGRESS PAR SPRINT ===")
print(wip)
print(f"\nWIP moyen : {avg_wip:.1f} tickets non terminés par sprint")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(wip['sprint_name'], wip['wip'], color='tomato')
ax.axhline(y=avg_wip, color='red', linestyle='--', label=f'Moyenne : {avg_wip:.1f} tickets')
ax.set_title('Work In Progress (tickets non terminés) par sprint', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Nombre de tickets')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/work_in_progress.png')
plt.show()

print("\nGraphique sauvegardé dans charts/work_in_progress.png")