from pathlib import Path
p=Path('C:/Users/yuva tpt/OneDrive/Documents/django/absal/.github/workflows/ci.yml')
b=p.read_bytes()
print('len=',len(b))
print('first 12 bytes repr:',repr(b[:12]))
print('first 12 bytes hex:', ' '.join(hex(x) for x in b[:12]))
try:
    print('decoded:', b[:64].decode('utf-8'))
except Exception as e:
    print('decode error:', e)
