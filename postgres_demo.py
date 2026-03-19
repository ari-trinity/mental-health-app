import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_CONFIG = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'MentalHealthApp2026!'
}

def connect_to_db():
    """Connect to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Successfully connected to PostgreSQL database!")
        return conn
    except Exception as e:
        print(f"✗ Error connecting to database: {e}")
        return None

def create_table(conn):
    """Create a sample users table"""
    try:
        cursor = conn.cursor()

        # Drop table if exists (for clean demo)
        cursor.execute("DROP TABLE IF EXISTS users")

        # Create users table
        create_table_query = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("✓ Table 'users' created successfully!")
        cursor.close()
    except Exception as e:
        print(f"✗ Error creating table: {e}")

def insert_fake_data(conn):
    """Insert sample data into users table"""
    try:
        cursor = conn.cursor()

        # Sample data
        users = [
            ('Alice Johnson', 'alice@example.com', 28),
            ('Bob Smith', 'bob@example.com', 34),
            ('Charlie Brown', 'charlie@example.com', 23),
            ('Diana Prince', 'diana@example.com', 31),
            ('Eve Williams', 'eve@example.com', 27)
        ]

        # Insert data
        insert_query = """
        INSERT INTO users (name, email, age)
        VALUES (%s, %s, %s)
        """
        cursor.executemany(insert_query, users)
        conn.commit()
        print(f"✓ Inserted {cursor.rowcount} rows of fake data!")
        cursor.close()
    except Exception as e:
        print(f"✗ Error inserting data: {e}")

def query_data(conn):
    """Query and display data from users table"""
    try:
        cursor = conn.cursor()

        # Query all users
        cursor.execute("SELECT * FROM users ORDER BY id")
        rows = cursor.fetchall()

        print("\n" + "="*70)
        print("USERS TABLE DATA:")
        print("="*70)
        print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Age':<5} {'Created At'}")
        print("-"*70)

        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<25} {row[3]:<5} {row[4]}")

        print("="*70)
        print(f"\nTotal users: {len(rows)}")

        # Additional query - users over 25
        cursor.execute("SELECT name, age FROM users WHERE age > 25 ORDER BY age DESC")
        adults = cursor.fetchall()

        print("\n" + "="*70)
        print("USERS OVER 25:")
        print("="*70)
        for user in adults:
            print(f"  • {user[0]} (Age: {user[1]})")
        print("="*70)

        cursor.close()
    except Exception as e:
        print(f"✗ Error querying data: {e}")

def main():
    """Main function to run the demo"""
    print("\n" + "="*70)
    print("PostgreSQL Connection Demo")
    print("="*70 + "\n")

    # Connect to database
    conn = connect_to_db()
    if not conn:
        return

    # Create table
    create_table(conn)

    # Insert fake data
    insert_fake_data(conn)

    # Query and display data
    query_data(conn)

    # Close connection
    conn.close()
    print("\n✓ Database connection closed.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
