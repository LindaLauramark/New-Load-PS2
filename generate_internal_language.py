#!/usr/bin/env python3
"""Generate internal English translation files from lng_tmpl/_base.yml."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parent
spec = yaml.safe_load((root / 'lng_tmpl/_base.yml').read_text(encoding='utf-8'))
entries = spec['gui_strings']
labels = [entry['label'] for entry in entries]
if len(labels) != len(set(labels)):
    raise SystemExit('Duplicate language labels')

def quote_c(value):
    text = str(value).replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')
    return '"' + text + '"'

header = ['/* Generated from lng_tmpl/_base.yml. Do not edit manually. */', '#ifndef NEWLOAD_LANG_AUTOGEN_H', '#define NEWLOAD_LANG_AUTOGEN_H', 'enum _STR_IDS {']
header += [f'    _STR_{label},' for label in labels]
header += ['    LANG_STR_COUNT', '};', '#endif', '']
source = ['/* Generated from lng_tmpl/_base.yml. Do not edit manually. */', '#include "include/lang.h"', 'char *internalEnglish[LANG_STR_COUNT] = {']
source += [f'    [{"_STR_" + entry["label"]}] = {quote_c(entry.get("string", ""))},' for entry in entries]
source += ['};', '']
(root / 'include/lang_autogen.h').write_text('\n'.join(header), encoding='utf-8')
(root / 'src/lang_internal.c').write_text('\n'.join(source), encoding='utf-8')
print(f'Generated {len(entries)} language entries')
