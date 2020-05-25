using System;

namespace Tarkov_randomItems
{
    class Program
    {
        static void Main(string[] args)
        {
            Gun_data gd = new Gun_data();
            Ammo_data ad = new Ammo_data();

            string guns_type = gd.guns_type();
            string guns_kind = gd.guns_kind(guns_type);
            Console.WriteLine(guns_type);
            Console.WriteLine(guns_kind);

            ad.ammo_types();
        }
    }
}
