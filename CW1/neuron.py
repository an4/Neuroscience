import matplotlib.pyplot as plt
import math
import numpy as np
from random import randint

tauM = 0.01
EL = -0.07
Vth = -0.04
Rm = 10000000
Ie = 3.1 * 10 ** -9
DT = 0.001

# Q1
def fireAndIntegrate(V) :
    dV_dt = (EL - V + Rm * Ie) / tauM
    return V + DT * dV_dt

time = np.arange (0, 1+DT, DT)
length = len(time)
V = []
V.append(EL)

for i in range(1,length) :
    Vtemp = fireAndIntegrate(V[-1])
    if Vtemp > Vth :
        Vtemp = EL
    V.append(Vtemp)

plt.figure(1)
plt.plot(time,V)
plt.title("Integrate And Fire Model")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage in the cell (V)")
plt.ylim(-0.072, -0.038)
plt.savefig("figure1.png", dpi=300, pad_inches=0.5)
plt.show()

# Q2 A
I_min = (EL - Vth) / Rm

# Q2 B
Ie = 3 * 10 ** -9

V = []
V.append(EL)
for i in range(1,length) :
    Vtemp = fireAndIntegrate(V[-1])
    if Vtemp > Vth :
        Vtemp = EL
    V.append(Vtemp)

plt.figure(2)
plt.plot(time,V)
plt.title("Integrate And Fire Model")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage in the cell (V)")
plt.ylim(-0.072, -0.038)
plt.savefig("figure2.png", dpi=300, pad_inches=0.5)
plt.show()

# Q3
amps = np.arange (2, 5.01, 0.1)

spikes = []
for amp in amps :
    Ie = amp * 10 ** -9
    V = []
    # V(0) = EL
    V.append(EL)
    spike = 0
    for i in range(1,length) :
        Vtemp = fireAndIntegrate(V[-1])
        if Vtemp > Vth :
            Vtemp = EL
            spike += 1
        V.append(Vtemp)
    spikes.append(spike)

plt.figure(3)
plt.plot(amps,spikes)
plt.title("Dependance Between Firing Rate And Current's Amplitude")
plt.xlabel("Current Amplitude [nA]")
plt.ylabel("Firing Rate - Spikes per second")
plt.xlim(2.0, 5.0)
plt.savefig("figure3.png", dpi=300, pad_inches=0.5)
plt.show()

# Q4
tauM    = 0.02
EL      = -0.07
Vreset  = -0.08
Vth     = -0.054
Rm_Ie   = 0.018

Rm_Gs   = 0.15
Pmax    = 0.5
tauS    = 0.01

DT      = 0.001

def fireAndIntegrate_2 (V, t) :
    dV_dt = (EL - V - Rm_Gs * (Pmax *math.exp(-t/tauS) ) * (V - Es) + Rm_Ie ) / tauM
    return V + DT * dV_dt

# Q4a

Es = 0
# Initial membrane potentials
V_one_start = randint(Vreset * 10 ** 3, Vth * 10 ** 3) * 10 ** -3
V_two_start = randint(Vreset * 10 ** 3, Vth * 10 ** 3) * 10 ** -3

time = np.arange(0, 1+DT, DT)

V_one = []
V_two = []

V_one.append(V_one_start)
V_two.append(V_two_start)
t_one = 0
t_two = 0

length = len(time)

for t in time[1:] :
    V_one.append(fireAndIntegrate_2(V_one[-1], t - t_two - DT))
    V_two.append(fireAndIntegrate_2(V_two[-1], t - t_one - DT))
    if V_one[-1] > Vth :
        V_one[-1] = Vreset
        t_one = t
    if V_two[-1] > Vth :
        V_two[-1] = Vreset
        t_two = t

plt.figure(4)
one, = plt.plot(time,V_one, color='r')
two, = plt.plot(time,V_two, color='b')
plt.legend([one, two], ['First Neuron', 'Second Neuron'])
plt.title("Integrate and Fire Model of two neurons with excitatory synapses.")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage in the cell (V)")
plt.ylim(-0.083, -0.045)
plt.savefig("figure4.png", dpi=300, pad_inches=0.5)
plt.show()

# Q4b

Es = -0.08
# Initial membrane potentials
V_one_start = randint(Vreset * 1000, Vth * 1000) * 0.001
V_two_start = randint(Vreset * 1000, Vth * 1000) * 0.001

V_one = []
V_two = []

V_one.append(V_one_start)
V_two.append(V_two_start)
t_one = 0
t_two = 0

length = len(time)

for i in range(1, length) :
    t = time[i]
    V_one.append(fireAndIntegrate_2(V_one[-1], t - t_two - DT))
    V_two.append(fireAndIntegrate_2(V_two[-1], t - t_one - DT))
    if V_one[-1] > Vth :
        V_one[-1] = Vreset
        t_one = t
    if V_two[-1] > Vth :
        V_two[-1] = Vreset
        t_two = t

plt.figure(5)
one, = plt.plot(time,V_one, color='r')
two, = plt.plot(time,V_two, color='b')
plt.legend([one, two], ['First Neuron', 'Second Neuron'])
plt.title("Integrate and Fire Model of two neurons with inhibatory synapses.")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage in the cell (V)")
plt.ylim(-0.083, -0.045)
plt.savefig("figure5.png", dpi=300, pad_inches=0.5)
plt.show()

# Q5
tauM = 0.01
EL = -0.07
Vth = -0.04
Rm = 10000000
Ie = 3.1 * 10 ** -9
DT = 0.001
EK = -0.08
C = (0.01 * 10 ** 6) ** -1
tauSlow = 0.2

time = np.arange (0, 1+DT, DT)
V = []
V.append(EL)

for t in time :
    Vtemp = fireAndIntegrate(V[-1])
    if Vtemp > Vth :
        Vtemp = EL
    V.append(Vtemp)

# plt.figure(5)
# plt.plot(time,V)
# plt.title("Integrate And Fire Model")
# plt.xlabel("Time (sec)")
# plt.ylabel("Voltage in the cell (V)")
# plt.ylim(-0.072, -0.038)
# plt.savefig("figure6.png", dpi=300, pad_inches=0.5)
# plt.show()
