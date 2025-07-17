class ExampleRepository:
    def fetch_item(self, item_id: int):
        # Simulate fetching data from a database
        return {"id": item_id, "name": f"Item {item_id}"}