import pandas as pd
import matplotlib.pyplot as plt
import yaml

def load_config(config_path='config.yml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def calculate_cycle_time(df_sprints, cols):
    """
    Calcule le cycle time par sprint.
    Retourne un DataFrame avec sprint_id, sprint_name et cycle_time.
    """
    df_sprints['cycle_time'] = (
    df_sprints[cols['sprint_complete_date']] - df_sprints[cols['sprint_start_date']]
).dt.days
    # Suppression des sprints sans date de complétion
    cycle_time = df_sprints[[cols['sprint_id'], cols['sprint_name'], 'cycle_time']].dropna()
    return cycle_time

def calculate_average_cycle_time(cycle_time):
    """
    Calcule le cycle time moyen à partir du DataFrame de cycle time.
    """
    avg_cycle_time = cycle_time['cycle_time'].mean()
    return avg_cycle_time

def vizualize_cycle_time(cycle_time, avg_cycle_time, cols):
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

if __name__ == "__main__":
    config = load_config()
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

    cycle_time = calculate_cycle_time(df_sprints, cols)
    avg_cycle_time = calculate_average_cycle_time(cycle_time)

    print("=== CYCLE TIME PAR SPRINT ===")
    print(cycle_time)
    print(f"\nCycle Time moyen : {avg_cycle_time:.1f} jours")

    vizualize_cycle_time(cycle_time, avg_cycle_time, cols)

    print("\nGraphique sauvegardé dans charts/cycle_time.png")


