import pandas as pd
import pytest
from src.lead_time import calculate_lead_time_exact, calculate_lead_time_approximate, calculate_average_lead_time
from tests.fixtures import make_sprint_df

COLS = {
    'sprint_id': 'sprintId',
    'sprint_name': 'sprintName',
    'sprint_start_date': 'sprintStartDate',
    'sprint_complete_date': 'sprintCompleteDate',
    'ticket_created_date': 'ticketCreatedDate',
    'ticket_resolved_date': 'ticketResolvedDate',
    'date_format': '%Y-%m-%d',
    'issue_status': 'issueStatus',
    'issue_sprint': 'issueSprint',
    'status_done_value': 'Done'
}

def test_calculate_lead_time_exact_columns():
    """Vérifie que le DataFrame retourné a les bonnes colonnes."""
    df = make_sprint_df()
    result = calculate_lead_time_exact(df, COLS)
    assert list(result.columns) == ['sprintName', 'lead_time']

def test_calculate_lead_time_exact_values():
    """Vérifie que les valeurs de lead_time sont correctes."""
    df = make_sprint_df()
    result = calculate_lead_time_exact(df, COLS)
    assert list(result['lead_time']) == [9.0, 3.0, 5.0]

def test_calculate_lead_time_exact_row_count():
    """Vérifie que le nombre de lignes est correct."""
    df = make_sprint_df()
    result = calculate_lead_time_exact(df, COLS)
    assert len(result) == 3

def test_calculate_average_lead_time_exact():
    """Vérifie que la moyenne est correcte."""
    df = make_sprint_df()
    lead_time_by_sprint = calculate_lead_time_exact(df, COLS)
    avg = calculate_average_lead_time(lead_time_by_sprint)
    assert avg == pytest.approx(5.66, abs=0.01)

def test_calculate_average_lead_time_single_ticket():
    """Vérifie le cas avec un seul ticket."""
    df = pd.DataFrame({
        'ticketCreatedDate': pd.to_datetime(['2026-06-19']),
        'ticketResolvedDate': pd.to_datetime(['2026-06-28']),
        'issueStatus': ['Done'],
        'issueSprint': [1]
    })
    lead_time_by_sprint = calculate_lead_time_exact(df, COLS)
    avg = calculate_average_lead_time(lead_time_by_sprint)
    assert avg == 9.0


def test_calculate_lead_time_empty_df():
    """Vérifie le comportement avec un DataFrame vide."""
    df = pd.DataFrame({
    'ticketCreatedDate': pd.to_datetime([]),
    'ticketResolvedDate': pd.to_datetime([]),
    'issueStatus': pd.Series([], dtype='str'),
    'issueSprint': pd.Series([], dtype='int64')
    })
    result = calculate_lead_time_exact(df, COLS)
    assert len(result) == 0