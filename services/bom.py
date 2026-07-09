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

            "category": (
                product._meta.verbose_name.title()
                if hasattr(product, "_meta")
                else product.__class__.__name__
            ),
            "manufacturer": (
                str(product.manufacturer)
                if getattr(product, "manufacturer", None)
                else ""
            ),
            "model": getattr(product, "model", ""),
            "description": str(product),
            "specification": self._get_specification(product),
            "quantity": quantity,
            "unit_price": Decimal(str(unit_price)),
            "total": total,

        }

    def _get_specification(self, product):

        if hasattr(product, "wattage"):
            return f"{product.wattage}W"

        if hasattr(product, "capacity_ah"):
            return (
                f"{product.voltage}V / "
                f"{product.capacity_ah}Ah"
            )

        if hasattr(product, "capacity_kva"):
            return f"{product.capacity_kva} kVA"

        if hasattr(product, "current_rating"):
            return (
                f"{product.voltage}V / "
                f"{product.current_rating}A"
            )

        return "-"




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

        item_count = len(items)

        return {
            "items": items,
            "item_count": item_count,
            "subtotal": subtotal,
            "vat": vat,
            "grand_total": grand_total,
        }