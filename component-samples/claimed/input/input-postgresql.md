# Input PostgreSQL
This component pulls data from a postgresql database as CSV on a given SQL statement. Parameters like
host, database, user, password and sql need to be set. Please note that data is processed in-memory (pandas) and can't spill on disk (spark) yet. Therefore, the queried data must fit onto main memory (of the POD in case running within KubeFlow context.
