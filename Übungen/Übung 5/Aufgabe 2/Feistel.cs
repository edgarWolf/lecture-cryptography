using System;
using System.Linq;
using System.Collections.Generic;

namespace Aufgabe_2
{
    /// <summary>
    /// A class representing a simple implementation of a feistel network.
    /// </summary>
    internal class Feistel 
    {
        /// <summary>
        /// Roundfunctions.
        /// </summary>
        private List<Func<long, long>> _Functions;

        /// <summary>
        /// Creates a new instance of this class.
        /// </summary>
        /// <param name="functions">The roundfunctions.</param>
        internal Feistel(List<Func<long, long>> functions)
        {
            _Functions = functions;
        }

        /// <summary>
        /// Encrypts the given datablock and returns the respective encrypted datablock.
        /// </summary>
        /// <param name="dataBlock">The datablock to encrypt.</param>
        /// <returns></returns>
        internal DataBlock Encrypt(DataBlock dataBlock) 
        {
            foreach (var function in _Functions) 
            {
                long f = function(dataBlock.Right);
                dataBlock.Left = f ^ dataBlock.Left;

                if (function != _Functions.LastOrDefault()) 
                {
                    dataBlock.Swap();
                }
            }

            return dataBlock;
        }

        /// <summary>
        /// Decrypts the given datablock and returns the respective decrypted datablock.
        /// </summary>
        /// <param name="dataBlock">The datablock.</param>
        /// <returns></returns>
        internal DataBlock Decrypt(DataBlock dataBlock) 
        {
            // Traveerse the feistel network in reverse order.
            int nrOfRounds = _Functions.Count;
            for (int i = nrOfRounds - 1; i >= 0; i--)
            {
                long f = _Functions[i](dataBlock.Right);
                dataBlock.Left = f ^ dataBlock.Left;

                if (i > 0) 
                {
                    dataBlock.Swap();
                }
            }

            return dataBlock;
        }

    }
}