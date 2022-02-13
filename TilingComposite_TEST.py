from dwave.system import TilingComposite
from dwave.system import DWaveSampler, DWaveCliqueSampler, EmbeddingComposite, TilingComposite

#sample = DWaveCliqueSampler(solver={'topology__type': 'chimera'})
#sampler = EmbeddingComposite(TilingComposite(sample, 4, 4))

# FROM OCEAN DOCUMENTATION
#>>> from dwave.system import DWaveSampler, EmbeddingComposite
#>>> from dwave.system import TilingComposite
#...
#>>> qpu_2000q = DWaveSampler(solver={'topology__type': 'chimera'})
#>>> sampler = EmbeddingComposite(TilingComposite(qpu_2000q, 1, 1, 4))
#>>> Q = {(1, 1): -1, (1, 2): 2, (2, 1): 0, (2, 2): -1}
#>>> sampleset = sampler.sample_qubo(Q)
#>>> len(sampleset)> 1
#True

#qpu = DWaveSampler(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', endpoint='https://cloud.dwavesys.com/sapi/', solver={'topology__type': 'chimera'})
qpu = DWaveSampler(solver={'topology__type': 'chimera'})
sampler = EmbeddingComposite(TilingComposite(qpu, 4, 4))
Q = {(1, 1): -1, (1, 2): 2, (2, 1): 0, (2, 2): -1}
sampleset = sampler.sample_qubo(Q)
#print(sampleset)
if len(sampleset) > 1:
    print("Length of sampleset is >1")
else:
    print("Length of sampleset is <=1")


#qpu_2000q = DWaveSampler(solver={'topology__type': 'chimera'})
#sampler = EmbeddingComposite(TilingComposite(qpu_2000q, 4, 4))
#Q = {(1, 1): -1, (1, 2): 2, (2, 1): 0, (2, 2): -1}
#sampleset = sampler.sample_qubo(Q)
#print(sampleset)
