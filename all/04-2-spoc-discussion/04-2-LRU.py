phypageframesize = 4
addrList = [2,0,3,1,4,1,0,1,2,3]

def lookForPages():
	memory = []		# include pages in memory
	cnt = 0			# current visit time
	dict_ref = {}	# last ref-time of pages
	miss = 0		# page-fault time
	for nStr in addrList:
		cnt += 1
		print("[%d]look for page[%d]"%(cnt,nStr))
		if(not nStr in memory):	# page fault
			miss += 1
			print("page fault[%d]"%miss)
			if(len(memory) < phypageframesize):	# add a page directly
				memory.append(nStr)
			else:	# need to swap out a pages
				# find the idx with smallest ref-time in dict_ref
				# (so it hasn't been visit for the longest time)
				min = 100
				for idx in range(len(memory)):
					if(dict_ref[memory[idx]] < min):
						idx_final = idx
						min = dict_ref[memory[idx]]
				# replace the page at idx_final by the new page
				memory[idx_final] = nStr
		# update the last-ref-time of nStr
		dict_ref[nStr] = cnt
		
		print("\nmemory:")
		for page in memory:
			print("page[%d] last-ref[%d]"%(page, dict_ref[page]))
		print()
	print("Total: %d, miss: %d"%(len(addrList), miss))

if __name__ == '__main__':
	lookForPages()