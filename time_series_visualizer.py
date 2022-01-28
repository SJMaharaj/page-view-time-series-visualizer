import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15,5))
    sns.lineplot(data = df, x = 'date', y = 'value', color = 'r').set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar['Months'] = df_bar['date'].dt.month_name()
    df_bar['Years'] = df_bar['date'].dt.year
    df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Months'], as_index=True, sort = False)['value'].mean()).rename(columns ={'value':'Average Page Views'}).reset_index()  
    
    

    # Draw bar plot

    fig, ax = plt.subplots(figsize = (11,9))
    sns.barplot(data = df_bar, x = 'Years' , y = 'Average Page Views', hue = 'Months', palette = 'Set1', hue_order = ['January','February','March','April','May','June','July','August','September','October','November','December'])
    plt.legend(loc='upper left', fontsize='14')
    plt.xticks(rotation=90)
    





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1,2,figsize = (22,8))
    ax[0] = sns.boxplot(data = df_box, x = 'year', y = 'value', ax = ax[0]).set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    ax[1] = sns.boxplot(data = df_box, x = 'month', y = 'value', ax = ax[1], order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']).set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
