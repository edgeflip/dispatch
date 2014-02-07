Paperboy
========

A simple fork of `django.dispatch` for use as a standalone Python library.


Use
---

Paperboy's `dispatch` may be used identically to Django's; they are essentially
the same.

A "signal dispatcher" helps decoupled applications notify each other of events.
A library, for instance, may thereby invoke callables of dependent applications,
without having been programmed for them, and without needing to extend or patch
the library. The *signal* notifies registered *receivers* on behalf of their
sender, via the *dispatcher*.

For example, say we have a pizza delivery library. Its job is only to
communicate with the pizza delivery Internet API; rather than program a single
user notification pipeline, this library's developer wants to send a signal to
subscribed receivers that a pizza has been delivered:

    from dispatch import Signal

    delivered = dispatch.Signal(providing_args=['parlor'])

Upon learning that a pizza has been delivered, the library could then send this
signal:

    class PizzaAPI(object):

        def check(self):
            response = self.get_response()
            if response.status == 'delivered':
                delivered.send(sender=self, parlor=response.parlor)

However, a signal's not much use if no one's around to receive it. Applications
making use of the pizza delivery library may register receivers with the
dispatcher via the signal they intend to receive:

    delivered.connect(popup_window)

or using the `receiver` decorator:

    from dispatch import receiver

    @receiver(delivered)
    def popup_window(sender, parlor, **kws):
        ...

See [Django's documentation](http://docs.djangoproject.com/en/1.6/topics/signals/) for more information.


Configuration
-------------

Paperboy's `dispatch` is ready for use. However, its `Signal`, as in Django,
respects a debugging mode, under which receivers are inspected upon connection.
Paperboy does not supply a configuration framework of its own, but you may
trivially configure it, as in the below examples.

Globally:

    from dispatch import Signal
    Signal.debug = True

By application:

    from dispatch import Signal
    
    class AtariSignal(Signal):

        debug = True

And with increasing sophistication:

    from dispatch import Signal
    from atari.conf import settings
    
    class AtariSignal(Signal):

        @property
        def debug(self):
            return settings.DEBUG


Installation
------------

With an installation tool such as pip:

    pip install Paperboy

From source:

    python setup.py install


Running tests
-------------

Via the setup.py file:

    python setup.py test
