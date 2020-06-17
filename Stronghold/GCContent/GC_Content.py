def nucAllCount(DNA):
    numNucleotides = 0
    for nucleotide in DNA:
        numNucleotides += 1
    return numNucleotides
def GCContent(DNA, **kwargs):
    subSeqStart = kwargs.get('start', None)
    subSeqEnd = kwargs.get('end', None)
    if (subSeqEnd and subSeqEnd > 0 and subSeqEnd and subSeqEnd < nucAllCount(DNA)):
        subSequence = DNA[subSeqStart-1:subSeqEnd]
        return ((subSequence.count("C") + subSequence.count("G")) / nucAllCount(subSequence)) * 100
    return ((DNA.count("C") + DNA.count("G")) / nucAllCount(DNA)) * 100

cg_percent_list = []
DNAstrands = []
currentDNA = ""
ids = []
list_ = []
myfile = open("rosalind_gc.txt", "rt")
list_ = myfile.readlines()

line_counter = 0 
while (line_counter <= len(list_) -1):
    if (list_[line_counter][0] == '>'):
        ids.append(list_[line_counter])
        if (line_counter > 0):
            DNAstrands.append(currentDNA)
            count = GCContent(currentDNA)
            cg_percent_list.append(count)
        currentDNA = ""  
    else :
        currentDNA = currentDNA + list_[line_counter].strip('\n')
    line_counter += 1    
              
biggest = max(cg_percent_list)
print(ids)
print(cg_percent_list)
print(len(DNAstrands))
print(ids[cg_percent_list.index(biggest)])
print(biggest)