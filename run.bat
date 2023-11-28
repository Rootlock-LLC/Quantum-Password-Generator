echo off
set count=%1
echo [*] Running Quantum Algorithm
dotnet run --length %1 > bits.txt
echo [*] Converting bits into Ascii
python Qbit-Ascii.py