import Tarkov.Random as rnd
import os
import random

def run():

    helmet = rnd.custom_setting.helmet_info()
    a = rnd.custom_setting.headset_info(helmet)
    # print('-' * 80)

    armor_type = rnd.custom_setting.armor_type[random.randint(0, len(rnd.custom_setting.armor_type)-1)]
    print("Armor Type : ", armor_type)
    armors = rnd.custom_setting.armor(armor_type)
    # print('-' * 80)

    weapon_type = rnd.custom_setting.weapon_type[random.randint(0, len(rnd.custom_setting.weapon_type)-1)]
    print("Weapons type : ", weapon_type)
    weapon = rnd.custom_setting.select_weapon(weapon_type)
    print("Modding : ", rnd.custom_setting.modding[random.randint(0, len(rnd.custom_setting.modding)-1)])
    # print('-' * 80)

    ammo_type = rnd.custom_setting.ammo_type(weapon)
    rnd.custom_setting.cartridges(weapon)
    print("Ammo Pcs : ", rnd.custom_setting.ammo_pcs(weapon_type))
    print("Magazine Type : ", rnd.custom_setting.magazine_type())
    print("Magazine Pcs : ", rnd.custom_setting.magazine)
    # print('-' * 80)

    print("Backpacks : ", rnd.custom_setting.backpacks[random.randint(0, len(rnd.custom_setting.backpacks)-1)])
    print("MAPS : ", rnd.custom_setting.maps[random.randint(0, len(rnd.custom_setting.maps) - 1)])
    # print('-' * 80)

if __name__ == '__main__':
    run()
