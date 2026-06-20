import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df_sprints = pd.read_csv('data/Spring XD Sprints.csv')

# Conversion des dates
df_sprints['sprintStartDate'] = pd.to_datetime(df_sprints['sprintStartDate'], format='%d-%b-%y')
df_sprints['sprintCompleteDate'] = pd.to_datetime(df_sprints['sprintCompleteDate'], format='%d-%b-%y')

# Calcul du Cycle Time en jours
df_sprints['cycle_time'] = (df_sprints['sprintCompleteDate'] - df_sprints['sprintStartDate']).dt.days

# Suppression des sprints sans date de complétion
cycle_time = df_sprints[['sprintId', 'sprintName', 'cycle_time']].dropna()

# Moyenne
avg_cycle_time = cycle_time['cycle_time'].mean()

print("=== CYCLE TIME PAR SPRINT ===")
print(cycle_time)
print(f"\nCycle Time moyen : {avg_cycle_time:.1f} jours")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(cycle_time['sprintName'], cycle_time['cycle_time'], color='darkorange')
ax.axhline(y=avg_cycle_time, color='red', linestyle='--', label=f'Moyenne : {avg_cycle_time:.1f} jours')
ax.set_title('Cycle Time par sprint — Spring XD', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Durée (jours)')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/cycle_time.png')
plt.show()

print("\nGraphique sauvegardé dans charts/cycle_time.png")