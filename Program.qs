namespace QRandom_bit_generator {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    
    operation randombit() : Int {
        use q = Qubit();
        H(q);
        let res = M(q);
        if res == Zero {                        // Returns Ints to represent Qubit state 
            return 0;
        }
        else {
            return 1;
        }
    }
    @EntryPoint()
    operation main_loop(length : Int) : Int[] {  // Return type Int[] returns Array of Ints
        if length == 0 {
            Message("Enter Required Password Length\n");
            return [0];
        } else {
            let input = length * 8;             // One ASCII character = 8 bits, multiply length of password by 8
            mutable bits = new Int[0];
            for bit in 1..input {
                set bits += [randombit()];      // Creates an Array of Random Bits
            }
            return bits;
        }
    }
}
