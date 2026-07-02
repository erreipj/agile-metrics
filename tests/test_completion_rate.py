import pandas as pd
import pytest
from src.completion_rate import calculate_completion_rate, calculate_average_completion_rate
from tests.fixtures import make_sprint_df

COLS = {
    'sprint_name': 'sprintName',
    'completed_issues_count': 'completedIssuesCount',
    'total_issues_count': 'totalNumberOfIssues'
}


def test_calculate_completion_rate_columns():
    """Vérifie que le DataFrame retourné a les bonnes colonnes."""
    df = make_sprint_df()
    result = calculate_completion_rate(df, COLS)
    assert list(result.columns) == ['sprintName', 'completion_rate']


def test_calculate_completion_rate_values():
    """Vérifie que les valeurs de completion_rate sont correctes."""
    df = make_sprint_df()
    result = calculate_completion_rate(df, COLS)
    assert list(result['completion_rate']) == [80.0, 75.0, 90.0]


def test_calculate_completion_rate_row_count():
    """Vérifie que le nombre de lignes est correct."""
    df = make_sprint_df()
    result = calculate_completion_rate(df, COLS)
    assert len(result) == 3


def test_calculate_average_completion_rate():
    """Vérifie que la moyenne est correcte."""
    df = make_sprint_df()
    completion = calculate_completion_rate(df, COLS)
    avg = calculate_average_completion_rate(completion)
    assert avg == pytest.approx(81.67, abs=0.01)


def test_calculate_completion_rate_single_sprint():
    """Vérifie le cas avec un seul sprint."""
    df = pd.DataFrame({
        'sprintName': ['Sprint 1'],
        'completedIssuesCount': [8.0],
        'totalNumberOfIssues': [10.0]
    })
    result = calculate_completion_rate(df, COLS)
    assert list(result['completion_rate']) == [80.0]


def test_calculate_completion_rate_perfect_sprint():
    """Vérifie le cas d'un sprint complété à 100%."""
    df = pd.DataFrame({
        'sprintName': ['Sprint 1'],
        'completedIssuesCount': [10.0],
        'totalNumberOfIssues': [10.0]
    })
    result = calculate_completion_rate(df, COLS)
    assert list(result['completion_rate']) == [100.0]


def test_calculate_completion_rate_empty_df():
    """Vérifie le comportement avec un DataFrame vide."""
    df = pd.DataFrame({
        'sprintName': [],
        'completedIssuesCount': [],
        'totalNumberOfIssues': []
    })
    result = calculate_completion_rate(df, COLS)
    assert len(result) == 0