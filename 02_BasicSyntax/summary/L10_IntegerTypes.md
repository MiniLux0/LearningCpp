L10 – Integer Types

C++ provides several integer types that differ in memory size and value range:

| Type      | Size (Windows/GCC) | Min                  | Max                 |
|-----------|--------------------|----------------------|---------------------|
| short     | 2 bytes            | -32,768              | 32,767              |
| int       | 4 bytes            | -2,147,483,648       | 2,147,483,647       |
| long      | 4 bytes            | -2,147,483,648       | 2,147,483,647       |
| long long | 8 bytes            | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 |

Key points:
- A type with n bytes uses n×8 bits, allowing 2^(n×8) distinct values.
- Signed types split that range between negative and positive values.
- The macros INT_MAX, INT_MIN, SHRT_MAX, LLONG_MAX, etc. (from <climits>)
  give the exact limits for your system at compile time.
- sizeof() is a compile-time operator that returns the byte size of a type
  or variable as a size_t value.