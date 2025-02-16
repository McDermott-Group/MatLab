"""
2021Oct
"""
from QPTunneling_LIU import QPTunneling_Wilen, plotMultiFittedPSD, QPTunneling_Liu, QPTunneling_Harrison
import matplotlib.pyplot as plt
import numpy as np

QP_path = ('Z:/mcdermott-group/data/Antenna/SUXmon/LIU/VitoChip1/{}/{}/MATLABData/{}')
date = '10-14-21'
# date = '2021Oct13Test'
QB_id = 'Q1'
# a1 = np.arange(0, 16000, 5000)
# a2 = np.arange(16000, 44000, 2000)
# JBlist = np.concatenate((a1, a2))
# JBlist = np.arange(34000, 64000, 2000)
JBlist = [0]
J_QPT_2D = []

for JB in JBlist:
    experiment_name_PSD = (QB_id+'_PSD_'+str(JB)+'uDACJB')
    PSD_file_Number = np.arange(0, 5, 1)
    PSD_file = [QP_path.format(date, experiment_name_PSD, experiment_name_PSD) + '_{:03d}.mat'.format(i) for i in PSD_file_Number]
    QPT_Q = QPTunneling_Wilen(name='{} with J6 = {} uDAC, {}GHz'.
                              format(QB_id, str(JB), str(JB*4.6)))
    # QPT_Q = QPTunneling_Liu(name='{} with J6 = {} uDAC, {}GHz'.
    #                           format(QB_id, str(JB), str(JB*4.6)))
    QPT_Q.add_datasets(PSD_file)
    QPT_List = [QPT_Q]
    plotMultiFittedPSD(QPT_List, save=False, name='{} with J2 ={} uDAC {}GHz'.
                              format(QB_id, str(JB), str(JB*4.6)))

    QPT_Q.get_fit()
    # print(QB_id)
    # print(J2Bias, '[{:.1f}]'.format(QPT_Q.params[0]))
    rate = QPT_Q.params[0]  # units is Hz
    rate = int(rate*100)/100.0
    # print('rate=', rate)
    J_QPT_2D.append([JB, rate])
    # print('J_QPT_2D=', J_QPT_2D)

print('QB_id=', QB_id)
print('J_QPT_2D=', J_QPT_2D)


