import FWCore.ParameterSet.Config as cms

pileupWeightMap = {
#from SimGeneral/MixingModule/python/mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi.py
"2016_25ns_SpringMC":cms.vdouble(
0.000829312873542,0.00124276120498 ,0.00339329181587 ,0.00408224735376,0.00383036590008,
0.00659159288946 ,0.00816022734493 ,0.00943640833116 ,0.0137777376066 ,0.017059392038  ,
0.0213193035468  ,0.0247343174676  ,0.0280848773878  ,0.0323308476564 ,0.0370394341409 ,
0.0456917721191  ,0.0558762890594  ,0.0576956187107  ,0.0625325287017 ,0.0591603758776 ,
0.0656650815128  ,0.0678329011676  ,0.0625142146389  ,0.0548068448797 ,0.0503893295063 ,
0.040209818868   ,0.0374446988111  ,0.0299661572042  ,0.0272024759921 ,0.0219328403791 ,
0.0179586571619  ,0.0142926728247  ,0.00839941654725 ,0.00522366397213,0.00224457976761,
0.000779274977993,0.000197066585944,7.16031761328e-05,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 71300 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON":cms.vdouble(
1.782745e+03,2.690151e+04,1.782663e+05,4.714121e+05,7.607781e+05,
1.024960e+06,1.477429e+06,7.351446e+06,2.295777e+07,3.753777e+07,
6.011602e+07,9.317925e+07,1.406152e+08,2.089582e+08,2.876763e+08,
3.531492e+08,3.932633e+08,4.086864e+08,3.995285e+08,3.689304e+08,
3.231239e+08,2.686611e+08,2.116473e+08,1.570575e+08,1.087794e+08,
6.962796e+07,4.086064e+07,2.188573e+07,1.069935e+07,4.796977e+06,
1.991051e+06,7.759526e+05,2.898794e+05,1.074600e+05,4.219007e+04,
1.950952e+04,1.162912e+04,8.731487e+03,7.497940e+03,6.849602e+03,
6.443459e+03,6.164290e+03,5.962505e+03,5.806678e+03,5.667294e+03,
5.528681e+03,5.378081e+03,5.206208e+03,5.008454e+03,4.783922e+03,
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 74865 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Up":cms.vdouble(
1.107849e+03,2.261339e+04,1.527120e+05,3.756942e+05,6.859520e+05,
9.168775e+05,1.129660e+06,3.687673e+06,1.557209e+07,2.930107e+07,
4.505088e+07,7.028203e+07,1.047705e+08,1.548708e+08,2.221351e+08,
2.924343e+08,3.466806e+08,3.786899e+08,3.894950e+08,3.791143e+08,
3.505225e+08,3.089284e+08,2.597274e+08,2.079864e+08,1.578937e+08,
1.127605e+08,7.510117e+07,4.630099e+07,2.629516e+07,1.373814e+07,
6.620171e+06,2.961507e+06,1.242537e+06,4.960967e+05,1.926378e+05,
7.554768e+04,3.205173e+04,1.621956e+04,1.040205e+04,8.119239e+03,
7.082606e+03,6.511396e+03,6.143724e+03,5.886598e+03,5.698458e+03,
5.553034e+03,5.425446e+03,5.300648e+03,5.168296e+03,5.019533e+03,
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 67735 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Dn":cms.vdouble(
2.620963e+03,3.378270e+04,2.115512e+05,5.769433e+05,8.612473e+05,
1.133396e+06,2.486344e+06,1.374395e+07,3.093915e+07,4.990281e+07,
8.123655e+07,1.259242e+08,1.931671e+08,2.791304e+08,3.575930e+08,
4.080549e+08,4.294270e+08,4.221082e+08,3.893581e+08,3.386685e+08,
2.780744e+08,2.149965e+08,1.553911e+08,1.038413e+08,6.344461e+07,
3.514593e+07,1.758808e+07,7.967131e+06,3.292463e+06,1.258110e+06,
4.534820e+05,1.591855e+05,5.779299e+04,2.422217e+04,1.322781e+04,
9.459536e+03,7.967598e+03,7.225058e+03,6.774019e+03,6.469837e+03,
6.252807e+03,6.084769e+03,5.931423e+03,5.775533e+03,5.601990e+03,
5.401304e+03,5.169621e+03,4.907362e+03,4.617921e+03,4.306564e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 71300 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T":cms.vdouble(
1.811381e+03,6.485605e+04,3.417245e+05,6.874719e+05,1.082006e+06,
1.523413e+06,2.138897e+06,8.857555e+06,3.003975e+07,6.281511e+07,
1.140486e+08,1.677066e+08,2.217580e+08,2.923082e+08,3.771719e+08,
4.576940e+08,5.164267e+08,5.435015e+08,5.394139e+08,5.110522e+08,
4.631278e+08,3.999488e+08,3.272788e+08,2.513622e+08,1.795783e+08,
1.191379e+08,7.378382e+07,4.295570e+07,2.366711e+07,1.243875e+07,
6.293865e+06,3.089516e+06,1.476147e+06,6.858958e+05,3.094330e+05,
1.360321e+05,5.939191e+04,2.707284e+04,1.407670e+04,9.048308e+03,
7.126813e+03,6.361481e+03,6.015268e+03,5.819755e+03,5.670293e+03,
5.529317e+03,5.378206e+03,5.206230e+03,5.008458e+03,4.783923e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 74865 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T_Up":cms.vdouble(
1.133932e+03,4.934046e+04,3.012609e+05,5.652183e+05,9.740640e+05,
1.338666e+06,1.711585e+06,4.610255e+06,1.912919e+07,4.363280e+07,
8.250602e+07,1.324371e+08,1.795169e+08,2.328994e+08,3.025979e+08,
3.805292e+08,4.501609e+08,4.984780e+08,5.187115e+08,5.125787e+08,
4.859050e+08,4.424071e+08,3.856057e+08,3.202340e+08,2.513639e+08,
1.849316e+08,1.271613e+08,8.201375e+07,4.991480e+07,2.883355e+07,
1.590832e+07,8.448003e+06,4.351374e+06,2.184805e+06,1.070474e+06,
5.110310e+05,2.375402e+05,1.081302e+05,4.924224e+04,2.358105e+04,
1.286644e+04,8.540255e+03,6.809974e+03,6.091136e+03,5.757096e+03,
5.568717e+03,5.429356e+03,5.301556e+03,5.168493e+03,5.019572e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 67735 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T_Dn":cms.vdouble(
2.653297e+03,8.448778e+04,3.886269e+05,8.288347e+05,1.230064e+06,
1.713876e+06,3.300952e+06,1.666090e+07,4.500962e+07,9.132205e+07,
1.519768e+08,2.097347e+08,2.800227e+08,3.706619e+08,4.631331e+08,
5.343865e+08,5.702064e+08,5.690479e+08,5.389221e+08,4.858616e+08,
4.151975e+08,3.340203e+08,2.501234e+08,1.727172e+08,1.099819e+08,
6.503945e+07,3.600609e+07,1.881295e+07,9.370906e+06,4.496100e+06,
2.091381e+06,9.439111e+05,4.124838e+05,1.747790e+05,7.297079e+04,
3.152934e+04,1.553047e+04,9.622158e+03,7.475129e+03,6.658714e+03,
6.299603e+03,6.095419e+03,5.933647e+03,5.775958e+03,5.602064e+03,
5.401316e+03,5.169623e+03,4.907363e+03,4.617921e+03,4.306564e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON":cms.vdouble(
1.827642e+03,6.059128e+04,3.396887e+05,6.519469e+05,1.074047e+06,
1.501117e+06,1.982683e+06,6.470305e+06,2.366553e+07,4.922270e+07,
9.055294e+07,1.422713e+08,1.906575e+08,2.448287e+08,3.150670e+08,
3.938074e+08,4.633652e+08,5.107552e+08,5.316173e+08,5.285932e+08,
5.070718e+08,4.702726e+08,4.207972e+08,3.626679e+08,3.000539e+08,
2.368030e+08,1.772530e+08,1.256785e+08,8.467061e+07,5.445397e+07,
3.358021e+07,1.994934e+07,1.148344e+07,6.446069e+06,3.547477e+06,
1.919327e+06,1.020838e+06,5.328258e+05,2.725589e+05,1.369243e+05,
6.823034e+04,3.457581e+04,1.867349e+04,1.143212e+04,8.249688e+03,
6.895534e+03,6.335506e+03,6.108908e+03,6.015830e+03,5.969526e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 72383 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_Up":cms.vdouble(
1.201548e+03,4.676716e+04,3.008725e+05,5.420738e+05,9.804709e+05,
1.318758e+06,1.700310e+06,3.673068e+06,1.513481e+07,3.574484e+07,
6.596769e+07,1.110088e+08,1.571718e+08,2.017265e+08,2.565703e+08,
3.250449e+08,3.963534e+08,4.556627e+08,4.940383e+08,5.091794e+08,
5.040965e+08,4.832648e+08,4.491942e+08,4.040599e+08,3.512362e+08,
2.942352e+08,2.362509e+08,1.808398e+08,1.317071e+08,9.145469e+07,
6.078689e+07,3.882864e+07,2.392876e+07,1.429309e+07,8.320747e+06,
4.746313e+06,2.662791e+06,1.471227e+06,7.999008e+05,4.272497e+05,
2.240457e+05,1.156925e+05,5.946075e+04,3.116776e+04,1.739840e+04,
1.092001e+04,7.969211e+03,6.664344e+03,6.102269e+03,5.865247e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 66016 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_Dn":cms.vdouble(
2.621526e+03,7.787448e+04,3.814820e+05,7.840881e+05,1.194340e+06,
1.689306e+06,2.643789e+06,1.180856e+07,3.476272e+07,6.900734e+07,
1.223743e+08,1.775351e+08,2.323706e+08,3.028372e+08,3.881155e+08,
4.690477e+08,5.273554e+08,5.555278e+08,5.553688e+08,5.332745e+08,
4.934138e+08,4.389367e+08,3.746769e+08,3.056256e+08,2.364744e+08,
1.725352e+08,1.186676e+08,7.726892e+07,4.788712e+07,2.839110e+07,
1.619692e+07,8.954894e+06,4.831820e+06,2.556327e+06,1.327713e+06,
6.759631e+05,3.366890e+05,1.642298e+05,7.915958e+04,3.866586e+04,
2.013510e+04,1.199229e+04,8.551242e+03,7.147703e+03,6.592690e+03,
6.377959e+03,6.291914e+03,6.245973e+03,6.199073e+03,6.128442e+03,
),
}

pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON"]
pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON_Up"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Up"]
pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON_Dn"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Dn"]