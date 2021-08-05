from collections import defaultdict

gene_index = defaultdict(int)

with open('rmskOutCurrent_activeL1s.txt', 'r') as fin, open('rmsk.gtf', 'w') as fout:
    for line in fin:
        s = line.split('\t')
        class_id = s[11]
        family_id = s[12]
        gene_id = f'{class_id}:{family_id}:{s[10]}:dup'
        gene_index[gene_id] += 1
        dup = str(gene_index[gene_id])
        gene_id = gene_id + dup
        suffix = '_active' if family_id == 'L1_active' else ''
        gene_name = f'{s[10]}{suffix}:dup{dup}' 

        for feature_type in ['gene', 'transcript', 'exon']:
            out = [
                    s[5],
                    'rmsk',
                    feature_type,
                    str(int(s[6]) + 1),
                    s[7],
                    '.',
                    s[9],
                    '.',
                    ' '.join([f'{k} "{v}";' for k, v in {
                        'gene_id': gene_id,
                        'transcript_id': gene_id,
                        'family_id': family_id,
                        'class_id': class_id,
                        'gene_name': gene_name
                        }.items()])
                    ]

            fout.write('\t'.join(out) + '\n')
