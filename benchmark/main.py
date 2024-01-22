import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def after_startup(df):
    df_stats = df[df['Trial'] != 1].groupby('Participant').agg({'Manual_Setup_Time': ['mean', 'min', 'max'],
                                                                'Docker_Setup_Time': ['mean', 'min', 'max']}).reset_index()
    df_stats.columns = [' '.join(col).strip() for col in df_stats.columns.values]
    
    fig, ax = plt.subplots(figsize=(14, 7))
    positions = np.arange(len(df_stats['Participant']))
    width = 0.35

    rects1 = ax.bar(positions - width/2, df_stats['Manual_Setup_Time mean'], width, 
                    label='Manuelle Einrichtungszeit nach Erstversuch', color='blue', capsize=5)

    rects2 = ax.bar(positions + width/2, df_stats['Docker_Setup_Time mean'], width, 
                    label='Docker Einrichtungszeit nach Erstversuch', color='orange', capsize=5)

    # Min/Max
    ax.scatter(positions - width/2, df_stats['Manual_Setup_Time min'], color='white', edgecolor='black', zorder=5)
    ax.scatter(positions - width/2, df_stats['Manual_Setup_Time max'], color='white', edgecolor='black', zorder=5)
    ax.scatter(positions + width/2, df_stats['Docker_Setup_Time min'], color='white', edgecolor='black', zorder=5)
    ax.scatter(positions + width/2, df_stats['Docker_Setup_Time max'], color='white', edgecolor='black', zorder=5)

    def autolabel(rects, data):
        for rect, datum in zip(rects, data):
            height = rect.get_height()
            ax.annotate('{}'.format(round(datum, 2)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(5, 0),
                        textcoords="offset points",
                        ha='left', va='bottom', weight='bold', fontsize=14)

    autolabel(rects1, df_stats['Manual_Setup_Time mean'])
    autolabel(rects2, df_stats['Docker_Setup_Time mean'])

    ax.set_xlabel('Teilnehmer', fontsize=14, weight='bold')
    ax.set_ylabel('Einrichtungszeit in Minuten', fontsize=14, weight='bold')
    ax.set_title('Durchschnittliche Einrichtungszeit (Minuten) jeweils 3 Versuche', fontsize=24, weight='bold')
    ax.set_xticks(positions)
    ax.set_xticklabels(df_stats['Participant'])
    ax.legend(frameon=True, fontsize=19)

    plt.tight_layout()
    plt.show()


def startup(df):
    first_trial_df = df[df['Trial'] == 1]

    positions = np.arange(len(first_trial_df['Participant'].unique()))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(positions - width/2, first_trial_df['Manual_Setup_Time'], width, label='Manuelle Einrichtungszeit', color='blue')
    rects2 = ax.bar(positions + width/2, first_trial_df['Docker_Setup_Time'], width, label='Docker Einrichtungszeit', color='orange')

    ax.set_ylabel('Einrichtungszeit in Minuten', fontsize=14, weight='bold')
    ax.set_xlabel('Teilnehmer', fontsize=14, weight='bold')
    ax.set_title('Vergleich der Ersten Einrichtungszeit nach Teilnehmer ', fontsize=18, weight='bold')
    ax.set_xticks(positions)
    ax.set_xticklabels(first_trial_df['Participant'].unique())
    ax.legend(frameon=True, fontsize=16)

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()
    plt.show()

    
def saved_time(df):
    """
    Stündlicher Lohn eines Softwareentwicklers in Österreich berechnet mit der Differenz zwischen verbrauchter manueller und Docker Einrichtungszeit
    Quelle: https://www.kununu.com/at/gehalt/softwareentwickler-in-15019
    Calc: https://www.finanz.at/steuern/lohnrechner/?calc=14270
    """

    diff_min = df['Manual_Setup_Time'].sum() - df['Docker_Setup_Time'].sum()
    diff_hours = diff_min / 60
    average_sal_per_hour = 22.35
    
    total_cost_savings = diff_hours * average_sal_per_hour 
    total_cost_savings 

    return print(f"Das Gesamtersparnis durch die Verwendung von Docker beträgt in den insgesamt 16 Versuchen: {total_cost_savings.round(2)}€")


if __name__ == '__main__':
    data = {
    "Participant": ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D'],
    "Trial": [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
    "Manual_Setup_Time": [43.21, 38.49, 37.51, 37.44, 40.32, 39.53, 38.19, 37.22, 95.12, 44, 52, 54, 100.32, 62.03, 59.02, 58.22],
    "Docker_Setup_Time": [90.33, 2.15, 1.59, 1.49, 87.22, 1.59, 1.54, 1.42, 140.46, 3.12, 2.59, 2.32, 132.35, 2.31, 2.22, 2.21]
    }
    df = pd.DataFrame(data)
    startup(df)
    after_startup(df)
    saved_time(df)