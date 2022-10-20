# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti sąskaitas bankuose.
# Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
# Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
# Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
# Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose
# Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
# Sukurti programą konsolėje, kuri leistų įvesti asmenis, bankus, sąskaitas. 
# Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

from models_asmuo_bankas import engine, Asmuo, Bankas, Saskaita
from sqlalchemy.orm import sessionmaker

session = sessionmaker(engine)()

while True:
    # pagrindinis meniu
    try:
        ivestis = int(input("Meniu:\
            \n 1 ivesti nauja \
            \n 2 perziureti \
            \n 3 pakeisti \
            \n 4 istrinti \
            \n 5 ivesti pajamas/islaidas \
            \n 6 iseiti is programos \
            \nPasirinkite: ")
        )
    except ValueError:
            print("KLAIDA: iveskite skaiciu")
    else:
        if ivestis == 6: 
            break
        elif ivestis == 1:
            # 1 submeniu
            while True:
                print("----Ivedimas----")
                try:
                    ivestis1 = int(input("Meniu:\
                        \n 1 ivesti nauja asmeni \
                        \n 2 ivesti nauja banka  \
                        \n 3 ivesti nauja saskaita  \
                        \n 4 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis1 == 4:
                        break
                    elif ivestis1 == 1:
                        print("----Naujas asmuo----")
                        ivestas_vardas = input("Vardas: ")
                        ivesta_pavarde = input("Pavarde: ")
                        try:
                            ivestas_asmens_kodas = int(input("Asmens kodas: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            ivestas_tel_nr = input("Telefono numeris: ")
                            asmuo = Asmuo(
                                vardas=ivestas_vardas, 
                                pavarde=ivesta_pavarde, 
                                asmens_kodas=ivestas_asmens_kodas, 
                                tel_nr=ivestas_tel_nr
                            )
                            session.add(asmuo)
                            session.commit()
                            print(f"Naujas asmuo {asmuo} sukurtas sekmingai")
                    elif ivestis1 == 2:
                        print("----Naujas bankas----")
                        ivestas_pavadinimas = input("Pavadinimas: ")
                        ivestas_adresas = input("Adresas: ")
                        ivestas_banko_kodas = input("Banko kodas: ")
                        ivestas_swift_kodas = input("SWIFT kodas: ")
                        bankas = Bankas(
                            pavadinimas=ivestas_pavadinimas, 
                            adresas=ivestas_adresas, 
                            banko_kodas=ivestas_banko_kodas, 
                            swift_kodas=ivestas_swift_kodas
                        )
                        session.add(bankas)
                        session.commit()
                        print(f"Naujas bankas {bankas} sukurtas sekmingai")
                    elif ivestis1 == 3:
                        print("----Nauja saskaita----")
                        ivestas_numeris = input("Saskaitos numeris: ")
                        pradinis_balansas = 0
                        print("Pasirinkite saskaitos savininka is siu galimu:")
                        print("(ID, vardas, pavarde, asmens kodas, tel. numeris)")
                        asmenys = session.query(Asmuo).all()
                        for asmuo in asmenys:
                            print(asmuo)
                        try:
                            pasirinktas_asmuo = int(input("Irasykite pasirinkto asmens ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            print("Pasirinkite saskaitos banka is siu galimu:")
                            print("(ID, pavadinimas, adresas, banko kodas, SWIFT kodas)")
                            bankai = session.query(Bankas).all()
                            for bankas in bankai:
                                print(bankas)
                            try:
                                pasirinktas_bankas = int(input("Irasykite pasirinkto banko ID: "))
                            except ValueError:
                                print("KLAIDA: iveskite skaiciu")
                            else:
                                saskaita = Saskaita(
                                    numeris=ivestas_numeris, 
                                    balansas=pradinis_balansas, 
                                    asmuo_id=pasirinktas_asmuo,
                                    bankas_id=pasirinktas_bankas
                                )
                                session.add(saskaita)
                                session.commit()
                                print(f"Nauja saskaita {saskaita} sukurta sekmingai")
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        elif ivestis == 2:
            # antras submeniu
            while True:
                print("----Perziura----")
                try:
                    ivestis2 = int(input("Meniu:\
                        \n 1 perziureti asmenis \
                        \n 2 perziureti bankus  \
                        \n 3 perziureti saskaitas  \
                        \n 4 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis2 == 4:
                        break
                    elif ivestis2 == 1:
                        print("----Asmenys----")
                        print("(ID, vardas, pavarde, asmens kodas, tel. numeris)")
                        asmenys2 = session.query(Asmuo).all()
                        for asmuo in asmenys2:
                            print(asmuo)
                    elif ivestis2 == 2:
                        print("----Bankai----")
                        print("(ID, pavadinimas, adresas, banko kodas, SWIFT kodas)")
                        bankai2 = session.query(Bankas).all()
                        for bankas in bankai2:
                            print(bankas)
                    elif ivestis2 == 3:
                        print("----Saskaitos----")
                        print("(ID, numeris, balansas, asmuo, bankas)")
                        saskaitos2 = session.query(Saskaita).all()
                        for saskaita in saskaitos2:
                            print(saskaita)
        elif ivestis == 3:
            # trecias submeniu
            while True:
                print("----Pakeitimai----")
                try:
                    ivestis3 = int(input("Meniu:\
                        \n 1 koreguoti asmeni \
                        \n 2 koreguoti banka \
                        \n 3 koreguoti saskaita  \
                        \n 4 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis3 == 4:
                        break
                    elif ivestis3 == 1:
                        print("----Asmenys----")
                        print("Pasirinkite, kurio asmens duomenis norite koreguoti, is siu galimu:")
                        print("(ID, vardas, pavarde, asmens kodas, tel. numeris)")
                        asmenys = session.query(Asmuo).all()
                        for asmuo in asmenys:
                            print(asmuo)
                        try:
                            koreguojamas_asmuo_id = int(input("Irasykite koreguojamo asmens ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if koreguojamas_asmuo_id:
                                koreguojamas_asmuo = session.query(Asmuo).get(koreguojamas_asmuo_id)
                                n_vardas = input(f"Vardas ({koreguojamas_asmuo.vardas}): ")
                                n_pavarde = input(f"Pavarde ({koreguojamas_asmuo.pavarde}): ")
                                try:
                                    n_asmens_kodas = int(input(f"Asmens kodas ({koreguojamas_asmuo.asmens_kodas}): "))
                                except ValueError:
                                    print("KLAIDA: asmens kodas turi buti skaicius")
                                else:
                                    n_tel_nr = input(f"Telefono numeris ({koreguojamas_asmuo.tel_nr}): ")
                                if len(n_vardas) > 0:
                                    koreguojamas_asmuo.vardas = n_vardas
                                if len(n_pavarde) > 0:
                                    koreguojamas_asmuo.pavarde = n_pavarde
                                if n_asmens_kodas:
                                    koreguojamas_asmuo.asmens_kodas = n_asmens_kodas   
                                if len(n_tel_nr) > 0:
                                    koreguojamas_asmuo.tel_nr = n_tel_nr
                                session.commit()
                                print(f"Asmuo {koreguojamas_asmuo} atnaujintas sekmingai")
                            else: 
                                print("---Tokio asmens nera---")
                    elif ivestis3 == 2:
                        print("----Bankai----")
                        print("Pasirinkite, kurio banko duomenis norite koreguoti, is siu galimu:")
                        print("(ID, pavadinimas, adresas, banko kodas, SWIFT kodas)")
                        bankai = session.query(Bankas).all()
                        for bankas in bankai:
                            print(bankas)
                        try:
                            koreguojamo_banko_id = int(input("Irasykite koreguojamo banko ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if koreguojamo_banko_id:
                                koreguojamas_bankas = session.query(Asmuo).get(koreguojamo_banko_id)
                                n_pavadinimas = input(f"Pavadinimas ({koreguojamas_bankas.pavadinimas}): ")
                                n_adresas = input(f"Adresas ({koreguojamas_bankas.adresas}): ")
                                try:
                                    n_banko_kodas = int(input(f"Banko kodas ({koreguojamas_bankas.banko_kodas}): "))
                                except ValueError:
                                    print("KLAIDA: banko kodas turi buti skaicius")
                                else:
                                    n_swift_kodas = input(f"SWIFT kodas ({koreguojamas_bankas.swift_kodas}): ")
                                if len(n_pavadinimas) > 0:
                                    koreguojamas_bankas.pavadinimas = n_pavadinimas
                                if len(n_adresas) > 0:
                                    koreguojamas_bankas.adresas = n_adresas
                                if n_banko_kodas:
                                    koreguojamas_bankas.banko_kodas = n_banko_kodas   
                                if len(n_swift_kodas) > 0:
                                    koreguojamas_bankas.swift_kodas = n_swift_kodas
                                session.commit()
                                print(f"Bankas {koreguojamas_bankas} atnaujintas sekmingai")
                            else: 
                                print("---Tokio banko nera---")
                    elif ivestis3 == 3:
                        print("----Saskaitos----")
                        print("Pasirinkite, kurios saskaitos duomenis norite koreguoti, is siu galimu:")
                        print("(ID, numeris, balansas, asmuo ID, bankas ID)")
                        saskaitos = session.query(Saskaita).all()
                        for saskaita in saskaitos:
                            print(saskaita)
                        try:
                            koreguojamos_saskaitos_id = int(input("Irasykite koreguojamos saskaitos ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if koreguojamos_saskaitos_id:
                                koreguojama_saskaita = session.query(Asmuo).get(koreguojamos_saskaitos_id)
                                try:
                                    n_numeris = int(input(f"Saskaitos numeris ({koreguojama_saskaita.numeris}): "))
                                except ValueError:
                                    print("KLAIDA: saskaitos numeris turi buti skaicius")
                                else:
                                    try:
                                        n_balansas = float(input(f"Adresas ({koreguojama_saskaita.adresas}): "))
                                    except ValueError:
                                        print("KLAIDA: balansas turi buti skaicius")
                                    else: 
                                        try:
                                            n_asmuo_id = int(input(f"Banko kodas ({koreguojama_saskaita.asmuo_id}): "))
                                        except ValueError:
                                            print("KLAIDA: banko kodas turi buti skaicius")
                                        else:
                                            n_bankas_id = input(f"SWIFT kodas ({koreguojama_saskaita.bankas_id}): ")
                                if n_numeris:
                                    koreguojama_saskaita.numeris = n_numeris
                                if n_balansas:
                                    koreguojama_saskaita.balansas = n_balansas
                                if n_asmuo_id:
                                    koreguojama_saskaita.asmuo_id = n_asmuo_id   
                                if n_bankas_id:
                                    koreguojama_saskaita.bankasn_bankas_id = n_bankas_id
                            print(f"Saskaita {koreguojama_saskaita} atnaujinta sekmingai")
                        else: 
                            print("---Tokios saskaitos nera---")
            else:
                print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        elif ivestis == 4:
            # ketvirtas submeniu
            while True:
                print("----Trynimas----")
                try:
                    ivestis4 = int(input("Meniu:\
                        \n 1 trinti asmeni \
                        \n 2 trinti banka \
                        \n 3 trinti saskaita  \
                        \n 4 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis4 == 4:
                        break
                    elif ivestis4 == 1:
                        print("----Asmenys----")
                        print("Pasirinkite asmeni is siu galimu:")
                        print("(ID, vardas, pavarde, asmens kodas, tel. numeris)")
                        asmenys = session.query(Asmuo).all()
                        for asmuo in asmenys:
                            print(asmuo)
                        try:
                            trinamas_asmuo_id = int(input("Irasykite trinamo asmens ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if trinamas_asmuo_id:
                                trinamas_asmuo = session.query(Asmuo).get(trinamas_asmuo_id)
                                session.delete(trinamas_asmuo)
                                session.commit()
                                print(f"Asmuo {trinamas_asmuo} istrintas sekmingai")
                            else: 
                                print("---Tokio asmens nera---")
                    elif ivestis4 == 2:
                        print("----Bankai----")
                        print("Pasirinkite banka is siu galimu:")
                        print("(ID, pavadinimas, adresas, banko kodas, SWIFT kodas)")
                        bankai = session.query(Bankas).all()
                        for bankas in bankai:
                            print(bankas)
                        try:
                            trinamas_bankas_id = int(input("Irasykite trinamo banko ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if trinamas_bankas_id:
                                trinamas_bankas = session.query(Bankas).get(trinamas_bankas_id)
                                session.delete(trinamas_bankas)
                                session.commit()
                                print(f"Bankas {trinamas_bankas} istrintas sekmingai")
                            else: 
                                print("---Tokio banko nera---")
                    elif ivestis4 == 3:
                        print("----Saskaitos----")
                        print("Pasirinkite saskaita is siu galimu:")
                        print("(ID, numeris, balansas, asmuo ID, bankas ID)")
                        saskaitos = session.query(Saskaita).all()
                        for saskaita in saskaitos:
                            print(saskaita)
                        try:
                            trinama_saskaita_id = int(input("Irasykite trinamos saskaitos ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            if trinama_saskaita_id:
                                trinama_saskaita = session.query(Saskaita).get(trinama_saskaita_id)
                                session.delete(trinama_saskaita)
                                session.commit()
                                print(f"Saskaita {trinama_saskaita} istrinta sekmingai")
                            else: 
                                print("---Tokios saskaitos nera---")
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        elif ivestis == 5:
            # penktas submeniu
            while True:
                print("----Pajamos/Islaidos----")
                try:
                    ivestis5 = int(input("Meniu:\
                        \n 1 ivesti pajamas \
                        \n 2 ivesti islaidas \
                        \n 3 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis5 == 3:
                        break
                    elif ivestis5 == 1:
                        print("----Pajamu ivedimas----")
                        print("Pasirinkite saskaita is siu galimu:")
                        print("(ID, numeris, balansas, asmuo)")
                        saskaitos = session.query(Saskaita).all()
                        for saskaita in saskaitos:
                            print(saskaita.id, saskaita.numeris, saskaita.asmuo.vardas, saskaita.asmuo.pavarde)
                        try:
                            saskaitos_id = int(input("Irasykite pasirinktos saskaitos ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
                            if pasirinkta_saskaita:
                                try:
                                    pajamu_irasas = float(input("Įveskite pajamas: "))
                                except ValueError:
                                    print("KLAIDA: Pajamos turi buti skaicius")
                                else:
                                    pasirinkta_saskaita.balansas += pajamu_irasas
                                    session.commit()
                                    print('----------------------')
                                    print(f"Pajamos {pajamu_irasas} priskirtos \n{pasirinkta_saskaita.asmuo.vardas} {pasirinkta_saskaita.asmuo.pavarde} saskaitai \n{pasirinkta_saskaita.numeris} sekmingai \nSaskaitos balansas {pasirinkta_saskaita.balansas}")
                            else: 
                                print("---Tokios saskaitos nera---")
                    elif ivestis5 == 2:
                        print("----Islaidu ivedimas----")
                        print("Pasirinkite saskaita is siu galimu:")
                        print("(ID, numeris, balansas, asmuo)")
                        saskaitos = session.query(Saskaita).all()
                        for saskaita in saskaitos:
                            print(saskaita.id, saskaita.numeris, saskaita.asmuo.vardas, saskaita.asmuo.pavarde)
                        try:
                            saskaitos_id = int(input("Irasykite pasirinktos saskaitos ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
                            if pasirinkta_saskaita:
                                try:
                                    islaidu_irasas = float(input("Įveskite islaidas: "))
                                except ValueError:
                                    print("KLAIDA: Islaidos turi buti skaicius")
                                else:
                                    pasirinkta_saskaita.balansas -= islaidu_irasas
                                    session.commit()
                                    print('----------------------')
                                    print(f"Islaidos {islaidu_irasas} priskirtos \n{pasirinkta_saskaita.asmuo.vardas} {pasirinkta_saskaita.asmuo.pavarde} saskaitai \n{pasirinkta_saskaita.numeris} sekmingai \nSaskaitos balansas {pasirinkta_saskaita.balansas}")
                            else: 
                                print("---Tokios saskaitos nera---")
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!")       
        else:
            print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!")

        