from sqlalchemy import create_engine, text

# Connection URL matching your docker-compose.yml configuration
DATABASE_URL = "postgresql://postgres:dss150p_pass@localhost:5432/dss150_db"

def verify_connection():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            # Execute required queries
            version_result = connection.execute(text("SELECT version();")).scalar()
            db_result = connection.execute(text("SELECT current_database();")).scalar()
            
            print("--- PostgreSQL Connection Successful! ---")
            print(f"Database Version: {version_result}")
            print(f"Current Database: {db_result}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    verify_connection()
    