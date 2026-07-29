// ============================================================================
// L09 — Binary Numbers, Bits & Memory Layout
// ============================================================================
// Objective: Understand binary base-2 representation, bits, bytes, and bitwise operations.
// ============================================================================

#include <iostream>
#include <bitset>
#include <cstdint>

using namespace std;

int main() {
    cout << "=== Binary Representation & Bitwise Operations ===\n\n";

    // 1. Decimal vs Binary Representation
    uint8_t number = 11; // 1011 in binary
    cout << "1. Number: " << static_cast<int>(number) << "\n";
    cout << "   Binary Representation (8 bits): " << bitset<8>(number) << "\n\n";

    // 2. Bitwise Operators: AND (&), OR (|), XOR (^)
    uint8_t a = 0b00001100; // 12 in decimal
    uint8_t b = 0b00000101; // 5 in decimal

    cout << "2. Bitwise Operations:\n";
    cout << "   a       = " << bitset<8>(a) << " (" << (int)a << ")\n";
    cout << "   b       = " << bitset<8>(b) << " (" << (int)b << ")\n";
    cout << "   a & b   = " << bitset<8>(a & b) << " (Bitwise AND)\n";
    cout << "   a | b   = " << bitset<8>(a | b) << " (Bitwise OR)\n";
    cout << "   a ^ b   = " << bitset<8>(a ^ b) << " (Bitwise XOR)\n\n";

    // 3. Bit Shifting: Left Shift (<<) and Right Shift (>>)
    cout << "3. Bit Shifting:\n";
    cout << "   a << 1  = " << bitset<8>(a << 1) << " (Multiply by 2 -> " << (a << 1) << ")\n";
    cout << "   a >> 1  = " << bitset<8>(a >> 1) << " (Divide by 2 -> " << (a >> 1) << ")\n";

    return 0;
}