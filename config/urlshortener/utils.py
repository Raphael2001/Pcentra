'''
Utilities for Shortener
'''
from random import choices

from string import ascii_letters, digits

AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return ''.join([str(elem) for elem in choices(chars, k=7)])


def create_shortened_url(model_instance):
    # creates a new shortened url
    random_code = create_random_code()
    # Gets the model class

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code


print(create_random_code())
