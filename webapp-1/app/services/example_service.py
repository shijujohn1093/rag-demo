from app.repositories.example_repository import ExampleRepository

class ExampleService:
    def __init__(self):
        self.repository = ExampleRepository()

    def get_item_details(self, item_id: int):
        # Business logic here
        return self.repository.fetch_item(item_id)