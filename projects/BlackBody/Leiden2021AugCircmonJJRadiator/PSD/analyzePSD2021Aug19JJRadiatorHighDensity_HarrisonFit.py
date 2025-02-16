"""
2021Jul
"""
from QPTunneling_LIU import QPTunneling_Wilen, plotMultiFittedPSD, QPTunneling_Liu, QPTunneling_Harrison, \
    OneStateCleanDirty, plotFittedPSD_Harrison
import matplotlib.pyplot as plt
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
"""Q2"""
QP_path = ('Z:/mcdermott-group/data/BlackBody/Circmon/LIU/CW20180514A_Ox2/{}/{}/MATLABData/{}')
# Z:\mcdermott-group\data\BlackBody\Circmon\LIU\CW20180514A_Ox2\08-19-21
# date = '08-19-21'
# date = 'JJRadiatorQPT_2021Aug19'
date = 'JJRadiatorQPT_2021Aug19_HighDensity'
# QBs = ['Q1','Q2','Q4']
QBs=['Q4']
#J2Biaslist = np.arange(35000,80001,500)
J2Biaslist=[39000]
# J2Biaslist = [40, 42, 44]
fparity = {}
uparity = {}
fidelity={}
# for J2Bias in J2Biaslist:
for QB_id in QBs:
    fparity[QB_id]=[]
    uparity[QB_id]=[]
    fidelity[QB_id]=[]
    if QB_id=='Q1':
        ylim=[10 ** (-5), 2*10 ** (-4)]
    if QB_id=='Q2':
        ylim=[5 * 10 ** (-5), 10 ** (-2)]
    if QB_id=='Q4':
        ylim=[10 ** (-5), 10 ** (-3)]
    for J2Bias in J2Biaslist:
        experiment_name_PSD = (QB_id+'_PSD_'+str(J2Bias)+'uDACJ2')
        PSD_file_Number = np.arange(0, 50, 1)
        PSD_file = [QP_path.format(date, experiment_name_PSD, experiment_name_PSD) + '_{:03d}.mat'.format(i) for i in PSD_file_Number]
        QPT_Q = QPTunneling_Harrison(name='{} with J2 = {} mDAC, {}GHz'.
                                  format(QB_id, str(J2Bias), str(J2Bias*4.8)))
        QPT_Q.add_datasets(PSD_file)

        cr = 1;
        ep = 4;
        if J2Bias < 55000 and QB_id=='Q2':
            cr = 1
            ep = 2
        elif J2Bias < 200000 and QB_id=='Q2':
            cr=0.5
            ep=4
        elif J2Bias < 55000and QB_id=='Q1':
            cr = 0.1
            ep = 2
        elif J2Bias < 200000 and QB_id=='Q1':
            cr=0.05
            ep=4
        elif J2Bias < 55000 and QB_id=='Q4':
            cr = 0.5
            ep = 4
        elif J2Bias < 200000 and QB_id=='Q4':
            cr=0.2
            ep=4
        else:
            cr=0.2
            ep=8


        avg_fidelity, avg_parity, parity_uncertainty =plotFittedPSD_Harrison(QPT_Q, save=True, name='{} with J2 ={} mDAC {}GHz'.
                                  format(QB_id, str(J2Bias), str(J2Bias*4.8)),excluded_points=ep,concatenate_records=cr,ylim=ylim)
        # print(QB_id)
        # print(J2Bias, '[{:.1f}]'.format(QPT_Q.params[0]))
        fparity[QB_id].append(avg_parity)
        uparity[QB_id].append(parity_uncertainty)
        fidelity[QB_id].append(avg_fidelity)

plt.figure(figsize=(8, 6))
plt.title('Parity Rate vs J2Bias')
plt.xlabel('J2Bias (uDAC)')
plt.ylabel('Parity Rate (Hz)')
for QB_id in QBs:
    plt.plot(J2Biaslist,fparity[QB_id])
    print('{}_J2Bias='.format(QB_id),J2Biaslist)
    print('{}_J2ParityRate='.format(QB_id), fparity[QB_id])
    print('{}_J2ParityUncertainty='.format(QB_id), uparity[QB_id])
    print('{}_J2Fidelity='.format(QB_id), fidelity[QB_id])
plt.show()
# plt.savefig('ParityRateVsBias.png')