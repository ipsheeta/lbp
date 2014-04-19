#encoding: utf-8

"""
Desc: A filter to highlight code blocks in html with Pygments and BeautifulSoup.
Usage:  {% load highlight_code %}
        {{ var_with_code|highlight|safe }}
"""
from BeautifulSoup import BeautifulSoup

from django import template
from django.template.defaultfilters import stringfilter

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

register = template.Library()

@register.filter
@stringfilter
def formatCode(html):
    # Pass our text block to beautiful soup
    soup = BeautifulSoup(unicode(html))
    # Find all pre blocks and grab the class we assigned them
    preblocks = soup.findAll('pre')
    for pre in preblocks:
        if pre.has_key('lang'):
            try:
                code = ''.join([unicode(item) for item in pre.contents])
                # Use the class to the correct lexer from Pygments
                lexer = get_lexer_by_name(pre['class'][0])
                formatter = HtmlFormatter(linenos='table')
                code_hl = highlight(code, lexer, formatter)
                pre.contents = [BeautifulSoup(code_hl)]
                pre.name = 'code'
            except:
                raise
    return unicode(soup)