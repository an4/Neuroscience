# for loading neuron 1 - 4 and time
f = open("neuron1.csv")
neuron1 = map( lambda x: int(x.strip()), f.readlines() )

# for loading x and y
f = open("x.csv")
neuron1 = map( lambda x: float(x.strip()), f.readlines() )

