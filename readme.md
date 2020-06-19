![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/152855/73064373-5ed69780-3ea1-11ea-8a71-3d370a5e7dd8.png)

# Kilka ważnych informacji

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj repozytorium na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres repozytorium możesz znaleźć na stronie repozytorium po naciśnięciu w guzik "Clone or download".
3. Rozwiąż zadania i skomituj zmiany do swojego repozytorium. Użyj do tego komend `git add nazwa_pliku`.
Jeżeli chcesz dodać wszystkie zmienione pliki użyj `git add .` 
Pamiętaj że kropka na końcu jest ważna!
Następnie skommituj zmiany komendą `git commit -m "nazwa_commita"`
4. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
5. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

Poszczególne zadania rozwiązuj w odpowiednich plikach.

# Poniżej znajdziesz wytyczne do zadań

# Warsztat &ndash; Przygotowanie projektu

1. Zrób fork repozytorium warsztatowego i sklonuj je na swój komputer.
2. Pamiętaj o robieniu backupów bazy danych, (najlepiej co każde ćwiczenie) 
    i tworzeniu commitów (również co każde ćwiczenie).
3. Utwórz środowisko wirtualne i zainstaluj tam biblioteki dla projektu (z pliku requirements.txt).
4. Stwórz bazę danych i skonfiguruj dostęp w pliku settings.py
5. Wywołaj polecenie manage.py migrate
6. Uruchom testy poleceniem pytest i zapoznaj się z wynikiem.
7. Uruchom serwer ( manage.py runserver) i sprawdź, czy aplikacja działa.
8. Zapoznaj się z kodem aplikacji.

#### Testy:

* Plik `tests.py` znajdujący się w katalogu `tests`, zawiera testy jednostkowe.
* Funkcje `test_*` sprawdzają poszczególne funkcjonalności aplikacji i obrazują, jak należy z nich korzystać.
* Fikstury do testów znajdziesz w pliku `contest.py`.
* Funkcje pomocnicze do testów znajdziesz w pliku `utils.py`.

#### Modele:

* Zajrzyj do pliku `models.py` i przeanalizuj, jakie dane trzyma aplikacja.
* Zwróć uwagę na relacje pomiędzy modelami `Movie` i `Person`.
> Jeżeli chcesz w jakiś sposób rozwinąć model, zrób to śmiało. :-)

#### Widoki:

* W pliku `views.py` zdefiniowane są widoki generyczne, które obsługują wszystkie metody na zasobie `Movie`.
* Klasa `MovieView` obsługuje akcje na pojedynczym obiekcie.
* `MovieListView` obsługuje pozostałe akcje, takie jak: pobranie wszystkich filmów czy dodanie nowego.

