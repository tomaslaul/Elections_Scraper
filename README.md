# Elections Scraper

** Třetí projekt do Engeto Online Python Akademie. **

## Popis projektu
Tento skript slouží pro získání dat z oficiálních webovýc stránek [Voleb do Poslanecké sněmovny Parlamentu České republiky konaných ve dnech 20. 10. – 21. 10. 2017](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny použité v tomto skriptu jsou uvedeny v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí a Package installer for Python (PIP).
```
$ pip3 --version
$ pip3 install -r requirements.txt
```

## Spuštění projektu

Pro správné spuštění skriptu je třeba spustit soubor `projekt_3.py` se dvěma povinnými argumenty.

`python projekt_3.py <odkaz-uzemniho-celku> <vysledny-soubor>`

Následně se stáhnou data ze zadaného odkazu a uloží se do souboru s příponou `.csv`.

## Ukázka projektu

Výsledky hlasování pro okres Hradec Králové:

1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201`
2. argument: `vysledky_Hradec_Kralove`

Spuštění programu:

`python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201" "vysledky_Hradec_Kralove"`

Průběh programu:
```
Stahuji data z adresy https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201
Exportuji do souboru vysledky_Hradec_Kralove.csv
Dokončeno.
```

Částečný výstup:
```
code;location;registered;envelopes;valid;...
569828;Babice;165;109;108;7;1;0;4;0;7;19;3;0;0;1;0;6;0;9;36;0;0;2;1;0;0;12;0
569836;Barchov;227;141;140;21;0;0;9;0;5;16;2;0;2;0;0;19;1;4;46;1;0;3;2;1;1;6;1
...
