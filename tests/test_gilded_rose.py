from gildedrose import Item


class Test:
    def test_normal_item(self):
        item = normal_item(5, 7)
        item_timeline = run_for_n_days(4, item)

        assert item_qualities(item_timeline) == [6, 5, 4, 3]
        assert item_sell_ins(item_timeline) == [4, 3, 2, 1]

    def test_aged_brie(self):
        item = aged_brie(2, 0)

    def test_sulfuras(self):
        item = sulfuras(10)

    def test_backstage_passes(self):
        item = backstage_pass(15, 20)


def run_for_n_days(days: int, item: Item) -> list[Item]:
    """Run the Gilded Rose for some days with a specific item

    Parameters:
        days (int): the duration of the simulation
        item (Item): the item in the shop

    Returns:
        list[Item]: the evolution of the item each day
    """
    raise NotImplementedError


def item_qualities(items: list[Item]) -> list[int]:
    raise NotImplementedError


def item_sell_ins(items: list[Item]) -> list[int]:
    raise NotImplementedError


def aged_brie(sell_in, quality) -> Item:
    return Item("Aged Brie", sell_in, quality)


def sulfuras(sell_in) -> Item:
    return Item("Sulfuras, Hand of Ragnaros", sell_in, 80)


def backstage_pass(sell_in, quality) -> Item:
    return Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)


def normal_item(sell_in, quality) -> Item:
    return Item("Health Elixir", sell_in, quality)


def conjured_item(sell_in, quality) -> Item:
    return Item("Conjured Mana Cake", sell_in, quality)
