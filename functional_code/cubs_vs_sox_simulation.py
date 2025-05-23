import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Historical data 
cubs_2023_runs = [
    4, 1, 5, 6, 12, 2, 2, 10, 2, 3, 14, 3, 2, 3, 8, 3, 12, 4, 3, 7,
    13, 4, 3, 6, 3, 5, 2, 6, 5, 3, 5, 1, 1, 3, 6, 2, 1, 4, 1, 4,
    4, 4, 7, 4, 1, 1, 4, 4, 5, 2, 1, 4, 2, 1, 3, 4, 1, 2,
    2, 4, 3, 1, 4, 2, 3, 1, 2, 3, 5, 3, 4, 3, 5, 3, 2, 3,
    4, 2, 3, 3, 4, 2, 1, 3, 5, 4, 3, 4, 3, 2, 1, 3, 2, 3,
    4, 3, 5, 3, 4, 3, 5, 4, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3,
    5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3,
    4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4,
    3, 5
]
cubs_2024_runs = [
    3, 2, 9, 5, 12, 9, 9, 6, 5, 4, 3, 7, 2, 1, 6, 3, 5, 2, 4, 3,
    7, 5, 3, 6, 4, 2, 5, 3, 4, 2, 3, 1, 2, 3, 5, 4, 3, 2, 1, 3,
    4, 2, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2,
    3, 4
]
cubs_runs = cubs_2023_runs + cubs_2024_runs
cws_2023_runs = [
    3, 3, 4, 6, 3, 7, 6, 3, 4, 3, 3, 6, 2, 4, 3, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5, 2, 3, 4, 3, 5,
    2, 3
]
cws_2024_runs = [
    0, 6, 2, 0, 3, 1, 4, 2, 3, 1, 0, 5, 2, 3, 4, 1, 2, 3, 0, 1,
    2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1,
    2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1,
    2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1,
    2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1,
    2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1,
    2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1,
    2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1,
    2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 1,
    2, 3
]
white_sox_runs = cws_2023_runs + cws_2024_runs

# --- 1. Get empirical probability mass functions (PMFs) ---
def get_empirical_pmf(data):
    counts = Counter(data)
    total = sum(counts.values())
    values, probabilities = zip(*[(val, count / total) for val, count in counts.items()])
    return np.array(values), np.array(probabilities)

cubs_values, cubs_probs = get_empirical_pmf(cubs_runs)
sox_values, sox_probs = get_empirical_pmf(white_sox_runs)

# --- 2. Run Monte Carlo Simulation ---
num_simulations = 100_000

cubs_simulated_scores = np.random.choice(cubs_values, size=num_simulations, p=cubs_probs)
sox_simulated_scores = np.random.choice(sox_values, size=num_simulations, p=sox_probs)

# --- 3. Analyze Results ---
cubs_avg = np.mean(cubs_simulated_scores)
sox_avg = np.mean(sox_simulated_scores)

cubs_wins = np.sum(cubs_simulated_scores > sox_simulated_scores)
sox_wins = np.sum(sox_simulated_scores > cubs_simulated_scores)
ties = num_simulations - cubs_wins - sox_wins

print(f"\n Simulated Game Results ({num_simulations} games):")
print(f"Average Score - Cubs: {cubs_avg:.2f}, White Sox: {sox_avg:.2f}")
print(f"Cubs Win Probability: {cubs_wins / num_simulations:.2%}")
print(f"White Sox Win Probability: {sox_wins / num_simulations:.2%}")
print(f"Tie Probability: {ties / num_simulations:.2%}")

# Optional: implied odds
cubs_win_prob = cubs_wins / num_simulations
sox_win_prob = sox_wins / num_simulations

def implied_odds(prob):
    if prob == 0:
        return "∞"
    return f"+{int((1 / prob - 1) * 100)}" if prob < 0.5 else f"-{int((prob / (1 - prob)) * 100)}"

print(f"\n Implied Betting Odds:")
print(f"Cubs: {implied_odds(cubs_win_prob)}")
print(f"White Sox: {implied_odds(sox_win_prob)}")

# --- 4. Visualize Score Distributions ---
plt.hist(cubs_simulated_scores, bins=range(0, 16), alpha=0.6, label="Cubs", density=True)
plt.hist(sox_simulated_scores, bins=range(0, 16), alpha=0.6, label="White Sox", density=True)
plt.xlabel("Runs Scored")
plt.ylabel("Probability")
plt.title("Simulated Run Distributions")
plt.legend()
plt.show()






