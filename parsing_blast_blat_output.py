#############################################################################################
#
#   This script provides a way to parse a BLAST/BLAT (if in BLAST format) output text files
# 
#
#   Author: Nicolas Schmelling
#
#############################################################################################

def blast_parse(file, e, output):

    result_handle = open(file)
    
    from Bio.Blast import NCBIStandalone
    blast_parser = NCBIStandalone.BlastParser()
    blast_iterator = NCBIStandalone.Iterator(result_handle, blast_parser)
    blast_record = next(blast_iterator)
    
    output = open(output, 'w')
    output.write('query title\talignment title\tlength\te value' + '\n')
    for blast_record in blast_iterator:
        E_VALUE_THRESH = e
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    output.write(str(blast_record.query[:18]) + ' \t')
                    output.write(str(alignment.title) + '\t')
                    output.write(str(alignment.length) + '\t')
                    output.write(str(hsp.expect) + '')
                    output.write('\n')
    
    
    output.close()