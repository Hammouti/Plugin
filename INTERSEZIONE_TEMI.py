import tempfile
from qgis.core import QgsApplication
from processing.core.Processing import Processing


def converter(alg_name, *args):
    params_dict = {}
    # get parameters list from alg_name
    # build params_dict by interleaving args and parameters
    alg = [a for a in QgsApplication.processingRegistry().algorithms() if alg_name[5:] in a.name()][0]
    for param in alg.parameterDefinitions():
        print(param.name())
    return {'OUTPUT': 'foo'}
    #return Processing.runAlgorithm(alg_name, params_dict, None)


##INTERSEZIONE_TEMI=name
##Vettore_intersezione_Censuarie_Hazard_OMI=vector
##Tabella_costi_ricostruzione=table
##Tabella_percentuale_danno=table
##Piani_tot=output vector
##A44=output vector
##Area_primo_piano_minore_15=output vector
##E1=output vector
##Output_Danno_TOT=output vector
##Area_minore_1000=output vector
##Industriale=output vector
outputs_QGISMULTIPARTTOSINGLEPARTS_1=converter('qgis:multiparttosingleparts', 'Vettore_intersezione_Censuarie_Hazard_OMI',None)
outputs_QGISFIELDCALCULATOR_17=converter('qgis:fieldcalculator', outputs_QGISMULTIPARTTOSINGLEPARTS_1['OUTPUT'],'F_AREA',0,10.0,11.0,True,'$area',None)
outputs_QGISFIELDCALCULATOR_18=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_17['OUTPUT_LAYER'],'AREA_PERC',0,10.0,6.0,False,'round(("F_AREA" / "AREA_OLD"),6)',None)
outputs_QGISFIELDCALCULATOR_19=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_18['OUTPUT_LAYER'],'P1',0,10.0,2.0,False,'round(("P1" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_20=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_19['OUTPUT_LAYER'],'A2',0,10.0,2.0,False,'round(("A2" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_21=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_20['OUTPUT_LAYER'],'A3',0,10.0,2.0,False,'round(("A3" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_22=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_21['OUTPUT_LAYER'],'A5',0,10.0,2.0,False,'round(("A5" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_23=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_22['OUTPUT_LAYER'],'A44',0,10.0,2.0,False,'round(("A44" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_24=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_23['OUTPUT_LAYER'],'E1',0,10.0,2.0,False,'round(("E1" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_25=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_24['OUTPUT_LAYER'],'E2',0,10.0,2.0,False,'round(("E2" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_26=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_25['OUTPUT_LAYER'],'E3',0,10.0,2.0,False,'round(("E3" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_27=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_26['OUTPUT_LAYER'],'E4',0,10.0,2.0,False,'round(("E4" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_28=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_27['OUTPUT_LAYER'],'E5',0,10.0,2.0,False,'round(("E5" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_29=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_28['OUTPUT_LAYER'],'E6',0,10.0,2.0,False,'round(("E6" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_30=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_29['OUTPUT_LAYER'],'E7',0,10.0,2.0,False,'round(("E7" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_31=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_30['OUTPUT_LAYER'],'E17',0,10.0,2.0,False,'round(("E17" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_32=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_31['OUTPUT_LAYER'],'E18',0,10.0,2.0,False,'round(("E18" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_33=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_32['OUTPUT_LAYER'],'E19',0,10.0,2.0,False,'round(("E19" * "AREA_PERC"),0)',None)
outputs_QGISFIELDCALCULATOR_34=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_33['OUTPUT_LAYER'],'E20',0,10.0,2.0,False,'round(("E20" * "AREA_PERC"),0)',None)
outputs_QGISEXTRACTBYATTRIBUTE_2=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_34['OUTPUT_LAYER'],'E1',1,'0',None)
outputs_QGISEXTRACTBYATTRIBUTE_8=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_34['OUTPUT_LAYER'],'E1',0,'0',E1)
outputs_QGISEXTRACTBYATTRIBUTE_9=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_2['OUTPUT'],'F_AREA',4,'1000',Area_minore_1000)
outputs_QGISEXTRACTBYATTRIBUTE_3=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_2['OUTPUT'],'F_AREA',2,'1000',None)
outputs_QGISFIELDCALCULATOR_1=converter('qgis:fieldcalculator', outputs_QGISEXTRACTBYATTRIBUTE_3['OUTPUT'],'PIANI_TOT',1,10.0,3.0,True,'"E17" + "E18" * 2 + "E19" *3 + "E20" * 4',None)
outputs_QGISEXTRACTBYATTRIBUTE_1=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_1['OUTPUT_LAYER'],'A44',1,'0',None)
outputs_QGISEXTRACTBYATTRIBUTE_4=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_1['OUTPUT'],'PIANI_TOT',1,'0',None)
outputs_QGISEXTRACTBYATTRIBUTE_11=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_1['OUTPUT'],'PIANI_TOT',0,'0',Piani_tot)
outputs_QGISEXTRACTBYATTRIBUTE_10=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_1['OUTPUT_LAYER'],'A44',0,'0',A44)
outputs_QGISFIELDCALCULATOR_2=converter('qgis:fieldcalculator', outputs_QGISEXTRACTBYATTRIBUTE_4['OUTPUT'],'AREA_1P',0,10.0,0.0,True,'"A44" / "PIANI_TOT"',None)
outputs_QGISEXTRACTBYATTRIBUTE_5=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_2['OUTPUT_LAYER'],'AREA_1P',2,'15',None)
outputs_QGISEXTRACTBYATTRIBUTE_7=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_5['OUTPUT'],'Cod_tip_pr',0,'20 OR "Cod_tip_pr" =  21',None)
outputs_QGISEXTRACTBYATTRIBUTE_6=converter('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_5['OUTPUT'],'Cod_tip_pr',0,'7 OR "Cod_tip_pr" = 8 OR "Cod_tip_pr" =9',Industriale)
outputs_QGISEXTRACTBYATTRIBUTE_12=converter('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_2['OUTPUT_LAYER'],'AREA_1P',4,'15',Area_primo_piano_minore_15)
outputs_QGISFIELDCALCULATOR_3=converter('qgis:fieldcalculator', outputs_QGISEXTRACTBYATTRIBUTE_7['OUTPUT'],'ESPO_MIN',0,10.0,0.0,True,'"COMPR_MIN" * "A44"',None)
outputs_QGISFIELDCALCULATOR_4=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_3['OUTPUT_LAYER'],'ESPO_MAX',0,10.0,0.0,True,'"COMPR_MAX" * "A44"',None)
outputs_QGISFIELDCALCULATOR_5=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_4['OUTPUT_LAYER'],'E1_OMI_MIN',0,10.0,0.0,True,'"COMPR_MIN" * "AREA_1P" * "E3"',None)
outputs_QGISFIELDCALCULATOR_6=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_5['OUTPUT_LAYER'],'E1_OMI_MAX',0,10.0,0.0,True,'"COMPR_MAX" * "AREA_1P" * "E3"',None)
outputs_QGISJOINATTRIBUTESTABLE_1=converter('qgis:joinattributestable', outputs_QGISFIELDCALCULATOR_6['OUTPUT_LAYER'],Tabella_costi_ricostruzione,'COD_TIP_PR','cod_tip_pr',None)
outputs_QGISJOINATTRIBUTESTABLE_2=converter('qgis:joinattributestable', outputs_QGISJOINATTRIBUTESTABLE_1['OUTPUT_LAYER'],Tabella_percentuale_danno,'COD_TIP_PR','cod_tip_pr',None)
outputs_QGISFIELDCALCULATOR_7=converter('qgis:fieldcalculator', outputs_QGISJOINATTRIBUTESTABLE_2['OUTPUT_LAYER'],'RIC_MIN_05',0,10.0,0.0,True,'("PERC_05" * "COSTO_MIN" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_8=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_7['OUTPUT_LAYER'],'RIC_MAX_05',0,10.0,0.0,True,'("PERC_05" * "COSTO_MAX" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_9=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_8['OUTPUT_LAYER'],'RICMIN05_1',0,10.0,0.0,True,'("PERC_05_1" * "COSTO_MIN" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_10=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_9['OUTPUT_LAYER'],'RICMAX05_1',0,10.0,0.0,True,'("PERC_05" * "COSTO_MAX" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_11=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_10['OUTPUT_LAYER'],'RICMIN_1',0,10.0,0.0,True,'("PERC_1" * "COSTO_MIN" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_12=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_11['OUTPUT_LAYER'],'RICMAX_1',0,10.0,0.0,True,'("PERC_1" * "COSTO_MAX" * "AREA_1P" * "E3")/100',None)
outputs_QGISFIELDCALCULATOR_13=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_12['OUTPUT_LAYER'],'E1_RIC_MIN',0,10.0,0.0,True,'"AREA_1P" * "COSTO_MIN" * "E3"',None)
outputs_QGISFIELDCALCULATOR_14=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_13['OUTPUT_LAYER'],'E1_RIC_MAX',0,10.0,0.0,True,'"AREA_1P" * "COSTO_MAX" * "E3"',None)
outputs_QGISFIELDCALCULATOR_15=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_14['OUTPUT_LAYER'],'ET_RIC_MIN',0,10.0,0.0,True,'"A44" * "COSTO_MIN"',None)
outputs_QGISFIELDCALCULATOR_16=converter('qgis:fieldcalculator', outputs_QGISFIELDCALCULATOR_15['OUTPUT_LAYER'],'ET_RIC_MAX',0,10.0,0.0,True,'"A44" * "COSTO_MAX"',Output_Danno_TOT)
