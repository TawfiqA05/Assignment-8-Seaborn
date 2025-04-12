import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in planets dataset
planets = sns.load_dataset("planets")

# Preview the dataset
print(planets.head())

# 1. Scatter plot: Orbital period vs. Mass
plt.figure(figsize=(8, 5))
sns.scatterplot(data=planets, x='orbital_period', y='mass', hue='method')
plt.title('Orbital Period vs. Mass by Detection Method')
plt.xscale('log')  # log scale helps readability
plt.yscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Jupiter Masses)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 2. Line plot: Number of discoveries over time
discoveries_per_year = planets.groupby('year').size().reset_index(name='discoveries')
plt.figure(figsize=(8, 5))
sns.lineplot(data=discoveries_per_year, x='year', y='discoveries')
plt.title('Number of Planet Discoveries per Year')
plt.xlabel('Year')
plt.ylabel('Number of Discoveries')
plt.tight_layout()
plt.show()
# 1. Histogram: Distribution of planet mass
plt.figure(figsize=(8, 5))
sns.histplot(data=planets, x='mass', bins=30, kde=True)
plt.title('Distribution of Planet Mass')
plt.xlabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.tight_layout()
plt.show()

# 2. KDE plot: Orbital period distribution
plt.figure(figsize=(8, 5))
sns.kdeplot(data=planets, x='orbital_period', fill=True)
plt.title('KDE of Orbital Period')
plt.xlabel('Orbital Period (days)')
plt.xscale('log')
plt.tight_layout()
plt.show()
# 1. Boxplot: Mass by detection method
plt.figure(figsize=(12, 6))
sns.boxplot(data=planets, x='method', y='mass')
plt.title('Planet Mass by Detection Method')
plt.xticks(rotation=90)
plt.yscale('log')
plt.tight_layout()
plt.show()

# 2. Countplot: Number of discoveries by method
plt.figure(figsize=(12, 6))
sns.countplot(data=planets, y='method', order=planets['method'].value_counts().index)
plt.title('Number of Discoveries by Method')
plt.xlabel('Number of Planets')
plt.ylabel('Detection Method')
plt.tight_layout()
plt.show()
