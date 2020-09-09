"""
Test modules for:

spellingtest.__main__
"""

import pytest
from click.testing import CliRunner

from spellingtest.__main__ import main


@pytest.mark.parametrize("args,expected", [([], 0), (["invoke"], 0)])
def test_main(args, expected):
    """
    GIVEN the spellingtest.__main__
    module entry point WHEN calling main THEN the call
    executes successfully.
    """
    # Setup
    runner = CliRunner()
    # Exercise
    result = runner.invoke(main, args)
    # Verify
    assert result.exit_code == expected  # nosec # noqa=S101
