import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as plt2
import seaborn as sns
import warnings
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def load_data():
    df = pd.read_csv('../../data/Pokemon.csv')
    return df

def clean_data(df):
    data_clean = df.copy()
    data_clean = data_clean[data_clean['is_legendary'] == 0]
    data_clean = data_clean.filter(['name', 'type1', 'type2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed'])
    data_clean['type2'].fillna(value='None', inplace=True)
    data_clean = data_clean.drop(data_clean[(data_clean['name']=='Blissey') | (data_clean['name']=='Chansey') | (data_clean['name']=='Shuckle')].index)
    return data_clean

def mod_data(df, arr):
    percent = .1
    role_data = df.copy()
    role_data['role_index'] = role_data[arr].sum(axis=1)
    num_rows = int(len(role_data)*percent)
    role_data = role_data.sort_values(by='role_index', ascending=False)
    limit = role_data.iloc[num_rows]['role_index']
    role_data = role_data[role_data['role_index']>=limit]
    return role_data

def do_elbow_method(df, arr):
    stats_std = StandardScaler().fit_transform(df[arr])

    cluster_range = range(1, 20)
    errors = []
    for k in cluster_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(stats_std)
        errors.append(kmeans.inertia_)
    
    # Show Elbow Graph; the point where adding another feature will cause the marginal gain in variance to drop (the elbow)
    plt.figure(figsize=(10, 5))
    plt.plot(cluster_range, errors)
    plt.grid(True)
    plt.title('Elbow curve')
    plt.show()
    return stats_std

def do_kmeans(df, df_std, arr):
    num_clusters = input("number of clusters? ")
    #cluster
    kmeans = KMeans(n_clusters = num_clusters, init='k-means++', random_state = 0).fit(df_std)
    #assign labels to original dataset and output it
    labels = kmeans.labels_
    df['clusters'] = labels
    plot = sns.FacetGrid(df, hue="clusters", size=5, aspect=1).map(plt.scatter, arr[0], arr[1]).add_legend()
    plot.fig.suptitle(str(arr[0] + ' vs ' + arr[1]))
    plt.show()
    return df

def get_type_counts(df):
    t1 = pd.DataFrame(df['type1'].value_counts())
    t2 = pd.DataFrame(df['type2'].value_counts())
    t1_t2_df = t1.join(t2)
    t1_t2_df['type2'].fillna(value=0, inplace=True)
    t1_t2_df['total'] = t1_t2_df.sum(axis=1)
    t1_t2_df['percentage'] = t1_t2_df['total']/t1_t2_df['total'].sum()
    print(t1_t2_df.sort_values(by='total', ascending=False))

def analyze_role(df, arr):
    df=df.filter(['name', 'type1', 'type2', arr[0], arr[1], 'clusters', 'role_index'])
    num_clusters = df['clusters'].nunique()
    for i in range(0, num_clusters):
        cluster_i = df[df['clusters']==i]
        print(cluster_i.sort_values(by='role_index', ascending=False))
        print('\nCluster' + str(i))
        get_type_counts(cluster_i)
    print('\nOverall')
    get_type_counts(df)

def process_role(df, arr):
    role_data = mod_data(df, arr)
    role_stats_std = do_elbow_method(role_data, arr)
    role_data = do_kmeans(role_data, role_stats_std, arr)
    analyze_role(role_data, arr)

def main():
    df = load_data()
    data_clean = clean_data(df)
    sp_tank_stats = ['sp_defense', 'hp']
    process_role(data_clean, sp_tank_stats)

if __name__ == "__main__":
    main()