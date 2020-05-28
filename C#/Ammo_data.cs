using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Text;

namespace Tarkov_randomItems
{
    class Ammo_data
    {
        //Gun_data gd = new Gun_data();
        Random r = new Random();

        string[] ammo_type = new string[14] { "5.56x45 mm NATO", "7.62x39mm", "5.45x39mm", "12.7x55 mm STs-130", "7.62x51 mm NATO", ".366 TKM", "9x39mm", "9x19 mm Parabellum", "4.6x30 mm HK", "5.7x28 mm FN", "9x18 mm Makarov", "12x70mm", "20x70mm", "7.62x54mmR" };

        string[][] smg_cartridges = new string[][] {
            new string [3] { "PP-91 \"Klin\"", "PP-91 \"Kedr\"", "PP-91-01 \"Kedr-B\"" },      //9x18 mm Makarov
            new string [7] { "MP5", "MP5K-N", "MPX", "PP-19-01 Vityaz-SN", "Saiga-9", "MP9", "MP9-N" },     //9x19 mm Parabellum
            new string [2] { "MP7A1", "MP7A2" },        //4.6x30 mm HK
            new string [1] {"P90"},       // 5.7x28 mm FN
            new string [1] {"PPSH-41"}      //7.62x25 mm Tokarev
        };

        string[][] rifle_cartridges = new string[][]
        {
            new string[10] { "AK-105", "AK-74", "AK-74M", "AK-74N", "AKS-74", "AKS-74N", "AKS-74U", "AKS-74UB", "AKS-74UN", "RPK-16" },   // 5.45x39mm
            new string[7] { "ADAR 2-15", "AK-101", "AK-102", "DT MDR 5.56x45", "HK 416A5", "M4A1", "TX-15 DML" },   // 5.56x45 mm NATO
            new string[9] { "OP-SKS", "SKS", "AK-103", "AK-104", "AKM", "AKMN", "AKMS", "AKMSN", "Vepr KM/VPO-136" },    // 7.62x39mm
            new string[9] { "Vepr Hunter/VPO-101", "SA-58", "DT MDR .308", "M1A", "RSASS", "SR-25", "DVL-10", "M700", "T-5000" },   // 7.62x51 mm NATO
            new string[4] { "SVDS", "Mosin", "Mosin Inf.", "SV-98" },    // 7.62x54mmR
            new string[2] { "AS VAL", "VSS Vintorez" },  // 9x39mm
            new string[2] { "Vepr AKM/VPO-209", "VPO-215" }, // .366 TKM
            new string[1] {"ASh-12"} // 12.7x55 mm STs-130

        };


        string[] shotgun = new string[] { "M870", "MP-133", "MP-153", "Saiga-12" };  // 12x70mm
        string toz = "TOZ-106"; // 20x70mm
        public string ammo_types(string gkind)
        {
            int i = 0;
            int j = 0;
            string ammo_type = "";

            for (j = 0; j < smg_cartridges.Length; j++)
            {
                for (i = 0; i < smg_cartridges[j].Length; i++)
                {
                    if (j == 0 && gkind == smg_cartridges[j][i])
                    {
                        ammo_type = "9x18 mm Makarov";
                    }
                    else if (j == 1 && gkind == smg_cartridges[j][i])
                    {
                        ammo_type = "9x19 mm Parabellum";
                    }
                    else if (j == 2 && gkind == smg_cartridges[j][i])
                    {
                        ammo_type = "9x19 mm Parabellum";
                    }
                    else if (j == 3 && gkind == smg_cartridges[j][i])
                    {
                        ammo_type = "5.7x28 mm FN";
                    }
                    else if (j == 4 && gkind == smg_cartridges[j][i])
                    {
                        ammo_type = "7.62x25 mm Tokarev";
                    }
                }
            }

            for (j = 0; j < rifle_cartridges.Length; j++)
            {
                for (i = 0; i < rifle_cartridges[j].Length; i++)
                {
                    if (j == 0 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "5.45x39mm";
                    }
                    else if (j == 1 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "5.56x45 mm NATO";
                    }
                    else if (j == 2 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "7.62x39mm";
                    }
                    else if (j == 3 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "7.62x51 mm NATO";
                    }
                    else if (j == 4 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "7.62x54mmR";
                    }
                    else if (j == 5 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "9x39mm";
                    }
                    else if (j == 6 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = ".366 TKM";
                    }
                    else if (j == 7 && gkind == rifle_cartridges[j][i])
                    {
                        ammo_type = "12.7x55 mm STs-130";
                    }
                }
            }

            for (i = 0; i < shotgun.Length; i++)
            {
                if (gkind == shotgun[i])
                {
                    ammo_type = "12x70mm";
                }
            }

            if (gkind == toz)
            {
                ammo_type = "20x70mm";
            }

            return ammo_type;
        }

