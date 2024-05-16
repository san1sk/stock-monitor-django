from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Test MongoDB connection'

    def handle(self, *args, **kwargs):
        mongo_uri = settings.DATABASES['default']['CLIENT']['host']
        client = MongoClient(mongo_uri)

        try:
            # Test the connection by listing the database names
            db_names = client.list_database_names()
            self.stdout.write(self.style.SUCCESS(f"MongoDB connection successful. Available databases: {db_names}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to connect to MongoDB: {str(e)}"))
        finally:
            client.close()
