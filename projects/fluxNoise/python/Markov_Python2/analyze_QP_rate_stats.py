"""
This is for test the analyze_QPTunneling_pomegranate.py robustness against noise.
"""
from .analyze_QPTunneling_pomegranate import *
from .heatedmap import *

t_meas = 0.2  # units ms

dummy_pool = np.linspace(100, 100, 1) / 100
t_QP_pool = np.linspace(75, 100, 1)
t_QP_VTB = 10
error = np.zeros((len(dummy_pool), len(t_QP_pool)))

for r in range(len(dummy_pool)):
    for c in range(len(t_QP_pool)):
        error_1D = []
        t_QP = t_QP_pool[c]  # units ms
        p_QP = 1.0 - exp(-t_meas/t_QP)
        p_QP_VTB = 1.0 - exp(-t_meas/t_QP_VTB)
        for i in range(10):
            Hidden_Signal = generate_hidden_signal(p_QP=[p_QP, p_QP])
            Observed_Signal = hidden_to_observed_signal(Hidden_Signal)
            Recovered_Signal = observed_to_recovered_signal(Observed_Signal, p_QP=p_QP_VTB)
            error_1D.append((float(transitions_count(Recovered_Signal) - transitions_count(Hidden_Signal)) /
                             transitions_count(Hidden_Signal)))
        error[r][c] = average(error_1D*100).round(decimals=2)

fig, ax = plt.subplots(figsize=(10, 10))
im, cbar = heatmap(error, dummy_pool, t_QP_pool, ax=ax,
                   cmap="YlGn", cbarlabel="error_1D [t_QP=10 ms]")
texts = annotate_heatmap(im, valfmt="{x:.0f} %")
fig.tight_layout()
plt.show()
