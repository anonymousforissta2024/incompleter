#Source: https://stackoverflow.com/questions/68492959/attributeerror-nonetype-object-has-no-attribute-fetchall-in-prefect
@task
def sql_run_procs():
    """This is a delete and update..."""
    # Get our logger
    logger = prefect.utilities.logging.get_logger()  # type: ignore

    conn = connect_db(prefect.config.kv.p.prod_db_constring, logger)  ## wrapper around create_engine()

    with conn.connect() as con:
        try:
            r = con.execute(
                f"EXECUTE fs.spETL_MyProc '{prefect.config.kv.p.staging_db_name}'"
            ).fetchall()
            for q in r[0]:
                if q == 1:
                    logger.info(f"Query {q} has failed")
                    raise signals.FAIL()
        except :
            raise SQLAlchemyError("Error in SQL Script")