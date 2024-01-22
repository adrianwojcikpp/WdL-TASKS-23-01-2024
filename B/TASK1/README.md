## Zadanie B-1: systemd
* Pobierz z repozytorium skrypt bash 'square_process'.
* Zmodyfikuj 4. linijkę skryptu: wprowadź własną nazawę użytkownika.
* Dodaj uprawnienia do egzekucji skryptu. 
* W katalogu 'Documents' utwórz plik tekstowy 'input.dat' i wprowadź do niego wartość numeryczną w zapisie dziesiętnym (np. "2.000").  
* Utwórz plik serwisu 'square_service.service', którego zadaniem jest uruchomienie skryptu 'square_process'.
* Przenieś plik 'square_service.service' do  katalogu '/etc/systemd/system/'. Zreastartuj systemd i uruchom nowy serwis.
* Zaprezentuj działanie serwisu, wydrukuj w terminalu zawartość pliku 'result.dat' z katalogu 'Documents'.