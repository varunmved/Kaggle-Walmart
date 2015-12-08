import psycopg2
import os
import sys
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
        database = url.pth[1:],
        user = url.username,
        password = url.password,
        host = url.hostname,
        port = url.port
)



