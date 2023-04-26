import pandas as pd

df = pd.read_csv('https://query.data.world/s/cuydddwqln3ihuwafn7atqitofapvn?dws=00000')

# Super Bowls by team
super_bowls_by_team = df['Winner'].value_counts().to_frame()
super_bowls_by_team.columns = ['Super Bowls Won']
print('Super Bowls by Team:')
print(super_bowls_by_team)

# Count the number of Super Bowl losses by team
super_bowls_by_team = df.groupby('Loser')['Loser'].count().to_frame()
super_bowls_by_team.columns = ['Super Bowls Lost']
print('Super Bowls Lost by Team:')
print(super_bowls_by_team)

# Super Bowls by state
super_bowls_by_state = df.groupby('State')['Winner'].value_counts().to_frame()
super_bowls_by_state.columns = ['Super Bowls Won']
print('\nSuper Bowls by State:')
print(super_bowls_by_state)
