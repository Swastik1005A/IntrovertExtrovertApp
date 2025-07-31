import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SwastikAs7:)",
        database="personality_db"
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO predictions (
            Time_spent_Alone, Stage_fear, Social_event_attendance,
            Going_outside, Drained_after_socializing,
            Friends_circle_size, Post_frequency, Personality
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    sample_data = (5.0, "Yes", 6.0, 5.0, "No", 4.0, 3.0, "Introvert")

    cursor.execute(query, sample_data)
    conn.commit()
    print("✅ Success")

except Exception as e:
    print("❌ Failed:", e)

finally:
    try:
        cursor.close()
        conn.close()
    except:
        pass
