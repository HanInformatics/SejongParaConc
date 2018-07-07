#-*-coding:utf-8-*-
# date: 2016. June.
# writer: Jo Eun Kyoung
# goal : to get pair sentences from sejong pararell corpus
# etc: This works in Python 2.X

import sys, os, pdb

err_fn = {}
err_id = {}

def conc_pair(list_pair_id, dic_k, dic_f, k_fn, f_fn, pair_fn):

	outfn = pair_fn +'.conc'
        print 'Currently, making this:', outfn
	outfile = open(outfn, 'w')
	for l_id in list_pair_id:
		k_ids = l_id[0].strip().split(' ')
		f_ids = l_id[1].strip().split(' ')
		outline = ''
		if len(k_ids) < 2 and len(f_ids) < 2 :
			outline ='[s][%s]\t' %pair_fn
			#outfile.write('[s][%s]\t' %pair_fn)
		else:
			outline = '[m][%s]\t' %pair_fn
			#outfile.write('[m][%s]\t' %pair_fn)

		for k_id in k_ids :
			add_line = '<s>[%s] %s' %(k_id, dic_k.get(k_id, 'fail'))
			outline += add_line
		outline += '\t'
		#6RT_01AL.txt, 1.10.p8.s1 no exist in ~EE.txt. there is no pairing.
		f_id_sen = ''
		for f_id in f_ids:
			f_id_sen = dic_f.get(f_id, 'fail')
			add_line = '<s>[%s] %s' %(f_id, f_id_sen)
			outline += add_line
			#outfile.write('<s>[%s] %s' %(f_id, dic_f.get(f_id, 'fail')))
		outline += '\n'
		if f_id_sen != 'fail' and outline[:3] != '[m]': outfile.write(outline)
	outfile.close()
	return

def make_pair_al(fn, k_fn, f_fn, dic_pair_id):
	list_pair_id = []
	infile = open(fn)
	#tfile = open(fn +'.tid', 'w')
	for line in infile.xreadlines():
		line = line.strip()
		s_tag = '<link xtargets="'
		s_pos = line.find(s_tag)
		if s_pos != -1 :
			tag_len = len(s_tag)
			#e_pos = line.find('"/>', s_pos + tag_len)
			e_pos = line.find('"', s_pos + tag_len)
			if e_pos != -1 :
				id_str = line[s_pos+tag_len:e_pos]
				if id_str == '' :
					print >> sys.stderr, 'xtargets are errors', line, 'fn', fn
					continue

				left_right = id_str.split(';') # 0, 1
				if len(left_right) != 2 : raw_input('%s' %line)
				if fn == 'AL/4RT_01AL.txt' or fn == 'AL/4RT_02AL.txt' or fn == 'AL/4RT_03AL.txt' : # left id is korean id
					if left_right[0].strip() != '':
						dic_pair_id[left_right[0].strip()] = left_right[1].strip()
						list_pair_id.append((left_right[0].strip(), left_right[1].strip()))
						#tfile.write('%s\t%s\n' %(left_right[0], left_right[1]))
					else:
						print >> sys.stderr, 'left_ids are empty', line, 'fn', fn
				else: # right id(left_right[1]) is korean id
					if left_right[1].strip() != '':
						dic_pair_id[left_right[1].strip()] = left_right[0].strip()
						list_pair_id.append((left_right[1].strip(), left_right[0].strip()))
						#tfile.write('%s\t%s\n' %(left_right[1], left_right[0]))
					else:
						print >> sys.stderr, 'right_ids are empty', line, 'fn', fn

		else: pass

	infile.close()
	#tfile.close()
	return list_pair_id


