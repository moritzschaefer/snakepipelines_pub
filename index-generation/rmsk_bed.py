import re

with open('rmsk.gtf') as f, open('rmsk.bed', 'w') as of:
    for l in f:
        f = l.strip().split('\t')

        if f[2] != 'gene':  # only take each TE once
            continue

        if int(f[3]) > 0:  # bed is 0-indexed (GTF is 1-indexed), however 0 seems to be forbidden..
            f[3] = str(int(f[3]) - 1)

        tid = re.search('transcript_id "([^"]+)"', f[8]).groups()[0]

        of.write('\t'.join([
            f[0], f[3], f[4], tid, '0', f[6], f[3], f[4], '0', '0', str(int(f[4]) - int(f[3])) + ',', '0,'
        ]) + '\n')
