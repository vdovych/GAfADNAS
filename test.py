from DPXDrop import Dynamic
from Greedy import Greedy
from time import time
import generators
a = '''1 tttgcaccgg ataacaaaac aaaaaacatt gtatatcaga tcgctctgca ctaatttcag
       61 gtcaaaaaaa tttgtcaatc caacgaaagg tttgtttaaa agtcatcact ttttttgatt
      121 atcaactaat tttgaattta aattttagga gaagatagga ataaggtaag gtaataatgt
      181 acgtcaaagt agaaacggaa cgtctcaatt taatttgttt taatcagtcg aagttggggc
      241 gagataaagt tcgccgggtc cgctagtagt aatataattc tattttaaat tgctataact
      301 ttaatttgca aaaagaatgg taaaaaagcg atactatcga tagtatcgaa ttttcgtatt
      361 caaaacatcg aaaatatcga atggtgccac tatcgatagt ttcccaactc tagtctagac
      421 ccgacgtccc tcgttgatat gagaatcgag gaggagagca gtataactat atgtttggca
      481 gcgctcattt acgttgccta tgtttgatcg atgtgcagtt ttattttctt cttttctcaa
      541 tgttatattt ttaaatggta gaatgtttta attattttaa gcacttaaat gtttcataaa
      601 acatgtttag ttattttaat gtgaaattat tctttggatc attttgtaaa agtgtctgga
      661 gttcaagatt tgcatttttg accaaagcat ttcgtgaaaa atcatctgtt aaaatattaa
      721 aatttatgaa tattatgaat attttttaga aagagtgaaa tttgaacctt ttacttgcgg
      781 gaacactcaa aatattttcg ttttaaacaa attatggtat tttttgacca ctttcaaatt
      841 ggccctttca tacataaatt gtcggctttc ttggtacttt cgggtatggt tttggctacc
      901 taaaaaatat taatatttta aaatatatta gtttttgtca attttgtaaa ataaatagga
      961 cacatgtttt agttaataaa agtttaaact gaatttatgc atttgtttct tggaaatggt
     1021 ctattatgtt cccc'''
a = a.replace(" ","")
a = a.replace("1","")
a = a.replace("2","")
a = a.replace("3","")
a = a.replace("4","")
a = a.replace("5","")
a = a.replace("6","")
a = a.replace("7","")
a = a.replace("8","")
a = a.replace("9","")
a = a.replace("0","")
a = a.replace("\n","")
b=a.upper()
a= '''1 tgaattcttt aaagagacgg gaccataaat ctggaaaagt aaattataaa caaatttcaa
       61 ttaatttgaa cttgctatta taaacaatac aatcagttat ttggaaactc tttaagaaac
      121 aaagcggggc aataaagaga gagacactac tacacgatga gaatgaaatc gattttagta
      181 aattggaatc aaggcacact actacctatt tatattctaa ataggaaatg agtgttattc
      241 tcggttatta gatatcaact aagtggtgct tacgttttcc tgtcagagtt aagcatggct
      301 atatcctcta attgatcgat aaacttattt agtgcagggc agcggaaacg aacctaaagc
      361 ctttaaggat tattagagaa cagatatgtg tacaaaagga ttttagagac agaagctttt
      421 acactaagaa ccagatttgg agcgacaaac attttgtgaa cagagtaaaa aaagtatatt
      481 catggctttt aataacaaaa atctattagg aatatataaa tcttaaatca cgataatttt
      541 cgatcactgg tttgaacaga ttagccgatt aaacttgact tgtccggtat ctcataccat
      601 tctccattat ttggagtaca ttcctatgaa attcaatgta taaaaaatac ccagtgaaac
      661 cagctagtca ttgggatatt tggtcataag atttttaaat attttaagta tacacaaatc
      721 gaccaatcaa actacactta ggacagagct tatcagcaga ctttgaactt ggcacaccca
      781 ccaacgtaat actcccttga cactacacac aatatactaa ttgaatcgaa ttgtaaccat
      841 ggactatgtg tgatatgcta atgctggttt ttctcctctt gcaaattcct cgaaataatg
      901 ctggtttacg aatgagtcgc gttaggagac tatagaccag gtttattggc cttgttgtat
      961 cgactcagtg gcaagtgttg tccaaggcat tggcgccccg ttcgccgtcg ataagatctt
     1021 aatgagataa gatt'''
a = a.replace(" ","")
a = a.replace("1","")
a = a.replace("2","")
a = a.replace("3","")
a = a.replace("4","")
a = a.replace("5","")
a = a.replace("6","")
a = a.replace("7","")
a = a.replace("8","")
a = a.replace("9","")
a = a.replace("0","")
a = a.replace("\n","")
a = a.upper()
print(Greedy(a, b)[0])
a = generators.DNAgenerator(1000)
b = generators.DNAchanger(a, 0.1)
print(Greedy(a, b)[0])
a = generators.DNAgenerator(1000)
b = generators.DNAgenerator(1000)
print(Greedy(a, b)[0])

lst = []
t1 = time()
for _ in range(1):
    a = generators.DNAgenerator(100)
    b = generators.DNAchanger(a, 0.1)
    lst.append(Greedy(a, b)[0])
print(sorted(lst),time()-t1)
