
n = 25  # rozmiar szachownicy
mozliwe_ruchy = {(-2, -1), (-2, 1), (-1, 2), (1, 2),
                 (2, 1), (2, -1), (1, -2), (-1, -2)}


def mozna_wykonac_ruch(pozycja, ruch, historia_ruchow):
    v, h = pozycja[0] + ruch[0], pozycja[1] + ruch[1]
    if (v, h) in historia_ruchow:
        return False
    if v > 0 and v <= n and h > 0 and h <= n:
        return True
    return False


def skocz(odwiedzone_pola, pozycja):
    if(len(odwiedzone_pola) == n*n):
        print(odwiedzone_pola)
    else:
        for ruch in mozliwe_ruchy:
            if mozna_wykonac_ruch(pozycja, ruch, odwiedzone_pola):
                if (pozycja[0] + ruch[0], pozycja[1] + ruch[1]) not in odwiedzone_pola:
                    odwiedzone_pola.append(pozycja)
                skocz(odwiedzone_pola,
                      (pozycja[0] + ruch[0], pozycja[1] + ruch[1]))


def main():
    print('Searching for ' + str(n) + '*' + str(n) + ' move combination...')
    skocz([], (2, 3))


if __name__ == '__main__':
    main()
