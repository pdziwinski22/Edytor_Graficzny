import numpy as np
import cv2


def wczytaj_obraz():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    obraz = cv2.imread(nazwa_pliku)
    return obraz


def pokaz_obraz(obraz):
    cv2.imshow("Obraz", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zapisz_obraz(obraz):
    nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
    cv2.imwrite(nazwa_pliku, obraz)


def transformacja_koloru(obraz):
    obraz_hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)
    obraz_lab = cv2.cvtColor(obraz, cv2.COLOR_BGR2LAB)
    return obraz_hsv, obraz_lab


def negatyw(obraz):
    obraz_negatyw = 255 - obraz
    return obraz_negatyw


def binaryzacja(obraz):
    prog = int(input("Podaj próg binaryzacji (0-255): "))
    ret, obraz_bin = cv2.threshold(obraz, prog, 255, cv2.THRESH_BINARY)
    return obraz_bin


def erozja(obraz):
    sasiedztwo = int(input("Podaj rozmiar sąsiedztwa (4 lub 8): "))
    if sasiedztwo == 4:
        kernel = np.ones((3, 3), np.uint8)
    elif sasiedztwo == 8:
        kernel = np.ones((5, 5), np.uint8)
    else:
        print("Niepoprawny rozmiar sąsiedztwa.")
        return obraz
    obraz_erozja = cv2.erode(obraz, kernel, iterations=1)
    return obraz_erozja


def otwarcie(obraz):
    sasiedztwo = int(input("Podaj rozmiar sąsiedztwa (4 lub 8): "))
    if sasiedztwo == 4:
        kernel = np.ones((3, 3), np.uint8)
    elif sasiedztwo == 8:
        kernel = np.ones((5, 5), np.uint8)
    else:
        print("Niepoprawny rozmiar sąsiedztwa.")
        return obraz
    obraz_otwarcie = cv2.morphologyEx(obraz, cv2.MORPH_OPEN, kernel)
    return obraz_otwarcie


def domkniecie(obraz):
    sasiedztwo = int(input("Podaj rozmiar sąsiedztwa (4 lub 8): "))
    if sasiedztwo == 4:
        kernel = np.ones((3, 3), np.uint8)
    elif sasiedztwo == 8:
        kernel = np.ones((5, 5), np.uint8)
    else:
        print("Niepoprawny rozmiar sąsiedztwa.")
        return obraz
    obraz_domkniecie = cv2.morphologyEx(obraz, cv2.MORPH_CLOSE, kernel)
    return obraz_domkniecie



def filtr(obraz):
    filtry = {
        "Rozmycie Gaussa": cv2.GaussianBlur,
        "Rozmycie medianowe": cv2.medianBlur,
        "Rozmycie bilateralne": cv2.bilateralFilter,
    }
    nazwa_filtra = input("Wybierz filtr (1 - Rozmycie Gaussa, 2 - Rozmycie medianowe, 3 - Rozmycie bilateralne): ")
    if nazwa_filtra == "1":
        rozmiar = int(input("Podaj rozmiar maski (3, 5, 7, ...): "))
        sigma = float(input("Podaj wartość sigma (np. 1.0, 1.5, 2.0, ...): "))
        obraz_filtr = filtry[nazwa_filtra](obraz, (rozmiar, rozmiar), sigma)
    elif nazwa_filtra == "2":
        rozmiar = int(input("Podaj rozmiar maski (3, 5, 7, ...): "))
        obraz_filtr = filtry[nazwa_filtra](obraz, rozmiar)
    elif nazwa_filtra == "3":
        s = int(input("Podaj wartość s (np. 50, 100, 150, ...): "))
        r = int(input("Podaj wartość r (np. 5, 10, 15, ...): "))
        obraz_filtr = filtry[nazwa_filtra](obraz, s, r, r)
    else:
        print("Niepoprawny wybór filtra.")
        return obraz
    return obraz_filtr


def wyrównanie_histogramu(obraz):
    obraz_gray = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    obraz_wyrownany = cv2.equalizeHist(obraz_gray)
    obraz_wyrownany = cv2.cvtColor(obraz_wyrownany, cv2.COLOR_GRAY2BGR)
    return obraz_wyrownany



def kompresja(obraz):
    jakość = int(input("Podaj jakość kompresji (0-100): "))
    parametry = [cv2.IMWRITE_JPEG_QUALITY, jakość]
    _, obraz_kompresja = cv2.imencode(".jpg", obraz, parametry)
    obraz_kompresja = cv2.imdecode(obraz_kompresja, 1)
    return obraz_kompresja



def wygladzanie(obraz):
    rozmiar = int(input("Podaj rozmiar maski (3, 5, 7, ...): "))
    kernel = np.ones((rozmiar, rozmiar), np.float32) / (rozmiar * rozmiar)
    obraz_wygladzony = cv2.filter2D(obraz, -1, kernel)
    return obraz_wygladzony




def glowna():

    nazwa_pliku = input("Podaj nazwę pliku: ")
    obraz = cv2.imread(nazwa_pliku)
    if obraz is None:
        print("Nie udało się wczytać pliku.")
    return obraz

obraz = glowna()


