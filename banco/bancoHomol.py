import psycopg2

conn = psycopg2.connect(
    dbname="cco_matrix_db",
    user="matrixcargo",
    password="f49247ac-cc6c-4af2-bbea-f1f40668a60d",
    host="localhost",
    port="5432"
)
