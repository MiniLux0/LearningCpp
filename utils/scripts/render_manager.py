#!/usr/bin/env python3
"""
===============================================================================
LearningCpp - Motor Central de Renderizado y Auditoría de Animaciones (CLI)
===============================================================================
Uso:
  python utils/scripts/render_manager.py --list
  python utils/scripts/render_manager.py --module 05
  python utils/scripts/render_manager.py --audit
  python utils/scripts/render_manager.py --all
===============================================================================
"""

import os
import sys
import argparse
import glob
import subprocess
import re

# Asegurar compatibilidad de salida UTF-8 en PowerShell / CMD Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANIMATIONS_DIR = os.path.join(REPO_ROOT, "utils", "diagrams", "animations")

def get_all_modules():
    """Retorna los directorios de módulos en utils/diagrams/animations."""
    if not os.path.exists(ANIMATIONS_DIR):
        return []
    return sorted([d for d in os.listdir(ANIMATIONS_DIR) if os.path.isdir(os.path.join(ANIMATIONS_DIR, d))])

def list_animations():
    """Lista todos los scripts de animación y el estado de sus GIFs generados."""
    print("===============================================================================")
    print("                   ESTADO DE ANIMACIONES MANIM (LearningCpp)                   ")
    print("===============================================================================")
    modules = get_all_modules()
    total_scripts = 0
    total_gifs = 0

    for mod in modules:
        mod_anim_dir = os.path.join(ANIMATIONS_DIR, mod)
        mod_asset_dir = os.path.join(REPO_ROOT, mod, "theory", "assets")
        scripts = sorted(glob.glob(os.path.join(mod_anim_dir, "*.py")))
        
        print(f"\n[{mod}] ({len(scripts)} scripts)")
        for s in scripts:
            total_scripts += 1
            s_name = os.path.basename(s)
            
            # Leer el nombre del GIF objetivo en el script
            with open(s, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
            gif_match = re.search(r'["\']([a-zA-Z0-9_]+\.gif)["\']', content)
            gif_name = gif_match.group(1) if gif_match else "unknown.gif"
            
            gif_path = os.path.join(mod_asset_dir, gif_name)
            if os.path.exists(gif_path):
                total_gifs += 1
                size_kb = os.path.getsize(gif_path) / 1024
                status = f"[OK] ({size_kb:>5.1f} KB) -> {gif_name}"
            else:
                status = f"[PENDING]       -> {gif_name}"
                
            print(f"   * {s_name:<34} {status}")

    print("\n-------------------------------------------------------------------------------")
    print(f"Resumen Total: {total_scripts} Scripts detectados | {total_gifs} GIFs renderizados")
    print("===============================================================================")

def render_module(mod_name):
    """Ejecuta todos los scripts .py de un módulo específico."""
    matching_mods = [m for m in get_all_modules() if mod_name in m]
    if not matching_mods:
        print(f"[ERROR] No se encontro ningun modulo que coincida con '{mod_name}'.")
        return

    for mod in matching_mods:
        print(f"\n===============================================================================")
        print(f"RENDERIZANDO MODULO: {mod}")
        print(f"===============================================================================")
        mod_anim_dir = os.path.join(ANIMATIONS_DIR, mod)
        scripts = sorted(glob.glob(os.path.join(mod_anim_dir, "*.py")))
        
        for s in scripts:
            s_name = os.path.basename(s)
            print(f"\n>> Ejecutando: {s_name}...")
            res = subprocess.run([sys.executable, s], cwd=REPO_ROOT)
            if res.returncode != 0:
                print(f"[FALLO] Error al renderizar {s_name}")
            else:
                print(f"[EXITO] Render completado: {s_name}")

def audit_markdown_assets():
    """Audita todos los archivos de teoría para verificar que los GIFs referenciados existan."""
    print("===============================================================================")
    print("                 AUDITORIA DE ACTIVOS MULTIMEDIA (GIFs) EN TEORIA              ")
    print("===============================================================================")
    
    md_files = glob.glob(os.path.join(REPO_ROOT, "**", "theory", "*.md"), recursive=True)
    broken_references = []
    valid_references = 0

    for md in md_files:
        md_dir = os.path.dirname(md)
        with open(md, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Buscar tags img y enlaces markdown a gifs
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+\.gif)["\']', content)
        md_links = re.findall(r'\[[^\]]*\]\(([^)]+\.gif)\)', content)
        all_refs = set(img_srcs + md_links)

        for ref in all_refs:
            full_path = os.path.normpath(os.path.join(md_dir, ref))
            if not os.path.exists(full_path) or os.path.getsize(full_path) == 0:
                broken_references.append((md, ref, full_path))
            else:
                valid_references += 1

    if broken_references:
        print(f"\n[ALERTA] SE ENCONTRARON {len(broken_references)} REFERENCIAS ROTAS:")
        for source, ref, resolved in broken_references:
            rel_src = os.path.relpath(source, REPO_ROOT)
            print(f"   * En {rel_src} -> No existe: '{ref}'")
    else:
        print(f"\n[AUDITORIA EXITOSA] {valid_references} referencias a GIFs verificadas y 100% funcionales.")
    print("===============================================================================")

def main():
    parser = argparse.ArgumentParser(description="LearningCpp - Motor Central de Animaciones")
    parser.add_argument("--list", action="store_true", help="Lista todas las animaciones y estado de sus GIFs")
    parser.add_argument("--module", type=str, help="Renderiza todas las animaciones de un modulo especifico (ej: 05)")
    parser.add_argument("--all", action="store_true", help="Renderiza absolutamente todas las animaciones del curso")
    parser.add_argument("--audit", action="store_true", help="Audita que todos los GIFs incrustados en Markdown existan")

    args = parser.parse_args()

    if args.list:
        list_animations()
    elif args.module:
        render_module(args.module)
    elif args.all:
        for mod in get_all_modules():
            render_module(mod)
    elif args.audit:
        audit_markdown_assets()
    else:
        list_animations()

if __name__ == "__main__":
    main()
