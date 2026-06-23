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

# Calcul du Sprint Completion Rate en %
df_sprints['completion_rate'] = (
    df_sprints[cols['completed_issues_count']] / df_sprints[cols['total_issues_count']] * 100
).round(1)

# On garde les colonnes utiles
completion = df_sprints[[cols['sprint_name'], 'completion_rate']].dropna()

# Moyenne globale
avg_completion = completion['completion_rate'].mean()

print("=== SPRINT COMPLETION RATE ===")
print(completion)
print(f"\nCompletion Rate moyen : {avg_completion:.1f}%")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(completion[cols['sprint_name']], completion['completion_rate'], color='mediumpurple')
ax.axhline(y=avg_completion, color='red', linestyle='--', label=f'Moyenne : {avg_completion:.1f}%')
ax.axhline(y=100, color='green', linestyle=':', label='Objectif : 100%')
ax.set_title('Sprint Completion Rate', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Taux de complétion (%)')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/completion_rate.png')
plt.show()

print("\nGraphique sauvegardé dans charts/completion_rate.png")