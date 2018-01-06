import csv
import glob


def main():
    filename = sorted(glob.glob('*.csv'))[-1]
    out_filename = 'genes.txt'

    kitties = {}

    with open(filename, mode='rt') as f:
        for row in csv.DictReader(f):
            kitties[int(row['id'])] = row

    max_id = max(kitties)
    default_kitty = {
        'genes_kai':
            '+++++++/++//+///////'
            '///////+//++/+++++++'
            '//++++//'
    }

    subscripts = '/lIO0'

    with open(out_filename, mode='wt', encoding='utf-8') as f:
        for i in range(1, max_id + 1):
            kitty = kitties.get(i, default_kitty)
            f.write(''.join(
                gene[-1] + subscripts[gene.count(gene[-1])]
                for gene in (kitty['genes_kai'][i*4:i*4+4] for i in range(len(kitty['genes_kai'])//4))
            ) + '\n')


if __name__ == '__main__':
    main()
