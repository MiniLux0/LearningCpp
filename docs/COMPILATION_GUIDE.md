# ⚙️ How to Compile & Run C++ Programs

A complete beginner-friendly tutorial explaining how to compile C++ code manually using the GCC compiler (`g++`) and how to use the automated `Makefile` build system.

---

## 🛠️ Method 1: Manual Compilation using GCC (`g++`)

If you want to compile a single `.cpp` file directly from your terminal:

### Step 1: Open Your Terminal
Navigate to the directory containing your `.cpp` file:
```bash
cd 01_GettingStarted/code
```

### Step 2: Run the Compiler Command
Use `g++` with strict, modern flags:
```bash
g++ -std=c++17 -Wall -Wextra L01_HelloWorld.cpp -o L01_HelloWorld.exe
```

#### What Do These Flags Mean?
- `g++`: Invokes the GNU C++ Compiler.
- `-std=c++17`: Tells the compiler to use the ISO C++17 standard.
- `-Wall -Wextra`: Enables helpful compiler warnings to catch bugs early.
- `L01_HelloWorld.cpp`: The source code file you want to compile.
- `-o L01_HelloWorld.exe`: Specifies the output name for your executable binary.

### Step 3: Run Your Program
Execute the compiled binary in your terminal:

- **On Windows (PowerShell / CMD)**:
  ```powershell
  .\L01_HelloWorld.exe
  ```
- **On Linux / macOS**:
  ```bash
  ./L01_HelloWorld
  ```

---

## 🚀 Method 2: Automated Compilation with `Makefile` (Recommended)

In this repository, every `code/` and `exercise/` directory includes an automated `Makefile`. You don't need to type long `g++` commands!

### Step 1: Navigate to the `code/` Folder
```bash
cd 01_GettingStarted/code
```

### Step 2: Run `make` Commands

| Desired Action | Terminal Command | What Happens |
|----------------|------------------|--------------|
| **Compile All Lessons** | `make` | Compiles all `.cpp` files into the `build/` directory |
| **Compile & Run a Lesson** | `make run-L01_HelloWorld` | Compiles `L01_HelloWorld.cpp` and runs it immediately |
| **Compile with Sanitizers** | `make asan` | Compiles with **AddressSanitizer** to detect memory leaks |
| **Clean Output Files** | `make clean` | Removes the `build/` directory |

---

## 💡 Quick Tips for Beginners
- If you see compiler **errors**, read the line number indicated by `g++` (e.g., `L01_HelloWorld.cpp:8:5: error: expected ';'`).
- Always make sure your files are saved before compiling!
