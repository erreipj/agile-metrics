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

# Conversion des dates
df_sprints[cols['sprint_start_date']] = pd.to_datetime(
    df_sprints[cols['sprint_start_date']], 
    format=cols['date_format']
)
df_sprints[cols['sprint_complete_date']] = pd.to_datetime(
    df_sprints[cols['sprint_complete_date']], 
    format=cols['date_format']
)

# Calcul du Cycle Time en jours
df_sprints['cycle_time'] = (
    df_sprints[cols['sprint_complete_date']] - df_sprints[cols['sprint_start_date']]
).dt.days

# Suppression des sprints sans date de complétion
cycle_time = df_sprints[[cols['sprint_id'], cols['sprint_name'], 'cycle_time']].dropna()

# Moyenne
avg_cycle_time = cycle_time['cycle_time'].mean()

print("=== CYCLE TIME PAR SPRINT ===")
print(cycle_time)
print(f"\nCycle Time moyen : {avg_cycle_time:.1f} jours")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(cycle_time[cols['sprint_name']], cycle_time['cycle_time'], color='darkorange')
ax.axhline(y=avg_cycle_time, color='red', linestyle='--', label=f'Moyenne : {avg_cycle_time:.1f} jours')
ax.set_title('Cycle Time par sprint', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Durée (jours)')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/cycle_time.png')
plt.show()

print("\nGraphique sauvegardé dans charts/cycle_time.png")