
import random

random.seed(0)

def read_csv(filein):
	f=open(filein)
	data=[ l.split(',') for l  in f.read().splitlines()]
	print data
	return data



def make_network(data):
	connections={}
	hid2level={}
	for line in data:
		hid=int(line[0])
		level=int(line[2])
		hid2level[hid]=level

	network_edges={}
	for hid1 in hid2level:
		network_edges[hid1]=[]
		for hid2 in hid2level:
			if hid2level[hid2] > hid2level[hid1]:
				network_edges[int(hid1)].extend(int(hid2)
	return network_edges,hid2level

if __name__=='__main__':

	inputfile='hospital_list.csv'
	number_pids=1000
	hospital_data=read_csv(inputfile)
	pids=range(1000)
	pid_data= dict([(pid,[]) for pid in pids])


	HIDs=[i[0] for i in hospital_data]
	network_edges,hid2level=make_network(hospital_data)


	#print HIDs
	#quit()
	#quit()
	for pid in pids:
		pid_data[pid]=(random.sample(HIDs,1))
	print pid_data

	for pid in pids:
		pid_data[pid][-1]
		#random()<0.03

		current_hospital=pid_data[pid][0]
		while current_hospital:
			print current_hospital
			pid_data[pid].extend(current_hospital)
			if len(network_edges[current_hospital])>0:
				current_hospital=random.sample(network_edges[current_hospital],1)[0]

	print pid_data



