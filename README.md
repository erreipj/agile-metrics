Agile Metrics

A Python project to track and visualize agile metrics — operational and strategic — from a Jira dataset.
Built as a personal learning project to deepen Python and data analysis skills in a product management context.

Metrics covered
    Velocity
        Average number of story points delivered per sprint.
        Helps the team and stakeholders understand the team's delivery capacity over time.
    Cycle Time
        Average time between when a ticket is started and when it is delivered.
        Measures the fluidity of the delivery flow and helps identify bottlenecks.
    Lead Time
        Average time between when a ticket is created and when it is delivered.
        Measures the overall responsiveness of the team from idea to production.

Dataset

Data sourced from a public Jira dataset available on Kaggle.

Tech stack

Python 3.14.4
pandas
matplotlib

Project structure

agile-metrics/
├── data/               # Raw dataset (not versioned)
├── notebooks/          # Exploratory analysis
├── src/                # Source code
│   ├── velocity.py
│   ├── cycle_time.py
│   └── lead_time.py
├── charts/             # Generated visualizations
├── requirements.txt
└── README.md

Roadmap

 Velocity
 Cycle Time
 Lead Time
 Sprint Completion Rate
 WIP (Work In Progress)
 Throughput
 Monte Carlo Forecasting


About

This project is part of my continuous learning path as a Product Owner and Agile Coach.
It reflects my interest in data-driven product management and the use of AI-assisted development.