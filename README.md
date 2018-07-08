# SejongParaConc


Sejong parallel corpus should be prepared. 
By 2015, CD for it could be given to researchers who request to 국립국어원. 
Thesedays, it's difficult to get this data from 언어정보나눔터 in National Institute of Korean Language(국립국어원). 

Korean English parallel corpus is composed of three types of files, ...AL.txt, ...KK/KE.txt, and ...EE/EK.txt
AL is for mapping sentence ids of Korean and English. 
KK/KE is for Korean texts. Here KE means this text is originally Korean text and translated into English. 
EE/EK is for English texts. Here EK means this text is originally English text and translated into Korean. 
In Sejong corpus CD, the directory of parallel corpus is like below. 

CD1/02_말뭉치/병렬/한영병렬/한영병렬_말뭉치/형태분석_말뭉치/TXT

All the files under the directory are encoded in 'utf-16'.

To convert utf-16 to convert-8, run convert_16t08.py. It assumes 'TXT' directory you have in the current directory. 

python convert_16t08.py

After running it, All the files encoded with utf-8 are created under 'para' which is newly created. 
So, all three types of files(...AL.txt, ...KK.txt, ...EE.txt) are under 'para' directory. 

Now, we are going to make files of pair sentences. To do this, 'para_conc.py' must be with 'para.list' in the parent directory of 'para'. And then give a command below. 

python para_conc.py

After running it, there are sentence paired files under 'conc' directory which is newly created. 
Voilà. 

Command 'ls' under 'conc'

4RT_01AL.txt.conc	6RT_14AL.txt.conc	8RT_22AL.txt.conc
4RT_02AL.txt.conc	6RT_15AL.txt.conc	8RT_23AL.txt.conc
4RT_03AL.txt.conc	6RT_16AL.txt.conc	8RT_24AL.txt.conc
....

Command 'head -n 1 4RT_01AL.txt.conc'

\[para/4RT_01AL.txt]	\<s>[1.1.h1] 베를린/NNP 자유대학/NNP 대통령/NNG 연설문/NNG	\<s>[1.1.h1] ADDRESS/NN BY/IN PRESIDENT/NN KIM/NNP DAE-JUNG/NNP OF/IN THE/DT REPUBLIC/NNP OF/IN KOREA/NNP AT/IN THE/DT FREE/NNP UNIVERSITY/NNP OF/IN BERLIN/NNP

