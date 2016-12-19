import pandas


bed = pandas.read_table('te_locations.bed', header=None, names=['Chr', 'Start', 'Stop', 'Insertion', 4, 5])
insertion_to_families = pandas.read_table('../conversion_files/dm6_FBti_to_Families.tab', header=None, names=['Insertion', 'family'])
families_to_superfamilies = pandas.read_table('../annotation_files/family_to_superfamily.tab', header=None, names=['family', 'superfamily'])
bed_families = pandas.merge(bed, insertion_to_families, on='Insertion')
bed_families_superfamilies = pandas.merge(bed_families, families_to_superfamilies, on='family')
with open('te_locations_family_superfamily.bed', 'w') as out:
        out.write(bed_families_superfamilies.to_csv(sep='\t', index=None))
