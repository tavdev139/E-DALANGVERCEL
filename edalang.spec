# -*- mode: python ; coding: utf-8 -*-
# ============================================================
# E-DALANG - PyInstaller Spec File
# Build: pyinstaller edalang.spec
# ============================================================

import os
from pathlib import Path

block_cipher = None

# Folder project
project_dir = Path(r"c:\Users\labta\Downloads\e-dalang\Bima_Arjuna_Wayang_FIX43")

# ── Data files yang wajib dibundle ──────────────────────────
added_files = [
    # Assets gambar wayang
    (str(project_dir / "assets"),                "assets"),
    # File audio narasi & dialog
    (str(project_dir / "audio"),                 "audio"),
    # Model MediaPipe hand landmark
    (str(project_dir / "hand_landmarker.task"),  "."),
    # Config & story JSON
    (str(project_dir / "config.json"),           "."),
    (str(project_dir / "story.json"),            "."),
]

a = Analysis(
    [str(project_dir / "main.py")],
    pathex=[str(project_dir)],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        # Pygame & OpenCV
        "pygame",
        "cv2",
        # MediaPipe
        "mediapipe",
        "mediapipe.python",
        "mediapipe.python.solutions",
        "mediapipe.python.solutions.hands",
        # pyserial (untuk Arduino)
        "serial",
        "serial.tools",
        "serial.tools.list_ports",
        # Standard library yang sering luput
        "queue",
        "threading",
        "json",
        "pathlib",
        "math",
        "time",
        "argparse",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Hanya buang modul GUI/test yang tidak terpakai
        "tkinter",
        "unittest",
        "test",
        "doctest",
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="E-DALANG",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,          # kompres binary (hemat ~30%)
    console=False,     # tidak ada jendela terminal hitam
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon="assets/icon.ico",  # Aktifkan jika ada file icon.ico
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="E-DALANG",
)
