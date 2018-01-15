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
        for i in range(max_id + 1):
            kitty = kitties.get(i, default_kitty)
            f.write(kitty['genes_kai'] + '\n')

if __name__ == '__main__':
    main()
