import sys
from lxml import etree

from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.html import XmlLexer


input = etree.parse(sys.stdin)
output = etree.tostring(input, pretty_print=True)

print(highlight(output, XmlLexer(), Terminal256Formatter()))
