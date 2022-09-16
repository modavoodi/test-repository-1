from dwave.system import DWaveSampler, EmbeddingComposite

## sampler = DWaveSampler(region="na-west-1")
## sampler = EmbeddingComposite(sampler)
sampler = EmbeddingComposite(DWaveSampler(region="na-west-1"))

h = {'a': -1., 'b': 2}
J = {('a', 'b'): 1.5}
sampleset = sampler.sample_ising(h, J, num_reads=100)
print(sampleset.first.energy)

