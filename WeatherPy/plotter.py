from scipy.stats import linregress

def scatter_linregress(ax, x, y, title, xlabel="", ylabel="", regress=True):
    """Takes two columns of data and creates a scatter plot with a linear regression"""
    xlabel = x.name if xlabel == "" else ""
    ylabel = y.name if ylabel == "" else ""
    
    #scatter plot
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    if regress:
        # linear regression and plot
        (slope, intercept, rvalue, pvalue, stderr) = linregress(x, y)
        ax.plot(x, intercept + slope * x, 'r', label='fitted line')
        ax.annotate(f"y = {round(slope, 2)} * x + {round(intercept, 2)}",(x.min(),y.min()),fontsize=15,color="red")