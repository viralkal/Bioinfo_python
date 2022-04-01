import re
dna = input("Enter a sequence:")
bind_trans = {'GGGCGG':'SP1','TGAGTCA':'AP-1','TTGGC(A|T|G|C)GCCAA':'NF-1','CACGTG':'c-Myc'}

pat = re.compile(r'(GGGCGG)|(TGA(G|C)TCA)|(TTGGC(A|T|G|C)GCCAA)|(CACGTG)')
match_obj = pat.search(dna)
for key,value in bind_trans.items():
   while True:
        if match_obj:
         test1 = match_obj.group()
         bind_site = test1
         bind_site == test1
         print('Binding site exits:',bind_site)
         print('Transcription factor for'+' '+bind_site+' '+'is'+' '+ bind_trans[bind_site])
         break
        else:
            print('No Binding Site')
            break


   

