# -*- coding: utf-8 -*-
"""
Created on Sat May  8 07:20:55 2021

@author: Michał
"""

from itertools import permutations
import sys;

def zadanie4(filename):
	"""
	Kolejnosc zlecen
	"""

	print('Zadanie 4: Kolejnosc zlecen');

	# otwieramy plik podany jako parametr
	with open(filename) as file:
		# wczytujemy caly plik i dzielimy go wierszami
		content = file.read().splitlines();

	# tutaj beda wczytane zlecenia
	zlecenia = list();

	# dla ulatwienia
	ID = 0;
	A = 1;
	B = 2;


	# przetwarzamy kolejne linie z pliku
	for line in content:

		# dzieli linie, np: '12 25.0 33.0' => ['12', '25.0', '33.0']
		data = line.split(' ');

		# zamienia tekst '12' na liczbe 12
		data[ID] = int(data[ID]);
		# zamienia tekst '25.0' na liczbe 25.0
		data[A] = float(data[A]);
		# zamienia tekst '33.0' na liczbe 33.0
		data[B] = float(data[B]);

		# dodajemy zlecenie do listy
		zlecenia.append(data);
		
	# obliczamy ilosc zlecen
	size = len(zlecenia);

	# tworzymy sekwencje
	# zawierac bedzie numery zlecen z list zlecen
	# dla size = 10 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# mamy 10 numerow zlecen, a raczej ich indeksy w liscie zlecen
	# w programowaniu od 0, wiec:
	# pierwsze zlecenie z listy (czyli pierwsza linijka pliku ktory wczytalismy) bedzie pod indeksem 0,
	# drugie zlecenie z listy bedzie pod indeksem 1, itd
	sequence = range(0, size);

	# wszystkie mozliwe kolejnosci wykonywania prac na obrabiarkach
	# tworzy nam liste unikalnych sekwencji, w jakie mozna uszeregowac podana sekwencje, uzywajac 'size' elementow z sekwencji
	# przyklad: 
	# size = 3
	# sequence = range(0, 3) = [0, 1, 2]
	# variants = [ (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0) ];
	# mamy wszystkie przeksztalcenia sekwencji liczb
	
	# parametr size mowi, ile elementow ma sie znalezc w pojedynczej sekwencji
	# przyklad: variants = permutations( range(0, 3), 2 )
	# range(0, 3) = [0, 1, 2]
	# variants = [ (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
	variants = permutations(sequence, size);

	# szukamy najlepszego czasu, wiec bierzemy najwieksza mozliwa liczbe
	best_time = sys.float_info.max;

	# sprawdzamy kazdza mozliwy wariant / sekwencje
	for variant in variants:

		# bedziemy liczyc czas jej wykonania
		time = 0;

		# dodanie czasu pierwszego zlecenia na obrabiarce A
		index = variant[0];
		first = zlecenia[index];
		time += first[A];

		# obliczanie czasow kolejnych zlecen
		for i in range(0, size-1):

			# pobieramy zlecenie dla konkretnej obrabiarki

			obrabiarka_a_index = variant[i+1];
			obrabiarka_a = zlecenia[obrabiarka_a_index][A];

			obrabiarka_b_index = variant[i];
			obrabiarka_b = zlecenia[obrabiarka_b_index][B];

			time += max(obrabiarka_a, obrabiarka_b);

		# dodanie czasu ostatniego zlecenia na obrabiarce B
		index = variant[size-1];
		last = zlecenia[index];
		time += last[B];

		# czy osiagnelismy lepszy wynik
		if time < best_time:
			best = variant;
			best_time = time;
		
	print('Best time: ', best_time);
	print(best)
	print('Sequence:');
	for i in best:
		obj = zlecenia[i];
		print(obj[ID],  obj[A], obj[B]);
		