"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Tomáš Laul
email: tomas.laul@me.com
discord: Tomáš#1025
"""


import sys
import csv
from bs4 import BeautifulSoup
import requests


def ziskat_data():
    stranka = requests.get(sys.argv[1])
    return BeautifulSoup(stranka.text, "html.parser")


def ziskat_kody(stranka):
    kody = []
    odkazy = []
    vsechny_odkazy = stranka.find_all("a")
    for odkaz in vsechny_odkazy:
        if odkaz.text.isnumeric() and len(odkaz.text) == 6:
            kody.append(odkaz.text)
            odkazy.append("https://volby.cz/pls/ps2017nss/" + odkaz["href"])
    return kody, odkazy


def sestav_hlavicku(odkaz):
    hlavicka = ["code", "location", "registered", "envelopes", "valid"]
    stranka = requests.get(odkaz)
    parsing = BeautifulSoup(stranka.text, "html.parser")
    for subjekt in parsing.find_all("td")[10::5]:
        if subjekt.text != "-":
            hlavicka.append(subjekt.text)
    return hlavicka


def uzemni_celky(uc_odkaz, uc_kod):
    uzemni_celek = [uc_kod]
    uc_data = requests.get(uc_odkaz)
    uc_data_bs = BeautifulSoup(uc_data.text, "html.parser")
    uzemni_celek.append(str(uc_data_bs.find_all("h3")[2].text).split(":")[1].strip()) # location 
    uzemni_celek.append("".join(str(uc_data_bs.find_all("td")[3].text).split()))  # registered
    uzemni_celek.append("".join(str(uc_data_bs.find_all("td")[4].text).split()))  # envelopes
    uzemni_celek.append("".join(str(uc_data_bs.find_all("td")[7].text).split()))  # valid
    for party in uc_data_bs.find_all("td")[11::5]:
        uzemni_celek.append(party.text)  # subjekt
    return uzemni_celek


def main():
    data = ziskat_data()
    print("Stahuji data z adresy", sys.argv[1])
    kody, odkazy = ziskat_kody(data)
    header = sestav_hlavicku(odkazy[0])
    with open(sys.argv[2] + ".csv", "w", newline="") as file:
        print("Exportuji do souboru", file.name)
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(header)
        for i in range(len(kody)):
            file_writer.writerow(uzemni_celky(odkazy[i], kody[i]))
    print("Dokončeno.")


main()