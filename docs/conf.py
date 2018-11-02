# -*- coding: utf-8 -*-
#
# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'Accern Python'

# The release process is documented at https://xtools.readthedocs.io/en/latest/development.html#releases
# pylint: disable=redefined-builtin
copyright = u'2018, Accern Corp.'
version = '0.1.0'
release = '0.1.0'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# -- HTML theme options for `dotted` style -------------------------------------

html_theme_options = {}

extensions = [
    'sphinx.ext.autosectionlabel',
]
