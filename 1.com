%chk=Tyrosinase_chromen.chk
%mem=48GB
%nprocshared=48
# restart

Title Card Required

2 2 0 1 0 2 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
 C(Fragment=7)    0    6.14407600    2.90273000    5.93840500 H
 O(Fragment=7)    0    4.26971400    2.08482700    7.19639600 H
 C(Fragment=7)    0    6.35374600    2.16460000    4.58824500 H
 C(Fragment=7)    0    5.03091400    1.82648800    3.95871700 H
 N(Fragment=7)    0    4.39566200    0.60704500    4.05259500 H
 C(Fragment=7)    0    4.12296200    2.65033300    3.32503100 H
 C(Fragment=7)    0    3.17286500    0.70104100    3.51249300 H
 N(Fragment=7)    0    2.97282600    1.93860800    3.06052100 H
 H(Fragment=7)    0    6.95936600    1.25507000    4.74061800 H
 H(Fragment=7)    0    6.91839700    2.84060100    3.92641600 H
 H(Fragment=7)    0    4.75754800   -0.25753600    4.45256500 H
 H(Fragment=7)    0    4.21612000    3.70376200    3.06498100 H
 H(Fragment=7)    0    2.47932000   -0.13775600    3.46832900 H
 H(Fragment=7)    0    5.44842000    3.73899900    5.76699600 H
 C(Fragment=8)    0   -3.68215700    4.44951400    5.17661300 H
 O(Fragment=8)    0   -5.07505900    5.03360500    6.99197500 H
 C(Fragment=8)    0   -3.35268900    2.92041200    5.22512100 H
 C(Fragment=8)    0   -1.94937100    2.63665900    4.77349000 H
 N(Fragment=8)    0   -0.89585000    2.52405000    5.64998800 H
 C(Fragment=8)    0   -1.38612200    2.49044800    3.52413600 H
 C(Fragment=8)    0    0.23898400    2.32997600    4.96584200 H
 N(Fragment=8)    0   -0.02043100    2.30158300    3.66048300 H
 H(Fragment=8)    0   -3.75279100    4.75016100    4.11880200 H
 H(Fragment=8)    0   -3.47225000    2.56333800    6.26267600 H
 H(Fragment=8)    0   -4.06898400    2.36651000    4.59704300 H
 H(Fragment=8)    0   -0.95732800    2.60463400    6.66074700 H
 H(Fragment=8)    0   -1.87607900    2.54117400    2.55283300 H
 H(Fragment=8)    0    1.22038700    2.22704100    5.42720700 H
 C(Fragment=4)    0    2.46734100    8.87366300   -0.02286800 H
 O(Fragment=4)    0    4.22614500    9.53721000   -1.47272600 H
 C(Fragment=4)    0    2.32444600    7.47334600   -0.67342700 H
 C(Fragment=4)    0    1.98964300    6.39090100    0.32412000 H
 N(Fragment=4)    0    1.22707600    6.64146700    1.44001000 H
 C(Fragment=4)    0    2.27619000    5.03860400    0.37566900 H
 C(Fragment=4)    0    1.06961900    5.50840200    2.13112800 H
 N(Fragment=4)    0    1.69249800    4.50402600    1.51042300 H
 H(Fragment=4)    0    3.19287800    8.79325800    0.80679000 H
 H(Fragment=4)    0    1.53645400    7.52338100   -1.44901400 H
 H(Fragment=4)    0    3.26693900    7.21747400   -1.17907700 H
 H(Fragment=4)    0    0.86405800    7.57810800    1.64290900 H
 H(Fragment=4)    0    2.83545100    4.41960600   -0.32618400 H
 H(Fragment=4)    0    0.51027800    5.43805800    3.06341000 H
 C(Fragment=6)    0  -12.06998200    0.48814800   -0.02576400 H
 O(Fragment=6)    0  -14.41281100    0.00357200    0.20847800 H
 C(Fragment=6)    0  -11.88015600    1.03788500    1.40537300 H
 C(Fragment=6)    0  -10.48020700    0.80998100    1.94652400 H
 C(Fragment=6)    0  -10.07844000   -0.47218900    2.36773100 H
 C(Fragment=6)    0   -9.56068200    1.86951000    2.04584900 H
 C(Fragment=6)    0   -8.78974700   -0.69061700    2.87412100 H
 C(Fragment=6)    0   -8.27128500    1.65747700    2.56070900 H
 C(Fragment=6)    0   -7.88107500    0.37485100    2.97493900 H
 H(Fragment=6)    0  -11.86510200   -0.59762200   -0.01809000 H
 H(Fragment=6)    0  -12.62345700    0.53819300    2.04827300 H
 H(Fragment=6)    0  -12.11144700    2.11859600    1.40617200 H
 H(Fragment=6)    0  -10.78480100   -1.30822000    2.30598900 H
 H(Fragment=6)    0   -9.85989700    2.87462000    1.72891900 H
 H(Fragment=6)    0   -8.49627300   -1.69413800    3.19848800 H
 H(Fragment=6)    0   -7.57570400    2.49810800    2.64608400 H
 H(Fragment=6)    0   -6.87659300    0.20605800    3.37431800 H
 C(Fragment=12)   0   -4.77411300    1.04976100   -5.12137100 H
 O(Fragment=12)   0   -3.57547500   -0.91398600   -4.48397000 H
 C(Fragment=12)   0   -4.71102200    2.27911200   -4.16746000 H
 C(Fragment=12)   0   -3.30885300    2.71450200   -3.85538300 H
 N(Fragment=12)   0   -2.80846300    2.84650500   -2.58664900 H
 C(Fragment=12)   0   -2.27405000    3.11319500   -4.68679200 H
 C(Fragment=12)   0   -1.53763700    3.29659500   -2.68047300 H
 N(Fragment=12)   0   -1.17775500    3.47194600   -3.94104100 H
 H(Fragment=12)   0   -3.88659600    1.08410200   -5.77969900 H
 H(Fragment=12)   0   -5.22792300    3.11420700   -4.67198200 H
 H(Fragment=12)   0   -5.26688200    2.07788000   -3.23702000 H
 H(Fragment=12)   0   -3.26466800    2.60645200   -1.70891200 H
 H(Fragment=12)   0   -2.26759900    3.15927500   -5.77591600 H
 H(Fragment=12)   0   -0.90563700    3.48296600   -1.81367100 H
 C(Fragment=11)   0   -5.53488700   -1.86872000   -2.76405500 H
 O(Fragment=11)   0   -4.61059600   -3.98552400   -3.47504700 H
 C(Fragment=11)   0   -6.79762300   -1.92320400   -1.86644800 H
 C(Fragment=11)   0   -6.74033000   -0.84039700   -0.76539000 H
 O(Fragment=11)   0   -5.72694900   -0.71267100   -0.09022100 H
 H(Fragment=11)   0   -4.62966600   -1.88959700   -2.13895200 H
 H(Fragment=11)   0   -6.82783900   -2.89852300   -1.34949100 H
 H(Fragment=11)   0   -7.70643100   -1.84433500   -2.48695600 H
 C(Fragment=10)   0   -1.22468800   -4.47540000   -3.97491400 H
 O(Fragment=10)   0   -0.62169900   -6.76564000   -4.01410400 H
 C(Fragment=10)   0   -1.38908900   -3.89303700   -2.53508500 H
 C(Fragment=10)   0   -0.61202800   -2.62022700   -2.38497600 H
 N(Fragment=10)   0    0.72262200   -2.62295000   -2.06759600 H
 C(Fragment=10)   0   -0.93017700   -1.28297400   -2.57172600 H
 C(Fragment=10)   0    1.15216300   -1.33665300   -2.05952600 H
 N(Fragment=10)   0    0.17853300   -0.49300500   -2.36354200 H
 H(Fragment=10)   0   -0.15793200   -4.42486900   -4.24823400 H
 H(Fragment=10)   0   -1.01163700   -4.62058700   -1.79557600 H
 H(Fragment=10)   0   -2.46261800   -3.71590500   -2.35685100 H
 H(Fragment=10)   0    1.24963300   -3.47445300   -1.84210600 H
 H(Fragment=10)   0   -1.89560700   -0.87070000   -2.86594000 H
 H(Fragment=10)   0    2.18476600   -1.06298000   -1.83384900 H
 C(Fragment=17)   0    3.42919900   -6.10139500   -1.97426900 H
 O(Fragment=17)   0    1.24181800   -5.32556200   -1.37479600 H
 C(Fragment=17)   0    3.39106700   -5.94264300   -3.51005100 H
 C(Fragment=17)   0    4.48647900   -4.98472700   -4.00231400 H
 S(Fragment=17)   0    4.14770000   -3.20991000   -3.56427600 H
 C(Fragment=17)   0    2.79274800   -2.85903300   -4.76812500 H
 H(Fragment=17)   0    3.74290700   -5.12447400   -1.56206400 H
 H(Fragment=17)   0    2.39957300   -5.57081000   -3.82173300 H
 H(Fragment=17)   0    3.52000800   -6.93562300   -3.98133800 H
 H(Fragment=17)   0    5.45481800   -5.21579100   -3.52651100 H
 H(Fragment=17)   0    4.61377500   -5.03801900   -5.09591800 H
 H(Fragment=17)   0    3.15909100   -2.98525400   -5.79972200 H
 H(Fragment=17)   0    2.48429400   -1.81420400   -4.60273900 H
 H(Fragment=17)   0    1.92826600   -3.51693200   -4.58013900 H
 C(Fragment=16)   0    0.38060800   -7.83620300   -0.57547200 H
 O(Fragment=16)   0   -1.00628100   -7.49972200    1.32582900 H
 H(Fragment=16)   0    0.21429400   -8.92027900   -0.67194800 H
 H(Fragment=16)   0   -0.38525700   -7.31353500   -1.17028000 H
 C(Fragment=13)   0    0.97455200   -6.71191500    3.00389200 H
 O(Fragment=13)   0    2.70235900   -5.06802900    3.04901600 H
 C(Fragment=13)   0    1.49471400   -7.79935400    4.00390900 H
 C(Fragment=13)   0    0.63135800   -9.06912000    3.90620800 H
 C(Fragment=13)   0    2.98321600   -8.13240800    3.79724400 H
 H(Fragment=13)   0   -0.11672600   -6.65831800    3.12853500 H
 H(Fragment=13)   0    1.36942800   -7.36736200    5.01509500 H
 H(Fragment=13)   0    0.71155300   -9.51607900    2.89873400 H
 H(Fragment=13)   0   -0.43254700   -8.85163200    4.10155300 H
 H(Fragment=13)   0    0.97393800   -9.82110200    4.63829600 H
 H(Fragment=13)   0    3.61706000   -7.23406200    3.86522500 H
 H(Fragment=13)   0    3.14258800   -8.59980500    2.80797600 H
 H(Fragment=13)   0    3.31601100   -8.85484800    4.56282500 H
 C(Fragment=14)   0    1.22535100   -3.24790400    4.53756800 H
 O(Fragment=14)   0    3.49548500   -2.48483900    4.51114300 H
 C(Fragment=14)   0    0.15511300   -2.61981500    5.46558800 H
 C(Fragment=14)   0    0.60386100   -1.21777100    5.91288500 H
 C(Fragment=14)   0   -1.22136500   -2.53479600    4.78048800 H
 H(Fragment=14)   0    1.31120300   -2.61440800    3.63614100 H
 H(Fragment=14)   0    0.07608200   -3.26757400    6.36014400 H
 H(Fragment=14)   0    0.66543300   -0.53924100    5.04005200 H
 H(Fragment=14)   0    1.58636700   -1.22862000    6.41659700 H
 H(Fragment=14)   0   -0.13077700   -0.79121100    6.61618700 H
 H(Fragment=14)   0   -1.15631500   -1.92109000    3.86246500 H
 H(Fragment=14)   0   -1.94747800   -2.05961300    5.46174600 H
 H(Fragment=14)   0   -1.63205600   -3.51985800    4.50052300 H
 C(Fragment=15)   0    5.01325900   -3.89634900    0.82313800 H
 O(Fragment=15)   0    6.51074600   -3.55922300   -1.00812200 H
 C(Fragment=15)   0    3.81172300   -2.93294300    0.72385200 H
 H(Fragment=15)   0    4.81045400   -4.76197300    0.16437200 H
 H(Fragment=15)   0    3.61974800   -2.65065700   -0.32808500 H
 H(Fragment=15)   0    4.00239500   -2.02466100    1.32264400 H
 H(Fragment=15)   0    2.91792700   -3.44162600    1.12407300 H
 C(Fragment=9)    0    5.82943700   -0.20858800   -4.70217400 H
 O(Fragment=9)    0    4.82102200    1.88888800   -5.22562000 H
 C(Fragment=9)    0    6.57742500   -0.38676700   -3.33842700 H
 C(Fragment=9)    0    6.29844900    0.54758100   -2.17696200 H
 C(Fragment=9)    0    6.92369300    1.80908200   -2.10937200 H
 C(Fragment=9)    0    5.51904200    0.12387800   -1.08580900 H
 C(Fragment=9)    0    6.77537400    2.62268800   -0.97850100 H
 C(Fragment=9)    0    5.36944700    0.93525600    0.04878900 H
 C(Fragment=9)    0    5.99894200    2.18592400    0.10643700 H
 H(Fragment=9)    0    4.76972400   -0.49558300   -4.59976300 H
 H(Fragment=9)    0    6.38321300   -1.42512900   -3.01708700 H
 H(Fragment=9)    0    7.65467800   -0.32450300   -3.57784600 H
 H(Fragment=9)    0    7.55076300    2.14527000   -2.94301800 H
 H(Fragment=9)    0    5.03937000   -0.86133400   -1.12524800 H
 H(Fragment=9)    0    7.27718500    3.59498100   -0.93796300 H
 H(Fragment=9)    0    4.76525100    0.58684700    0.89486200 H
 H(Fragment=9)    0    5.89226200    2.81388300    0.99625800 H
 C(Fragment=5)    0    2.44365100    4.78183600   -5.97258000 H
 O(Fragment=5)    0    1.64313700    6.94597600   -6.65310800 H
 C(Fragment=5)    0    3.09964900    5.03686200   -4.58642300 H
 C(Fragment=5)    0    2.81237300    3.95499300   -3.58468500 H
 N(Fragment=5)    0    1.59839300    3.33799900   -3.42578900 H
 C(Fragment=5)    0    3.62310000    3.39576000   -2.60988100 H
 C(Fragment=5)    0    1.71034500    2.45792600   -2.39705700 H
 N(Fragment=5)    0    2.92401700    2.46723400   -1.87082900 H
 H(Fragment=5)    0    1.35445100    4.67616300   -5.82243300 H
 H(Fragment=5)    0    2.73166900    6.00952100   -4.21384000 H
 H(Fragment=5)    0    4.18977500    5.12515100   -4.70338400 H
 H(Fragment=5)    0    0.70902800    3.50991200   -3.91946900 H
 H(Fragment=5)    0    4.67525700    3.60465900   -2.41860800 H
 H(Fragment=5)    0    0.90278500    1.77381100   -2.12339400 H
 Cu(Fragment=3)   0    1.34105600    2.65804200    2.24848100 H
 C(Fragment=1)    0   -2.14849100   -1.40480700    0.60326500 H
 C(Fragment=1)    0   -1.94586700    0.93447900    0.35091200 H
 C(Fragment=1)    0   -0.77760400   -1.55787500    0.89675500 H
 C(Fragment=1)    0   -0.52554500    0.81787700    0.67265700 H
 O(Fragment=1)    0    0.11841700    2.02778300    0.66453800 H
 H(Fragment=1)    0   -0.54043700    2.68484700    0.35541900 H
 N(Fragment=4)    0    1.19308400    9.30098300    0.54978700 H
 H(Fragment=4)    0    1.26885000   10.15149400    1.10779100 H
 H(Fragment=4)    0    0.45702400    9.41696800   -0.14907700 H
 C(Fragment=4)    0    3.14391200    9.83707600   -1.01296600 H
 O(Fragment=4)    0    2.54626800   10.98003100   -1.31594400 H
 H(Fragment=4)    0    1.69828200   11.04032900   -0.84801700 H
 C(Fragment=5)    0    2.51777300    6.09427000   -6.77180900 H
 O(Fragment=5)    0    3.76005200    6.71603800   -6.43595800 H
 H(Fragment=5)    0    3.60229900    7.65943700   -6.59527400 H
 N(Fragment=5)    0    2.87569800    3.58620300   -6.71059100 H
 H(Fragment=5)    0    2.48637400    2.72027200   -6.35954400 H
 H(Fragment=5)    0    3.88100100    3.45483000   -6.57280300 H
 N(Fragment=9)    0    6.61935900   -1.02769800   -5.63296300 H
 H(Fragment=9)    0    6.74904700   -1.95419600   -5.22081600 H
 H(Fragment=9)    0    6.09561600   -1.18495600   -6.49708100 H
 C(Fragment=9)    0    5.85738700    1.22646700   -5.17001000 H
 O(Fragment=9)    0    7.03033100    1.69034500   -5.58045700 H
 H(Fragment=9)    0    7.61745400    0.91045100   -5.65902600 H
 C(Fragment=14)   0    2.65760600   -3.17548000    5.07970000 H
 O(Fragment=14)   0    3.09241300   -4.53623800    5.13480900 H
 H(Fragment=14)   0    4.05098100   -4.48108600    4.99146400 H
 N(Fragment=17)   0    4.32645300   -7.17705100   -1.52848700 H
 H(Fragment=17)   0    4.89879100   -7.59765400   -2.24886400 H
 H(Fragment=17)   0    4.95222100   -6.86183200   -0.78972700 H
 N(Fragment=7)    0    7.39426100    3.43428700    6.44344400 H
 H(Fragment=7)    0    7.99822800    2.66256200    6.73695600 H
 H(Fragment=7)    0    7.21646700    3.97753800    7.29010500 H
 C(Fragment=7)    0    5.42935900    1.97389200    6.91785600 H
 O(Fragment=7)    0    6.23214700    1.03164000    7.41873400 H
 H(Fragment=7)    0    5.71341100    0.47884400    8.02723200 H
 C(Fragment=8)    0   -5.02007200    4.63368400    5.85855300 H
 O(Fragment=8)    0   -6.37825800    4.46829000    5.44380800 H
 H(Fragment=8)    0   -6.83029200    4.71226200    6.26566000 H
 N(Fragment=8)    0   -2.62870600    5.22374300    5.84850100 H
 H(Fragment=8)    0   -2.49520100    6.14923300    5.45721200 H
 H(Fragment=8)    0   -2.89488200    5.34743300    6.82702700 H
 N(Fragment=15)   0    5.20750600   -4.28235300    2.22817800 H
 H(Fragment=15)   0    4.29852800   -4.54311000    2.59889200 H
 H(Fragment=15)   0    5.79445700   -5.11703300    2.26704200 H
 C(Fragment=15)   0    6.19797200   -3.21401700    0.11680500 H
 O(Fragment=15)   0    6.78022900   -2.23206900    0.79056100 H
 H(Fragment=15)   0    7.45063700   -1.82567200    0.21467000 H
 N(Fragment=6)    0  -11.16068600    1.14312700   -0.97726100 H
 H(Fragment=6)    0  -11.40893000    0.99433400   -1.94947200 H
 H(Fragment=6)    0  -11.22187100    2.15552600   -0.84772100 H
 C(Fragment=6)    0  -13.54735200    0.61034600   -0.42531200 H
 O(Fragment=6)    0  -13.80079600    1.38293200   -1.46944900 H
 H(Fragment=6)    0  -14.76178200    1.37130400   -1.62107100 H
 N(Fragment=12)   0   -6.03640200    1.14068300   -5.87010600 H
 H(Fragment=12)   0   -6.28419700    2.06942500   -6.18171600 H
 H(Fragment=12)   0   -6.01670300    0.53673200   -6.69081400 H
 C(Fragment=11)   0   -5.43854600   -3.09134200   -3.69541600 H
 O(Fragment=11)   0   -6.29321300   -3.08629800   -4.69800800 H
 H(Fragment=11)   0   -6.16204800   -3.89459600   -5.22399200 H
 N(Fragment=11)   0   -7.84249300   -0.08033300   -0.57359200 H
 H(Fragment=11)   0   -7.82711300    0.64762900    0.13349000 H
 H(Fragment=11)   0   -8.68934300   -0.15312100   -1.12928500 H
 N(Fragment=10)   0   -2.02130700   -3.80900500   -5.00454600 H
 H(Fragment=10)   0   -1.89178700   -2.79687200   -4.89826700 H
 H(Fragment=10)   0   -3.00386300   -3.95445600   -4.75579800 H
 C(Fragment=10)   0   -1.52860100   -5.96235100   -3.93624900 H
 O(Fragment=10)   0   -2.80509900   -6.29027700   -3.79929600 H
 H(Fragment=10)   0   -2.86315700   -7.26071600   -3.77522100 H
 C(Fragment=1)    0    0.05799000   -0.37682100    0.92203100 H
 H(Fragment=1)    0    1.13001300   -0.46721600    1.12227300 H
 O(Fragment=1)    0   -2.44781700    2.02513000    0.11910300 H
 O(Fragment=1)    0   -2.67629100   -0.17362100    0.32880500 H
 C(Fragment=1)    0   -1.15609300   -3.95416000    1.10252400 H
 H(Fragment=1)    0   -0.77807100   -4.96492800    1.27661400 H
 C(Fragment=1)    0   -3.03563700   -2.48694400    0.57361700 H
 H(Fragment=1)    0   -4.08869700   -2.28323200    0.35188900 H
 C(Fragment=1)    0   -2.52812400   -3.76241700    0.83045100 H
 H(Fragment=1)    0   -3.20121600   -4.62423700    0.81018200 H
 C(Fragment=1)    0   -0.29107700   -2.86374500    1.13446000 H
 H(Fragment=1)    0    0.77779800   -2.99931800    1.32820600 H
 N(Fragment=11)   0   -5.57793590   -0.60706278   -3.51722686 H
 H(Fragment=11)   0   -4.77393897   -0.05676010   -3.29193617 H
 H(Fragment=11)   0   -5.58294275   -0.80411387   -4.49760730 H
 C(Fragment=12)   0   -4.59442100   -0.25352600   -4.34065300 H
 O(Fragment=12)   0   -5.42255605   -0.98176533   -3.43029054 H
 H(Fragment=12)   0   -5.67401811   -1.81955720   -3.82585548 H
 N(Fragment=14)   0    0.79871247   -4.58712442    4.10702387 H
 H(Fragment=14)   0   -0.04692603   -4.83549792    4.57947083 H
 H(Fragment=14)   0    0.64066691   -4.58521215    3.11959390 H
 C(Fragment=13)   0    1.57938700   -5.36549400    3.37990300 H
 O(Fragment=13)   0    1.11134964   -4.26120799    4.15861568 H
 H(Fragment=13)   0    1.49323800   -4.30471470    5.03831361 H
 N(Fragment=13)   0    1.17637728   -7.11493411    1.60469861 H
 H(Fragment=13)   0    0.46906746   -7.77098868    1.34143977 H
 H(Fragment=13)   0    1.12039351   -6.30964283    1.01446835 H
 C(Fragment=16)   0    0.14200000   -7.45774900    0.88141600 H
 O(Fragment=16)   0    0.99986781   -7.06253395    1.95508629 H
 H(Fragment=16)   0    0.70022273   -7.46970478    2.77118968 H
 C(Fragment=17)   0    2.01738100   -6.27939100   -1.44846500 H
 O(Fragment=17)   0    1.29853370   -7.40691537   -0.94166389 H
 H(Fragment=17)   0    1.07116007   -7.25476711   -0.02147253 H
 N(Fragment=16)   0    1.71782746   -7.49951555   -1.08477120 H
 H(Fragment=16)   0    2.16740447   -8.32943132   -1.41510486 H
 H(Fragment=16)   0    1.63334021   -6.84469448   -1.83581798 H
