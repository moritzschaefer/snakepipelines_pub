# Readme

This repository assists our publication and contains code for NGS data analysis

# Installation and file generation notes

I installed snakepipes as documented with conda https://snakepipes.readthedocs.io/en/latest/content/setting_up.html

Here I store and edit config files.

activate using conda activate snakePipes (or snakePipes2 or better snakePipes3)

An index/genome/etc by the name GRCm38_release98 has been created as follows:

    createIndices --local -o ~/data/snakepipes/GRCm38_98 --genome ftp://ftp.ensembl.org/pub/release-98/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna_sm.primary_assembly.fa.gz --gtf ftp://ftp.ensembl.org/pub/release-98/gtf/mus_musculus/Mus_musculus.GRCm38.98.gtf.gz GRCm38_98 -j 20

For e. coli spike-ins, I generated the following index from https://www.ncbi.nlm.nih.gov/genome/?term=Escherichia+coli:

    createIndices --local -o ~/data/snakepipes/ecoli --genome https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz --gtf https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz ecoli_K12 -j 20
    # Note: createIndices partially failed, because gff is not supported (only gtf). Therefore, to make this index complete/valid, the gff first needs to be converted to gtf..
    

atac-seq-no-fdr does the diff-peak analysis without post-FDR filtering

noncoding-RNA-seq is a pipeline to detect TEs (e.g. LINE elements) using TEtranscripts.


Conda requirements:
python
entrez-direct
sra-tools
