#!/usr/bin/env python3
"""
===============================================================================
LearningCpp - Auditor Automatizado de Módulos y Estándares de Ingeniería
===============================================================================
Uso:
  python utils/scripts/audit_module.py --list
  python utils/scripts/audit_module.py --module 05
  python utils/scripts/audit_module.py --all
===============================================================================
"""

import os
import sys
import glob
import re
import subprocess
import argparse

# Asegurar salida UTF-8 en consolas Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_module_dirs(filter_name=None):
    """Obtiene los directorios de módulos en la raíz (ej: 01_GettingStarted)."""
    pattern = os.path.join(REPO_ROOT, "[0-1][0-9]_*")
    mods = sorted(glob.glob(pattern))
    if filter_name:
        mods = [m for m in mods if filter_name.lower() in os.path.basename(m).lower()]
    return mods

def audit_module(mod_dir):
    """Ejecuta una auditoría completa sobre un módulo individual."""
    mod_name = os.path.basename(mod_dir)
    print(f"\n{'='*80}")
    print(f"🔍 AUDITANDO MÓDULO: {mod_name}")
    print(f"{'='*80}")

    issues = []
    passes = 0

    # -------------------------------------------------------------------------
    # 1. Auditoría de Estructura de Directorios
    # -------------------------------------------------------------------------
    required_dirs = ["theory", "theory/assets", "lab", "lab/demos", "exercise", "summary"]
    for rd in required_dirs:
        p = os.path.join(mod_dir, rd.replace("/", os.sep))
        if not os.path.exists(p):
            issues.append(f"[ESTRUCTURA] Falta la carpeta requerida: '{rd}'")
        else:
            passes += 1

    # -------------------------------------------------------------------------
    # 2. Auditoría de Archivos C++ (.cpp / .h)
    # -------------------------------------------------------------------------
    cpp_files = glob.glob(os.path.join(mod_dir, "**", "*.cpp"), recursive=True) + \
                glob.glob(os.path.join(mod_dir, "**", "*.h"), recursive=True)

    for cpp in cpp_files:
        rel_cpp = os.path.relpath(cpp, REPO_ROOT)
        with open(cpp, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # A. Cero Emojis en código
        if re.search(r'[\U00010000-\U0010ffff]', content):
            issues.append(f"[EMOJI EN C++] Se detectaron emojis en: {rel_cpp}")
        else:
            passes += 1

        # B. Prohibición de using namespace std; global
        if re.search(r'^\s*using\s+namespace\s+std\s*;', content, re.MULTILINE):
            issues.append(f"[VETO STD] 'using namespace std;' global en: {rel_cpp}")
        else:
            passes += 1

        # C. Compilación con g++ (Excluyendo demos y plantillas de ejercicios con errores intencionales)
        is_demo = "demos" in cpp
        is_ex_template = "exercise" in cpp and "solution" not in cpp

        if not is_demo:
            out_bin = os.path.join(os.path.dirname(cpp), "temp_audit_bin.exe")
            cmd = ["g++", "-std=c++17", "-Wall", "-Wextra", cpp, "-o", out_bin]
            res = subprocess.run(cmd, capture_output=True, text=True)
            
            if is_ex_template:
                # Los templates pueden o no compilar según la naturaleza del reto (ej. retos de sintaxis rota)
                pass
            else:
                if res.returncode != 0:
                    issues.append(f"[COMPILACIÓN] Falló g++ en: {rel_cpp}\n   Error: {res.stderr.strip()[:180]}")
                else:
                    passes += 1

            if os.path.exists(out_bin):
                try:
                    os.remove(out_bin)
                except Exception:
                    pass

    # -------------------------------------------------------------------------
    # 3. Auditoría de Ejercicios (Subcarpetas y Estructura)
    # -------------------------------------------------------------------------
    ex_root = os.path.join(mod_dir, "exercise")
    if os.path.exists(ex_root):
        loose_cpp = glob.glob(os.path.join(ex_root, "*.cpp"))
        if loose_cpp:
            for lcpp in loose_cpp:
                issues.append(f"[EJERCICIO SUELTO] Archivo .cpp en la raíz de exercise/: {os.path.basename(lcpp)}")

        ex_folders = [d for d in glob.glob(os.path.join(ex_root, "E*")) if os.path.isdir(d)]
        for ef in ex_folders:
            ef_name = os.path.basename(ef)
            sol_dir = os.path.join(ef, "solution")
            sol_cpp = os.path.join(sol_dir, f"{ef_name}.cpp")
            ex_cpp = os.path.join(ef, f"{ef_name}.cpp")
            ex_readme = os.path.join(ef, "README.md")

            if not os.path.exists(ex_readme):
                issues.append(f"[EJERCICIO] Falta README.md en: {ef_name}")
            if not os.path.exists(ex_cpp):
                issues.append(f"[EJERCICIO] Falta {ef_name}.cpp en: {ef_name}")
            if not os.path.exists(sol_cpp):
                issues.append(f"[EJERCICIO] Falta solution/{ef_name}.cpp en: {ef_name}")

    # -------------------------------------------------------------------------
    # 4. Auditoría de Markdown (.md), Enlaces y Visual Translations
    # -------------------------------------------------------------------------
    md_files = glob.glob(os.path.join(mod_dir, "**", "*.md"), recursive=True)
    footer_pattern = re.compile(r'Maintained by\s*<strong>MiniLux0</strong>\s*·\s*2026', re.IGNORECASE)

    for md in md_files:
        rel_md = os.path.relpath(md, REPO_ROOT)
        with open(md, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # A. Footer oficial
        if not footer_pattern.search(content):
            issues.append(f"[FOOTER FALTANTE] Falta footer de MiniLux0 en: {rel_md}")
        else:
            passes += 1

        # B. Enlaces relativos (404 check)
        md_dir = os.path.dirname(md)
        links = re.findall(r'\[.*?\]\((?!http|#|mailto:)(.*?)\)', content)
        for link in links:
            clean_link = link.split('#')[0]
            if clean_link:
                target = os.path.normpath(os.path.join(md_dir, clean_link))
                if not os.path.exists(target):
                    issues.append(f"[ENLACE ROTO] En {rel_md} -> No existe: '{clean_link}'")
                else:
                    passes += 1

        # C. Incrustación de GIFs y Traducción Visual en Teoría
        if "theory" in md and os.path.basename(md).startswith("L"):
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+\.gif)["\']', content)
            if img_srcs:
                for img in img_srcs:
                    img_path = os.path.normpath(os.path.join(md_dir, img))
                    if not os.path.exists(img_path):
                        issues.append(f"[GIF 404] En {rel_md} -> No existe imagen: '{img}'")
                    else:
                        passes += 1

                # Verificar traducción visual obligatoria
                if "Traducción Visual" not in content and "Traduccion Visual" not in content:
                    issues.append(f"[TRADUCCIÓN VISUAL] Falta la sección 'Traducción Visual' bajo el GIF en: {rel_md}")
                else:
                    passes += 1

    # -------------------------------------------------------------------------
    # Resumen del Módulo
    # -------------------------------------------------------------------------
    if not issues:
        print(f"✅ [100% CONFORME] {mod_name} aprobó todos los chequeos de ingeniería ({passes} verificaciones exitosas).")
        return True
    else:
        print(f"❌ [PENDIENTES DETECTADOS] Se encontraron {len(issues)} discrepancias:")
        for iss in issues:
            print(f"   * {iss}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Auditor Automatizado de Módulos LearningCpp")
    parser.add_argument("--module", type=str, help="Audita un módulo específico (ej: 04, 05, Scope)")
    parser.add_argument("--all", action="store_true", help="Audita todos los módulos del repositorio")
    parser.add_argument("--completed", action="store_true", help="Audita únicamente los módulos actualmente implementados")
    parser.add_argument("--list", action="store_true", help="Lista los módulos disponibles")

    args = parser.parse_args()

    if args.list:
        mods = get_module_dirs()
        print("\nMódulos disponibles en el repositorio:")
        for m in mods:
            print(f"  - {os.path.basename(m)}")
        return

    if args.completed:
        target_mods = [m for m in get_module_dirs() if os.path.exists(os.path.join(m, "lab"))]
    elif args.module:
        target_mods = get_module_dirs(args.module)
    elif args.all:
        target_mods = get_module_dirs()
    else:
        target_mods = []

    if not target_mods:
        print("Uso: python utils/scripts/audit_module.py --module <nombre/numero> | --completed | --all | --list")
        sys.exit(1)

    total_passed = 0
    for m in target_mods:
        if audit_module(m):
            total_passed += 1

    print(f"\n{'='*80}")
    print(f"🏁 RESULTADO GLOBAL: {total_passed}/{len(target_mods)} módulos aprobados.")
    print(f"{'='*80}\n")

    if total_passed < len(target_mods):
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
