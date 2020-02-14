import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as plt2
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler

def load_data_frame():
    df = pd.read_csv('../../data/Pokemon.csv')
    return df

def clean_df(df):
    df_clean = df.copy()
    df_clean = df_clean[df_clean['is_legendary'] == 0]
    df_clean = df_clean.filter(['name', 'type1', 'type2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed'])
    df_clean['type2'].fillna(value='None', inplace=True)
    df_clean = df_clean.set_index('name')
    return df_clean

def explore_types(df):
    t1 = df.groupby('type1').size().reset_index(name='counts').sort_values(by='counts', ascending=False).reset_index(drop=True)
    t1['percentage'] = t1['counts']/t1['counts'].sum()
    print(t1.head())
    t2 = df.groupby('type2').size().reset_index(name='counts').sort_values(by='counts', ascending=False).reset_index(drop=True)
    t2['percentage'] = t2['counts']/t2['counts'].sum()
    print(t2.head())

    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='type1', data=df, order=df['type1'].value_counts().index).set_title("Type1 Frequencies")
    plt.show()
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='type2', data=df, order=df['type2'].value_counts().index).set_title("Type2 Frequencies")
    plt.show()

def explore_stats(df, class_type, stat):
    t1_med = df.groupby(class_type).median().sort_values(by=stat, ascending=False)
    t1_med['std'] = StandardScaler().fit_transform(t1_med)
    t1_med.columns = ['med_' + stat, 'med_std']
    t1_mean = df.groupby(class_type).mean().sort_values(by=stat, ascending=False)
    t1_mean['std'] = StandardScaler().fit_transform(t1_mean)
    t1_mean.columns = ['mean_' + stat, 'mean_std']
    t1_stats = t1_med.join(t1_mean, how='outer')
    print('\n' + stat + ': ' + class_type)
    print(t1_stats.sort_values(by='med_std', ascending=False).head())

    high_low = t1_stats[(t1_stats['med_std'] <= -2) | (t1_stats['med_std'] >= 2)| (t1_stats['mean_std'] <= -2) | (t1_stats['mean_std'] >= 2)]
    print('\n'+ 'Standouts:')
    print(high_low)

def explore_stats_wrapper(df, arr):
    for stat in arr:
        explore_stats(df.filter(['type1', stat]), 'type1', stat)

def explore_top(df, stat):
    top = df.filter(['name', 'type1', 'type2', stat]).sort_values(by=stat, ascending=False)
    print("\n" + stat)
    print(top.head(10))

def explore_top_wrapper(df, arr):
    for stat in arr:
        explore_top(df, stat)

def standardize_stats(df):
    df_std = df.copy()
    stats = ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']
    df_std[stats] = StandardScaler().fit_transform(df_std[stats])
    return df_std

def combine_dfs_for_plots(df1, df2):
    df1.rename(columns={'type1':'type', 'grade_std':'grade_std1'}, inplace=True)
    df2.rename(columns={'type2':'type', 'grade_std':'grade_std2'}, inplace=True)
    types_combined_df = pd.merge(df1, df2, on='type', how='outer')
    types_combined_df = types_combined_df.set_index('type')
    types_combined_df['final_grade'] = types_combined_df.mean(axis=1)
    types_combined_df = types_combined_df.dropna().sort_values(by='final_grade', ascending=False)
    types_combined_df = types_combined_df.reset_index(drop=False)
    return types_combined_df

def make_plots(df, text):
    #Median
    type_grade_df1 = df.groupby('type1')[['grade_std']].median().sort_values(by='grade_std').reset_index(drop=False)
    type_grade_df2 = df.groupby('type2')[['grade_std']].median().sort_values(by='grade_std').reset_index(drop=False)
    types_combined_df = combine_dfs_for_plots(type_grade_df1, type_grade_df2)
    fig = plt.figure(figsize=(15, 5))
    sns.barplot(
        x='type',
        y='final_grade',
        data=types_combined_df
    ).set_title('Type: ' + text + ' Capacity Median')
    plt.show()

    #Mean
    type_grade_df1 = df.groupby('type1')[['grade_std']].mean().sort_values(by='grade_std').reset_index(drop=False)
    type_grade_df2 = df.groupby('type2')[['grade_std']].mean().sort_values(by='grade_std').reset_index(drop=False)
    types_combined_df = combine_dfs_for_plots(type_grade_df1, type_grade_df2)
    fig = plt.figure(figsize=(15, 5))
    sns.barplot(
        x='type',
        y='final_grade',
        data=types_combined_df
    ).set_title('Type: ' + text + ' Capacity Mean')
    plt.show()

def mod_plot_df(df, arr, text):
    df_cpy = df.copy()
    role_df = df_cpy.filter(['name', 'type1', 'type2', arr[0], arr[1]])
    role_df['grade'] = role_df[arr].sum(axis=1)
    std_indx = role_df.filter(['grade'])
    std_indx = StandardScaler().fit_transform(std_indx)
    role_df['grade_std'] = std_indx
    grade_df = role_df.filter(['type1', 'type2', 'grade_std'])
    make_plots(grade_df, text)
    explore_top(grade_df, 'grade_std')

def analyze_roles(df):
    p_sweep_stats = ['attack', 'speed']
    sp_sweep_stats = ['sp_attack', 'speed']
    p_tank_stats = ['defense', 'hp']
    sp_tank_stats = ['sp_defense', 'hp']
    mod_plot_df(df, p_sweep_stats, 'Physical Sweeper')
    mod_plot_df(df, sp_sweep_stats, 'Special Sweeper')
    mod_plot_df(df, p_tank_stats, 'Physical Tank')
    mod_plot_df(df, sp_tank_stats, 'Special Tank')

# def explore_t3(df, arr):
#     for type in arr:
#         t3x = df[(df.type1 == type) | (df.type2 == type)]
#         print(type + ": ")
#         print(t3x["speed"].median())

def main():
    df = load_data_frame()
    df_clean = clean_df(df)
    explore_types(df_clean)
    stats = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
    # types = ['grass', 'fire', 'water', 'bug', 'normal', 'poison', 'electric', 'ground', 'fairy', 'fighting', 'psychic', 'rock', 'ghost', 'ice', 'dragon', 'dark', 'steel', 'flying']
    # print(df_clean.type1.unique())
    # t3 = df_clean.copy()
    # explore_t3(t3, types)
    explore_stats_wrapper(df_clean, stats)
    explore_top_wrapper(df_clean, stats)
    analyze_roles(df_clean)

if __name__ == "__main__":
    main()