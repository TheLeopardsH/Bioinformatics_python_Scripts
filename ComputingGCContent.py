#Computing GC Content 
def GCcount(File):
    genes = {}
    array = []
    score = []
    with open(File) as FR:
        Lines=FR.readlines()
        for line in Lines:
            line = line.rstrip()
            if line.startswith(">"):
                name=line
                array.append(name)
                line1=""
            else:
                line1+=line
            genes[name] =line1
    for i in range(len(array)):
        score.append(((genes[array[i]].count('C')+genes[array[i]].count('G'))/len(genes[array[i]]))*100)
    maxvalue = score.index(max(score))
    print(array[maxvalue][1:])
    print(round(score[maxvalue],6))
GCcount('rosalind_gc(1).txt')

