# Edytor_Graficzny

# Cel projektu
Ten projekt służy do wczytywania, przetwarzania i zapisywania obrazów za pomocą różnych technik przetwarzania obrazu przy użyciu biblioteki OpenCV. Umożliwia użytkownikowi wykonywanie różnorodnych operacji na obrazach, takich jak transformacja kolorów, binaryzacja, erozja, operacje morfologiczne, filtracja oraz kompresja.

# Funkcje
1. wczytaj_obraz: Wczytuje obraz z pliku podanego przez użytkownika.
2. pokaz_obraz: Wyświetla obraz w nowym oknie.
3. zapisz_obraz: Zapisuje przetworzony obraz do pliku.
4 transformacja_koloru: Konwertuje obraz do przestrzeni kolorów HSV i LAB.
5.negatyw: Generuje negatyw obrazu.
6. binaryzacja: Przeprowadza binaryzację obrazu na podstawie progu podanego przez użytkownika.
7. erozja: Przeprowadza erozję obrazu z różnym sąsiedztwem.
8. otwarcie: Wykonuje operację morfologicznego otwarcia.
9. domkniecie: Wykonuje operację morfologicznego domknięcia.
10. filtr: Stosuje wybrane przez użytkownika filtry (Gaussa, medianowy, bilateralny).
11. wyrównanie_histogramu: Wyrównuje histogram obrazu w skali szarości.
12. kompresja: Kompresuje obraz do pliku JPEG z wybraną jakością.
13. wygladzanie: Wygładza obraz za pomocą uśredniania.

# Instrukcja użytkowania

1. Wczytanie obrazu: Po uruchomieniu skryptu użytkownik zostanie poproszony o podanie nazwy pliku obrazu do wczytania.

2. Wybór operacji: Skrypt wyświetli listę dostępnych operacji. Użytkownik wybiera operację poprzez wpisanie odpowiedniej cyfry.

3. Parametry operacji: Dla niektórych operacji, użytkownik będzie musiał podać dodatkowe parametry (np. próg binaryzacji, rozmiar maski).

4. Podgląd obrazu: Po każdej operacji obraz zostanie wyświetlony w nowym oknie.

5. Zapisanie obrazu: Po zakończeniu przetwarzania użytkownik może zapisać obraz do pliku.

# Przykładowe użycie
Po uruchomieniu skryptu, użytkownik może:

- Wczytać obraz z pliku.
- Wybrać operację np. binaryzację i podać odpowiedni próg.
- Przeglądać przetworzony obraz.
- Zapisać przetworzony obraz do pliku.

# Wymagania
- Python 3.x
- OpenCV
- NumPy

# Instalacja
1. Zainstaluj Python 3.x z oficjalnej strony Pythona.
2. Zainstaluj wymagane biblioteki:

- cmd -> pip install opencv-python numpy