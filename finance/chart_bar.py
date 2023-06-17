import pandas as pd
import matplotlib.pyplot as plt
from finance.models import FinancialMetrics

def generate_bar_chart(capitaux_propres, financement_permanent, autonomie_financiere):
    # Extract the required columns
    capitaux_propres = pd.Series(capitaux_propres)
    financement_permanent = pd.Series(financement_permanent)
    autonomie_financiere = pd.Series(autonomie_financiere)

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))
    bar_width = 0.4
    opacity = 0.8

    # Create the bar chart
    rects = ax.bar(range(len(capitaux_propres)), autonomie_financiere, bar_width,
                   alpha=opacity, color='steelblue', edgecolor='black')

    # Customize the chart
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Autonomie Financière')
    ax.set_title('Autonomie Financière')

    # Add data labels to the bars
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height,
                f'{height:.2f}', ha='center', va='bottom')

    # Add a grid
    ax.grid(axis='y', linestyle='--')

    # Remove the top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Show the chart
    plt.tight_layout()
    plt.show()

# Retrieve data from the database
financial_metrics = FinancialMetrics.objects.all()
capitaux_propres_data = [metric.capitaux_propres for metric in financial_metrics]
financement_permanent_data = [metric.financement_permanent for metric in financial_metrics]
autonomie_financiere_data = [metric.autonomie_financiere for metric in financial_metrics]

# Generate the bar chart
generate_bar_chart(capitaux_propres_data, financement_permanent_data, autonomie_financiere_data)
