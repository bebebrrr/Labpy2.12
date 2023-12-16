#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tag(tag="h1"):
    def decorator(func):
        def wrapper(string):
            result = func(string)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@tag(tag="div")
def lowercase_string(string):
    return string.lower()

# Вызов декорированной функции
decorated_string = lowercase_string("HELLO")
print(decorated_string)