while True:
    print("\nWybierz operację:")
    print("1 - Transformacja pomiędzy przestrzeniami barw")
    print("2 - Negatyw")
    print("3 - Binaryzacja")
    print("4 - Erozja")
    print("5 - Otwarcie")
    print("6 - Domknięcie")
    print("7 - Wybrany filtr")
    print("8 - Wyrównanie histogramu")
    print("9 - Kompresja")
    print("10 - Wygładzanie przez uśrednianie")
    print("11 - Zapisz i wyjdź")
    wybor = input("Wybór: ")

    if wybor == "1":
        obraz = transformacja_barw(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "2":
        obraz = negatyw(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "3":
        obraz = binaryzacja(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "4":
        obraz = erozja(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "5":
        obraz = otwarcie(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "6":
        obraz = domkniecie(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "7":
        obraz = filtr(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "8":
        obraz = wyrównanie_histogramu(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "9":
        obraz = kompresja(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "10":
        obraz = wygladzanie(obraz)
        cv2.imshow("Obraz", obraz)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif wybor == "11":
        nazwa_zapisu = input("Podaj nazwę pliku do zapisu: ")
        cv2.imwrite(nazwa_zapisu, obraz)
        cv2.destroyAllWindows()
        break
    else:
        print("Niepoprawny wybór operacji.")



def transformacja_barw(obraz):
    obraz_hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(obraz_hsv)
    s = cv2.add(s, 50)
    obraz_hsv = cv2.merge([h, s, v])
    obraz_wynikowy = cv2.cvtColor(obraz_hsv, cv2.COLOR_HSV2BGR)
    return obraz_wynikowy



def negatyw(obraz):
    obraz_wynikowy = 255 - obraz
    return obraz_wynikowy



def binaryzacja(obraz):
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    _, obraz_wynikowy = cv2.threshold(obraz_szary, 127, 255, cv2.THRESH_BINARY)
    return obraz_wynikowy



def erozja(obraz):
    if obraz is None or obraz.size == 0:
        raise ValueError("Niepoprawny obraz")
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    _, obraz_binarny = cv2.threshold(obraz_szary, 127, 255, cv2.THRESH_BINARY)
    kernel_8 = np.ones((3, 3), np.uint8)
    kernel_4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    obraz_wynikowy_8 = cv2.erode(obraz_binarny, kernel_8, iterations=1)
    obraz_wynikowy_4 = cv2.erode(obraz_binarny, kernel_4, iterations=1)
    if obraz_wynikowy_8.shape == obraz_wynikowy_4.shape:
        obraz_wynikowy = np.concatenate((obraz_wynikowy_8, obraz_wynikowy_4), axis=1)
    else:
        obraz_wynikowy = obraz_wynikowy_8
    return obraz_wynikowy



def otwarcie(obraz):
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    _, obraz_binarny = cv2.threshold(obraz_szary, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    obraz_wynikowy = cv2.morphologyEx(obraz_binarny, cv2.MORPH_OPEN, kernel)
    return obraz_wynikowy



def domkniecie(obraz):
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    _, obraz_binarny = cv2.threshold(obraz_szary, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    obraz_wynikowy = cv2.morphologyEx(obraz_binarny, cv2.MORPH_CLOSE, kernel)
    return obraz_wynikowy



def filtr(obraz):
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    _, obraz_binarny = cv2.threshold(obraz_szary, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.float32) / 25

    obraz_wynikowy = cv2.filter2D(obraz_binarny, -1, kernel)
    return obraz_wynikowy


def wyrownanie_histogramu(obraz):
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    obraz_wynikowy = cv2.equalizeHist(obraz_szary)
    return obraz_wynikowy



def kompresja(obraz):
    _, obraz_skompresowany = cv2.imencode('.jpg', obraz, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    obraz_wynikowy = cv2.imdecode(obraz_skompresowany, cv2.IMREAD_COLOR)
    return obraz_wynikowy



def wygladzanie(obraz):
    kernel = np.ones((5, 5), np.float32) / 25
    obraz_wynikowy = cv2.filter2D(obraz, -1, kernel)
    return obraz_wynikowy



nazwa_pliku = input("Podaj nazwę pliku: ")


obraz = cv2.imread(nazwa_pliku)


obraz_po_edycji = transformacja_barw(obraz)
obraz_po_edycji = negatyw(obraz_po_edycji)
obraz_po_edycji = binaryzacja(obraz_po_edycji)
obraz_po_edycji = erozja(obraz_po_edycji)
obraz_po_edycji = np.concatenate((obraz_po_edycji, otwarcie(obraz_po_edycji)), axis=1)
obraz_po_edycji = np.concatenate((obraz_po_edycji, domkniecie(obraz_po_edycji)), axis=1)
obraz_po_edycji = filtr(obraz_po_edycji)
obraz_po_edycji = wyrownanie_histogramu(obraz_po_edycji)
obraz_po_edycji = kompresja(obraz_po_edycji)
obraz_po_edycji = wygladzanie(obraz_po_edycji)


cv2.imshow('Obraz po edycji', obraz_po_edycji)
cv2.waitKey(0)


nazwa_pliku_wyjsciowego = input("Podaj nazwę pliku wyjściowego: ")
cv2.imwrite(nazwa_pliku_wyjsciowego, obraz_po_edycji)


cv2.destroyAllWindows()
