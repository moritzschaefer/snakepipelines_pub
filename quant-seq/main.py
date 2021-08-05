#!/usr/bin/env python
# requires conda activate snakePipes3

import glob
import os
import subprocess
from pathlib import Path

import pandas as pd
from tqdm.contrib.concurrent import process_map

try:
    os.mkdir('./data')
except FileExistsError:
    pass
# generate symlinks for all rna-seq files into one folder
# files.csv was copied from moritzschaefers rna-seq-star-deseq2 pipeline
sample_df = pd.read_csv('files.csv')
for _, row in sample_df.iterrows():
    try:
        os.symlink(row[f'fq1'], f'data/{row["sample"]}_R1.fastq.gz')
    except FileExistsError:
        pass

try:
    os.mkdir('./data/polya_trimmed')
except FileExistsError:
    pass

def trim_sample(sample):
    target_file = Path('data/polya_trimmed') / sample.name
    if target_file.exists():
        return
    # Run illumina trimming
    subprocess.run(['trim_galore', '--output_dir', 'data/illumina_trimmed',
                    '--stringency', '3', '--illumina', sample],
                   check=True)
    trimgalore_out = Path('data/illumina_trimmed') / sample.name

    # Rename files
    subprocess.run(['mv',
                    str(trimgalore_out).replace('.fastq.gz', '_trimmed.fq.gz'),
                    trimgalore_out],
                   check=True)
    # NOTE: output_dir is buggy with the polyA option
    subprocess.run(['trim_galore', '--polyA', (trimgalore_out)],
                   check=True)
    subprocess.run(['mv',
                    sample.name.replace('.fastq.gz', '_trimmed.fq.gz'),
                    str(target_file)],
                   check=True)


process_map(trim_sample, list(Path('data/').glob('*.fastq.gz')))

# quant-seq files
for sheet in glob.glob('sampleSheets/*.tsv'):
    # for all samples:
    #     subprocess.run([trimgalore --illumina]) data -> data/illumina_trimmed

        # Trim polyA using bbduk (https://www.biostars.org/p/236515/) <- didn't work out..
        # bbduk_out = trimgalore_out.replace('illumina_trimmed', 'bbduk_trimmed')
        # 
        # subprocess.run(['bbduk.sh', f'in={sample}', f'out={bbduk_out}',
        #                 'literal=AAAAAAAAA', 'k=13', 'ktrim=r', 'forcetrimleft=11',
        #                 'ref=/home/schamori/anaconda3/opt/bbmap-38.90-0/resources/truseq.fa.gz', 'useshortkmers=t',
        #                 'mink=5', 'qtrim=t', 'trimq=10', 'minlength=20'])

    # finally run
    subprocess.check_call([
        'mRNA-seq', '-i', './data/polya_trimmed', '-o', '.',
        '--libraryType', '1', '--local', '-j', '32',
        '--featureCountsOptions', '\--primary',
        '--mode', 'alignment,alignment-free,deepTools_qc',
        '--sampleSheet', sheet, '--fastqc', 'GRCm38_98'])
