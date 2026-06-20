# Agile Metrics

A Python project to track and visualize agile metrics — operational and strategic — from a Jira dataset.

Built as a personal learning project to deepen Python and data analysis skills in a product management context.

---

## Metrics covered

### Velocity
Average number of story points delivered per sprint.
Helps the team and stakeholders understand the team's delivery capacity over time.

### Cycle Time
Average time between when a ticket is started and when it is delivered.
Measures the fluidity of the delivery flow and helps identify bottlenecks.

### Lead Time
Average time between when a ticket is created and when it is delivered.
Measures the overall responsiveness of the team from idea to production.

---

## Dataset

Data sourced from a public GitHub repository containing real Jira sprint data from 4 open source projects (Spring XD, Meso, Aurora, UserGrid): [AgileScrumSprintVelocityDataSet](https://github.com/RandulaKoralage/AgileScrumSprintVelocityDataSet).

> **Dataset limitations:** This dataset does not include individual ticket creation dates. As a result, Lead Time and Cycle Time are both approximated from sprint duration (start date to complete date). In a real Jira export, Lead Time would be calculated from ticket creation date to delivery date, and Cycle Time from the moment work starts on a ticket.

---

## Configuration

The project uses a `config.yml` file to map column names and file paths to the dataset. This makes the code agnostic to the dataset structure — to use it with a different Jira export, simply update `config.yml` without touching the source code.

```yaml
dataset:
  sprints_file: "data/Spring XD Sprints.csv"
  issues_file: "data/Spring XD Issues.csv"

columns:
  sprint_id: "sprintId"
  sprint_name: "sprintName"
  ...
```

---

## Tech stack

- Python 3.x
- pandas
- matplotlib
- pyyaml

---

## Project structure

```
agile-metrics/
├── data/               # Raw dataset (not versioned)
├── src/                # Source code
│   ├── velocity.py
│   ├── cycle_time.py
│   └── lead_time.py
├── charts/             # Generated visualizations
├── config.yml          # Dataset configuration
├── requirements.txt
└── README.md
```

---

## Roadmap

- [x] Velocity
- [x] Cycle Time
- [x] Lead Time
- [ ] Sprint Completion Rate
- [ ] WIP (Work In Progress)
- [ ] Throughput
- [ ] Monte Carlo Forecasting

---

## About

This project is part of my continuous learning path as a Product Owner and Agile Coach.
It reflects my interest in data-driven product management and the use of AI-assisted development.