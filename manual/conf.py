# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AggScatVIR'
copyright = '2022, Ryo Tazaki'
author = 'Ryo Tazaki'
release = 'v0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../python/'))

#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon','nbsphinx','sphinx.ext.githubpages']
extensions = ['sphinx.ext.autodoc', 'numpydoc','sphinx.ext.autosummary','nbsphinx','sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','api/modules.rst']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
html_static_path = ['_static']
