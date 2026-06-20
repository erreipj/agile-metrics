import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df_issues = pd.read_csv('data/Spring XD Issues.csv')
df_sprints = pd.read_csv('data/Spring XD Sprints.csv')

# Conversion des dates
df_sprints['sprintStartDate'] = pd.to_datetime(df_sprints['sprintStartDate'], format='%d-%b-%y')
df_sprints['sprintCompleteDate'] = pd.to_datetime(df_sprints['sprintCompleteDate'], format='%d-%b-%y')

# Calcul de la durée par sprint
df_sprints['sprint_duration'] = (df_sprints['sprintCompleteDate'] - df_sprints['sprintStartDate']).dt.days

# Jointure issues + sprints sur l'id du sprint
df_merged = df_issues.merge(
    df_sprints[['sprintId', 'sprintName', 'sprint_duration']],
    left_on='sprint',
    right_on='sprintId',
    how='left'
)

# On garde uniquement les tickets Done avec une durée connue
df_done = df_merged[(df_merged['status'] == 'Done') & (df_merged['sprint_duration'].notna())]

# Lead Time moyen par sprint
lead_time_by_sprint = df_done.groupby('sprintName')['sprint_duration'].mean().reset_index()
lead_time_by_sprint.columns = ['sprint_name', 'lead_time']

# Moyenne globale
avg_lead_time = lead_time_by_sprint['lead_time'].mean()

print("=== LEAD TIME MOYEN PAR SPRINT ===")
print(lead_time_by_sprint)
print(f"\nLead Time moyen global : {avg_lead_time:.1f} jours")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(lead_time_by_sprint['sprint_name'], lead_time_by_sprint['lead_time'], color='seagreen')
ax.axhline(y=avg_lead_time, color='red', linestyle='--', label=f'Moyenne : {avg_lead_time:.1f} jours')
ax.set_title('Lead Time moyen par sprint — Spring XD', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Durée (jours)')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/lead_time.png')
plt.show()

print("\nGraphique sauvegardé dans charts/lead_time.png")