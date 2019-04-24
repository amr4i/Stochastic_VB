import matplotlib.pyplot as plt 
from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline, BSpline
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np 



def read_files(kappa, batchsize):	
	time = []
	perplexity = []
	f = open('log_results/log_'+str(kappa)+'_'+str(batchsize)+'.dat')
	lines = f.readlines()
	for i in range(1,len(lines)):
		values = [float(j) for j in lines[i].strip().split()]
		time.append(values[1])
		perplexity.append(values[3]/values[4])
	return np.array(time), np.array(perplexity)


def main():
	combinations = [[0.5, 100], [0.7, 50], [0.7, 100], [0.7, 200], [0.9, 100]]
	time = []
	perplexity = []

	for i, c in enumerate(combinations):
		t,p = read_files(c[0], c[1])
		time.append(t)
		perplexity.append(p)

	"""kappa variation"""
	kappa = [0, 2, 4]
	lowest = time[kappa[0]][-1]

	plt_time = []
	plt_perplexity = []

	for k in kappa:
		if lowest > time[k][-1]:
			lowest = time[k][-1]

	for k in kappa:
		temp = time[k]
		for i, t in enumerate(temp.tolist()):
			if (t >= lowest):
				break

		tv = time[k][:i]
		tv = tv/3600.0
		pv = perplexity[k][:i]
		plt_time.append(tv)
		plt_perplexity.append(pv)




	plt.figure()
	for tv, pv in zip(plt_time, plt_perplexity):

		# xnew = np.linspace(tv.min(),tv.max(),1000) 
		# smooth = spline(tv,pv,xnew)
		# plt.plot(xnew, smooth)
		plt.plot(tv, pv)

	plt.legend(('kappa = 0.5', 'kappa = 0.7', 'kappa =0.9'))

	plt.ylabel('Log likelihood per word')
	plt.xlabel('Time')
	plt.title('Variation with kappa (Online HDP)')

	"""batchsize variation"""

	batchsize = [1, 2, 3]

	lowest = time[batchsize[0]][-1]

	plt_time = []
	plt_perplexity = []

	for k in batchsize:
		if lowest > time[k][-1]:
			lowest = time[k][-1]

	for k in batchsize:
		temp = time[k]
		for i, t in enumerate(temp.tolist()):
			if (t >= lowest):
				break

		tv = time[k][:i]
		tv = tv/3600.0
		pv = perplexity[k][:i]
		plt_time.append(tv)
		plt_perplexity.append(pv)




	plt.figure()
	for tv, pv in zip(plt_time, plt_perplexity):

		# xnew = np.linspace(tv.min(),tv.max(),10) 
		# spl = make_interp_spline(tv, pv, k=9)
		# smooth = spl(xnew)
		
		# smooth = spline(tv,pv,xnew)
		
		# plt.plot(xnew, smooth)
		# plt.plot(xnew,smooth)
		plt.plot(tv, pv)
	plt.ylabel('Log likelihood per word')
	plt.xlabel('Time(in Hrs.)')
	plt.title('Variation with batchsize (Online HDP)')




	plt.legend(('batchsize = 50', 'batchsize = 100', 'batchsize = 200'))



	plt.show()





if __name__ == '__main__':
	main()