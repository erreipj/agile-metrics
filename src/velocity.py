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

# Calcul de la velocity
velocity = df_sprints[[cols['sprint_id'], cols['sprint_name'], cols['completed_points']]].copy()
velocity.columns = [cols['sprint_id'], cols['sprint_name'], 'velocity']

# Velocity moyenne
avg_velocity = velocity['velocity'].mean()

print("=== VELOCITY PAR SPRINT ===")
print(velocity)
print(f"\nVelocity moyenne : {avg_velocity:.1f} points")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(velocity[cols['sprint_name']], velocity['velocity'], color='steelblue')
ax.axhline(y=avg_velocity, color='red', linestyle='--', label=f'Moyenne : {avg_velocity:.1f} pts')
ax.set_title('Velocity par sprint — Spring XD', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Story Points livrés')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/velocity.png')
plt.show()

print("\nGraphique sauvegardé dans charts/velocity.png")