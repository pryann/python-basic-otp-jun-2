def generate_new_id(items: list[dict]) -> int:
    return max(item["id"] for item in items) + 1


def find_item(id: int, items: list[dict]) -> dict | None:
    for item in items:
        if item["id"] == id:
            return item


def create_item(item_payload: dict, items: list[dict]) -> dict:
    items.append({"id": generate_new_id(), **item_payload})
    return items[-1]


def update_item(id: int, item_payload: dict, items: list[dict]) -> dict | None:
    item = find_item(id, items)
    if item is not None:
        item.update(item_payload)
        return item


def remove_item(id: int, items: list[dict]) -> None:
    item = find_item(id, items)
    if item is not None:
        items.remove(item)
