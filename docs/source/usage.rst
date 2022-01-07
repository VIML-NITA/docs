Usage
=====

.. _installation-1:

Installation
------------

To use CuBot, first install it using pip:

.. code-block:: console

   (.venv) $ pip install CuBot

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``CuBot.get_random_ingredients()`` function:

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``.
Otherwise, :py:func:`CuBot.get_random_ingredients`
will raise an exception.

For example:

>>> import CuBot
>>> CuBot.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

