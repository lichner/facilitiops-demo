"""Contract checks for the GitHub Pages version of the reference site."""

from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Markup(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.local_hashes = []
        self.frames = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.local_hashes.append(attrs["href"][1:])
        if tag == "iframe":
            self.frames.append(attrs)


class StaticSiteContract(unittest.TestCase):
    def test_pages_are_plain_static_html_without_design_component_runtime(self):
        pages = [ROOT / "ProductLedSlite.dc.html", ROOT / "ExampleEmail.dc.html", ROOT / "PortfolioSummary.dc.html"]
        for page in pages:
            markup = page.read_text()
            with self.subTest(page=page.name):
                self.assertNotRegex(markup, r"(?i)<x-dc\b|<dc-import\b|DCLogic|vendor/react|support\.js")

    def test_outfit_font_stylesheet_is_loaded_from_the_document_head(self):
        for name in ("ProductLedSlite.dc.html", "ExampleEmail.dc.html", "PortfolioSummary.dc.html"):
            markup = (ROOT / name).read_text()
            head = markup.split("</head>", 1)[0]
            with self.subTest(page=name):
                self.assertIn("fonts.googleapis.com/css2?family=Outfit", head)

    def test_landing_page_keeps_all_local_navigation_targets(self):
        markup = Markup()
        markup.feed((ROOT / "ProductLedSlite.dc.html").read_text())
        self.assertTrue(markup.local_hashes)
        self.assertEqual([], sorted(set(markup.local_hashes) - markup.ids))

    def test_landing_page_embeds_both_example_pages(self):
        markup = Markup()
        markup.feed((ROOT / "ProductLedSlite.dc.html").read_text())
        sources = {frame.get("src") for frame in markup.frames}
        self.assertEqual({"./PortfolioSummary.dc.html", "./ExampleEmail.dc.html"}, sources)
        self.assertTrue(all(frame.get("title") for frame in markup.frames))
        for source in sources:
            self.assertTrue((ROOT / source.removeprefix("./")).is_file())

    def test_pages_deploy_at_site_root_with_domain_file(self):
        workflow = ROOT / ".github/workflows/pages.yml"
        self.assertTrue(workflow.is_file())
        self.assertTrue((ROOT / "CNAME").is_file())
        self.assertIn("impex.facilitiops.io", (ROOT / "CNAME").read_text())
        self.assertIn("ProductLedSlite.dc.html", workflow.read_text())
        self.assertIn("index.html", workflow.read_text())

    def test_landing_page_title_and_icons_are_published(self):
        markup = (ROOT / "ProductLedSlite.dc.html").read_text()
        head = markup.split("</head>", 1)[0]
        workflow = (ROOT / ".github/workflows/pages.yml").read_text()
        self.assertIn("<title>FacilitiOps</title>", head)
        for icon in ("favicon.svg", "favicon.ico", "apple-touch-icon.png"):
            with self.subTest(icon=icon):
                self.assertIn(f'href="./{icon}"', head)
                self.assertTrue((ROOT / icon).is_file())
                self.assertIn(icon, workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
