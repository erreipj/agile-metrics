import pandas as pd
import pytest
from src.cycle_time import calculate_cycle_time, calculate_average_cycle_time
from tests.fixtures import make_sprint_df

COLS = {
    'sprint_id': 'sprintId',
    'sprint_name': 'sprintName',
    'sprint_start_date': 'sprintStartDate',
    'sprint_complete_date': 'sprintCompleteDate'
}

def test_calculate_cycle_time_columns():
    """Vérifie que le DataFrame retourné a les bonnes colonnes."""
    df = make_sprint_df()
    result = calculate_cycle_time(df, COLS)
    assert list(result.columns) == ['sprintId', 'sprintName', 'cycle_time']

def test_calculate_cycle_time_values():
    """Vérifie que les valeurs de cycle_time sont correctes."""
    df = make_sprint_df()
    result = calculate_cycle_time(df, COLS)
    assert list(result['cycle_time']) == [14.0, 14.0, 15.0]

def test_calculate_cycle_time_row_count():
    """Vérifie que le nombre de lignes est correct."""
    df = make_sprint_df()
    result = calculate_cycle_time(df, COLS)
    assert len(result) == 3

def test_calculate_average_cycle_time():
    """Vérifie que la moyenne est correcte."""
    df = make_sprint_df()
    cycle_time = calculate_cycle_time(df, COLS)
    assert calculate_average_cycle_time(cycle_time) == pytest.approx(14.33, abs=0.01)

def test_calculate_average_cycle_time_single_sprint():
    """Vérifie le cas avec un seul sprint."""
    df = pd.DataFrame({
        'sprintId': [1],
        'sprintName': ['Sprint 1'],
        'sprintStartDate': pd.to_datetime(['2026-06-15']),
        'sprintCompleteDate': pd.to_datetime(['2026-06-29']),
    })
    cycle_time = calculate_cycle_time(df, COLS)
    avg = calculate_average_cycle_time(cycle_time)
    assert avg == 14.0


def test_calculate_cycle_time_empty_df():
    """Vérifie le comportement avec un DataFrame vide."""
    df = pd.DataFrame({
        'sprintId': [],
        'sprintName': [],
        'sprintStartDate': pd.to_datetime([]),
        'sprintCompleteDate': pd.to_datetime([]),
    })
    result = calculate_cycle_time(df, COLS)
    assert len(result) == 0