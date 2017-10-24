import sys
from typing import Union

from lxml import etree
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.html import XmlLexer


def to_str(x: Union[etree.Element, str]) -> str:
    try:
        return etree.tounicode(x, pretty_print=True).strip()
    except TypeError:
        return x


query = sys.argv[1] if len(sys.argv) > 1 else None
input = etree.parse(sys.stdin)

if query:
    matches = input.xpath(query)
    output = '\n'.join([to_str(el) for el in matches])
else:
    output = etree.tostring(input, pretty_print=True)

print(highlight(output, XmlLexer(), TerminalFormatter()).strip())
