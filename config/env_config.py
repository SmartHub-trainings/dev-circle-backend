from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
DATABASE_URL=os.getenv("DATABASE_URL")
ENVIRONMENT=os.getenv("ENVIRONMENT")

