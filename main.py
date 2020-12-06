import Levenshtein


def compare_levenshtein(str1, str2):
    l_dist = Levenshtein.distance(str1, str2)
    return l_dist


def compare_hamming(str1, str2):
    if len(str1) == len(str2):
        return Levenshtein.hamming(str1, str2)
    else:
        raise ValueError("Each string must be of equal length")


def compare_jaro(str1, str2):
    return Levenshtein.jaro(str1, str2)


def compare_jaro_winkler(str1, str2):
    return Levenshtein.jaro_winkler(str1, str2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_pairs = [
        ('bart simpson', 'bartholomew simpson'),
        ('lisa simpson', 'Lisa Simpson'),
        ('homer simpson', 'mr. homer simpson'),
        ('marge simpson', 'simpson, marge'),
        ('Rabbi Hyman Krustofsky', ''),
        ('crazy cat lady', 'Crazy Cat Lady'),
        ('jess lovejoy', 'Jessica Lovejoy'),
        ('booberella', 'Booberella'),
        ('capital city goofball', 'Capital City Goofball'),
        ('leprechaun', 'Leprechaun'),
        ('ling bouvier', 'Ling Bouvier'),
        ('julio', 'Julio'),
        ('mrs muntz', 'Mrs.Muntz'),
        ('chazz busby', 'Chazz Busby'),
        ('roger meyers', 'Roger Meyers, Jr.'),
        ('shauna chalmers', 'Shauna Chalmers'),
        ('kumiko albertson', 'Kumiko Albertson'),
        ('surly duff', 'Surly Doff')
    ]

    for np in name_pairs:

        first, second = np[0], np[1]
        line_length = len(first + second + '  -  ')
        levenshtein_dist = compare_levenshtein(first, second)
        jaro_dist = compare_jaro(first, second)
        jaro_winkler = compare_jaro_winkler(first, second)
        print('{:^25} - {:^25}'.format(first, second))
        print(f'{"=" * 53}')
        print('{:25} | {:25}'.format('Levenshtein Distance', levenshtein_dist, align='right'))
        print('{:25} | {:25.2%}'.format('Jaro Distance', jaro_dist, align='right'))
        print('{:25} | {:25.2%}'.format('Jaro-Winkler Distance', jaro_winkler, align='right'))
        print('\n\n')



