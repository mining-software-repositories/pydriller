# https://towardsdatascience.com/treemap-basics-with-python-777e5ed173d0
# https://plotly.com/python/treemaps/
import os

import matplotlib.pyplot as plt
import squarify
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))



repository = "/Users/armandosoaressousa/git/sysrepomsr"
#list_files(repository)
def treemap1():
    sizes = [50, 25, 12, 6]
    squarify.plot(sizes)
    plt.show()

def treemap2():
    sizes=[50, 25, 12, 6]
    label=["50", "25", "12", "6"]
    squarify.plot(sizes=sizes, label=label, alpha=0.6 )
    plt.axis('off')
    plt.show()

def treemap3():
    sizes=[50, 25, 12, 6]
    label=["50", "25", "12", "6"]
    color=['red','blue','green','grey']
    squarify.plot(sizes=sizes, label=label, color=color, alpha=0.6 )
    plt.axis('off')
    plt.show()

def dfAnimals():
    df = pd.read_csv('animal-population-by-breed-on_1-march-2010.csv')
    # convert to numeric and drop na
    df['Number of Animals'] = pd.to_numeric(df['Number of Animals'], errors='coerce')
    df.dropna(inplace=True)
    df.head()
    return df

def treemapAnimals():
    fig, ax = plt.subplots(1, figsize = (12,12))
    df = dfAnimals()
    squarify.plot( sizes=df['Number of Animals'], label=df['Breed'], alpha=.8 )
    plt.axis('off')
    plt.show()

def treemapAnimals2():
    df = dfAnimals()
    df.sort_values('Number of Animals', ascending=False, inplace=True)
    fig, ax = plt.subplots(1, figsize = (12,12))
    squarify.plot(sizes=df['Number of Animals'], label=df['Breed'][:5], alpha=.8 )
    plt.axis('off')
    plt.show()

def dfVideoGamesSales():
    df = pd.read_csv('vgsales.csv')
    df.dropna(inplace=True)
    return df

def treemapVideoGamesSales():
    df = dfVideoGamesSales()
    fig = px.treemap(df, 
                 path=['Platform', 'Genre'], 
                 values='Global_Sales',
                 color='NA_Sales'
                )
    fig.show()

def treemapBasicPlotly():
    fig = px.treemap(
    names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    )
    fig.show()

def treemapBasicPlotly2():
    df = px.data.tips()
    fig = px.treemap(df, path=['day', 'time', 'sex'], values='total_bill')
    fig.show()

def treemapBasicPlotlyHeatmap():
    df = px.data.gapminder().query("year == 2007")
    df["world"] = "world" # in order to have a single root node
    fig = px.treemap(df, path=['world', 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    fig.show()

def treemapBasicPlotlyHeatmap2():
    df = px.data.tips() 
    fig = px.treemap(df, path=['day', 'time', 'tip'], 
				values='total_bill', 
				color='total_bill') 

    fig.show()

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    """
    Build a hierarchy of levels for Sunburst or Treemap charts.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum(),
                              color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

def treemapSalesForce():
    df = pd.read_csv('sales_success.csv')
    print(df.head())

    levels = ['salesperson', 'county', 'region'] # levels used for the hierarchical chart
    color_columns = ['sales', 'calls']
    value_column = 'calls'

    df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
    average_score = df['sales'].sum() / df['calls'].sum()

    fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)

    fig.add_trace(go.Treemap(
            labels=df_all_trees['id'],
            parents=df_all_trees['parent'],
            values=df_all_trees['value'],
            branchvalues='total',
            marker=dict(
                colors=df_all_trees['color'],
                colorscale='RdBu',
                cmid=average_score),
            hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
            name=''
            ), 1, 1)

    fig.add_trace(go.Treemap(
            labels=df_all_trees['id'],
            parents=df_all_trees['parent'],
            values=df_all_trees['value'],
            branchvalues='total',
            marker=dict(
                colors=df_all_trees['color'],
                colorscale='RdBu',
                cmid=average_score),
            hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
            maxdepth=2
            ), 1, 2)

    fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
    fig.show()

#treemapVideoGamesSales()
treemapBasicPlotlyHeatmap()
#treemapSalesForce()