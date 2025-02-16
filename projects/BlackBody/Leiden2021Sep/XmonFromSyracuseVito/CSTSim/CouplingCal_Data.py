from antennalib import AntennaCoupling
import matplotlib.pyplot as plt
import numpy as np

### parameters to be tuned
e_eff = 6 # limit (1, 6.5), the voltage can also be built in to have a larger range
C_eff = 100*1e-21   # Commonly used (50-100)
Jbias_offset = 1    # mDAC should be +-1 mDAC basically +-5 GHz
k = 1   # Coupling between radiator and receiver, this could be larger than one due to the
        # fact we can generate QPs locally at the recevier's test pad

k1 = 0.0   # coupling between on chip phonon mitigation
f_DAC = 4.604*1.1
### parameteres tuned done

JJ7 = [4.2*1e3, None, 0, 1000*150]   #[R, L, C, A]
JJ1 = [33*1e3, None, 0, 180*150]   #[R, L, C, A]
JQ1 = [15.67*1e3, None, 0, 360*150]

# fileJ7 = "Z_syracuse_injector.txt"
# fileJ7_noleads = "Z_syracuse_injector_no_leads.txt"
fileJ1 = "Z_syracuse_injector_with_leads.txt"
fileJ7 = "Z_syracuse_injector_with_leads.txt"
# fileQ1 = "Z_syracuse_xmon_5.1GHz.txt"
# fileQ1 = "Z_syracuse_xmon_5.1GHz_withRO_ChargeCoupler.txt"
# fileQ1 = "Z_syracuse_xmon_5.1GHz_withRO_ChargeCoupler_short.txt"
# fileQ1 = "Z_syracuse_xmon_5.1GHz_withROCoupler.txt"
fileQ1 = "Z_syracuse_xmon_5.1GHz_no_Coupler.txt"

J1 = AntennaCoupling()
J1.import_data(fileJ1, JJ1)
ecJ1 = J1.e_c_dB

J7 = AntennaCoupling()
J7.import_data(fileJ7, JJ7)
f = J7.Antenna["f"]
ecJ7 = J7.e_c_dB
pgJ7 = J7.p_g
refJ7 = J7.ref

# J7_noleads = AntennaCoupling()
# # J7_noleads.import_data(fileJ7_noleads, JJ7)
# J7_noleads.import_data(fileJ7_noleads, JJ7_highR)
# ecJ7_noleads = J7_noleads.e_c_dB

Q1 = AntennaCoupling()
Q1.import_data(fileQ1, JQ1)
f_Q1 = Q1.Antenna["f"]
ecQ1 = Q1.e_c_dB
eQ1 = Q1.e_c
Z_ReQ1 = Q1.Antenna["Z_Re"]

