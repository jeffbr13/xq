import sys

from lxml import etree
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.html import XmlLexer


query = sys.argv[1] if len(sys.argv) > 1 else None
input = etree.parse(sys.stdin)

if query:
    matches = [etree.tostring(el, pretty_print=True) for el in input.xpath(query)]
    output = b'<results>\n' + b''.join(matches) + b'</results>'
else:
    output = etree.tostring(input, pretty_print=True)

print(highlight(output, XmlLexer(), TerminalFormatter()))
