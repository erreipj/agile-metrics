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
df_issues = pd.read_csv(dataset['issues_file'])


def calculate_lead_time_exact(df_issues, cols):
    """
    Calcul exact du Lead Time par ticket.
    Nécessite les colonnes ticket_created_date et ticket_resolved_date dans le dataset.
    Lead Time = date de résolution - date de création du ticket.
    """
    df = df_issues.copy()
    df[cols['ticket_created_date']] = pd.to_datetime(
        df[cols['ticket_created_date']], format=cols['date_format']
    )
    df[cols['ticket_resolved_date']] = pd.to_datetime(
        df[cols['ticket_resolved_date']], format=cols['date_format']
    )
    df['lead_time'] = (
        df[cols['ticket_resolved_date']] - df[cols['ticket_created_date']]
    ).dt.days
    df_done = df[df[cols['issue_status']] == cols['status_done_value']]
    lead_time_by_sprint = df_done.groupby(cols['issue_sprint'])['lead_time'].mean().reset_index()
    lead_time_by_sprint.columns = [cols['sprint_name'], 'lead_time']
    return lead_time_by_sprint


def calculate_lead_time_approximate(df_issues, df_sprints, cols):
    """
    Calcul approximatif du Lead Time basé sur la durée du sprint.
    Utilisé quand les dates individuelles de création de ticket ne sont pas disponibles.
    Lead Time ≈ durée du sprint (sprintStartDate → sprintCompleteDate).
    """
    df_sprints = df_sprints.copy()
    df_sprints[cols['sprint_start_date']] = pd.to_datetime(
        df_sprints[cols['sprint_start_date']], format=cols['date_format']
    )
    df_sprints[cols['sprint_complete_date']] = pd.to_datetime(
        df_sprints[cols['sprint_complete_date']], format=cols['date_format']
    )
    df_sprints['sprint_duration'] = (
        df_sprints[cols['sprint_complete_date']] - df_sprints[cols['sprint_start_date']]
    ).dt.days

    df_merged = df_issues.merge(
        df_sprints[[cols['sprint_id'], cols['sprint_name'], 'sprint_duration']],
        left_on=cols['issue_sprint'],
        right_on=cols['sprint_id'],
        how='left'
    )
    df_done = df_merged[
        (df_merged[cols['issue_status']] == cols['status_done_value']) &
        (df_merged['sprint_duration'].notna())
    ]
    lead_time_by_sprint = df_done.groupby(cols['sprint_name'])['sprint_duration'].mean().reset_index()
    lead_time_by_sprint.columns = [cols['sprint_name'], 'lead_time']
    return lead_time_by_sprint


# Sélection du mode de calcul selon la config
if cols.get('ticket_created_date') and cols.get('ticket_resolved_date'):
    print("Mode : calcul exact (dates individuelles disponibles)")
    lead_time_by_sprint = calculate_lead_time_exact(df_issues, cols)
else:
    print("Mode : calcul approximatif (durée du sprint)")
    lead_time_by_sprint = calculate_lead_time_approximate(df_issues, df_sprints, cols)

# Moyenne globale
avg_lead_time = lead_time_by_sprint['lead_time'].mean()

print("=== LEAD TIME MOYEN PAR SPRINT ===")
print(lead_time_by_sprint)
print(f"\nLead Time moyen global : {avg_lead_time:.1f} jours")

# Visualisation
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(lead_time_by_sprint[cols['sprint_name']], lead_time_by_sprint['lead_time'], color='seagreen')
ax.axhline(y=avg_lead_time, color='red', linestyle='--', label=f'Moyenne : {avg_lead_time:.1f} jours')
ax.set_title('Lead Time moyen par sprint', fontsize=14)
ax.set_xlabel('Sprint')
ax.set_ylabel('Durée (jours)')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/lead_time.png')
plt.show()

print("\nGraphique sauvegardé dans charts/lead_time.png")