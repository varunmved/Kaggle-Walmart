import psycopg2
import os
import sys
import urlparse

DATABASE_URL = "postgres://odtcggsjshuzqc:_dcb6-RrKLBvXKVAZ-J38NiSoz@ec2-54-204-5-56.compute-1.amazonaws.com:5432/d95i58bvuk7cle"
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ[DATABASE_URL])

conn = psycopg2.connect(
        database = url.pth[1:],
        user = url.username,
        password = url.password,
        host = url.hostname,
        port = url.port
)


