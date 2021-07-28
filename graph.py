
def graph():
    import numpy as np
    import matplotlib.pyplot as plt
    xdata1 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
    ydata1 = [980130,1012592,1039135,999836,1001278,973706,973957,1022895,948008,1040154,1029593,1054081,1138536]
    xdata2 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
    ydata2 = [1741160,1657005,1655904,1596639,1360847,1623195,1636483,1674204,1590513,159948,1667703,1709991,1804854]
    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    plt.plot(xdata1,'go--',linewidth=2,markersize=12,label='Total vehicles')
    plt.title('Total vehicles vs Year')
    plt.xlabel('Year')
    plt.ylabel('Total Vehicles')
    plt.grid(True)
    plt.legend();
    plt.show()

graph()