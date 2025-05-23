# Functional Specification: Cubs vs. White Sox Monte Carlo Simulation

## Project Title
Chicago Cubs vs. Chicago White Sox Game Outcome Simulation using Monte Carlo Methods

## Purpose
To simulate the outcome of a baseball game between the Chicago Cubs and the Chicago White Sox using historical run data and Monte Carlo techniques. The simulation estimates:
- Average runs per team
- Win probabilities
- Tie probabilities
- Implied betting odds
- Run distribution histograms

## Inputs
1. **Historical Game Data (2023–2024)**
   - Source: MLB box scores or manually collected data
   - Format: CSV or in-code Python list
   - Fields: Number of runs scored per game

2. **Simulation Parameters**
   - Number of simulations (e.g., 100,000)

## Core Logic
1. Load historical runs scored for each team.
2. Build an empirical probability distribution for each team’s run output.
3. Run a Monte Carlo simulation to generate game outcomes:
   - For each simulation:
     - Randomly sample a run score for each team based on their empirical distribution.
     - Determine the outcome (win/loss/tie).
4. Track and aggregate:
   - Win counts
   - Average scores
   - Score margins
   - Score distributions

## Outputs
1. **Console Output**
   - Predicted average score per team
   - Win percentages for each team
   - Tie percentage
   - Implied betting odds

2. **Files (stored in `/results/`)**
   - `score_distributions.png`: Histogram of run distributions
   - `simulation_summary.txt`: Summary stats
   - `implied_odds.txt`: Betting odds derived from simulation results

## Output Destination
All results are saved in the `results/` folder.

## Assumptions
- Each game’s outcome is independent.
- No consideration of injuries, weather, or starting pitchers (can be added later).
- Simulation uses historical runs scored, not detailed play-by-play data.

## Future Enhancements
- Include pitcher and park factors
- Weight recent games more heavily
- Add confide
