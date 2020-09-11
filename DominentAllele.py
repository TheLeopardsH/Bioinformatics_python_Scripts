# Mendel's First Law ->problem was to compute an individual possessing a dominant allele
# k are homozygous dominant for a factor
# m are heterozygous
# n are homozygous recessive.
def DominantAllele(k,m,n):
    population=k+m+n
    #we chose homozygous dominent first
    Pk=k/population
    #we chose heterozygous first
    Pmk= (m/population)*(k / (population - 1.0))
    Pmm= (m / population) * ((m - 1.0) / (population - 1.0)) * 0.75
    Pmn= (m / population) * (n / (population - 1.0)) * 0.5
    # we chose homozygous recessive  first
    Pnk = (n / population) * (k / (population - 1.0))
    pnm = (n / population) * (m / (population - 1.0)) * 0.5
    print(Pk+Pmk+Pmm+Pmn+Pnk+pnm)

DominantAllele(27,30,27)
