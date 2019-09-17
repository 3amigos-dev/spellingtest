"""Test text plugin."""
from spellingtest import check


class TestCheckFilter(check.PluginTestCase):
    """Check testing spelling filters works."""

    def setup_fs(self):
        """Setup files."""

        good_words = ["yes", "word"]
        self.bad_words1 = ["zxq", "helo", "begn"]
        self.mktemp("test1.txt", "\n".join(self.bad_words1 + good_words), "utf-8")

        config = self.dedent(
            """
            matrix:
            - name: name
              group: group1
              default_encoding: utf-8
              sources:
              - '{temp}/**/test1.txt'
              aspell:
                lang: en
              hunspell:
                d: en_AU
              pipeline: null
            """
        ).format(temp=self.tempdir)
        self.mktemp(".source.yml", config, "utf-8")

    def test_all(self):
        """Test all."""

        self.assert_spellcheck(".source.yml", self.bad_words1)
