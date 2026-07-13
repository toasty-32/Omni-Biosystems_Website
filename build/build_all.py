#!/usr/bin/env python3
"""Build both language trees: EN at /, ZH at /zh/."""
import sys, pathlib, importlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_pages

for lang in ('en', 'zh'):
    build_pages.LANG = lang
    print(f"\n=== building {lang.upper()} ===")
    for mod in ('pages_a', 'pages_b', 'pages_c'):
        if mod in sys.modules:
            importlib.reload(sys.modules[mod])
        else:
            importlib.import_module(mod)

build_pages.report_missing()
