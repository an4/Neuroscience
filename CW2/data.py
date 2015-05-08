import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

################################################################################
# Calculate firing rates of each neuron (in each 1 second interval), and plot  #
# histograms of the firing rates.                                              #
################################################################################
def firingRate(N, i) :
    minimum = int(min(N)/10000)
    maximum = int(max(N)/10000)

    bins = int(maximum-minimum)
    mi = minimum-20
    ma = maximum+20
    title = "Firing rate of Neuron " + str(i)
    if i == 4 :
        height = 30
    else :
        height = 25

    sec = []
    for n in N :
        sec.append(int(n/10000))

    name = "firingrate%d.eps" % i

    plt.figure(figsize=(20,5))
    plt.hist(sec, bins=bins, histtype='bar')
    plt.xlabel("Time (sec)")
    plt.ylabel("Firing rate")
    plt.axis([minimum-20, maximum+20, 0, height])
    plt.xticks(np.arange(minimum-20, maximum+20, 100), np.arange(mi, ma, 100))
    plt.title(title)
    plt.savefig(name)
    plt.show()

################################################################################
# Generate plots showing positions in which each neuron fired.                 #
################################################################################

def position(N1, N2, N3, N4, N, T, X, Y) :
    X_max = max(X)
    X_min = min(X)
    Y_max = max(Y)
    Y_min = min(Y)
    X_range = X_max - X_min
    Y_range = Y_max - Y_min
    X_maze = 170
    Y_maze = 130

    # print X_max
    # print X_min
    # print Y_max
    # print Y_min

    prev_t = T[0]
    prev_x = X[0]
    prev_y = Y[0]

    P1 = []
    P2 = []
    P3 = []
    P4 = []

    plt.figure()

    for t, x, y in zip(T, X, Y) :
        for n1 in N1 :
            if prev_t <= n1 <= t :
                plt.plot((prev_x/X_range)*X_maze, (prev_y/Y_range)*Y_maze, 'r.')
                P1.append([prev_x, prev_y])
        for n2 in N2 :
            if prev_t <= n2 <= t :
                plt.plot((prev_x/X_range)*X_maze, (prev_y/Y_range)*Y_maze, 'y.')
                P2.append([prev_x, prev_y])
        for n3 in N3 :
            if prev_t <= n3 <= t :
                plt.plot((prev_x/X_range)*X_maze, (prev_y/Y_range)*Y_maze, 'g.')
                P3.append([prev_x, prev_y])
        for n4 in N4 :
            if prev_t <= n4 <= t :
                plt.plot((prev_x/X_range)*X_maze, (prev_y/Y_range)*Y_maze, 'b.')
                P4.append([prev_x, prev_y])
        prev_t = t
        prev_x = x
        prev_y = y

    red = mpatches.Patch(color='red', label='Neuron 1')
    yellow = mpatches.Patch(color='yellow', label='Neuron 2')
    green = mpatches.Patch(color='green', label='Neuron 3')
    blue = mpatches.Patch(color='blue', label='Neuron 4')
    plt.legend(handles=[red, yellow, green, blue])
    plt.axis([0, 180, 0, 180])
    # plt.axis([0, 170, 0, 130])
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("Positions in which each neuron fired.")
    # plt.title("Positions in which neuron 4 fired.")
    plt.savefig("positions.eps")
    plt.show()

    return (P1, P2, P3, P4)

################################################################################
# Plot auto-correlograms of neurons                                            #
################################################################################
def autocorrelogram(A, i) :
    diff = []

    for a in A :
        for b in A :
            diff.append(a-b)

    title = "Autocorrelogram for Neuron %d" % i
    name = "autocorrelogram%d.eps" % i

    plt.figure()
    plt.hist(diff, bins=50, histtype='bar', color='green')
    plt.title(title)
    plt.xlabel("Time difference 1/10000 sec")
    plt.ylabel("Coefficient")
    plt.savefig(name)
    plt.show()

################################################################################
# Plot cross-correlograms of pairs of neurons                                  #
################################################################################
def crosscorrelogram(A, i, B, j) :
    diff = []

    for a in A :
        for b in B :
            diff.append(a-b)

    title = "Cross-correlogram between Neuron %d and Neuron %d" % (i,j)
    name = "crosscorrelogram%d%d.eps" % (i,j)

    plt.figure()
    plt.hist(diff, bins=30, histtype='bar', color='blue')
    plt.title(title)
    plt.xlabel("Time difference 1/10000 sec")
    plt.ylabel("Coefficient")
    plt.savefig(name)
    plt.show()

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

    # P1, P2, P3, P4 = position(N1, N2, N3, N4, N, T, X, Y)

    # autocorrelogram(N1, 1)
    # autocorrelogram(N2, 2)
    # autocorrelogram(N3, 3)
    # autocorrelogram(N4, 4)

    # crosscorrelogram(N1, 1, N2, 2)
    # crosscorrelogram(N1, 1, N3, 3)
    # crosscorrelogram(N1, 1, N4, 4)
    # crosscorrelogram(N2, 2, N1, 1)
    # crosscorrelogram(N2, 2, N3, 3)
    # crosscorrelogram(N2, 2, N4, 4)
    # crosscorrelogram(N3, 3, N1, 1)
    # crosscorrelogram(N3, 3, N2, 2)
    # crosscorrelogram(N3, 3, N4, 4)
    # crosscorrelogram(N4, 4, N1, 1)
    # crosscorrelogram(N4, 4, N2, 2)
    # crosscorrelogram(N4, 4, N3, 3)
