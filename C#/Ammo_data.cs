using System;
using System.Collections.Generic;
using System.Text;

namespace Tarkov_randomItems
{
    class Ammo_data
    {
        string[] ammo_type = new string[14] { "5.56x45mm NATO", "7.62x39mm", "5.45x39mm", "12.7x55mm STs-130", "7.62x51mm NATO", ".366 TKM", "9x39mm", "9x19mm Parabellum", "4.6x30mm HK", "5.7x28mm FN", "9x18mm Makarov", "12x70mm", "20x70mm", "7.62x54mmR" };
        string[] smg_cartridges1 = new string[3] {"PP-9 \"Klin\"", "PP-91 \"Kedr\"", "PP-91-01 \"Kedr - B\""}; //9x18mm Makarov
        string[] smg_cartridges2 = new string[7] {"MP5", "MP5K-N", "MPX", "PP-19-01 Vityaz-SN", "Saiga-9", "MP9", "MP9-N"}; //9x19mm Parabellum
        string[] smg_cartridges3 = new string[2] {"MP7A1", "MP7A2"}; //4.6x30mm HK
        string smg_cartridges4 = "P90";    // 5.7x28mm FN

        string[] rifle_cartridges1 = new string[10] {"AK-105", "AK-74", "AK-74M", "AK-74N", "AKS-74", "AKS-74N", "AKS-74U", "AKS-74UB", "AKS-74UN", "RPK-16"};   // 5.45x39mm
        string[] rifle_cartridges2 = new string[7] {"ADAR 2-15", "AK-101", "AK-102", "DT MDR 5.56x45", "HK 416A5", "M4A1", "TX-15 DML"};   // 5.56x45mm NATO
        string[] rifle_cartridges3 = new string[9] {"OP-SKS", "SKS", "AK-103", "AK-104", "AKM", "AKMN", "AKMS", "AKMSN", "Vepr KM/VPO-136"};    // 7.62x39mm
        string[] rifle_cartridges4 = new string[9] {"Vepr Hunter/VPO-101", "SA-58", "DT MDR .308", "M1A", "RSASS", "SR-25", "DVL-10", "M700", "T-5000"};   // 7.62x51mm NATO
        string[] rifle_cartridges5 = new string[4] {"SVDS", "Mosin", "Mosin Inf.", "SV-98"};    // 7.62x54mmR
        string[] rifle_cartridges6 = new string[2] {"AS VAL", "VSS Vintorez"};  // 9x39mm
        string[] rifle_cartridges7 = new string[2] {"Vepr AKM/VPO-209", "VPO-215"}; // .366 TKM
        string rifle_cartridges8 = "ASh-12"; // 12.7x55mm STs-130

        string[] shotgun = new string[] { "M870", "MP-133", "MP-153", "Saiga-12" };  // 12x70mm
        string toz = "toz"; // 12x70mm
        public void ammo_types()
        {
            
        }
    }
}
