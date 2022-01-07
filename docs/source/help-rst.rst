Basic reStructured Text (.rst) Guide / Pointers
===============================================

TOP Level HEADING
==================

Referential Hyperlink for any topic/section/anything:
.. _referentialHyperlinks:

Subheadings
------------

General Paragraphs

.. code-block:: console

   (.venv) $ ./CuBot

.. code-block:: <language>

   <TAB> Syntax

Paragraph Styling
------------------

Insert Random Garbage ``Inline Code or emphasized word``  more random text.

Backticks render `italic text` , *Italic in another form*, **Bold Text**, ``"fish"``,
Language Specific Styling Inline Code, :py:func:`CuBot.get_random_ingredients`

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, (default styling is python) 
   except that the indentation is removed.
   Indentation separates normal paragraph from code-blocks.

   It can span multiple lines.

   :: before codeblocks are mandatory

```python
Normal Markdown Style Code-Blocks wont render correctly
```
::

   Unless Indentation is given And ::
      is mandatory

This is a normal text paragraph again.


Python Specific Interpreter Shell Syntax Highlighting and Styling, aka Doctest:

>>> import CuBot
>>> CuBot.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

To get exactly unedited lines same as source:

| These lines are
| broken exactly like in
| the source file.

Use `Link text <https://domain.invalid/>`_ for inline web links.

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

.. _sectionReference:

Section Naming and Referencing
-------------------------------

For more infor on Referencing Sections click here: :ref:`sectionReference`

Images
-------

.. image:: gnu.png
   .. :height: 100px
   .. :width: 200 px
   .. :scale: 50 %
   .. :alt: alternate text
   .. :align: right

MATHEMATICAL Equations
----------------------
LaTex is Supported.

.. math::

   α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

.. note::
   And this is how you can insert NOTE Blocks.

Musch More Directives can be easily Browsed and Implemented as per your Liking. Check them out by going here: `docutils <https://docutils.sourceforge.io/docs/ref/rst/directives.html#math/>`_ and `Sphinx-Docs <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html/>`_