> O widokach generycznych w Django Rest Framework przeczytasz w dokumentacji:
> [http://www.django-rest-framework.org/api-guide/generic-views/](http://www.django-rest-framework.org/api-guide/generic-views/)
    
#### Serializatory

* Klasa zawarta w pliku `serializers.py` określa, jak będzie wyglądać **JSON** reprezentujący obiekt modelu `Movie`,
    czyli jak aplikacja będzie go wysyłać.
* Zwróć uwagę na pola `SlugRelatedField`. Odpowiadają one za reprezentację obiektów `Person` 
    połączonych kluczami obcymi do filmu, który serializujemy.
* W tym przypadku osoba jest zapisywana jako imię i nazwisko.
* Możliwe są inne reprezentacje obiektów w relacji (np. id, link):
    [http://www.django-rest-framework.org/api-guide/relations/](http://www.django-rest-framework.org/api-guide/relations/)


#### Przeglądarka **API**

* Wejdź za pomocą przeglądarki internetowej na stronę pod adresem **URL**: `/movies/`.
* Wyświetli się strona **HTML** zawierająca dane filmów w formacie **JSON** oraz kilka dodatkowych opcji.
* Jeśli wykonamy takie samo zapytanie z poziomu skryptu (np. przez **curl**, **ajax**, bibliotekę **requests**), 
    otrzymamy jedynie obiekt JSON. Aplikacja rozpoznaje po nagłówkach, kiedy można pokazać wersję **HTML**.
* Żeby otrzymać surowe dane, można użyć menu pod przyciskiem **GET** i wybrać opcję **json**.
* Pod listą znajduje się formularz dodawania nowych obiektów.
* Widoki obsługują też żądania **OPTIONS**. Zwracają wtedy opis danego endpointu. 
    Kliknij przycisk OPTIONS, żeby go zobaczyć.

> Więcej o przeglądarce API w Django Rest Framework:
> [http://www.django-rest-framework.org/topics/browsable-api/](http://www.django-rest-framework.org/topics/browsable-api/)    
# Warsztat &ndash; Nowa aplikacja

Utwórz wewnątrz projektu django nową aplikację o nazwie `showtimes`. 
Użyj polecenia `python manage.py startapp`. 
Wszystkie kolejne zadania wykonuj w tej aplikacji.

# Warsztat &ndash; Modele

Utwórz modele `Cinema` i `Screening`.

Model `Cinema` ma zawierać pola:
* `name` &ndash; nazwa kina (`string` maks 255 znaków),
* `city` &ndash; miasto (`string` maks 255 znaków),
* `movies` &ndash; relacja wiele do wielu z modelem `Movie` (za pośrednictwem modelu `Screening`).

Model `Screening` ma zawierać:
* `movie` &ndash; relacja do modelu `Movie`,
* `cinema` &ndash; relacja do modelu `Cinema`,
* `date` &ndash; data seansu (pole typu `datetime`).

> Jeżeli chcesz w jakiś sposób rozwinąć modele, zrób to śmiało.

# Warsztat &ndash; Serializator kina

Stwórz serializator dla klasy `Cinema`:
* W katalogu nowej aplikacji dodaj plik `serializers.py`,
* Utwórz w nim serializator dla klasy `Cinema`,
* Filmy w polu `movies` mają być reprezentowane jako linki do odpowiadających im zasobów API.
> Informacje o serializatorach znajdziesz w dokumentacji Django REST Framework:
> [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)
# Warsztat &ndash; Widoki kina

Stwórz widoki dla kina:
* W pliku views.py napisz widoki obsługujące zasób `cinemas`:
    * `CinemaListView`,
    * `CinemaView`.
* Dodaj adresy **URL** do widoków, modyfikując plik `urls.py` w katalogu `moviebase`/
* Napisz testy sprawdzające działanie wszystkich udostępnianych adresów `url` i metod `HTTP`.


#### Testy:

Stwórz testy:
* `test_add_cinema` &ndash; sprawdzający, czy dodawanie nowego kina działa.
* `test_get_cinema_list` &ndash; sprawdzający, czy działa lista wszystkich kin.
* `test_get_cinema_detail` &ndash; sprawdzający, czy szczegółowy widok kina działa.
* `test_delete_cinema` &ndash; sprawdzający usuwanie kina.
* `test_update_cinema` &ndash; sprawdzający, czy aktualizacja kina działa.


##### Podpowiedzi:
* Do sprawdzania, jak działają nowo powstające widoki używaj testów jednostkowych.
* Umieść je w pliku `tests.py` w katalogu `tests` (aplikacji `showtimes`).
* Zanim zaczniesz pisać testy dodaj do katalogu tests plik `conftest.py`.
* Tworzenie testów rozpocznij od dodania fikstury `set_up`, w której stworzysz kilka obiektów w bazie testowej. 
    Umieść ją w pliku `conftest.py`.
* Nie zapomnij o dekoratorze `@pytest.mark.django_db`, aby móc korzystać z bazy danych.
* Możesz wzorować się na istniejących testach z aplikacji `movielist`.
# Warsztat &ndash; Serializator seansu

* Dodaj nowy serializator dla klasy `Screening`.
* Kina mają być reprezentowane jako ich nazwy.
* Filmy mają być reprezentowane jako ich tytuły.
# Warsztat &ndash; Widoki seansu

Stwórz widoki dla seansu:
* W pliku views.py napisz widoki obsługujące zasób `screening`:
    * `ScreeningListView`,
    * `ScreeningView`.
* Dodaj adresy **URL** do widoków, modyfikując plik `urls.py` w katalogu `moviebase`/
* Napisz testy sprawdzające działanie wszystkich udostępnianych adresów `url` i metod `HTTP`.


#### Testy:

Stwórz testy:
* `test_add_screening` &ndash; sprawdzający, czy dodawanie nowego seansu działa.
* `test_get_screening_list` &ndash; sprawdzający, czy działa lista wszystkich seansów.
* `test_get_screening_detail` &ndash; sprawdzający, czy szczegółowy widok seansu działa.
* `test_delete_screening` &ndash; sprawdzający usuwanie seansu.
* `test_update_screening` &ndash; sprawdzający, czy aktualizacja seansu działa.


##### Podpowiedzi:
* Do sprawdzania, jak działają nowo powstające widoki używaj testów jednostkowych.
* Umieść je w pliku `tests.py` w katalogu `tests` (aplikacji `showtimes`).
* Nie zapomnij o dekoratorze `@pytest.mark.django_db`, aby móc korzystać z bazy danych.
* Możesz wzorować się na istniejących testach z aplikacji `movielist`.
# Warsztat &ndash; Filtrowanie filmów (zadanie dodatkowe)

Zmodyfikuj serializer dla kina tak, żeby w polu movies przesyłał tylko nazwy filmów, 
które będą grane w ciągu najbliższych 30 dni.

Dodaj test, który sprawdzi nową funkcjonalność.
# Warsztat &ndash; Wyszukiwanie seansów (zadanie dodatkowe)

* Dodaj opcje filtrowania listy seansów po nazwie filmu. Parametry filtrowania będą przekazywane metodą GET, 
    czyli doklejone do adresu url.
* Dodaj filtrowanie po mieście, w którym znajduje się kino.
> Podpowiedź: [https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend)    


Dodaj testy dla nowej funkcjonalności.
---

Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.
