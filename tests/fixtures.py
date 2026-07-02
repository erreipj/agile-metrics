import pandas as pd

def make_sprint_df():
    """
    Crée un DataFrame de test avec des données connues.
    """
    return pd.DataFrame({
        'sprintId': [1, 2, 3],
        'sprintName': ['Sprint 1', 'Sprint 2', 'Sprint 3'],
        'sprintStartDate': pd.to_datetime(['2026-06-15', '2026-06-29', '2026-07-13']),
        'sprintCompleteDate': pd.to_datetime(['2026-06-29', '2026-07-13', '2026-07-28']),
        'ticketCreatedDate': pd.to_datetime(['2026-06-19', '2026-07-09', '2026-07-22']),
        'ticketResolvedDate': pd.to_datetime(['2026-06-28', '2026-07-12', '2026-07-27']),
        'issueStatus': ['Done', 'Done', 'Done'],
        'issueSprint': ['1', '2', '3'],
        'completedIssuesEstimateSum': [10.0, 20.0, 30.0],
        'completedIssuesCount': [8.0, 9.0, 9.0],
        'totalNumberOfIssues': [10.0, 12.0, 10.0]
    })