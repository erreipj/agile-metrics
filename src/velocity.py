import pandas as pd
import matplotlib.pyplot as plt
import yaml


def load_config(config_path='config.yml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def calculate_velocity(df_sprints, cols):
    """
    Calcule la velocity par sprint.
    Retourne un DataFrame avec sprint_id, sprint_name et velocity.
    """
    velocity = df_sprints[[cols['sprint_id'], cols['sprint_name'], cols['completed_points']]].copy()
    velocity.columns = ['sprint_id', 'sprint_name', 'velocity']
    return velocity


def calculate_average_velocity(velocity_df):
    """
    Calcule la velocity moyenne à partir du DataFrame de velocity.
    """
    return velocity_df['velocity'].mean()


def plot_velocity(velocity_df, avg_velocity):
    """
    Génère et sauvegarde le graphique de velocity.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(velocity_df['sprint_name'], velocity_df['velocity'], color='steelblue')
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


if __name__ == "__main__":
    config = load_config()
    cols = config['columns']
    dataset = config['dataset']

    df_sprints = pd.read_csv(dataset['sprints_file'])

    velocity = calculate_velocity(df_sprints, cols)
    avg_velocity = calculate_average_velocity(velocity)

    print("=== VELOCITY PAR SPRINT ===")
    print(velocity)
    print(f"\nVelocity moyenne : {avg_velocity:.1f} points")

    plot_velocity(velocity, avg_velocity)