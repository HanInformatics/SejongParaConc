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

Command 'head -n 3 4RT_01AL.txt.conc'

\[para/4RT_01AL.txt]	<s>[1.1.h1] 베를린/NNP 자유대학/NNP 대통령/NNG 연설문/NNG	<s>[1.1.h1] ADDRESS/NN BY/IN PRESIDENT/NN KIM/NNP DAE-JUNG/NNP OF/IN THE/DT REPUBLIC/NNP OF/IN KOREA/NNP AT/IN THE/DT FREE/NNP UNIVERSITY/NNP OF/IN BERLIN/NNP
 
\[para/4RT_01AL.txt]	<s>[1.1.p1.s1] 존경/NNG 하/XSV 는/ETM 피터/NNP 궤트겐스/NNP 총장/NNG ,/SP 존경/NNG 하/XSV 는/ETM 교수/NNG 및/MAJ 내외/NNG 귀빈/NNG ,/SP 그리고/MAJ 친애/NNG 하/XSV 는/ETM 학생/NNG 여러분/NP !/SF	<s>[1.1.p1.s1] President/NN Gaehtsgens/NNP ,/, faculty/NN members/NNS ,/, honorable/JJ guests/NNS ,/, and/CC students/NNS of/IN the/DT Free/NNP University/NNP of/IN Berlin/NNP ,/,

\[para/4RT_01AL.txt\]	<s>[1.1.p2.s1] 나/NP 는/JX 먼저/MAG 이/MM 자리/NNG 를/JKO 빌리/VV ㅓ/EC 폐허/NNG 와/JC 분단/NNG 을/JKO 딛/VV 고/EC 일어서/VV ㅓ서/EC 오늘/NNG 의/JKG 번영/NNG 과/JC 통일/NNG 의/JKG 위대/NNG 하/XSA ᄂ/ETM 역사/NNG 를/JKO 창조/NNG 하/XSV ᄂ/ETM 독일/NNP 국민/NNG 에게/JKB 마음/NNG 으로부터/JKB 경의/NNG 와/JC 축하/NNG 를/JKO 드리/VV 고자/EC 하/VV ᄇ니다/EF ./SF	<s>[1.1.p2.s1] First/RB and/CC foremost/RB ,/, I/PRP would/MD like/VB to/TO express/VB my/PRP$ deepest/JJS respect/NN for/IN and/CC heartfelt/JJ congratulations/NNS to/TO the/DT great/JJ nation/NN of/IN Germany/NNP which/WDT has/VBZ achieved/VBN the/DT historic/JJ task/NN of/IN reunification/NN and/CC prosperity/NN overcoming/VBG the/DT ruins/NNS of/IN war/NN and/CC division/NN of/IN the/DT territory/NN ./.
  

