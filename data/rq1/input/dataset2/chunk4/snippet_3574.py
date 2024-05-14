#Source: https://stackoverflow.com/questions/76755756/typeerror-argument-2-must-be-a-connection-cursor-or-none-in-psycopg2
def connect_with_retry(alias):
    """
    Try to establish a database connection with retry.
    :param alias: Alias of the database
    :return: psycopg2.extensions.connection object if successful, otherwise raise exception
    """
    attempt = 1
    retry_count = PGBOUNCER_RETRY_COUNT
    retry_delay = PGBOUNCER_RETRY_DELAY
    conn_string = os.getenv('DATABASE_URL')

    try:
        url_parts = urlparse.urlparse(conn_string)
        username = url_parts.username
        password = url_parts.password
        host = url_parts.hostname
        port = url_parts.port
        database_name = url_parts.path.lstrip('/')
    except Exception as ex:
        logger.error(f"Error parsing database URL: {ex}")
        # Set default values or raise an exception if appropriate
        username = password = host = port = database_name = None

    while True:
        try:
            logger.debug(
                f"Trying to make a connection with database: username - {username}, host - {host}, database_name - {database_name}"
            )
            conn = psycopg2.connect(
                dbname=database_name,
                user=username,
                password=password,
                host=host,
                port=port,
                connect_timeout=retry_delay,
            )
            logger.info(f"Connections details {conn}")
            return conn
        except (psycopg2.OperationalError, psycopg2.DatabaseError) as ex:
            attempt += 1
            if attempt > retry_count:
                logger.info(f"Database connection retry max-limit exceeded")
                raise ConnectionError("Failed to establish a database connection")
            logger.info(
                f"Connection failed, retrying in {retry_delay} seconds... (Attempt {attempt}/{retry_count})"
            )


DATABASES = {}
DATABASES["default"] = dj_database_url.config()
DATABASES["default"]["ENGINE"] = "psqlextra.backend"
DATABASES["default"]["OPTIONS"] = {
    'connection_factory': lambda alias: connect_with_retry("default")
}
POSTGRES_EXTRA_DB_BACKEND_BASE = "core.database_backend"