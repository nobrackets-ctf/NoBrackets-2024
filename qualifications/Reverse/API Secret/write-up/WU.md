```
$ docker build -t obfuscated-script-runner .

$ docker run -d --name my_obfuscated_container -v "$(pwd)/dist:/app" obfuscated-script-runner
e19848ced9cbbf2f8f1bc3dee04aaaad7445948f6cf8979b52b340dc2026dfd6

$ docker logs my_obfuscated_container obfuscated-script-runner
Process ID: 1
 * Serving Flask app 'python_secret'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 936-023-080
```

```
$ curl -X GET http://172.17.0.2:8080
{
  "message": "Il faut faire une requete POST avec un payload de type {'password': 'password \u00e0 remplacer'}"
}

$ curl -X POST http://172.17.0.2:8080 -H "Content-Type: application/json" -d '{"password": "remplacer"}'
{
  "message": "Login failed, Pas si facile, n'est t'il pas ? Le bon mot de passe s'il vous plait"
}
```

```
$ docker cp memdump.py my_obfuscated_container:/app/
$ docker exec -it my_obfuscated_container /bin/sh
```

```
# memdump.py
#https://gist.githubusercontent.com/Dbof/b9244cfc607cf2d33438826bee6f5056/raw/aa4b75ddb55a58e2007bf12e17daadb0ebebecba/memdump.py
#! /usr/bin/env python3
import sys
import re

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<process PID>', file=sys.stderr)
        exit(1)

    pid = sys.argv[1]

    # maps contains the mapping of memory of a specific project
    map_file = f"/proc/{pid}/maps"
    mem_file = f"/proc/{pid}/mem"

    # output file
    out_file = f'{pid}.dump'

    # iterate over regions
    with open(map_file, 'r') as map_f, open(mem_file, 'rb', 0) as mem_f, open(out_file, 'wb') as out_f:
        for line in map_f.readlines():  # for each mapped region
            m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
            if m.group(3) == 'r':  # readable region
                start = int(m.group(1), 16)
                end = int(m.group(2), 16)
                mem_f.seek(start)  # seek to region start
                print(hex(start), '-', hex(end))
                try:
                    chunk = mem_f.read(end - start)  # read region contents
                    out_f.write(chunk)  # dump contents to standard output
                except OSError:
                    print(hex(start), '-', hex(end), '[error,skipped]', file=sys.stderr)
                    continue
    print(f'Memory dump saved to {out_file}')
```

```
# ls
memdump.py  pyarmor_runtime_000000  python_secret.py  pytransform
# python memdump.py 1
0x400000 - 0x41f000
0x41f000 - 0x6dd000
0x6dd000 - 0x93f000
0x93f000 - 0x940000
0x940000 - 0xa80000
0xa80000 - 0xac5000
0x26a8000 - 0x2c57000
0x7f24b0426000 - 0x7f24b0428000
0x7f24b0428000 - 0x7f24b042f000
0x7f24b042f000 - 0x7f24b0431000
0x7f24b213a000 - 0x7f24b213c000
0x7f24b213c000 - 0x7f24b213e000
0x7ffe27ec4000 - 0x7ffe27ee6000
0x7ffe27fca000 - 0x7ffe27fce000
0x7ffe27fca000 - 0x7ffe27fce000 [error,skipped]
0x7ffe27fce000 - 0x7ffe27fd0000
Memory dump saved to 1.dump
```

```
$ strings -n 10 1.dump | grep -i VeryObfuscatedpythoncode -C 5
is_argument
_type_check
parameters
MatchOr(pattern* patterns)
after_this_request
VeryObfuscatedpythoncode
pyarmor_runtime.so
PyArmor v8+ runtime module
pyarmor_runtime_000000
<frozen python_secret>
tuloser_tse_eretsym_el
```

```
$ curl -X POST http://172.17.0.2:8080 -H "Content-Type: application/json" -d '{"password": "VeryObfuscatedpythoncode"}'
{
  "message": "NBCTF{13_mystere_reste_entier}"
}
```

Je l'ai trouvé après avoir fait le chall, mais ça peux servir de ressource :
https://medium.com/@liad_levy/reverse-pyarmor-obfuscated-python-script-using-memory-dump-technique-9823b856be7a