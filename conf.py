# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LQCD.eu'
copyright = '2020, Simone Bacchio'
author = 'Simone Bacchio'

# The full version, including alpha/beta/rc tags
release = '0.0.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
#    'sphinxcontrib.bibtex',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_baseurl = 'lqcd.eu'


# -- Options for HTML output -------------------------------------------------

master_doc = 'index'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css?v=%s'%release,
]

exclude_patterns = [
    '__*',
]

html_favicon = '_static/icon.png'

html_sidebars = {
    '**': [
        'about.html',
#        'googlegroups.html',
        'searchbox.html',
        'navigation.html',
    ]
}

html_theme_options = {
    'logo': 'logo.png',
    'fixed_sidebar': False,
    'body_text_align': 'justify',
    'caption_font_size': '14px',
    'page_width': '960px',
    'sidebar_hr': '#004B6B',
    'sidebar_header': '#004B6B',
    'sidebar_list': '#004B6B',
    'sidebar_text': '#004B6B',
#    'gray_1': '#008800',
    'gray_2': '#008800',
    'gray_3': '#008800',
}
