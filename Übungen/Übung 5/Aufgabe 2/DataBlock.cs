using System;

namespace Aufgabe_2
{
    /// <summary>
    /// A simple struct representing a datablock for usage in a feistel network.
    /// </summary>
    internal struct DataBlock
    {

        /// <summary>
        /// The left part.
        /// </summary>
        /// <value></value>
        internal long Left { get; set; }

        /// <summary>
        /// The right part.
        /// </summary>
        /// <value></value>
        internal long Right { get; set; }


        /// <summary>
        /// Creates a new instance of this struct.
        /// </summary>
        /// <param name="left">The left part.</param>
        /// <param name="right">The right part.</param>
        internal DataBlock(long left, long right)
        {

            Left = left;
            Right = right;

        }

        /// <summary>
        /// Swaps the left and right part of the current datablock.
        /// </summary>
        internal void Swap() 
        {
            long temp = Left;
            Left = Right;
            Right = temp;
        }

        /// <summary>
        /// Returns a representation of this datablock as a string.
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            return string.Format("{0}{1}", Left, Right);
        }
    }
}