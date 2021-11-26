import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connstr = sys.argv[1]
dbname = sys.argv[2]

if len(sys.argv) > 3:
    template = sys.argv[3]
else:
    template = None

print('connstr:', connstr)
c = psycopg2.connect(sys.argv[1])
c.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

with c.cursor() as cur:
    if template is None:
        cur.execute(f'create database {dbname}')
    else:
        cur.execute(f'create database {dbname} with template {template}')
