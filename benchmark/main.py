import csv
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

from typing import List
import os

headers: List[str] = ['Participant', 'Trial', 'Manual_Setup_Time', 'Docker_Setup_Time']

data: List[List[int]] = []

# Artificial data right now: Generate data for 6 participants over 10 trials (demo is in minutes - rounded) - though, in real won't be 10 trials. - maybe 3 trials.

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'setup_times.csv')

for participant in range(1, 7):
    for trial in range(1, 11): 
        # For the first trial, Docker setup time might be longer due to initial setup.. Hopefully, reduced with my Documentation.
        if trial == 1:
            manual_time: int = random.randint(30, 80)
            docker_time: int = random.randint(40, 100)
        else:
            # For the subsequent trials, Docker setup time is significantly reduced as the environment is already set up!
            manual_time: int = random.randint(30, 60)
            docker_time: int = random.randint(1, 5)
        data.append([participant, trial, manual_time, docker_time])

# Writes artificial data to CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

df: pd.DataFrame = pd.read_csv(csv_file_path)

# Calculate average setup time for each trial
average_times: pd.DataFrame = df.groupby('Trial').mean()[['Manual_Setup_Time', 'Docker_Setup_Time']]

# Calculate cumulative setup time for each participant
df['Cumulative_Manual_Time'] = df.groupby('Participant')['Manual_Setup_Time'].cumsum()
df['Cumulative_Docker_Time'] = df.groupby('Participant')['Docker_Setup_Time'].cumsum()

# Calculate total time saved using Docker
total_time_saved: int = df['Cumulative_Manual_Time'].sum() - df['Cumulative_Docker_Time'].sum()

print(f"Total time saved using Docker: {total_time_saved} minutes, or {round(total_time_saved / 60, 2)} hours in a 10 trial experiment.")

sns.set_theme()
plt.figure(figsize=(10, 6))
plt.plot(average_times.index, average_times['Manual_Setup_Time'], marker='o', label='Manual Setup Time')
plt.plot(average_times.index, average_times['Docker_Setup_Time'], marker='o', label='Docker Setup Time')

plt.title('Average Setup Times for Manual and Docker Methods', fontsize=16)
plt.xlabel('Trial', fontsize=14)
plt.ylabel('Time (in minutes - rounded)', fontsize=14)


plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.grid(True)
plt.show()


"""
TODO: 
1. Write Rules for the experiment.
2. Write Instructions for the experiment.
3. Send Rules and Instructions to the participants.
4. Conduct the experiment.
5. Collect the data.
6. Compare to variables like cost per hour of median developer in Austria.
In between: Search for other trusted sources to compare the results to.
"""