# Jigme Lobsang Lepcha Roll no: 2016045
# Rajat Kumar Singh Roll no: 2016182
def offByK(s1,s2,k):
	#Returns True if s1 and s2 differ in exactly k positions
	count=0
	if len(s1)==len(s2):
		 for i in range(len(s1)):
		 	if s1[i]!=s2[i]:
		 		count+=1
		 if k==count:
		 	return True
		 else:
		 	return False
	else:
		return False

def offBySwaps(s1,s2):
	w1=""
	w2=""
	if len(s1)==len(s2):
		w1="".join(sorted(s1))
		w2="".join(sorted(s2))
		if w1==w2:
			return True
		else:
			return False
	else:
		return False
def offByKExtra(s1,s2,k):
	x1=[]
	x2=[]
	count=0
	for i in s1:
		x1.append(i)
	for i in s2:
		x2.append(i)
	if len(s1)>len(s2):
		diff=len(s1)-len(s2)
		for i in range(diff):
			x2.append("")
		for i in range(len(s1)):
			if x1[i]!=x2[i]:
				if x1[i].lower()==x2[i].lower():
					count+=1
					x1[i]=x2[i]
				else:
					x2.insert(i,x1[i])
					count+=1
		for i in range(diff):
			x1.append("")
	else:
		diff=len(s2)-len(s1)
		for i in range(diff):
			x1.append("")
		for i in range(len(s2)):
			if x1[i]!=x2[i]:
				if x1[i].lower()==x2[i].lower():
					count+=1
					x1[i]=x2[i]
				else:
					x1.insert(i,x2[i])
					count+=1
		for i in range(diff):
			x2.append("")
	if (x1==x2 and k==count):
		return True
	else:
		return False


def ListOfNearStrings(s,L,k):
	d=[]
	for i in range(len(L)):
		if L[i]!=s:
			offk=offByK(L[i],s,k)
			offswap=offBySwaps(L[i],s)
			offbk=offByKExtra(s,L[i],k)
			if (offk==True or offswap==True or offbk==True):
				d.append(L[i])
	return d
	
def compare_distr(L1,L2,bin):
	a=len(L1)
	b=len(L2)
	x1=[]
	x2=[]
	if(a!=b):
		return False
	elif(a==0 or b==0):
		return False
	else:
		#computing frequency distributuion for L1
		L1.sort()
		LL_L1=L1[0]
		UL_L1=L1[a-1]
		range_L1=UL_L1-LL_L1
		temp_LL_L1=LL_L1
		temp_UL_L1=LL_L1+bin
		count_L1=int(range_L1/bin)+1
		for x in range(count_L1):
			count1=0
			for y in range(a):
				if(temp_LL_L1<=L1[y]<temp_UL_L1):
					count1+=1
			x1.append(count1)
			temp_LL_L1+=bin
			temp_UL_L1+=bin
		#in a similar fashion, computing frequency distributuion for L2
		L2.sort()
		LL_L2=L2[0]
		UL_L2=L2[b-1]
		range_L2=UL_L2-LL_L2
		temp_LL_L2=LL_L2
		temp_UL_L2=LL_L2+bin
		count_L2=int(range_L2/bin)+1
		for x in range(count_L2):
			count2=0
			for z in range(b):
				if(temp_LL_L2<=L2[z]<temp_UL_L2):
					count2+=1
			x2.append(count2)
			temp_LL_L2+=bin
			temp_UL_L2+=bin
		
		if(x1==x2):
			return True
		else:
			return False