from decimal import Decimal


class BillOfMaterialsService:
    """
    Builds a Bill of Materials (BOM) from the
    RecommendationEngine output.
    """

    VAT_RATE = Decimal("0.075")  # 7.5%

    def __init__(self, recommendation):
        self.recommendation = recommendation

    def _build_item(self, product, quantity):
        """
        Create a BOM item dictionary.
        """

        if not product:
            return None

        unit_price = getattr(product, "price", 0) or 0
        total = Decimal(str(unit_price)) * quantity

        return {
            "product": product,
            "description": str(product),
            "quantity": quantity,
            "unit_price": Decimal(str(unit_price)),
            "total": total,
        }

    def generate(self):

        items = []

        # Solar Panels
        panel = self.recommendation.get("panel")
        panel_qty = self.recommendation.get("panel_quantity", 0)

        item = self._build_item(panel, panel_qty)
        if item:
            items.append(item)

        # Battery
        battery = self.recommendation.get("battery")
        battery_qty = self.recommendation.get("battery_quantity", 1)

        item = self._build_item(battery, battery_qty)
        if item:
            items.append(item)

        # Inverter
        inverter = self.recommendation.get("inverter")

        item = self._build_item(inverter, 1)
        if item:
            items.append(item)

        # Charge Controller
        controller = self.recommendation.get("controller")

        item = self._build_item(controller, 1)
        if item:
            items.append(item)

        subtotal = sum(item["total"] for item in items)

        vat = subtotal * self.VAT_RATE

        grand_total = subtotal + vat

        return {
            "items": items,
            "subtotal": subtotal,
            "vat": vat,
            "grand_total": grand_total,
        }