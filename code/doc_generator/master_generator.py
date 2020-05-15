from generators.demo_page import DemoPageGenerator

class MasterGenerator(object):
    generator_classes = {
        'demo-page': DemoPageGenerator,
    }

    def __init__(self):
        # Instantantiate all the generators
        generators = {
        }
        for name, cls in self.generator_classes.items():
            generators[name] = cls()
        self.generators = generators

    def generate_all(self):
        for name, generator in self.generators.items():
            generator.generate()
