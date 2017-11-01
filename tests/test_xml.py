import unittest
from io import StringIO
from lxml import etree

from lxml.builder import E

from xq.__main__ import apply_xpath


SAMPLE_XML = """
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
    <channel>
        <atom:link rel="self" type="application/rss+xml" href="http://example.com/rss"/>
        <language>en-gb</language>

        <title>Example RSS feed</title>
        <description>This is a podcast RSS feed</description>
        <itunes:summary>This is a podcast RSS feed</itunes:summary>
        <itunes:image href="http://example.com/rss.png"/>
        <itunes:category text="Music"/>
        <itunes:explicit>yes</itunes:explicit>
        <copyright>Example</copyright>

        <item>
            <guid>http://example.com/rss/1</guid>
            <title>Episode 1</title>
            <description>This is the first podcast episode.</description>
            <itunes:summary>This is the first podcast episode</itunes:summary>
            <pubDate>Wed, 13 Sep 2017 10:49:56 +0000</pubDate>
            <itunes:duration>2:00:00</itunes:duration>
            <enclosure url="http://example.com/rss/1/download" length="287686422" type="audio/mp3"/>
        </item>

        <item>
            <guid>http://example.com/rss/2</guid>
            <title>Episode 2</title>
            <description>This is the second podcast episode.</description>
            <itunes:summary>This is the second podcast episode</itunes:summary>
            <pubDate>Mon, 11 Sep 2017 11:48:21 +0000</pubDate>
            <itunes:duration>1:00:00</itunes:duration>
            <enclosure url="http://example.com/rss/2/download" length="169357320" type="audio/mp3"/>
        </item>

        <item>
            <guid>http://example.com/rss/3</guid>
            <title>Episode 3</title>
            <description>This is the third podcast episode.</description>
            <itunes:summary>This is the third podcast episode</itunes:summary>
            <pubDate>Thu, 24 Aug 2017 00:50:10 +0000</pubDate>
            <itunes:duration>1:03:00</itunes:duration>
            <enclosure url="http://example.com/rss/3/download" length="151042044" type="audio/mp3"/>
        </item>
    </channel>
</rss>
"""


class TestXmlXpathExpressions(unittest.TestCase):

    def setUp(self):
        self.test_input = StringIO(SAMPLE_XML)

    def tearDown(self):
        self.test_input.close()

    def test_extract_elements(self):
        expected_output = etree.tounicode(
            E.results(
                E.result(
                    E.title('Episode 1')
                ),
                E.result(
                    E.title('Episode 2')
                ),
                E.result(
                    E.title('Episode 3')
                ),
            ),
            pretty_print=True
        )
        self.assertEqual(expected_output, apply_xpath(self.test_input, './channel/item/title', colorize=False))

    def test_extract_single_attribute(self):
        expected_output = etree.tounicode(
            E.results(
                E.result('http://example.com/rss/2/download'),
            ),
            pretty_print=True
        )
        self.assertEqual(expected_output, apply_xpath(self.test_input, './channel/item[2]/enclosure/@url', colorize=False))

    def test_extract_text(self):
        expected_output = etree.tounicode(
            E.results(
                E.result('Episode 1'),
                E.result('Episode 2'),
                E.result('Episode 3'),
            ),
            pretty_print=True
        )
        self.assertEqual(expected_output, apply_xpath(self.test_input, './channel/item/title/text()', colorize=False))
