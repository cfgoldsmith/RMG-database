# This file contains a dictionary of kinetics families.  The families
# set to `True` are recommended by RMG and turned on by default by setting
# kineticsFamilies = 'default' in the RMG input file. Families set to `False` 
# are not turned on by default because the family is severely lacking in data.
# These families should only be turned on with caution.

recommendedFamilies = {
'Surface_Adsorption_Single': False, #True
'Surface_Adsorption_Double': False,
'Surface_Adsorption_vdW': False, # vdW bond doesn't exist yet
'Surface_Adsorption_Dissociative': False, #True
'Surface_Adsorption_Bidentate': False, #True
'Surface_Recombination': False, #DEPRICATED. USE SURFACE_DISSOCIATION INSTEAD!
'Surface_Bidentate_Dissociation': False,
'Surface_Dissociation': False, #True
'Surface_Abstraction': False, #True
'1+2_Cycloaddition':True,
'1,2-Birad_to_alkene':True,
'1,2_Insertion_CO':True,
'1,2_Insertion_carbene':True,
'1,2_shiftS':True,
'1,3_Insertion_CO2':True,
'1,3_Insertion_ROR':True,
'1,3_Insertion_RSR':True,
'1,4_Cyclic_birad_scission':True,
'1,4_Linear_birad_scission':True,
'2+2_cycloaddition_CCO':True,
'2+2_cycloaddition_CO':True,
'2+2_cycloaddition_Cd':True,
'Birad_recombination':True,
'Cyclic_Ether_Formation':True,
'Diels_alder_addition':True,
'Disproportionation':True,
'HO2_Elimination_from_PeroxyRadical':True,
'H_Abstraction':True,
'H_shift_cyclopentadiene':True,
'Intra_Diels_alder':True,
'Intra_Disproportionation':True,
'Intra_RH_Add_Endocyclic':True,
'Intra_RH_Add_Exocyclic':True,
'Intra_R_Add_Endocyclic':True,
'Intra_R_Add_ExoTetCyclic':True,
'Intra_R_Add_Exocyclic':True,
'Korcek_step1':True,
'Korcek_step2':True,
'Oa_R_Recombination':True,
'R_Addition_COm':True,
'R_Addition_CSm':True,
'R_Addition_MultipleBond':True,
'R_Recombination':True,
'SubstitutionS':True,
'Substitution_O':True,
'intra_H_migration':True,
'intra_NO2_ONO_conversion':True,
'intra_OH_migration':True,
'intra_substitutionCS_cyclization':True,
'intra_substitutionCS_isomerization':True,
'intra_substitutionS_cyclization':True,
'intra_substitutionS_isomerization':True,
'ketoenol':True,
'lone_electron_pair_bond':True,
}
