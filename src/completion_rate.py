import pandas as pd
import matplotlib.pyplot as plt
import yaml


def load_config(config_path='config.yml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def calculate_completion_rate(df_sprints, cols):
    """
    Calcule le taux de complétion par sprint en %.
    Retourne un DataFrame avec sprint_name et completion_rate.
    """
    df = df_sprints.copy()
    df['completion_rate'] = (
        df[cols['completed_issues_count']] / df[cols['total_issues_count']] * 100
    ).round(1)
    completion = df[[cols['sprint_name'], 'completion_rate']].dropna()
    return completion


def calculate_average_completion_rate(completion_df):
    """
    Calcule le taux de complétion moyen.
    """
    return completion_df['completion_rate'].mean()


def plot_completion_rate(completion_df, avg_completion, cols):
    """
    Génère et sauvegarde le graphique du completion rate.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(completion_df[cols['sprint_name']], completion_df['completion_rate'], color='mediumpurple')
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


if __name__ == "__main__":
    config = load_config()
    cols = config['columns']
    dataset = config['dataset']

    df_sprints = pd.read_csv(dataset['sprints_file'])

    completion = calculate_completion_rate(df_sprints, cols)
    avg_completion = calculate_average_completion_rate(completion)

    print("=== SPRINT COMPLETION RATE ===")
    print(completion)
    print(f"\nCompletion Rate moyen : {avg_completion:.1f}%")

    plot_completion_rate(completion, avg_completion, cols)