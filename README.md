# SejongParaConc


Sejong parallel corpus should be prepared. 
By 2015, CD for it could be given to researchers who request to 국립국어원. 
Thesedays, it's difficult to get this data from 언어정보나눔터 in National Institute of Korean Language(국립국어원). 

Korean English parallel corpus is composed of three types of files, ...AL.txt, ...KK/KE.txt, and ...EE/EK.txt
AL is for mapping sentence ids of Korean and English. 
KK/KE is for Korean texts. Here KE means this text is originally Korean text and translated into English. 
EE/EK is for English texts. Here EK means this text is originally English text and translated into Korean. 
All three types of files must be 'para' directory. 
And 'para.list' must be with 'para_conc.py' in the parent directory of 'para'. 

para_conc.py works in Python2.
To run this, 

python para_conc.py

After running it, there are sentence paired files under 'conc' directory which is created newly. 
Voilà. 

Command 'ls' under 'conc'

4RT_01AL.txt.conc	6RT_14AL.txt.conc	8RT_22AL.txt.conc
4RT_02AL.txt.conc	6RT_15AL.txt.conc	8RT_23AL.txt.conc
4RT_03AL.txt.conc	6RT_16AL.txt.conc	8RT_24AL.txt.conc
....

Command 'head -n 1 4RT_01AL.txt.conc'

\[para/4RT_01AL.txt]	<s>[1.1.h1] 베를린/NNP 자유대학/NNP 대통령/NNG 연설문/NNG	<s>[1.1.h1] ADDRESS/NN BY/IN PRESIDENT/NN KIM/NNP DAE-JUNG/NNP OF/IN THE/DT REPUBLIC/NNP OF/IN KOREA/NNP AT/IN THE/DT FREE/NNP UNIVERSITY/NNP OF/IN BERLIN/NNP

