#!/usr/bin/env python3
import base64, zlib, pathlib
parts=[]
base=pathlib.Path('source/zparts')
for name in sorted(base.glob('z*.txt')):
    parts.append(name.read_text().strip())
data=zlib.decompress(base64.b64decode(''.join(parts)))
pathlib.Path('public').mkdir(exist_ok=True)
pathlib.Path('public/calculator.html').write_bytes(data)
pathlib.Path('source/BakeryTime_Portable_v7.html').write_bytes(data)
pathlib.Path('source/BakeryTime_Calculator_FullPeriod_v7.html').write_bytes(data)
print('OK', len(data), 'bytes written')
