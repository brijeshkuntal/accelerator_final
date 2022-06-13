from injector import Injector


class Mediator:
    handlers = {}
    injector: Injector = None

    def send(self, entity):
        print("entity", entity)
        entity_type = type(entity)
        print(Mediator.handlers, entity_type, dir(entity_type))
        handler = Mediator.injector.get(Mediator.handlers[entity_type])
        result = handler.handle(entity)
        return result

    def send_all(self, entities):
        for entity in entities:
            self.send(entity)

    @staticmethod
    def register_handler(key):
        def wrapper(*args, **kwargs):
            print("key, args", key, args)
            Mediator.handlers[key] = args[0]
            return key
        return wrapper