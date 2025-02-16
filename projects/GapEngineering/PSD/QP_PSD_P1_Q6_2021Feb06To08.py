"""
2020Dec03
This is for clean and dirty state
"""
from QPTunneling_LIU import QPTunneling_Wilen, plotMultiFittedPSD, QPTunneling_Liu, OneStateCleanDirty
import matplotlib.pyplot as plt
import numpy as np

"""Q6"""
QP_path = ('Z:/mcdermott-group/data/GapEngineer/Nb_GND_Dev06_Trap/Leiden_2021Jan/P1PSD/LIU/Q6_withQ5Poison/{}/{}/MATLABData/{}')

date = '2021Feb06'
power = 'Neg10'
P1 = 0.02

experiment_name_P1 = ('Interleave_P1_'+power)
experiment_name_PSD = ('Interleave_PSD_'+power)
P1_file_Number = np.arange(0, 50, 1)
PSD_file_Number = P1_file_Number
P1_file = [QP_path.format(date, experiment_name_P1, experiment_name_P1) + '_{:03d}.mat'.format(i) for i in P1_file_Number]
P1CleanDirty = OneStateCleanDirty()
P1CleanDirty.update_experiment_name(experiment_name_P1, experiment_name_PSD)
P1CleanDirty.add_p1_data_from_matlab(P1_file, P1_threshold=P1)
PSD_Clean_Files = P1CleanDirty.clean_files
# PSD_Dirty_Files = P1CleanDirty.dirty_files

QPT_Q6_Poison_Clean = QPTunneling_Wilen(name='Q6_Clean_P1<{} with poison={}'.format(P1, power))
# QPT_Q6_Poison_Clean = QPTunneling_Liu(name='Q6_Clean_P1<{} with poison={}'.format(P1, power))
# QPT_Q6_Poison_Clean_HMM = QPTunneling_Liu(name='HMM Q6_Clean_P1<{} with poison={}'.format(P1, power))
# QPT_Q6_Poison_Dirty = QPTunneling_Wilen(name='Q6_Dirty_P1>{} with poison={}'.format(P1, power))
QPT_Q6_Poison_Clean.add_datasets(PSD_Clean_Files)
# QPT_Q6_Poison_Clean_HMM.add_datasets(PSD_Clean_Files, HMM=True)
# QPT_Q6_Poison_Dirty.add_datasets(PSD_Dirty_Files)


# QPT_List = [QPT_Q6_Poison_Clean, QPT_Q6_Poison_Dirty]
QPT_List = [QPT_Q6_Poison_Clean]
#
plotMultiFittedPSD(QPT_List)
