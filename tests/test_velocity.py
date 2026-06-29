import pandas as pd
import pytest
from src.velocity import calculate_velocity, calculate_average_velocity


def make_sprint_df():
    """
    Crée un DataFrame de test avec des données connues.
    """
    return pd.DataFrame({
        'sprintId': [1, 2, 3],
        'sprintName': ['Sprint 1', 'Sprint 2', 'Sprint 3'],
        'completedIssuesEstimateSum': [10.0, 20.0, 30.0]
    })


COLS = {
    'sprint_id': 'sprintId',
    'sprint_name': 'sprintName',
    'completed_points': 'completedIssuesEstimateSum'
}


def test_calculate_velocity_columns():
    """Vérifie que le DataFrame retourné a les bonnes colonnes."""
    df = make_sprint_df()
    result = calculate_velocity(df, COLS)
    assert list(result.columns) == ['sprint_id', 'sprint_name', 'velocity']


def test_calculate_velocity_values():
    """Vérifie que les valeurs de velocity sont correctes."""
    df = make_sprint_df()
    result = calculate_velocity(df, COLS)
    assert list(result['velocity']) == [10.0, 20.0, 30.0]


def test_calculate_velocity_row_count():
    """Vérifie que le nombre de lignes est correct."""
    df = make_sprint_df()
    result = calculate_velocity(df, COLS)
    assert len(result) == 3


def test_calculate_average_velocity():
    """Vérifie que la moyenne est correcte."""
    df = make_sprint_df()
    velocity = calculate_velocity(df, COLS)
    avg = calculate_average_velocity(velocity)
    assert avg == 20.0


def test_calculate_average_velocity_single_sprint():
    """Vérifie le cas avec un seul sprint."""
    df = pd.DataFrame({
        'sprintId': [1],
        'sprintName': ['Sprint 1'],
        'completedIssuesEstimateSum': [42.0]
    })
    velocity = calculate_velocity(df, COLS)
    avg = calculate_average_velocity(velocity)
    assert avg == 42.0


def test_calculate_velocity_empty_df():
    """Vérifie le comportement avec un DataFrame vide."""
    df = pd.DataFrame({
        'sprintId': [],
        'sprintName': [],
        'completedIssuesEstimateSum': []
    })
    result = calculate_velocity(df, COLS)
    assert len(result) == 0