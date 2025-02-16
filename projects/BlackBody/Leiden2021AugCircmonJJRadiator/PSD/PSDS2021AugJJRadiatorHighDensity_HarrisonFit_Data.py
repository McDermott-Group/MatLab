import matplotlib.pyplot as plt

Q1_J2Bias=[35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000, 39500, 40000, 40500, 41000, 41500, 42000, 42500, 43000, 43500, 44000, 44500, 45000, 45500, 46000, 46500, 47000, 47500, 48000, 48500, 49000, 49500, 50000, 50500, 51000, 51500, 52000, 52500, 53000, 53500, 54000, 54500, 55000, 55500, 56000, 56500, 57000, 57500, 58000, 58500, 59000, 59500, 60000, 60500, 61000, 61500, 62000, 62500, 63000, 63500, 64000, 64500, 65000, 65500, 66000, 66500, 67000, 67500, 68000, 68500, 69000, 69500, 70000, 70500, 71000, 71500, 72000, 72500, 73000, 73500, 74000, 74500, 75000, 75500, 76000, 76500, 77000, 77500, 78000, 78500, 79000, 79500, 80000]
Q1_J2ParityRate= [2760.6635121375671, 3701.8622172085475, 2738.6350700079765, 2372.4826089705703, 3269.8922395904624, 3236.0203076327261, 3312.1113815953081, 2835.0268209310743, 2912.0324026305125, 2429.5616420308525, 2307.9190206840108, 2521.9672568421688, 2611.0143012110552, 2669.515262931538, 3168.2292546969506, 5352.3895530237214, 6488.5178847044881, 4718.618770125875, 5926.6922400464073, 5216.1283110007216, 4404.3698103005363, 4692.1162749821906, 14636.584860212377, 18682.722949174993, 22073.854836183378, 19502.697647277706, 16644.615399358288, 5516.3478120305517, 6337.4284525175935, 8681.0181924909793, 10040.030449385056, 10088.432604551133, 9413.1651951158856, 9403.8771676903143, 5657.6179410466211, 5735.2708039813388, 4887.9784299145567, 5054.0227154840113, 6069.7172779885786, 7106.116365562717, 9344.3390826949253, 7720.5350571968547, 7108.3990007015773, 7093.1809508330889, 7723.3052706025783, 6943.4449357855019, 6371.9411591167191, 7184.0245672411102, 7077.6224757917171, 9265.642606931222, 8826.1274696882829, 5739.1251669686326, 8177.4702431960568, 7382.0072574856204, 7676.4621814757147, 7701.9537982648171, 7599.0611470613194, 9007.1186044936112, 8769.2648655361154, 8572.6425599833929, 10397.629269841142, 9726.4618659984371, 9831.4769779262224, 8292.9349820438074, 7766.1984864285923, 6527.6867994714275, 7142.145239333342, 5925.8832172397597, 6488.4341333962393, 6355.6039950003369, 7624.4668036117837, 12826.241613925133, 6865.6437332952746, 10147.197724779568, 9316.3477932472251, 8102.12135837398, 10580.082782608957, 7621.4870007366289, 6311.9923480501056, 7174.4889675755167, 7098.1980569381722, 8067.2119257964032, 8623.9917474584836, 8214.8930159220999, 6635.5075228616388, 6210.2699992780235, 6290.202167104916, 6861.7523180182025, 7176.3822193275, 7207.057673774927, 6654.2340281080978]
Q1_J2ParityUncertainty=[115.96547301798412, 947.67108600056417, 81.879827594083991, 41.671501827354753, 112.60032658872964, 96.177045644932122, 103.26882379921415, 22.788213447671691, 110.51454394337249, 119.60403632152548, 48.683887304566817, 79.492650731693345, 96.528587726186416, 97.053090467536919, 117.31275629028254, 539.77230151705396, 403.27546947991198, 108.0586968617306, 412.62473213705533, 477.74585326624685, 241.46187258808445, 405.82017459031027, 988.12064768131529, 631.33024924760355, 1831.5866492535422, 3408.8312281953968, 1417.6631218366163, 301.57131211681707, 561.90449018530489, 586.82376867845085, 1277.4941808187482, 1929.3652026194316, 910.06546127117053, 506.30651524321007, 204.32112069052499, 127.07482650450062, 88.405278379951895, 227.27497664923106, 1349.3160358981595, 350.56521271196181, 288.20605230476201, 267.3317136159809, 102.62072796011957, 164.07253310349259, 1291.4558853815854, 171.3892109123102, 370.81079893155891, 247.11305232841841, 399.08461396789602, 1005.0230118660439, 450.99252198628926, 324.57957144804459, 1274.5810679435681, 262.77175605761545, 272.97601402753389, 182.67647733924576, 216.99797088836718, 798.56692417243437, 116.54514716409055, 326.84227549121721, 1115.8514587800396, 1223.74777750313, 1549.1574206743999, 281.40899247505325, 1681.5006184339861, 251.28743484019739, 738.78225166270465, 163.35694060649152, 506.87269707652058, 509.7254390254547, 337.83940770601873, 3360.3707014066663, 355.55367288134778, 1132.4291362423994, 731.54750479042411, 174.78066027931084, 1707.3103202840709, 368.71818406839907, 258.56586130699674, 272.31692543715337, 66.913567648073425, 223.21539862371077, 1071.7960422049157, 587.31763734506831, 185.81656861091335, 98.658673073349831, 176.87594157915098, 136.08498499209549, 132.82092585955135, 77.285673611660357, 122.43219351867774]
Q1_J2Fidelity= [0.52914285714285714, 0.53828571428171434, 0.52000000000000002, 0.43314285714285722, 0.50628571428571434, 0.50171428571428567, 0.5108571428571429, 0.54285714285714293, 0.50628571428571445, 0.43314285714285716, 0.4285714285714286, 0.44228571428571434, 0.45600000000000007, 0.4468571428571429, 0.43314285714285722, 0.44228571428571434, 0.43771428571428578, 0.31428571428571428, 0.3051428571428571, 0.29599999999999999, 0.29142857142857143, 0.30971428571428572, 0.2045714285714286, 0.20000000000000004, 0.22285714285714289, 0.20000000000000004, 0.2045714285714286, 0.20000000000000004, 0.2045714285714286, 0.21828571428571433, 0.23199999999999998, 0.20914285714285716, 0.25485714285714284, 0.27314285714285713, 0.3051428571428571, 0.31428571428571428, 0.31428571428571428, 0.33714285714285713, 0.33714285714285713, 0.33257142857142857, 0.41028571428571431, 0.40114285714285719, 0.4285714285714286, 0.42399999999999999, 0.43314285714285716, 0.41942857142857143, 0.36914285714285716, 0.31885714285714284, 0.31885714285714284, 0.33257142857142857, 0.33714285714285713, 0.35085714285714287, 0.43314285714285716, 0.40571428571428575, 0.41028571428571431, 0.42399999999999999, 0.4285714285714286, 0.4285714285714286, 0.4285714285714286, 0.34171428571428569, 0.32800000000000007, 0.3234285714285714, 0.37371428571428572, 0.34628571428571431, 0.35085714285714287, 0.40571428571428575, 0.35542857142857143, 0.31885714285714284, 0.34171428571428569, 0.34628571428571425, 0.32800000000000007, 0.35085714285714287, 0.37371428571428572, 0.33714285714285713, 0.3234285714285714, 0.31428571428571428, 0.36457142857142855, 0.36914285714285716, 0.34171428571428569, 0.39200000000000002, 0.4285714285714286, 0.41942857142857143, 0.43314285714285722, 0.43771428571428578, 0.44228571428571434, 0.54285714285714293, 0.5337142857142857, 0.50171428571428567, 0.52914285714285714, 0.5337142857142857, 0.53828571428571437]
Q2_J2Bias=[35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000, 39500, 40000, 40500, 41000, 41500, 42000, 42500, 43000, 43500, 44000, 44500, 45000, 45500, 46000, 46500, 47000, 47500, 48000,48500, 49000, 49500, 50000, 50500, 51000, 51500, 52000, 52500, 53000, 53500, 54000, 54500, 55000, 55500, 56000, 56500, 57000, 57500, 58000, 58500, 59000, 59500, 60000, 60500, 61000, 61500, 62000, 62500, 63000, 63500, 64000, 64500, 65000, 65500, 66000, 66500, 67000, 67500, 68000, 68500, 69000, 69500, 70000, 70500, 71000, 71500, 72000, 72500, 73000, 73500, 74000, 74500, 75000,75500, 76000, 76500, 77000, 77500, 78000, 78500, 79000, 79500, 80000]
Q2_J2ParityRate= [55.112562958970003, 50.408723212496952, 53.673000502567078, 2794.3043997000518, 54.170871078345868, 55.06895654219872, 60.543264958215097, 55.943670776984064, 50.438915282328963, 53.220217334086946, 56.259419857155969, 53.849684642098566, 51.546437000958285, 56.563239831571046, 52.664648567820763, 60.475355636450438, 55.949551367326734, 61.755083293195995, 65.570750151230683, 85.709650943500549, 111.43081600356903, 149.11203097965301, 183.73743796010459, 223.08427630666409, 291.97654432600251, 314.81583895956516, 294.92995788872929, 308.2268301394854, 303.70012380369263, 308.21540395321631, 278.9651774130694, 289.23046617397824, 295.35464927442888, 281.37954115210181, 269.95081072912308, 222.89121004859192, 200.17486597848864, 193.88355980910765, 216.1831023097329, 217.59837961955446, 222.77921234335199, 224.05649717238967, 235.20793609480003, 251.65520668627673, 295.70240652479981, 327.74028639670485, 768.64692301243997, 401.30039108822842, 472.24665902518018, 497.1742715232109, 516.50123365899356, 475.33957711926081, 465.14453766780338, 485.36818500997555, 530.70850562255998, 522.87820719427441, 490.26777683892834, 479.39752849431198, 534.23469073570232, 599.37470168412267, 626.72762186452167, 659.73822672695587, 671.37225939247833, 362.11659883866326, 271.04034991506387, 466.06249286503606, 492.7025894487997, 466.78253707223013, 483.66558285069596, 530.31212475587074, 613.20126032782093, 616.71881605262911, 590.52843311928223, 575.81401092210831, 574.95634177035504, 557.43763627435226, 499.98468410517273, 575.21994408879891, 1088.2606560545498, 415.54639415945718, 421.47182548212629, 420.44618125702226, 391.875315361579, 357.34931505162103, 344.62363594000146, 393.97602213871068, 442.69835704888413, 466.68641579999326, 435.7842636679905, 380.84425434064281, 360.59772938615532]
Q2_J2ParityUncertainty= [2.9436878338784216, 2.7450141775109089, 2.5147926228210267, 2689.156768851768, 2.7718310173271954, 2.4880438528970403, 2.9362410102865351, 2.7622966150231196, 3.0562585927394545, 3.1133592236997671, 2.371612766939144, 2.6605038261720821, 2.7039210143271664, 2.4973081428946395, 2.7323202241386588, 2.6205510317232332, 2.4314560933187925, 2.5719571766702827, 3.6015767337711724, 4.5154210212477786, 4.5043232312531449, 4.9923658693430371, 5.186709977562507, 6.3961692907472738, 6.2034445658072848, 8.894790023395327, 13.686285633701646, 10.431091231945478, 7.1055312914442679, 7.1281058899781859, 9.0783906183678713, 4.515122850633051, 6.901225874264945, 7.2032568146849112, 10.847692727008171, 8.0728581821866587, 6.0420006084216675, 6.770091163648094, 6.1438372482037282, 7.0064603950143329, 3.7761497778998421, 2.9902298413031745, 3.3976339288798001, 2.6651128652304488, 4.450492862817339, 4.4747375130564668, 332.33251570731289, 5.1808901927708435, 8.1250630478616852, 6.2450473575671142, 6.5864883800948286, 6.3150039094812209, 5.1457338616312418, 5.9506976502362727, 5.7055901146724972, 7.644311840625182, 7.3689575639406222, 5.1008178044955876, 4.3999045842797901, 5.4717614147807137, 7.8782362537806341, 6.1275821851888015, 7.7782426664086355, 100.60329774169566, 3.3622417990101292, 6.3959901966208879, 4.5517841519093922, 4.8133734135912194, 5.8579752126308557, 9.4818517416158166, 7.9099755740596356, 8.3243571671351457, 6.0463224695282607, 6.6799577738874047, 7.3582584122805379, 6.1972006996083957, 5.3971737776004352, 91.801415499565721, 448.05390335805242, 4.6868137167780928, 6.3864462376050364, 3.6755179222401955, 2.9115127178033915, 4.0526141123879711, 4.4895609914495882, 4.9047938231618815, 3.7293139465325016, 7.2965802099824018, 4.2596603765330432, 2.6557640033314143, 3.0060664659234488]
Q2_J2Fidelity=[0.55713038023114125, 0.58553546989273852, 0.56812697472425067, 0.52060326201118312, 0.52678127760281601, 0.57615156870961359, 0.54822271997427297, 0.55753496445040229, 0.57417784089710577, 0.58791019161756686, 0.60756342786644957, 0.58926732677572058, 0.58815432771899312, 0.59941891522598401, 0.59472686578437406, 0.61335239222066329, 0.55760631535822225, 0.57303337905542495, 0.54854859902314912, 0.58291585038697946, 0.56182161496490368, 0.56791339135593621, 0.53806156657278137, 0.56581952733018459, 0.60222337396089831, 0.55426659386142874, 0.54353291700770223, 0.58821753892715056, 0.57574511258288386, 0.54977880629087739, 0.54142325533360502, 0.56248609639538694, 0.59401519019429416, 0.54719759045252547, 0.55005388188020843, 0.57919625274387521, 0.54395387980203846, 0.5369150863599963, 0.55954831730344157, 0.56185866933542916, 0.57391345565088547, 0.60849928978385481, 0.59941449332387442, 0.58133896446339162, 0.59868200503542301, 0.61330124166972944, 0.54528418890087471, 0.59109702834750977, 0.57259489391499574, 0.57217465485572572, 0.58281554871153896, 0.56967944130235382, 0.59616781924948081, 0.58848050670462559, 0.6121012468306799, 0.59081472400813628, 0.57232347784858195, 0.5685718366072593, 0.60717443739867094, 0.6090739744639756, 0.58346589861604159, 0.58622018614932225, 0.56394175704141913, 0.56841976974748998, 0.62652236688772167, 0.60520582452954874, 0.62210240791157323, 0.60488233461425711, 0.59324822962750545, 0.5727168034867971, 0.60912464348960682, 0.61920435190152001, 0.58273548978906609, 0.58866225819525542, 0.60157574478662434, 0.58777709208162576, 0.5924705523167989, 0.55889075254700604, 0.56827013733947251, 0.6121355247736755, 0.60475172173248704, 0.59644445150531811, 0.61856738946249035, 0.5977719242654187, 0.61551753327433556, 0.6082075661582097, 0.61189840215833247, 0.5811026415458691, 0.6191050025287681, 0.61483116219312395, 0.5964965785375913]
Q4_J2Bias=[35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000, 39500, 40000, 40500, 41000, 41500, 42000, 42500, 43000, 43500,44000, 44500, 45000, 45500, 46000, 46500, 47000, 47500, 48000, 48500, 49000, 49500, 50000, 50500, 51000, 51500, 52000, 52500, 53000, 53500, 54000, 54500, 55000, 55500, 56000, 56500, 57000, 57500, 58000, 58500, 59000, 59500, 60000, 60500, 61000, 61500, 62000, 62500, 63000, 63500, 64000, 64500, 65000, 65500, 66000, 66500, 67000, 67500, 68000, 68500, 69000, 69500, 70000, 70500, 71000, 71500, 72000, 72500, 73000, 73500, 74000, 74500, 75000, 75500, 76000, 76500, 77000, 77500, 78000, 78500, 79000, 79500, 80000]
Q4_J2ParityRate= [630.32220129154553, 625.47907266047946, 866.68764059613591, 612.50124896046918, 631.47634220794214, 608.61331936288252, 608.23379924584299, 602.59257042596289, 618.46970101705313, 635.03798463900932, 633.62094715244882, 637.34420432551497, 637.92674606577884, 618.14066698053966, 613.40837593637298, 624.25794658009272, 642.12279177096707, 655.96822104827118, 770.25142495173088, 867.52974928084063, 1097.1176199928882, 1350.9251375169054, 1473.7844953072677, 1612.5441908415744, 1728.3330468334395, 1732.9970037408521, 1699.8764920490132, 1696.5477876517436, 1632.504397888363, 1684.2100288306665, 3636.0588808461216, 2373.4519332534292, 2798.2298131423618, 2876.9288159884977, 2404.1444455918477, 2119.1149656193011, 2185.0557007074722, 2536.2468582244687, 2869.2204152675749, 3816.9950960559531, 3982.6441359028117, 3617.763624850561, 3258.4826428168262, 2932.8689214210103, 2936.8543688794998, 3148.7861487268942, 4006.0592768071047, 4196.5308582536363, 5849.4470602879937, 5963.6233165946496, 6868.4572509064828, 6752.8927011814485, 6802.2220377181229, 6269.8002795781031, 7445.1787949752479, 8288.8036629397775, 7566.3488356732551, 7851.6898133124041, 8459.30304017446, 7948.5720336429686, 7943.932405000548, 8161.6516386740586, 7983.0607977738182, 8675.2613776182716, 8184.1630062987169, 7991.1522614393771, 8090.1439618677878, 8733.7760825543992, 7434.9778512118428, 7494.5081315119241, 8010.2273505539815, 8481.8144077991201, 8153.908758876647, 8399.7727598743804, 8978.7323712951929, 9270.4609830143254, 8841.105569697449, 8769.2648655361154, 8590.674024635875, 9187.9986666428595, 8892.8929702001187, 8568.0750159195504, 9272.062153573781, 8469.503983937866, 8409.9737036377865, 7773.4330277658646, 7861.8907570758101, 7256.3143871543916, 7554.0384118120037, 7009.7403276282266, 6407.587345424723]
Q4_J2ParityUncertainty= [15.646185371918325, 12.658356741603583, 258.52617810055824, 11.871249258759793, 8.475164655030202, 8.1115155706153335, 6.1265615747495046, 8.6166483120317956, 12.76804839769019, 9.3312069979947143, 10.18002168012571, 10.082543621632338, 14.160700163454221, 8.6842678555261728, 8.3775821083878892, 9.6258991088534724, 11.740995890946403, 17.540485728438327, 12.883261253075963, 14.155514569209421, 16.221828257586139, 34.576854984721059, 24.524071532118771, 30.441097264261863, 54.515036499482939, 32.106809174582402, 15.777099671429552, 24.290554203686696, 21.796561315055236, 19.394910720129428, 1447.1076667484228, 24.98415546112702, 48.376892803579793, 45.099508072869497, 46.977791735324807, 26.570711721787653, 29.000937248450352, 48.366504417357021, 36.149589953947704, 150.04320815806528, 51.449001892649555, 65.464637148069031, 62.033815184907333, 60.585094154047169, 67.406850542929575, 119.72755031611278, 158.90891882305215, 55.035375212773424, 92.711673837454683, 0.0, 138.78202613113282, 118.39040768801981, 115.05479533999446, 133.5446616078996, 132.98910063710187, 167.48112778806637, 161.16071482508298, 147.75027011567107, 144.36322002545026, 341.32871271983981, 205.73398151379635, 172.16017757774458, 177.52762914653326, 201.3070749011458, 209.83139130241329, 181.07557904239511, 361.14459177142624, 813.12291851453961, 109.1208062468226, 119.06056060016063, 237.75879609170681, 186.26535404784454, 271.63051173746709, 152.20851969988519, 242.16494339924242, 313.63395004193325, 134.36434247028043, 116.54514716409055, 155.37321604601064, 161.28198083777582, 241.30276940226059, 231.53476101599901, 281.67290180419252, 160.57261016929817, 167.80595493909041, 206.16990622103305, 165.13274789783, 181.70054417666759, 127.12189222586309, 119.62553894011975, 118.39040768801981]
Q4_J2Fidelity=[0.6225187528999141, 0.64953924188737955, 0.65566867928972028, 0.68454582980975143, 0.68538762450655089, 0.6860869548066133, 0.67863305315260714, 0.67080535936156149, 0.67872556450036658, 0.68641792356321163, 0.66799163437683606, 0.67083391633667322, 0.65046580715982916, 0.66395698116706925, 0.64343120727636494, 0.65525925273213514, 0.64737013568797241, 0.63322632258283063, 0.63191426858562472, 0.65214329628745571, 0.63868085145611564, 0.63331131241993843, 0.63731555896508252, 0.6111902189722912, 0.64678324777514751, 0.6598618643805374, 0.64618239578401071, 0.6622160138764448, 0.66082324364823508, 0.65342934493457261, 0.64831754609909309, 0.63438215357255923, 0.67233367706201719, 0.65105506666934632, 0.65301936451334197, 0.6278304558543697, 0.65396449408283575, 0.62551900540878835, 0.6574771035652559, 0.61545565463873209, 0.63428571428571434, 0.64800000000000013, 0.63428571428571434, 0.64800000000000013, 0.62971428571428578, 0.59314285714285719, 0.58400000000000007, 0.6388571428571429, 0.59771428571428575, 0.65257142857142869, 0.59771428571428575, 0.58857142857142863, 0.62057142857142866, 0.50171428571428567, 0.46514285714285719, 0.52000000000000002, 0.41942857142857148, 0.41485714285714287, 0.41485714285714287, 0.41485714285714287, 0.46971428571428575, 0.48800000000000004, 0.43314285714285716, 0.41028571428571431, 0.41942857142857143, 0.46971428571428575, 0.45600000000000002, 0.41485714285714287, 0.43314285714285722, 0.40571428571428575, 0.38742857142857146, 0.39657142857142857, 0.31428571428571428, 0.30514285714285716, 0.30057142857142854, 0.3051428571428571, 0.30971428571428572, 0.30971428571428572, 0.30971428571428572, 0.31428571428571428, 0.29142857142857143, 0.30057142857142854, 0.40571428571428575, 0.40571428571428569, 0.48800000000000004, 0.49714285714285716, 0.51542857142857157, 0.46057142857142858, 0.52000000000000002, 0.50628571428571434, 0.54285714285714282]


### J2 Bias offset
J2_Offset = 19.2
Q1_J2Bias[:] = [bias/1000.-J2_Offset for bias in Q1_J2Bias]
Q2_J2Bias[:] = [bias/1000.-J2_Offset for bias in Q2_J2Bias]
Q4_J2Bias[:] = [bias/1000.-J2_Offset for bias in Q4_J2Bias]

plt.errorbar(Q1_J2Bias, Q1_J2ParityRate,yerr=Q1_J2ParityUncertainty, label='Q1', ecolor='k', capthick=2,color='r')
plt.errorbar(Q2_J2Bias, Q2_J2ParityRate,yerr=Q2_J2ParityUncertainty, label='Q2', ecolor='k', capthick=2,color='g')
plt.errorbar(Q4_J2Bias, Q4_J2ParityRate,yerr=Q4_J2ParityUncertainty, label='Q4', ecolor='k', capthick=2,color='b')
plt.xlabel('J2 Bias (mDAC)')
plt.ylabel('QPT (Hz)')
plt.yscale('log')
plt.grid()
plt.legend()
plt.draw()
plt.show()