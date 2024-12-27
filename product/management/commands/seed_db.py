
from django.core.management.base import BaseCommand
from django.core.management import call_command

from .factory_data import (
    ProductWithCompositeIndexFactory,
    ProductWithSingleIndexFactory,
    ProductWithoutIndexFactory,
)


class Command(BaseCommand):
    help = "Seed the database with dummy data with 3 different categories (electronics, clothing, home appliances)"

    def handle(self, *args, **kwargs):
        print("Seeding data...")
        call_command("flush", "--noinput")

        for category in ["electronics", "clothing", "home appliances"]:
            print(f"Seeding data for category: {category}")
            print("*" * 50)
            print("\nCreating 500,000 records for ProductWithoutIndex")
            ProductWithoutIndexFactory.create_batch(500000, category=category)
            print("#" * 50)
            print("\nCreating 500,000 records for ProductWithSingleIndex")

            ProductWithSingleIndexFactory.create_batch(500000, category=category)
            print("#" * 50)
            print("\nCreating 500,000 records for ProductWithCompositeIndex")
            ProductWithCompositeIndexFactory.create_batch(500000, category=category)
        
            print("#" * 50)
            print("Done")

        print("Data seeded successfully")
