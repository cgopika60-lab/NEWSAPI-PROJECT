import psycopg2


DB_HOST = "DB_HOST"

DB_NAME = "DB_NAME"

DB_USER = "DB_USER"

DB_PASSWORD = "DB_PASSWORD"

PORT = "PORT"


def upload_to_rds(final_data):

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=PORT
    )

    cur = conn.cursor()

    # ---------------- CREATE TABLE ----------------
    create_table_query = """
    CREATE TABLE IF NOT EXISTS news_data (
        id SERIAL PRIMARY KEY,
        author TEXT,
        published_date TIMESTAMP,
        description TEXT,
        sentiment_score FLOAT
    )
    """

    cur.execute(create_table_query)

    conn.commit()

    # ---------------- INSERT DATA ----------------
    for news in final_data:

        try:

            query = """
            INSERT INTO news_data
            (author, published_date, description, sentiment_score)
            VALUES (%s, %s, %s, %s)
            """

            cur.execute(query, (

                news["author"],
                news["published_date"],
                news["description"],
                news["sentiment_score"]

            ))

            conn.commit()

            cur.execute(
                "SELECT COUNT(*) FROM public.news_data"
            )

            count = cur.fetchone()[0]

            print("CURRENT ROW COUNT:", count)

        except Exception as e:

            print("INSERT ERROR:", e)

            conn.rollback()

    cur.close()

    conn.close()