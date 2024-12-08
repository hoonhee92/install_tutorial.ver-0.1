# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'coremaxtech.openstack.guide'
copyright = '2024, coremaxtech'
author = '박훈희'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# conf.py 파일에서 추가 또는 확인할 설정
html_allow_unicode = True  # HTML 특수 문자 및 유니코드를 허용

# -- Options for EPUB output
epub_show_urls = 'footnote'
