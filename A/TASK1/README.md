## Zadanie A-1: systemd
* Pobierz z repozytorium skrypt bash 'sqrt_process'.
* Zmodyfikuj 4. linijkę skryptu: wprowadź własną nazawę użytkownika.
* Dodaj uprawnienia do egzekucji skryptu. 
* W katalogu 'Documents' utwórz plik tekstowy 'input.dat' i wprowadź do niego wartość numeryczną w zapisie dziesiętnym (np. "4.000").  
* Utwórz plik serwisu 'sqrt_service.service', którego zadaniem jest uruchomienie skryptu 'sqrt_process'.
* Przenieś plik 'sqrt_service.service' do  katalogu '/etc/systemd/system/'. Zreastartuj systemd i uruchom nowy serwis.
* Zaprezentuj działanie serwisu, wydrukuj w terminalu zawartość pliku 'result.dat' z katalogu 'Documents'.