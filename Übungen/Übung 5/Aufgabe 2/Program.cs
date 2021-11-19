using System;
using System.Collections.Generic;

namespace Aufgabe_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Feistel feistel = new Feistel(new List<Func<long, long>>() 
            {
                (input => input << 4),
                (input => input >> 2)

            });

            DataBlock datablock = new DataBlock(406124124L, 512123124L);
            Console.WriteLine("Source datablock: " + datablock.ToString());

            DataBlock encrypt = feistel.Encrypt(datablock);
            Console.WriteLine("Encrypted datablock: " + encrypt.ToString());

            DataBlock decrypt = feistel.Decrypt(encrypt);
            Console.WriteLine("Decrypted datablock: " + decrypt.ToString());
            
        }
    }
}
