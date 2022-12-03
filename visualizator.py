import matplotlib
import seaborn as sns
import warnings
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
warnings.filterwarnings("ignore")


def hist_plot(df, params=None):
    if not params:
        params = dict(x='Amount', data=df, color='red')
        # params = dict(x='Pregnancies', data=df, stat='frequency')
        # params = dict(x='Pregnancies', data=df, stat='percent')
        # params = dict(x='Pregnancies', data=df, stat='density')
        # params = dict(x='Pregnancies', data=df, cbar=True)
        # params = dict(x='Pregnancies', data=df, hue='Pregnancies')
        # params = dict(x='Pregnancies', data=df, hue='Pregnancies', element='step')
        # params = dict(x='Pregnancies', y='Glucose', data=df, cbar=True)
        # params = dict(x='Pregnancies', y='Glucose', data=df, hue='Pregnancies')
        # params = dict(x='Pregnancies', y='Glucose', data=df, hue='Pregnancies')

    sns.histplot(**params)
    plt.show()


def scatter_plot(df, params=None):
    sns.set_style('dark')

    if not params:
        params = dict(x='Time', y='Amount', data=df,  hue='Class')

    sns.scatterplot(**params)
    plt.show()


def line_plot(df, params=None):
    if not params:
        params = dict(x='Time', y='Amount', data=df, ci=None, lw=2, color='#aa00aa', alpha=0.6)

    sns.lineplot(**params)
    plt.show()




