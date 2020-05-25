import random

class custom_setting:

    armor_type = ['Body Armor', 'Chest rigs Armor']

    weapon_type = ['Assault rifles', 'Assault carbines', 'Light machine guns', 'Submachine guns', 'Shotguns', 'Designated marksman rifles', 'Sniper rifles']
    modding = ['None', 'Scope only', 'Random Modding', 'Full - Vertical', 'Full-Ergo']
    backpacks = ['None', '6SH118 raid backpack', 'Mystery Ranch Blackjack 50 backpack (multicam)', 'SSO "Attack 2" raid backpack', 'Pilgrim tourist backpack', '3V G Paratus 3-Day Operator''s Tactical Backpack', 'LBT-2670 Slim Field Med Pack', 'Oakley Mechanism heavy duty backpack (black)', 'Camelbak Tri-Zip Backpack', 'Ana tactical Beta 2 battle backpack', 'Wartech Berkut VV-102 backpack', 'Scav Backpack', 'Flyye MBSS Backpack', 'Duffle bag', 'Transformer Bag', 'VKBO army bag', 'Tactical sling bag']
    magazine = random.randint(0, 3)
    maps = ['CUSTOMS', 'SHORELINE', 'INTERCHANGE', 'WOODS', 'RESERVE', 'FACTORY']

    def headset_info(helmet):
        headset = ['None', 'ComTac2', 'Soldin', 'Razer', 'GSSh-01', 'Tactical Sport']
        headset_not_support = ['Soft tank crew helmet TSH-4M-L', 'Kolpak-1S riot helmet', 'SHPM Firefighter''s helmet', 'PSH-97 "Djeta" helmet', 'Jack-o''-lantern tactical pumpkin helmet', 'Kiver-M Helmet', 'SSSh-95 Sfera-S (Sphere-S)', 'ZSh-1-2M helmet', 'BNTI LSHZ-2DTM Helmet', 'Maska 1Sch helmet', 'Altyn helmet', 'Vulkan-5 (LShZ-5) heavy helmet']
        headset_enable = headset[random.randint(0, len(headset) - 1)]
        for i in range(len(headset_not_support)):
            if helmet == headset_not_support[i]:
                print("Headset : Not Support")
                break
        else:
            print("Headset : ", headset_enable)


    def helmet_info():
        helmet = ['Soft tank crew helmet TSH-4M-L', 'Kolpak-1S riot helmet', 'SHPM Firefighter''s helmet', 'PSH-97 "Djeta" helmet', 'Jack-o''-lantern tactical pumpkin helmet', 'UNTAR helmet', '6B47 Ratnik-BSh Helmet', 'LZSh light helmet', 'SSh-68 helmet (1968 steel helmet)', 'Kiver-M Helmet', 'DEVTAC Ronin ballistic helmet', 'SSSh-95 Sfera-S (Sphere-S)', 'MSA ACH TC-2001 MICH Series Helmet', 'MSA ACH TC-2002 MICH Series Helmet', 'MSA Gallet TC 800 High Cut combat helmet', 'Highcom Striker ACHHC IIIA helmet', 'ZSh-1-2M helmet', 'Highcom Striker ULACH IIIA helmet', 'Ops-Core Fast MT SUPER HIGH CUT Helmet', 'Crye Precision Airframe Tan',
                  'Team Wendy EXFIL Ballistic Helmet', 'BNTI LSHZ-2DTM Helmet', 'Maska 1Sch helmet', 'Altyn helmet', 'Vulkan-5 (LShZ-5) heavy helmet', 'Kinda cowboy hat', 'Ushanka ear-flap cap', 'Miltec panama hat', '"Door Kicker" Boonie hat', 'Beanie', 'Kotton beanie', 'Army cap', 'Baseball cap',
                  'Ded Moroz hat', 'Santa''s hat', 'Police cap', 'Tactical fleece hat', 'UX PRO Beanie', 'USEC baseball cap', 'BEAR baseball cap', 'USEC baseball cap black', 'BEAR baseball cap black', 'EmerCom cap', 'Pompon hat', 'Bandana', 'Ski hat with holes for eyes']
        helmet_visor_enable = ['LZSh light helmet', 'Kiver-M Helmet', 'MSA Gallet TC 800 High Cut combat helmet', 'ZSh-1-2M helmet', 'Ops-Core Fast MT SUPER HIGH CUT Helmet', 'Crye Precision Airframe Tan', 'Team Wendy EXFIL Ballistic Helmet', 'BNTI LSHZ-2DTM Helmet', 'Maska 1Sch helmet', 'Altyn helmet', 'Vulkan-5 (LShZ-5) heavy helmet']
        visor = [True, 'None']
        cover = [True, 'None']

        helmet_setting = helmet[random.randint(0, len(helmet)-1)]
        print("Helmet : ", helmet_setting)
        for i in range(len(helmet_visor_enable)):
            if helmet_setting == helmet_visor_enable[i]:
                print("Visor : ", visor[random.randint(0, 1)])
                if helmet_setting == 'Crye Precision Airframe Tan':
                    print("Cover : ", cover[random.randint(0, 1)])
                elif (helmet_setting == 'Team Wendy EXFIL Ballistic Helmet' or helmet_setting == 'Ops-Core Fast MT SUPER HIGH CUT Helmet' or helmet_setting == 'LZSh light helmet' or helmet_setting == 'BNTI LSHZ-2DTM Helmet') and visor[random.randint(0, 1)] == 'None':
                    print("Cover : ", cover[random.randint(0, 1)])
                else:
                    print("Cover : Not Support")

        return helmet_setting

    def armor(types):
        chest_rigs_armor = ['None', '6B5-16 Zh -86 "Uley" armored rig', '6B3TM-01M armored rig',
                           '6B5-15 Zh -86 "Uley" armored rig', 'ANA Tactical M2 armored rig',
                           'ANA Tactical M1 armored rig', 'Crye Precision AVS platecarrier',
                           'Ars Arma A18 Skanda plate carrier', 'Wartech TV-110 plate carrier',
                           '5.11 Tactec plate carrier', 'Ars Arma CPC MOD.2 plate carrier']

        body_armor = ['None', 'Module-3M bodyarmor', 'PACA Soft Armor', '6B2 armor (flora)', 'MF-UNTAR armor vest',
                      'Zhuk-3 Press armor', '6B23-1 armor (digital flora pattern)', 'BNTI Kirasa-N armor',
                      'Highcom Trooper TFO armor (multicam)', '6B13 assault armor',
                      '6B23-2 armor (mountain flora pattern)', 'FORT Redut-M body armor', '6B13 M assault armor (tan)',
                      'IOTV Gen4 armor (high mobility kit)',
                      'BNTI Gzhel-K armor', 'IOTV Gen4 armor (assault kit)', 'IOTV Gen4 armor (full protection)',
                      'FORT Redut-T5 body armor', 'LBT 6094A Slick Plate Carrier', 'Zhuk-6a heavy armor',
                      '6B43 Zabralo-Sh 6A Armor']

        chest_rigs = ['None', 'Scav Vest', 'Spiritus Systems Bank Robber Chest Rig', 'SOE Micro Rig',
                     'Wartech gear rig (TV-109, TV-106)', 'UMTBS 6sh112 Scout-Sniper', 'Splav Tarzan M22 Rig',
                     'Haley Strategic D3CRX Chest Harness', 'Triton M43-A Chest Harness',
                     'Blackhawk! Commando Chest Harness', 'BlackRock chest rig', 'Wartech MK3 chest rig (TV-104)',
                     'ANA Tactical Alpha chest rig', 'Velocity Systems Multi-Purpose Patrol Vest',
                     'Belt-A + Belt-B gear rig']

        if types == 'Body Armor':
            size = len(body_armor)
            print("Body Armor : ", body_armor[random.randint(0, size-1)])
            size = len(chest_rigs)
            print("Chest rigs : ", chest_rigs[random.randint(0, size-1)])


        if types == 'Chest rigs Armor':
            size = len(chest_rigs_armor)
            print("Chest rigs Armor : ", chest_rigs_armor[random.randint(0, size - 1)])

    def select_weapon(weapon):
        if weapon == 'Assault rifles':
            w = {1:  "ADAR 2-15", 2: "AK-101", 3: "AK-102", 4: "AK-103", 5: "AK-104", 6: "AK-105", 7: "AK-74", 8: "AK-74M", 9: "AK-74N", 10: "AKM", 11: "AKMN", 12: "AKMS", 13: "AKMSN", 14: "AKS-74", 15: "AKS-74N", 16: "AKS-74U", 17: "AKS-74UB", 18: "AKS-74UN", 19: "ASh-12",20: "DT MDR 5.56x45", 21: "DT MDR .308", 22: "HK416A5", 23: "M4A1", 24: "SA-58", 25: "TX-15 DML", 26: "Vepr AKM/VPO-209", 27: "Vepr KM/VPO-136"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result

        if weapon == 'Assault carbines':
            w = {1: "AS VAL", 2: "OP-SKS", 3: "SKS", 4: "Vepr Hunter/VPO-101"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result

        if weapon == 'Light machine guns':
            w = {0: "RPK-16"}
            result = w[0]
            print("Weapon : ", result)

            return result

        if weapon == 'Submachine guns':
            w = {1: "MP5", 2: "MP5K-N", 3: "MP7A1", 4: "MP7A2", 5: "MP9", 6: "MP9-N", 7: "MPX", 8: "P90",
                 9: "PP-19-01 Vityaz-SN", 10: "PP-9 ""Klin""", 11: "PP-91 ""Kedr""", 12: "PP-91-01 ""Kedr-B""",
                 13: "Saiga-9"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result

        if weapon == 'Shotguns':
            w = {1: "M870", 2: "MP-133", 3: "MP-153", 4: "Saiga-12", 5: "TOZ-106"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result
        if weapon == 'Designated marksman rifles':
            w = {1: "M1A", 2: "RSASS", 3: "SR-25", 4: "SVDS", 5: "VSS Vintorez"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result
        if weapon == 'Sniper rifles':
            w = {1: "DVL-10", 2: "M700", 3: "Mosin", 4: "Mosin Inf.", 5: "SV-98", 6: "T-5000", 7: "VPO-215"}
            size = len(w)
            result = w[random.randint(1, size)]
            print("Weapon : ", result)

            return result

    def ammo_type(weapon):
        ammo_type = {"ADAR 2-15": "5.56x45mm NATO", "AK-101": "5.56x45mm NATO", "AK-102": "5.56x45mm NATO",
                     "AK-103": "7.62x39mm", "AK-104": "7.62x39mm", "AK-105": "5.45x39mm", "AK-74": "5.45x39mm",
                     "AK-74M": "5.45x39mm", "AK-74N": "5.45x39mm", "AKM": "7.62x39mm", "AKMN": "7.62x39mm",
                     "AKMS": "7.62x39mm", "AKMSN": "7.62x39mm", "AKS-74": "5.45x39mm", "AKS-74N": "5.45x39mm",
                     "AKS-74U": "5.45x39mm", "AKS-74UB": "5.45x39mm", "AKS-74UN": "5.45x39mm",
                     "ASh-12": "12.7x55mm STs-130", "DT MDR 5.56x45": "5.56x45mm NATO",
                     "DT MDR .308": "7.62x51mm NATO",
                     "HK 416A5": "5.56x45mm NATO", "M4A1": "5.56x45mm NATO", "SA-58": "7.62x51mm NATO",
                     "TX-15 DML": "5.56x45mm NATO", "Vepr AKM/VPO-209": ".366 TKM", "Vepr KM/VPO-136": "7.62x39mm",
                     "AS VAL": "9x39mm", "OP-SKS": "7.62x39mm", "SKS": "7.62x39mm",
                     "Vepr Hunter/VPO-101": "7.62x51mm NATO", "RPK-16": "5.45x39mm", "MP5": "9x19mm Parabellum",
                     "MP5K-N": "9x19mm Parabellum", "MP7A1": "4.6x30mm HK",
                     "MP7A2": "4.6x30mm HK", "MP9": "9x19mm Parabellum", "MP9-N": "9x19mm Parabellum",
                     "MPX": "9x19mm Parabellum", "P90": "5.7x28mm FN", "PP-19-01 Vityaz-SN": "9x19mm Parabellum",
                     "PP-9 ""Klin""": "9x18mm Makarov", "PP-91 ""Kedr""": "9x18mm Makarov",
                     "PP-91-01 ""Kedr-B""": "9x18mm Makarov", "Saiga-9": "9x19mm Parabellum", "M870": "12x70mm",
                     "MP-133": "12x70mm", "MP-153": "12x70mm", "Saiga-12": "12x70mm",
                     "TOZ-106": "20x70mm", "M1A": "7.62x51mm NATO", "RSASS": "7.62x51mm NATO",
                     "SR-25": "7.62x51mm NATO",
                     "SVDS": "7.62x54mmR",
                     "VSS Vintorez": "9x39mm", "DVL-10": "7.62x51mm NATO", "M700": "7.62x51mm NATO",
                     "Mosin": "7.62x54mmR",
                     "Mosin Inf.": "7.62x54mmR", "SV-98": "7.62x54mmR", "T-5000": "7.62x51mm NATO",
                     "VPO-215": ".366 TKM"}

        ammo = ammo_type[weapon]
        print("Ammo Type : ", ammo)
        return ammo

    def cartridges(weapon):
        smg_cartridges1 = ('PP-9 "Klin"', 'PP-91 "Kedr"', 'PP-91-01 "Kedr-B"')     #9x18mm Makarov
        smg_cartridges2 = ('MP5', 'MP5K-N', 'MPX', 'PP-19-01 Vityaz-SN', 'Saiga-9', 'MP9', 'MP9-N')    #9x19mm Parabellum
        smg_cartridges3 = ('MP7A1', 'MP7A2')   #	4.6x30mm HK
        smg_cartridges4 = 'P90'    # 5.7x28mm FN

        rifle_cartridges1 = ('AK-105', 'AK-74', 'AK-74M', 'AK-74N', 'AKS-74', 'AKS-74N', 'AKS-74U', 'AKS-74UB', 'AKS-74UN', 'RPK-16')   # 5.45x39mm
        rifle_cartridges2 = ('ADAR 2-15', 'AK-101', 'AK-102', 'DT MDR 5.56x45', 'HK 416A5', 'M4A1', 'TX-15 DML')    # 5.56x45mm NATO
        rifle_cartridges3 = ('OP-SKS', 'SKS', 'AK-103', 'AK-104', 'AKM', 'AKMN', 'AKMS', 'AKMSN', 'Vepr KM/VPO-136')    # 7.62x39mm
        rifle_cartridges4 = ('Vepr Hunter/VPO-101', 'SA-58', 'DT MDR .308', 'M1A', 'RSASS', 'SR-25', 'DVL-10', 'M700', 'T-5000')    # 7.62x51mm NATO
        rifle_cartridges5 = ('SVDS', 'Mosin', 'Mosin Inf.', 'SV-98')    # 7.62x54mmR
        rifle_cartridges6 = ('AS VAL', 'VSS Vintorez')  # 9x39mm
        rifle_cartridges7 = ('Vepr AKM/VPO-209', 'VPO-215') # .366 TKM
        rifle_cartridges8 = ('ASh-12') # 12.7x55mm STs-130

        shotgun = ('M870', 'MP-133', 'MP-153', 'Saiga-12')  # 12x70mm
        toz = 'toz' # 12x70mm

        for i in range(len(smg_cartridges1)):
            ammo = ('9x18 mm PM SP8 gzh', '9x18 mm PM SP7 gzh', '9x18 mm PM PSV', '9x18 mm PM 9 P gzh', '9x18 mm PM PSO gzh', '9x18 mm PM PS gs PPO', '9x18 mm PM PRS gs', '9x18 mm PM PPe gzh', '9x18 mm PM PPT gzh', '9x18 mm PM Pst gzh', '9x18 PM mm RG028 gzh', '9x18 mm PM 9 BZT gzh', '9x18 mm PM PBM', '9x18 mm PM PMM')
            if weapon == smg_cartridges1[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(smg_cartridges2)):
            ammo = ('9x19 mm RIP', '9x19 mm PSO gzh', '9x19 mm Luger CCI', '9x19 mm Green Tracer', '9x19 mm Pst gzh', '9x19 mm AP 6.3')
            if weapon == smg_cartridges2[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(smg_cartridges3)):
            ammo = ('4.6x30mm Action SX', '4.6x30mm FMJ SX', '4.6x30mm Subsonic SX', '4.6x30mm AP SX')
            if weapon == smg_cartridges3[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        if weapon == smg_cartridges4:
            ammo = ('5.7x28 mm R37.F', '5.7x28 mm SS198LF', '5.7x28 mm R37.X', '5.7x28 mm SS197SR', '5.7x28 mm L191', '5.7x28 mm SB193', '5.7x28 mm SS190')
            print("Cartiridges : ", ammo[random.randint(0, len(ammo) - 1)])

        for i in range(len(rifle_cartridges1)):
            ammo = ('5.45x39 mm SP', '5.45x39 mm HP', '5.45x39 mm PRS', '5.45x39 mm US S', '5.45x39 mm FMJ', '5.45x39 mm T', '5.45x39 mm PS', '5.45x39 mm PP', '5.45x39 mm BP', '5.45x39 mm BT', '5.45x39 mm BS', '5.45x39 mm 7N39 "Igolnik"')
            if weapon == rifle_cartridges1[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges2)):
            ammo = ('5.56x45 mm Warmage', '5.56x45 mm 55 HP', '5.56x45 mm Mk 255 Mod 0', '5.56x45 mm M856', '5.56x45 mm 55 FMJ', '5.56x45 mm M855', '5.56x45 mm M856A1', '5.56x45 mm M855A1', '5.56x45 mm M995')
            if weapon == rifle_cartridges2[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges3)):
            ammo = ('7.62x39 mm HP', '7.62x39 mm US S', '7.62x39 mm T45M', '7.62x39 mm PS', '7.62x39 mm BP')
            if weapon == rifle_cartridges3[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges4)):
            ammo = ('7.62x51 mm Ultra Nosler', '7.62x51 mm BPZ FMJ', '7.62x51 mm TPZ SP', '7.62x51 mm M80', '7.62x51 mm M62', '7.62x51 mm M61')
            if weapon == rifle_cartridges4[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges5)):
            ammo = ('7.62x54R T-46M', '7.62x54R LPS Gzh', '7.62x54R 7N1 Sniper cartridge', '7.62x54R 7BT1', '7.62x54R SNB', '7.62x54R 7N37')
            if weapon == rifle_cartridges5[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges6)):
            ammo = ('9x39 mm SP-5 S', '9x39 mm SP-6 S', '9x39 mm 7N9 SPP', '9x39 mm 7N12 BP')
            if weapon == rifle_cartridges6[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        for i in range(len(rifle_cartridges7)):
            ammo = ('.366 TKM Geksa', '.366 TKM FMJ', '.366 TKM EKO')
            if weapon == rifle_cartridges7[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break


        if weapon == rifle_cartridges8:
            ammo = ('12.7x55 mm PS12A', '12.7x55 mm PS12', '12.7x55 mm PS12B')
            print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])

        for i in range(len(shotgun)):
            ammo = ('12/70 5.25mm Buckshot', '12/70 8.5 mm "Magnum" Buckshot', '12x70 6.5 mm "Express" Buckshot', '12x70 7mm Buckshot', '12/70 Flechette', '12x70 RIP', '12/70 HP Slug "SuperFormance"', '12/70 Grizzly 40 Slug', '12/70 HP Slug Copper Sabot Premier', '12x70 Led slug', '12/70 Dual Sabot Slug',
'12/70 "Poleva-3" Slug', '12/70 FTX Custom LIte Slug', '12/70 "Poleva-6u" Slug', '12x70 shell with .50 BMG bullet', '12/70 AP-20 Slug')
            if weapon == shotgun[i]:
                print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])
                break

        if weapon == toz:
            ammo = ('20/70 5.6mm Buckshot', '20/70 6.2mm Buckshot', '20x70 7.5mm Buckshot', '20/70 7.3mm Buckshot', '20/70 Devastator Slug', '20/70 Slug "Poleva-3"', '20/70 Star Slug', '20/70 Slug Poleva-6u')
            print("Cartiridges : ", ammo[random.randint(0, len(ammo)-1)])


    def ammo_pcs(weapon_type):
        weapon_Pcs = ['Designated marksman rifles', 'Sniper rifles']
        for i in range(len(weapon_Pcs)):
            if weapon_type == weapon_Pcs[i]:
                ammo_rnd = int(random.randint(0, 180) / 5)
                return ammo_rnd
        else:
            ammo_rnd = int(random.randint(0, 180))
            return ammo_rnd

    def magazine_type():
        type = (1, 2, 45, 10, 20, 30, 40, 45, 50, 100)
        result = type[random.randint(0, len(type)-1)]
        return result
