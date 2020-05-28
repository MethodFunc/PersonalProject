using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;

namespace Tarkov_randomItems
{

    class Gun_data
    {
        Random r = new Random();
        string[] types = new string[7] { "Assault rifles", "Assault carbines", "Light machine guns", "Submachine guns", "Shotguns", "Designated marksman rifles", "Sniper rifles" , "Pistol"};

        public string guns_type()
        {
          
            int rand = r.Next(0, 6);
            string guns_output = types[rand];

            return guns_output;
        }

        public string guns_kind(string typei)
        {
            string kind_output = "";

            if (typei == types[0])
            {
                string[] Ar = new string[27] { "ADAR 2-15", "AK-101", "AK-102", "AK-103", "AK-104", "AK-105", "AK-74", "AK-74M", "AK-74N", "AKM", "AKMN", "AKMS", "AKMSN", "AKS-74", "AKS-74N", "AKS-74U", "AKS-74UB", "AKS-74UN", "ASh-12", "DT MDR 5.56x45", "DT MDR .308", "HK416A5", "M4A1", "SA-58", "TX-15 DML", "Vepr AKM/VPO-209", "Vepr KM/VPO-136" };
                kind_output = Ar[r.Next(0, Ar.Length)];
            }

            else if (typei == types[1])
            {
                string[] Ac = new string[4] { "AS VAL", "OP-SKS", "SKS", "Vepr Hunter/VPO-101" };
                kind_output = Ac[r.Next(0, Ac.Length)];
            }

            else if (typei == types[2])
            {
                string Lmg = "RPK-16";
                kind_output = Lmg;
            }

            else if (typei == types[3])
            {
                string[] smg = new string[14] { "MP5", "MP5K-N", "MP7A1", "MP7A2", "MP9", "MP9-N", "MPX", "P90", "PP-19-01 Vityaz-SN", "PP-91 \"Klin\"", "PP-91 \"Kedr\"", "PP-91-01 \"Kedr-B\"", "Saiga-9" , "PPSH-41"};
                kind_output = smg[r.Next(0, smg.Length)];
            }

            else if (typei == types[4])
            {
                string[] shotgun = new string[5] { "M870", "MP-133", "MP-153", "Saiga-12", "TOZ-106" };
                kind_output = shotgun[r.Next(0, shotgun.Length)];
            }
            else if (typei == types[5])
            {
                string[] dmr = new string[5] { "M1A", "RSASS", "SR-25", "SVDS", "VSS Vintorez" };
                kind_output = dmr[r.Next(0, dmr.Length)];
            }
            else if (typei == types[6])
            {
                string[] sr = new string[7] { "DVL-10", "M700", "Mosin", "Mosin Inf.", "SV-98", "T-5000", "VPO-215" };
                kind_output = sr[r.Next(0, sr.Length)];
            }
            
            else if (typei == types[7)
           {
               string[] pistol = new string[] {}
           }

            return kind_output;

        }


    }

}
