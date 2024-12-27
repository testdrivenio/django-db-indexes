from django.core.management.base import BaseCommand, CommandParser

from pprint import pprint
import json

from product.models import (
    ProductWithCompositeIndex,
    ProductWithSingleIndex,
    ProductWithoutIndex,
)

from django.db.models import Q


class Command(BaseCommand):
    help = "Test select queries with and without indexes"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--table_type",
            type=int,
            default=1,
            help="1: ProductWithoutIndex, 2: ProductWithSingleIndex, 3: ProductWithCompositeIndex",
        )
        parser.add_argument(
            "--category",
            type=str,
            choices=["electronics", "clothing", "home appliances"],
            help="category",
        )

        parser.add_argument(
            "--price",
            type=int,
            help="price",
        )

    def handle(self, *args, **kwargs):
        print("Running tests...")

        table_type = kwargs.get("table_type")
        if table_type < 1 or table_type > 3:
            print("Table type must be between 1 and 3")
            return
        
        if table_type == 1:
            table_model = ProductWithoutIndex
        elif table_type == 2:
            table_model = ProductWithSingleIndex
        else:
            table_model = ProductWithCompositeIndex

        category = kwargs.get("category", None)
        price = kwargs.get("price", None)

        if category and price:
            queryset = table_model.objects.filter(Q(category=category) & Q(price__lte=price))
        elif category:
            queryset = table_model.objects.filter(category=category)
        elif price:
            queryset = table_model.objects.filter(price__lte=price)
        else:
            queryset = table_model.objects.all()

        explain_output = queryset.explain(analyze=True, verbose=True, format="json")
        pprint(json.loads(explain_output))
