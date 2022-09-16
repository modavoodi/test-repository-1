from dwave.system import DWaveSampler

sampler = DWaveSampler(region="eu-central-1")
qubit_a = sampler.nodelist[0]
qubit_b = next(iter(sampler.adjacency[qubit_a]))
sampleset = sampler.sample_ising({qubit_a: -1, qubit_b: 1}, {}, num_reads=100)

print( sampleset.first.sample[qubit_a] == 1 and sampleset.first.sample[qubit_b] == -1 )