Q1_PSD = np.array([
    [0.0, 100.56], [0.005, 95.14], [0.01, 93.09], [0.015, 105.55], [0.02, 290.07],
    [0.025, 464.17], [0.0275, 389.05], [0.03, 580.15], [0.0325, 1755.69],
    [0.0349, 2195.63], [0.0374, 2354.61], [0.04, 1303.42], [0.041, 1706.05],
    [0.042, 1083.28], [0.043, 1217.15], [0.044, 1030.59], [0.045, 1729.76],
    [0.046, 1727.71], [0.047, 1845.05], [0.048, 3773.84], [0.049, 2620.48],
    [0.05, 4296.21], [0.051, 4929.87], [0.052, 4990.22], [0.053, 6261.39],
    [0.054, 4160.39], [0.055, 6191.23], [0.056, 6714.55], [0.057, 5577.27],
    [0.058, 6579.94], [0.059,6267.85], [0.06, 4146.44], [0.061, 5740.52],
    [0.062, 4549.68], [0.063, 3588.3], [0.064, 1955.06], [0.065, 1598.07],
    [0.066, 1266.78], [0.067, 1964.89], [0.068, 2945.25], [0.069, 3255.49],
    [0.07, 1989.67], [0.07, 1989.67], [0.0725, 1769.13], [0.075, 943.87],
    [0.0775, 866.63], [0.08, 497.36], [0.0825, 411.43], [0.085, 397.27],
    [0.0875, 414.55], [0.09, 447.09], [0.0925, 384.19], [0.095, 443.21],
    [0.0975, 449.53], [0.1, 511.58], [0.1025, 568.87], [0.105, 656.25],
    [0.1075, 756.29], [0.11, 853.78], [0.1125, 907.46], [0.115, 1048.06],
    [0.1175, 1110.32], [0.12, 1217.71], [0.1225, 1255.77], [0.125, 1353.19],
    [0.1275, 1457.7], [0.13, 1673.28], [0.1325, 1746.96], [0.135, 1884.08],
    [0.1375, 1996.61], [0.14, 2121.16], [0.1425, 2342.79], [0.145, 3016.99],
    [0.1475, 3711.24], [0.15, 3845.02], [0.155, 4165.38], [0.16, 4976.58],
    [0.165, 5837.55], [0.17, 5307.72], [0.175, 6209.49], [0.18, 7348.67],
    [0.185, 8213.85], [0.19, 10537.9], [0.195, 9946.68], [0.2, 9379.72],
    [0.205, 9908.34], [0.21, 12343.38], [0.215, 12469.27], [0.22, 10444.79],
    [0.225, 17334.14], [0.23, 14653.09], [0.235, 27709.83], [0.24, 28095.84],
    [0.245, 39425.95]
])
Q2_PSD = np.array([
    [0.0, 118.5], [0.005, 119.1], [0.01, 121.42], [0.015, 121.03], [0.02, 209.13],
    [0.025, 460.9],[0.0275, 514.62], [0.03, 544.43], [0.0325, 2226.0],
    [0.034999999999999996, 1983.08], [0.03749999999999999, 3576.29],
    [0.04, 1859.23], [0.041, 2660.26], [0.042, 1781.72],
    [0.043000000000000003, 2545.09], [0.044000000000000004, 2176.37],
    [0.045000000000000005, 3303.2], [0.046000000000000006, 2267.5],
    [0.04700000000000001, 3954.45], [0.04800000000000001, 4464.5],
    [0.04900000000000001, 4151.85], [0.05000000000000001, 5897.78],
    [0.05100000000000001, 6452.59], [0.05200000000000001, 8355.18],
    [0.05300000000000001, 5182.63], [0.05400000000000001, 6321.19],
    [0.055000000000000014, 6519.59], [0.056000000000000015, 5902.87],
    [0.057000000000000016, 7342.28], [0.05800000000000002, 5739.51],
    [0.05900000000000002, 6505.53], [0.06000000000000002, 5000.0],
    [0.06100000000000002, 4004.72], [0.06200000000000002, 2852.82],
    [0.06300000000000003, 2602.81], [0.06400000000000003, 1590.88],
    [0.06500000000000003, 1991.29], [0.06600000000000003, 1990.53],
    [0.06700000000000003, 2174.81], [0.06800000000000003, 2698.5],
    [0.06900000000000003, 3250.48], [0.07000000000000003, 1747.16],
    [0.07, 1747.16], [0.07250000000000001, 1438.88], [0.07500000000000001, 1213.73],
    [0.07750000000000001, 746.56], [0.08000000000000002, 584.42],
    [0.08250000000000002, 559.4], [0.08500000000000002, 470.7],
    [0.08750000000000002, 490.13], [0.09000000000000002, 620.25],
    [0.09250000000000003, 500.0], [0.09500000000000003, 550.43],
    [0.09750000000000003, 626.31],
    [0.1, 749.47], [0.1025, 803.96], [0.105, 875.73], [0.1075, 900.76],
    [0.11, 947.89], [0.1125, 1094.55], [0.115, 1261.48], [0.1175, 1357.7],
    [0.12, 1484.91], [0.1225, 1601.74], [0.125, 1673.66], [0.1275, 1771.45],
    [0.13, 1948.53], [0.1325, 2048.36], [0.135, 2270.02], [0.1375, 2534.45],
    [0.14, 2771.26], [0.1425, 3213.17], [0.145, 3581.75], [0.1475, 4133.89],
    [0.15, 4219.86], [0.155, 5095.85], [0.16, 5589.36], [0.165, 6382.48],
    [0.17, 6100.54], [0.175, 6089.17], [0.18, 7057.6], [0.185, 8531.59],
    [0.19, 7347.81], [0.195, 10171.93], [0.2, 6799.01], [0.205, 13530.97],
    [0.21, 14076.17], [0.215, 16301.69], [0.22, 18397.19], [0.225, 11487.74],
    [0.23, 35110.89], [0.235, 30132.43], [0.24, 35185.73], [0.245, 35453.78]
])
Q3_PSD = np.array([
    [0.0, 111.71], [0.005, 113.28], [0.01, 118.51], [0.015, 120.27],
    [0.02, 202.89], [0.025, 328.07], [0.0275, 745.28], [0.03, 707.93],
    [0.0325, 1528.62], [0.0349, 1463.74], [0.0374, 3177.34], [0.04, 4445.66],
    [0.041, 2485.02], [0.042, 3056.44], [0.043, 1069.82], [0.044, 1596.28],
    [0.045, 2212.78], [0.046, 2444.96], [0.047, 3453.38], [0.048, 3481.83],
    [0.049, 4552.12], [0.05, 5000.0], [0.051, 6071.34], [0.052, 5187.64],
    [0.053, 6511.48], [0.054, 5787.67], [0.055, 6065.16], [0.056, 6233.79],
    [0.057, 6124.5], [0.058, 7604.65], [0.059, 5140.7], [0.06, 4706.46],
    [0.061, 4139.2], [0.062, 2857.5], [0.063, 2504.14], [0.064, 2000.39],
    [0.065, 1508.36], [0.066, 1528.22], [0.067, 1925.71], [0.068, 1452.71],
    [0.069, 2514.15], [0.07, 1566.89], [0.07, 1566.89], [0.0725, 1194.21],
    [0.075, 1257.06], [0.0775, 614.7], [0.08, 524.3], [0.0825, 460.68],
    [0.085, 418.27], [0.0875, 489.04], [0.09, 486.07], [0.0925, 476.72],
    [0.095, 463.84], [0.0975, 592.62], [0.1, 732.79], [0.1025, 775.74],
    [0.105, 819.67], [0.1075, 834.9], [0.11, 964.24], [0.1125, 1056.72],
    [0.115, 1173.54], [0.1175, 1329.44], [0.12, 1439.05], [0.1225, 1598.49],
    [0.125, 1618.58], [0.1275, 1741.54], [0.13, 1836.09], [0.1325, 1970.85],
    [0.135, 2119.5], [0.1375, 2328.07], [0.14, 2633.17], [0.1425, 2894.16],
    [0.145, 3229.14], [0.1475, 3851.36], [0.15, 4120.32], [0.155, 4734.22],
    [0.16, 5154.17], [0.165, 5898.55], [0.17, 6591.85], [0.175, 5975.21],
    [0.18, 6855.72], [0.185, 7087.44], [0.19, 6539.53], [0.195, 7255.34],
    [0.2, 9470.42], [0.205, 8018.11], [0.21, 9886.61], [0.215, 11989.54],
    [0.22, 9053.94], [0.225, 12644.08], [0.23, 11473.66], [0.235, 18689.07],
    [0.24, 27486.9], [0.245, 22777.21]
])
Q1_PSD[:, 0] = (Q1_PSD[:, 0])*1000-Jbias_offset
Q2_PSD[:, 0] = (Q2_PSD[:, 0])*1000-Jbias_offset
Q3_PSD[:, 0] = (Q3_PSD[:, 0])*1000-Jbias_offset

