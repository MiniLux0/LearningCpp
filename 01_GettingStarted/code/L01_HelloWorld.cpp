// ============================================================================
// L01 — Welcome to C++ & Your First Program
// ============================================================================
// Objective: Understand the structure of a basic C++ program.
//
// LINE-BY-LINE EXPLANATION FOR BEGINNERS:
// 1. #include <iostream> : Includes the "Input/Output Stream" library.
//                            Required to use 'std::cout' to print text to the screen.
// 2. int main()          : The starting point (entry function) of every C++ program.
// 3. { ... }             : Curly braces mark the beginning and end of code blocks.
// 4. std::cout << "..."  : Sends text inside quotes to the console output.
// 5. return 0;           : Tells the Operating System that the program finished successfully.
// ============================================================================

#include <iostream>

int main() {
    // Print a friendly welcome message to the console
    std::cout << "Hello, World! Welcome to Learning C++.\n";
    std::cout << "This is your very first C++ program running successfully!\n";

    // Return 0 indicates success to the operating system
    return 0;
}
