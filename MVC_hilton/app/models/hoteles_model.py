# app/models/product_model.py
def get_hotel_count(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS hotel_count FROM hotel")
        return cursor.fetchone()['hotel_count']
