import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    obj_module = inspect.getmodule(obj)
    properties = {
        'is_instance': isinstance(obj, object),
        'doc_string': inspect.getdoc(obj),
        'is_callable': callable(obj),
        'is_iterable': hasattr(obj, '__iter__'),
        'has_attr': lambda attr: hasattr(obj, attr)
    }
    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'properties': properties
    }

    return result


number_info = introspection_info(42)
print(number_info)


class Example:
    def method1(self):
        pass

    def method2(self):
        pass


example_obj = Example()

info = introspection_info(example_obj)
print(info)
