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

### Sprint Completion Rate
Ratio between committed tickets at the start of a sprint and tickets actually delivered.
Measures the team's ability to meet its commitments and identifies over-engagement patterns.

### Work In Progress (WIP)
Number of tickets actively in progress but not completed at the end of each sprint.
Helps identify bottlenecks and flow inefficiencies.

### Throughput
Number of tickets delivered per week, regardless of story points.
A flow-based metric that complements velocity for more reliable forecasting.

### Monte Carlo Forecasting
Probabilistic simulation based on historical throughput data.
Answers the question: "Given a backlog of N tickets, what is the probability of delivering everything within X sprints?"
Returns delivery forecasts at 50%, 85%, and 95% confidence levels.

---

## Dataset

Data sourced from a public GitHub repository containing real Jira sprint data from 4 open source projects (Spring XD, Meso, Aurora, UserGrid): [AgileScrumSprintVelocityDataSet](https://github.com/RandulaKoralage/AgileScrumSprintVelocityDataSet).

> **Dataset limitations:** This dataset does not include individual ticket creation dates. As a result, Lead Time and Cycle Time are both approximated from sprint duration (start date to complete date). In a real Jira export, Lead Time would be calculated from ticket creation date to delivery date, and Cycle Time from the moment work starts on a ticket. The `lead_time.py` script supports both calculation modes — exact and approximate — depending on column availability in `config.yml`.

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

monte_carlo:
  backlog_size: 50
  simulations: 10000
```

---

## Tech stack

- Python 3.x
- pandas
- matplotlib
- numpy
- pyyaml

---

## Project structure

```
agile-metrics/
├── data/               # Raw dataset (not versioned)
├── src/                # Source code
│   ├── velocity.py
│   ├── cycle_time.py
│   ├── lead_time.py
│   ├── completion_rate.py
│   ├── work_in_progress.py
│   ├── throughput.py
│   └── monte_carlo.py
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
- [x] Sprint Completion Rate
- [x] Work In Progress
- [x] Throughput
- [x] Monte Carlo Forecasting
- [ ] Dockerization
- [ ] Unit testing
- [ ] Jira API integration

---

## About

This project is part of my continuous learning path as a Product Owner and Agile Coach.
It reflects my interest in data-driven product management and the use of AI-assisted development.