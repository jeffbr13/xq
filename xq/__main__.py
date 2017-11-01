import argparse
import sys
from typing import Union

from lxml import etree
from lxml.builder import E
from pygments import highlight
from pygments.formatters.other import NullFormatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.html import XmlLexer

from . import NAME, DESCRIPTION, VERSION


def wrap_in_results(elements: [Union[etree._Element, etree._ElementUnicodeResult]]) -> etree._Element:
    results = E.results()
    for el in elements:
        results.append(E.result(el))
    return results


def apply_xpath(infile, xpath_query=None, colorize=False):
    try:
        parsed = etree.parse(infile, etree.XMLParser(remove_blank_text=True))
    except etree.XMLSyntaxError:
        parsed = etree.parse(infile, etree.HTMLParser(remove_blank_text=True))

    if xpath_query:
        matches = parsed.xpath(xpath_query)
        results = wrap_in_results(matches)
        output = etree.tostring(results, pretty_print=True)
    else:
        output = etree.tostring(parsed, pretty_print=True)

    formatter = TerminalFormatter() if colorize else NullFormatter()
    return highlight(output, XmlLexer(), formatter)


def main():
    parser = argparse.ArgumentParser(
        prog=NAME,
        description=DESCRIPTION,
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)
    parser.add_argument(
        'xpath_query', nargs='?', type=str,
        help='XPath query to apply to XML document.'
    )
    parser.add_argument(
        'file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='XML file to process. Defaults to STDIN.',
    )
    args = parser.parse_args()
    sys.stdout.write(apply_xpath(args.file, args.xpath_query, sys.stdout.isatty()))


if __name__ == '__main__':
    main()