f_scale = np.sqrt(e_eff/6.0)
f = f/1e9
f = f*f_scale
f_Q1 = f_Q1/1e9
f_Q1 = f_Q1*f_scale

### two vertical plots
# fig, axs = plt.subplots(4)
# # axs[0].plot(f, ecJ1, color="red")
# axs[0].plot(f, ecJ7, color="black", marker="o")
# # axs[0].plot(f, ecJ7_noleads, color="red")
# axs[0].set_ylabel("Radiator (dB)",color="black", fontsize=10)
# axs[0].set_xlim([50, 600])
# axs[0].set_ylim([-60, 0])
#
# axs[1].plot(f_Q1, ecQ1, color="green", marker="o")
# axs[1].set_ylabel("Receiver QB (dB)",color="green", fontsize=10)
# axs[1].set_xlim([50, 600])
# axs[1].set_ylim([-50, 0])
#
# axs[2].plot(f_Q1, ecQ1+ecJ7*k, color="red", marker="o")
# axs[2].set_ylabel("Sum (dB)", color="red", fontsize=10)
# axs[2].set_xlim([50, 600])
# axs[2].set_ylim([-70, -30])
#
# axs[3].plot(Q1_PSD[:, 0]*f_DAC, Q1_PSD[:, 1], color='b', label='Q1_PSD')
# # axs[3].plot(Q2_PSD[:, 0]*f_DAC, Q2_PSD[:, 1], color='r', label='Q2_PSD')
# # axs[3].plot(Q3_PSD[:, 0]*f_DAC, Q3_PSD[:, 1], color='k', label='Q3_PSD')
# axs[3].set_xlabel("Freq (GHz)", color="black", fontsize=10)
# axs[3].set_ylabel("PSD (Hz)", color="blue", fontsize=10)
# axs[3].set_yscale('log')
# axs[3].set_xlim([50, 600])
# axs[3].set_ylim([100, 10000])