        public string ammo_kinds(string ammo)
        {
            string result = "";
            if (ammo == ammo_type[0])
            {
                string[] ammos = new string[9] { "5.56x45 mm Warmage", "5.56x45 mm 55 HP", "5.56x45 mm Mk 255 Mod 0", "5.56x45 mm M856", "5.56x45 mm 55 FMJ", "5.56x45 mm M855", "5.56x45 mm M856A1", "5.56x45 mm M855A1", "5.56x45 mm M995" };
                result =  ammo_results(ammos);

            }

            if (ammo == ammo_type[1])
            {
                string[] ammos = new string[5] { "7.62x39 mm HP", "7.62x39 mm US", "7.62x39 mm T45M", "7.62x39 mm PS", "7.62x39 mm BP" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[2])
            {
                string[] ammos = new string[12] { "5.45x39 mm SP", "5.45x39 mm HP", "5.45x39 mm PRS", "5.45x39 mm US S", "5.45x39 mm FMJ", "5.45x39 mm T", "5.45x39 mm PS", "5.45x39 mm PP", "5.45x39 mm BP", "5.45x39 mm BT", "5.45x39 mm BS", "5.45x39 mm 7N39 \"Igolnik\"" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[3])
            {
                string[] ammos = new string[3] { "12.7x55 mm PS12A", "12.7x55 mm PS12", "12.7x55 mm PS12B" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[4])
            {
                string[] ammos = new string[6] { "7.62x51 mm Ultra Nosler", "7.62x51 mm BPZ FMJ", "7.62x51 mm TPZ SP", "7.62x51 mm M80", "7.62x51 mm M62", "7.62x51 mm M61" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[5])
            {
                string[] ammos = new string[3] { ".366 TKM Geksa", ".366 TKM FMJ", ".366 TKM EKO" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[6])
            {
                string[] ammos = new string[4] { "9x39 mm SP-5 S", "9x39 mm SP-6 S", "9x39 mm 7N9 SPP", "9x39 mm 7N12 BP" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[7])
            {
                string[] ammos = new string[6] { "9x19 mm RIP", "9x19 mm PSO gzh", "9x19 mm Luger CCI", "9x19 mm Green Tracer", "9x19 mm Pst gzh", "9x19 mm AP 6.3" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[8])
            {
                string[] ammos = new string[4] { "4.6x30mm Action SX", "4.6x30mm FMJ SX", "4.6x30mm Subsonic SX", "4.6x30mm AP SX" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[9])
            {
                string[] ammos = new string[7] { "5.7x28 mm R37.F", "5.7x28 mm SS198LF", "5.7x28 mm R37.X", "5.7x28 mm SS197SR", "5.7x28 mm L191", "5.7x28 mm SB193", "5.7x28 mm SS190" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[10])
            {
                string[] ammos = new string[14] { "9x18 mm PM SP8 gzh", "9x18 mm PM SP7 gzh", "9x18 mm PM PSV", "9x18 mm PM 9 P gzh", "9x18 mm PM PSO gzh", "9x18 mm PM PS gs PPO", "9x18 mm PM PRS gs", "9x18 mm PM PPe gzh", "9x18 mm PM PPT gzh", "9x18 mm PM Pst gzh", "9x18 PM mm RG028 gzh", "9x18 mm PM 9 BZT gzh", "9x18 mm PM PBM", "9x18 mm PM PMM" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[11])
            {
                string[] ammos = new string[16] { "12/70 5.25mm Buckshot", "12/70 8.5 mm \"Magnum\" Buckshot", "12x70 6.5 mm \"Express\" Buckshot", "12x70 7mm Buckshot", "12/70 Flechette", "12x70 RIP", "12/70 HP Slug \"SuperFormance\"", "12/70 Grizzly 40 Slug", "12/70 HP Slug Copper Sabot Premier", "12x70 Led slug", "12/70 Dual Sabot Slug",
"12/70 \"Poleva-3\" Slug", "12/70 FTX Custom LIte Slug", "12/70 \"Poleva-6u\" Slug", "12x70 shell with .50 BMG bullet", "12/70 AP-20 Slug" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[12])
            {
                string[] ammos = new string[8] { "20/70 5.6mm Buckshot", "20/70 6.2mm Buckshot", "20x70 7.5mm Buckshot", "20/70 7.3mm Buckshot", "20/70 Devastator Slug", "20/70 Slug \"Poleva - 3\"", "20/70 Star Slug", "20/70 Slug Poleva-6u" };
                result = ammo_results(ammos);
            }

            if (ammo == ammo_type[13])
            {
                string[] ammos = new string[6] { "7.62x54R T-46M", "7.62x54R LPS Gzh", "7.62x54R 7N1 Sniper cartridge", "7.62x54R 7BT1", "7.62x54R SNB", "7.62x54R 7N37" };
                result = ammo_results(ammos);
            }



            return result;
        }

        string ammo_results(string[] ammo)
        {
            string ammo_result = "";
            ammo_result = ammo[r.Next(0, ammo.Length)];
            return ammo_result;
        }
    }
}

