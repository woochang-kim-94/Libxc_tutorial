import numpy as np
#data = np.loadtxt('./VXC.txt', skiprows=13, dtype=np.complex128)
#print(data)
f = open('./RHOtot.txt', 'r')
f.readline()
#nsf, ng_g, ntran, cell_symmetry, nat, ecutrho = np.int32(f.readline().split())
f.readline()
#n1, n2, n3 = no.int32(f.readline().split())
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()
ng = np.int32(f.readline().split()[0])
gvec = np.int32(f.readline().split()).reshape((ng,3))
print(gvec[:5])
f.readline()
ng = np.int32(f.readline().split()[0])
data = f.readline().split()
f.close()
data = np.array([np.float64(eval(str)) for str in data]).view(np.complex128).reshape(ng)
print(data[0:5])
print(data.shape)
np.savetxt('rhotot_gvec.txt',gvec)
np.save('rhotot_pw2bgw',data)
