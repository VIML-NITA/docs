# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CuBot'
copyright = '2022, VIML-NITA Contributors'
author = 'VIML-NITA Contributors'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
#    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
#    'myst_parser', # Markdown Parser (Disabled For Now)
#    'sphinx.ext.todo', # 'TODO:' Tag Parser
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
source_suffix = ['.rst']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env', 'generated', '.vscode', 'README.rst']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
