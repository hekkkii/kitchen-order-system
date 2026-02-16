class Material:
    def __init__(self, name, price_per_sqm):
        self.name = name
        self.price_per_sqm = price_per_sqm
    def __str__(self):
        return f"{self.name}: {self.price_per_sqm} руб/м²"
materials = [
    Material("Дуб", 5000),
    Material("Сосна", 2500),
    Material("ЛДСП", 1500)
]
