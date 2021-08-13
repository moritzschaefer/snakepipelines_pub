# Readme

This repository assists our publication and contains code for NGS data analysis

# Installation and file generation notes

I installed snakepipes as documented with conda https://snakepipes.readthedocs.io/en/latest/content/setting_up.html

Here I store and edit config files.

activate using conda activate snakePipes (or snakePipes2 or better snakePipes3)

An index/genome/etc by the name GRCm38_release98 has been created as follows:

    createIndices --local -o ~/data/snakepipes/GRCm38_98 --genome ftp://ftp.ensembl.org/pub/release-98/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna_sm.primary_assembly.fa.gz --gtf ftp://ftp.ensembl.org/pub/release-98/gtf/mus_musculus/Mus_musculus.GRCm38.98.gtf.gz GRCm38_98 -j 20


Conda requirements:
python
entrez-direct
sra-tools
