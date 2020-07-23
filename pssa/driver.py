import random

import dwave_networkx as dnx
import networkx as nx
from matplotlib import pyplot as plt
from minorminer import find_embedding

from pssa.annealer import run_simulated_annealing
from pssa.context import OptimizationContext
from pssa.initializer import triangle_semi_clique_embed, divide_guiding_pattern

random.seed(1)

G = dnx.chimera_graph(16, 16, 4)  # Dwave 2000q arch
input = nx.generators.fast_gnp_random_graph(128, 0.4, seed=1)

print(input.number_of_edges())

embed = find_embedding(input, G, verbose=1)

# gp = triangle_semi_clique_embed(16, 4)
# initial = divide_guiding_pattern(gp, len(input))
#
# context = OptimizationContext(16, 4, input, gp)
# embed = run_simulated_annealing(context, initial)
#
# embed = {i: embed[i] for i in range(len(embed))}

plt.ion()
plt.figure(figsize=(20, 20))
dnx.draw_chimera_embedding(G, embed)