def make_line(fn, dic_sentences, file_type=0):

	infile = open(fn, 'r')
	flag_start = 0
	flag_sentence = 0
	sentence_id = ''
	l_cnt = 0
	list_sentences = [] # pair sentence id with its sentence
	list_sentence = [] # accumulate <tok>s to a list
	for line in infile.xreadlines():
		line = line.strip()
		l_cnt += 1
		#8RT_10EE, 8RT_15KE
		if (line.find('<chunk>') != -1 or line.find('<div id') != -1 ) and flag_start == 0 :
			flag_start = 1
		elif flag_start == 1 and ( line.find('<head id=') != -1 or line.find('<p id=') != -1 or line.find('<s id=') != -1) :
			flag_sentence = 1
			sentence_id = line.replace('<head id="', '').replace('<p id="', '').replace('<s id="', '').replace('">', '')
			#print sentence_id #.decode('utf-8').encode('cp949')
		elif flag_start == 1 and flag_sentence == 1 :
			if line.find('<tok>') != -1 or line.find('<orth>') != -1 or line.find('<ctag>') != -1 or line.find('<seg><mor>') != -1  :
				#print line #.decode('utf-8').encode('cp949')
				if file_type == 0 :
					add_k_toks(line, list_sentence)
				else:
					#pdb.set_trace()
					add_f_toks(line, list_sentence)
			elif line.find('</head>') != -1 or line.find('</p>') != -1 or line.find('</s>') != -1 :
				flag_sentence = 0
				line_sentence = ''.join(list_sentence)
				dic_sentences[sentence_id] = line_sentence.strip()
				list_sentences.append((sentence_id, line_sentence.strip()))
				del list_sentence[0:len(list_sentence)]
		else:
			pass

	infile.close()
	return list_sentences

def add_k_toks(line, tok_list):
	if line.find('<orth>') != -1 : return

	n_line = line.replace('<tok>', '').replace('<seg><mor>', '').replace('</mor><pos>', '/').replace('</pos></seg>', ' ').replace('</tok>', 'sp/sp')
	#morpheme delimiter is ' '. <tok>(space) is sp/sp
	tok_list.append(n_line)
	return

def add_f_toks(line, tok_list) :
	if line.find('<seg><mor>') != -1 :
		s_pos = line.find('<pos>')
		if s_pos != -1 :
			e_pos = line.find('</pos>', s_pos)
			n_line = line[s_pos+5:e_pos] + ' '
	else:
		n_line = line.replace('<tok>', '').replace('<orth>', '').replace('</orth>', '/').replace('<ctag>', '').replace('</ctag>', ' ').replace('</tok>', 'sp/sp')
	#morpheme delimiter is ' '. <tok>(space) is sp/sp
	if n_line != '' : tok_list.append(n_line)
	return

def write_dic(dic, fn):
	tmpfile = open(fn, 'wb')
	for ele in sorted(dic) :
		tmpfile.write('%s\t%s\n' %(ele, dic[ele]))
	tmpfile.close()

def write_list(s_list, fn):
	tmpfile = open(fn, 'wb')
	for ele in s_list :
		tmpfile.write('%s\t%s\n' %(ele[0], ele[1]))
	tmpfile.close()


def pair_sentence_al(pair_fn, k_fn, f_fn):
	try :
		dic_pair_id = {} # left id : right id
		dic_k = {} # korean id : sentence
		dic_f = {} # english id : sentence
		list_pair_id = make_pair_al(pair_fn, k_fn, f_fn, dic_pair_id)
		#write_dic(dic_pair_id, pair_fn + '.id')
		#pdb.set_trace()
		write_list(list_pair_id, pair_fn + '.id')

		list_k = make_line(k_fn, dic_k)
		write_list(list_k, k_fn +'.id')

		#pdb.set_trace()
		list_f = make_line(f_fn, dic_f, 1)
		write_list(list_f, f_fn +'.id')

		conc_pair(list_pair_id, dic_k, dic_f, k_fn, f_fn, pair_fn)
	except Exception, e:
		print pair_sentence_al.__name__, e

def proc_all(infn):
	infile = open(infn)
	for l in infile.xreadlines():
		l = l.strip()
		tabs = l.split('\t')
		if len(tabs) != 3 : continue
		try:
			pair_sentence_al(tabs[0], tabs[1], tabs[2])
		except Exception, e:
			print proc_all.__name__, e
	infile.close()

	for each in sorted(err_fn) :
		print >> sys.stderr, each, err_fn[each]

if __name__ == "__main__" :
	try :
		proc_all('pair.list')
                if os.path.exists('conc') != True:
                    os.system('mkdir conc')
                print 'Now, moving para/*.conc to conc/'
                os.system("mv para/*.conc conc/")
	except Exception, e:
		print e
		print 'usage: python %s pair_file_name'
