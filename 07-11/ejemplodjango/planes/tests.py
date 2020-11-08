from django.test import TestCase
from .models import Plan

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            title="Plan S",
            price=10990,
            minutes=50,
            internet=1024
        )

        Plan.objects.create(
            title="Plan M",
            price=14990,
            minutes=80,
            internet=2048
        )

        Plan.objects.create(
            title="Plan L",
            price=18990,
            minutes=120,
            internet=4096
        )

        Plan.objects.create(
            title="Plan XL",
            price=25990,
            minutes=200,
            internet=10000
        )
    
    def test_plan_price(self):
        plan = Plan.objects.get(title="Plan S")
        self.assertEqual(plan.price, 10990)

    def test_assert_equal_generar_descuento(self):
        plan = Plan.objects.get(title="Plan M")
        self.assertEqual(plan.generarDescuento(), 0.4)

    def test_assert_equal_precio_final(self):
        plan = Plan.objects.get(title="Plan L")
        self.assertEqual(plan.calcularPrecioFinal(), 9495)

        plan = Plan.objects.get(title="Plan M")
        self.assertEqual(plan.calcularPrecioFinal(), 8994)
