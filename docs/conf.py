# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'EPANET'
copyright = '2020'
author = u'Lewis Rossman \\and Hyoungmin Woo \\and Michael Tryby \\and Feng Shang \\and Terranna Haxton \\and Robert Janke'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '2.2'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    'sphinx.ext.intersphinx',
#    'sphinx.ext.todo',
#    'sphinx.ext.mathjax'
#]
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of all reST source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['A_units.rst', 'B_error_messages.rst', 'C_command_line_EPANET.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'EPANETdoc'


# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',
    'classoptions': ',oneside',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
   'maketitle': r'''       
        \pagenumbering{Roman}
        \begin{titlepage}
            \centering
            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {EPANET 2.2 User Manual}}
            
            \vspace*{10mm} %%% * is used to give space from top
            \textbf{\Large {Lew Rossman}}
            
            \vspace*{1mm} %%% * is used to give space from top
            \textbf{\Large {Hyoungmin Woo}}
            
            \vspace*{1mm} %%% * is used to give space from top
            \textbf{\Large {Michael Tryby}}
            
            \vspace*{1mm} %%% * is used to give space from top
            \textbf{\Large {Feng Shang}}
            
            \vspace*{1mm} %%% * is used to give space from top
            \textbf{\Large {Terranna Haxton}}
            
            \vspace*{1mm} %%% * is used to give space from top
            \textbf{\Large {Robert Janke}}            
        \end{titlepage}
        \setcounter{page}{1}
        \pagenumbering{roman}
        \tableofcontents
        \listoffigures
        \listoftables
        \chapter*{Disclaimer}
          This User Manual is an updated version of the EPANET 2 Users Manual
            (EPA/600/R-00/057) written by Lewis Rossman in 2000. The EPANET 2 software
            was developed by the United States Environmental Protection Agency (EPA).

            EPANET Version 2.2 includes contributions from EPA and individuals outside
            the United States Government. It has been subjected to review by the Office of Research and Development and approved for publication. Approval does not signify that the contents reflect the views of the Agency, nor does mention of trade names or commercial products constitute endorsement or recommendation for use. 

            Execution of any EPANET installation program, and modification to system configuration files must be made at the user's own risk. Neither the U.S. EPA nor the program author(s) can assume responsibility for program modification, content, output, interpretation, or usage.

            EPANET installation programs have been extensively tested and verified. However, as for all complex software, these programs may not be completely free of errors and may not be applicable for all cases. In no event will the U.S. EPA be liable for direct, indirect, special, incidental, or consequential damages arising out of the use of the programs and/or associated documentation.
        \chapter*{ACKNOWLEDGEMENT}
           The U.S. Environmental Protection Agency acknowledges the individuals that 
           assisted with the technical review and beta-testing of the EPANET software and user manual.
        \chapter*{ABBREVIATION}
            \textbf{CAD}: Computer aided design

            \textbf{CV}: Check valve

            \textbf{DDA}: Demand driven analysis

            \textbf{EPA}: Environmental Protection Agency

            \textbf{EPS}: Extended period simulation

            \textbf{FCV}: Flow control valve

            \textbf{FIFO}: First in first out

            \textbf{GGA}: Global gradient algorithm

            \textbf{GIS}: Geographic information system

            \textbf{GPV}: General purpose valve

            \textbf{LIFO}: Last in first out 

            \textbf{PBV}: Pressure breaker valve

            \textbf{PDA}: Pressure driven analysis

            \textbf{PDD}: Pressure driven demand

            \textbf{PRV}: Pressure reducing valve

            \textbf{PSV}: Pressure sustaining valve 

            \textbf{SI}: International System of Units

            \textbf{TCV}: Throttle control valve

            \textbf{THM}: Trihalomethanes

            \textbf{US}: United States

        ''',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index_latex', 'EPANET.tex', 'EPANET USERS MANUAL',
     author, 'manual'),
]

#latex_appendices = ['A_units', 'B_error_messages', 'C_command_line_EPANET']
latex_appendices = ['back_matter']
numfig = True
math_numfig = True

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'EPANET', 'EPANET USERS MANUAL',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'EPANET', 'EPANET USERS MANUAL',
     author, 'EPANET', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
