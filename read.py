import sys

import psycopg2


connstr = sys.argv[1]
print('connstr:', connstr)
c = psycopg2.connect(sys.argv[1])
with c.cursor() as cur:
    cur.execute('select * from foo')
    print(cur.fetchall())
