import dimod 

cqm = dimod.CQM()
integers = dimod.IntegerArray(10)
binaries = dimod.BinaryArray(2)

cqm.set_objective(sum(i*i for i in integers))
cqm.add_discrete(sum(binaries) == 1)
