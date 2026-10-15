def get_expenses_by_category(cursor, category_id):
    cursor.execute(
        """
    SELECT
        expenses.*,
        categories.name
    FROM expenses
    JOIN categories
        ON expenses.category_id = categories.id
    WHERE expenses.category_id = %s
    order by expenses.id asc
    """,
        (category_id,),
    )
    return cursor.fetchall()


def get_all_expenses(cursor):
    cursor.execute("""
    SELECT
        expenses.*,
        categories.name
    FROM expenses
    JOIN categories
        ON expenses.category_id = categories.id
    order by id asc
    """)
    return cursor.fetchall()


def get_expense(cursor, expense_id):
    cursor.execute(
        """
        SELECT
            expenses.id,
            expenses.title,
            expenses.amount,
            expenses.date,
            categories.name AS category
        FROM expenses
        LEFT JOIN categories
            ON expenses.category_id = categories.id
        WHERE expenses.id = %s
        """,
        (expense_id,),
    )
    return cursor.fetchone()


def add_expense(cursor, title, amount, category_id):
    cursor.execute(
        """
        INSERT INTO expenses (title, amount, category_id)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (title, amount, category_id),
    )

    return cursor.fetchone()[0]


def update_expense(cursor, expense_id, new_amount):
    cursor.execute(
        """
            UPDATE expenses
            SET amount = %s
            WHERE id = %s
            """,
        (new_amount, expense_id),
    )
    return cursor.rowcount > 0


def delete_expense(cursor, expense_id):
    cursor.execute(
        """
            DELETE from expenses
            WHERE id = %s
            """,
        (expense_id,),
    )
    return cursor.rowcount > 0


# ! warning
# * important
# ? question
# todo added some feature
