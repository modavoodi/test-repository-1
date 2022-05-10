# # Here's how you can use the DWaveCliqueSampler and find_clique_embedding. The DWaveCliqueSampler is a wrapper around find_clique_embedding, so you should get similar results with either approach. 

# from dwave.system import DWaveCliqueSampler, DWaveSampler, FixedEmbeddingComposite, EmbeddingComposite
# import minorminer.busclique 

# # using CliqueSampler
# sampleset = DWaveCliqueSampler().sample_qubo(Q)

# # using find_clique_embedding
# qpu = DWaveSampler()
# embedding = minorminer.busclique.find_clique_embedding(set().union(*Q), qpu.to_networkx_graph())
# sampleset = FixedEmbeddingComposite(qpu, embedding).sample_qubo(Q)

# #----------------------------------------------------------------

# DWaveCliqueSampler can only handle cliques of size up to 119.  You can check this by printing "DWaveCliqueSampler().largest_clique_size". With our current Advantage_system1.1 solver, this is the largest size clique that we can reliably find in the Pegasus 16x16 topology, so it is limited with this solver to problems of size 119 or smaller. 

from dwave.system import DWaveCliqueSampler
import dimod

print (DWaveCliqueSampler().largest_clique_size)

# or
# bqm = dimod.generators.ran_r(1, 6)
sampler = DWaveCliqueSampler()
print (sampler.largest_clique_size)
