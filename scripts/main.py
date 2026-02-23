q=0.06#תדירות האלל c
gen=500#מספר הדורות
p=1-q#תדירות האלל C
i=0
file=open('results/CF_freq','w')
file.write("Generation\tFreq_c\tFreq_CC\tFreq_Cc\tFreq_cc\n")
while gen > i:
    next_gen_hetrozigot=2*p*q
    nexst_gen_homozigot_C=p**2
    nexst_gen_homozigot_c=q**2 
    
    next_gen = 0.98*nexst_gen_homozigot_C + next_gen_hetrozigot
    nexst_gen_homozigot_C_NEW= (0.98*nexst_gen_homozigot_C)/next_gen
    nexst_gen_hetrozigot_NEW= next_gen_hetrozigot/next_gen
    nexst_gen_homozigot_c_NEW=0

    file.write(f"{i}\t{q}\t{nexst_gen_homozigot_C_NEW}\t{nexst_gen_hetrozigot_NEW}\t{nexst_gen_homozigot_c_NEW}\n")
    q = nexst_gen_hetrozigot_NEW/2 
    p = 1 - q
    i += 1






file.close()