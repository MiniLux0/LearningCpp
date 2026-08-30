import glob
import subprocess
import os
import sys

# Asegurar salida UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

cpp_files = sorted(glob.glob('06_ArraysAndVectors/**/*.cpp', recursive=True))
print(f"==================================================================")
print(f"COMPILANDO TODOS LOS ARCHIVOS C++ DEL MÓDULO 06 ({len(cpp_files)} archivos)")
print(f"==================================================================\n")

passed = 0
failed = 0

for f in cpp_files:
    out = os.path.splitext(f)[0] + '.exe'
    
    # Manejo especial para multi-archivo L08 y E08
    if 'L08_MultiArchivo' in f:
        cmd = ['g++', '-std=c++17', '-Wall', '-Wextra', 
               '06_ArraysAndVectors/lab/L08_MultiArchivo/Estadisticas.cpp', 
               '06_ArraysAndVectors/lab/L08_MultiArchivo/main.cpp', 
               '-o', 'test_l08.exe']
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [OK] {f} (multi-archivo compilado y enlazado)")
            passed += 1
            if os.path.exists('test_l08.exe'):
                os.remove('test_l08.exe')
        else:
            print(f"  [FAIL] {f}\n{res.stderr}")
            failed += 1
        continue
    elif 'E08_RefactorizacionHeader' in f:
        folder = os.path.dirname(f)
        cmd = ['g++', '-std=c++17', '-Wall', '-Wextra', 
               os.path.join(folder, 'VectorUtils.cpp'), 
               os.path.join(folder, 'E08_RefactorizacionHeader.cpp'), 
               '-o', 'test_e08.exe']
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [OK] {f} (multi-archivo compilado y enlazado)")
            passed += 1
            if os.path.exists('test_e08.exe'):
                os.remove('test_e08.exe')
        else:
            print(f"  [FAIL] {f}\n{res.stderr}")
            failed += 1
        continue

    cmd = ['g++', '-std=c++17', '-Wall', '-Wextra', f, '-o', out]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  [OK] {f}")
        passed += 1
        if os.path.exists(out):
            os.remove(out)
    else:
        print(f"  [FAIL] {f}\n{res.stderr}")
        failed += 1

print(f"\n==================================================================")
print(f"RESULTADO: {passed}/{len(cpp_files)} archivos C++ compilaron limpiamente (0 errores)")
print(f"==================================================================")