# axs[1].plot(f_Q1, ecQ1, color="green", marker="o")
# axs[1].set_ylabel("Receiver QB (dB)",color="green", fontsize=10)
# axs[1].set_xlim([50, 600])
# # axs[1].set_ylim([-60, -30])

# axs[2].plot(f, ecJ1, color="green", marker="o")
# axs[2].set_ylabel("Receiver J1 (dB)",color="green", fontsize=10)
# axs[2].set_xlim([50, 600])
#
# axs[3].plot(f_Q1, ecQ1+ecJ7*k+ecJ1*k*k1, color="red", marker="o")
# axs[3].set_ylabel("Sum (dB)", color="red", fontsize=10)
# axs[3].set_xlim([50, 600])
# axs[3].set_ylim([-60, -30])
#
# axs[4].plot(Q1_PSD[:, 0]*f_DAC, Q1_PSD[:, 1], color='b', label='Q1_PSD')
# # axs[3].plot(Q2_PSD[:, 0]*f_DAC, Q2_PSD[:, 1], color='r', label='Q2_PSD')
# # axs[3].plot(Q3_PSD[:, 0]*f_DAC, Q3_PSD[:, 1], color='k', label='Q3_PSD')
# axs[4].set_xlabel("Freq (GHz)", color="black", fontsize=10)
# axs[4].set_ylabel("PSD (Hz)", color="blue", fontsize=10)
# axs[4].set_yscale('log')
# axs[4].set_xlim([50, 600])
# axs[4].set_ylim([100, 10000])

### same plot
# fig, ax = plt.subplots()
# ax.plot(f_Q1, ecQ1+ecJ7*k, color="red", marker="o")
# # ax.plot(f, ecJ7, color="blue", marker="o")
# ax.set_xlabel("freq",fontsize=14)
# ax.set_ylabel("ec (dB)",color="red",fontsize=14)
#
# # ax2=ax.twinx()
# # ax2.plot(Q1_PSD[:, 0]*4.604, Q1_PSD[:, 1], color='b', label='Q1_PSD')
# # ax2.set_ylabel("PSD (Hz)", color="blue", fontsize=14)
# # ax2.set_yscale('log')
# # ax2.set_ylim([100, 10000])
# plt.grid()
# plt.show()

### Absolute photon rate
fig, axs = plt.subplots(4)
axs[0].plot(f, pgJ7, color="black", marker="o")
axs[0].set_ylabel("Photons/Sec", color="black", fontsize=10)
axs[0].set_xlim([50, 600])
axs[0].set_ylim([1e7, 1e12])
axs[0].set_yscale('log')
axs[0].grid(True, which="both")

axs[1].plot(f_Q1[100:], eQ1[100:], color="green", marker="o")
axs[1].set_ylabel("Receiver QB Gamma", color="green", fontsize=10)
axs[1].set_xlim([50, 600])
axs[1].set_ylim([1e-5, 1e0])
axs[1].set_yscale('log')
axs[1].grid(True, which="both")


pgJ1Q = []
for i in range(len(pgJ7)):
    pgJ1Q.append(pgJ7[i]*eQ1[i]*refJ7[i])
# print(pgJ1Q)
axs[2].plot(f_Q1[100:], pgJ1Q[100:], color="red", marker="o")
# axs[2].plot(f_Q1[100:], refJ1[100:], color="red", marker="o")
axs[2].set_ylabel("Photons/Sec", color="red", fontsize=10)
axs[2].set_xlim([50, 600])
# axs[2].set_ylim([1e3, 1e8])
axs[2].set_yscale('log')
axs[2].grid(True, which="both")

axs[3].plot(Q3_PSD[:, 0]*f_DAC, Q3_PSD[:, 1], color='k', label='Q3_PSD')
axs[3].set_xlabel("Freq (GHz)", color="black", fontsize=10)
axs[3].set_ylabel("PSD (Hz)", color="blue", fontsize=10)
axs[3].set_yscale('log')
axs[3].set_xlim([50, 600])
axs[3].set_ylim([100, 10000])
axs[3].grid(True, which="both")

plt.show()