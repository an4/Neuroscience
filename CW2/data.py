import matplotlib.pyplot as plt
import numpy as np

################################################################################
# Calculate firing rates of each neuron (in each 1 second interval), and plot  #
# histograms of the firing rates.                                              #
################################################################################
def firingRate(N, i) :
    minimum = min(N)
    maximum = max(N)
    bins = int((maximum-minimum)/10000)
    mi = int((minimum-200000)/10000)
    ma = int((maximum+200000)/10000)
    if i < 5 :
        title = "Firing rate of Neuron " + str(i)
        height = 30
    else :
        title = "Firing rate of All 4 Neurons."
        height = 35
    plt.figure(figsize=(10,5))
    plt.hist(N, bins=bins)
    plt.xlabel("Time (sec)")
    plt.ylabel("Firing rate")
    plt.axis([minimum-200000, maximum+200000, 0, height])
    plt.xticks(np.arange(minimum-200000, maximum+200000, 1000000), np.arange(mi, ma, 100))
    plt.title(title)
    plt.show()

################################################################################
# Generate plots showing positions in which each neuron fired.                 #
################################################################################


################################################################################
if ( __name__ == "__main__" ) :
    f = open("neuron1.csv")
    N1 = map( lambda x: int(x.strip()), f.readlines() )
    f = open("neuron2.csv")
    N2 = map( lambda x: int(x.strip()), f.readlines() )
    f = open("neuron3.csv")
    N3 = map( lambda x: int(x.strip()), f.readlines() )
    f = open("neuron4.csv")
    N4 = map( lambda x: int(x.strip()), f.readlines() )

    f = open("x.csv")
    X = map( lambda x: float(x.strip()), f.readlines() )
    f = open("y.csv")
    Y = map( lambda x: float(x.strip()), f.readlines() )

    f = open("time.csv")
    T = map( lambda x: float(x.strip()), f.readlines() )

    N = N1 + N2 + N3 + N4

    # firingRate(N1, 1)
    # firingRate(N2, 2)
    # firingRate(N3, 3)
    # firingRate(N4, 4)
    # firingRate(N, 5)
