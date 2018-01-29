import csv
import glob


def main():
    out_filename = 'genes.js'
    kitties = {}

    for filename in reversed(sorted(glob.glob('*.csv*'))):
        print("Reading", filename)
        with open(filename, mode='rt') as f:
            for row in csv.DictReader(f):
                kitty_id = int(row['id'])
                if kitty_id not in kitties:
                    kitties[kitty_id] = row

    max_id = max(kitties)

    print("Loaded", len(kitties), "🐈 kitties, with max id", max_id)
    print(max_id - len(kitties), "kitty IDs unaccounted-for.")

    default_kitty = {
        'genes_kai':
            '+++++++/++//+///////'
            '///////+//++/+++++++'
            '//++++//'
    }

    print("Writing", out_filename)
    with open(out_filename, mode='wt', encoding='utf-8') as f:
        f.write("window['/genes.js/byLine']=(s=>s.split(/\\n/g))(`\n")

        for i in range(1, max_id + 1):
            kitty = kitties.get(i, default_kitty)
            f.write(kitty['genes_kai'] + '\n')

        f.write(" ` ) || 'https://cryptokittydex.com/resources';")

    print("All done. 🐱")

if __name__ == '__main__':
    main()
