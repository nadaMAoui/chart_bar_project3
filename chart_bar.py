import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")

# Fetch the data from the database
query = "SELECT capitaux_propres, financement_permanent, autonomie_financière FROM your_table"
df = pd.read_sql(query, conn)

# Disconnect from the database
conn.close()

# Extract the required columns
capitaux_propres = df['capitaux_propres']
financement_permanent = df['financement_permanent']
autonomie_financiere = df['autonomie_financière']

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
