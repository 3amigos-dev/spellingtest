#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TOP="$(dirname "${BASEDIR}")"

cd "${TOP}"
git checkout -- \
 app/pip/3.4/app/requirements.txt \
 app/spellingtest/check.py \
 app/spellingtest/version.py \
 app/tests/test_check.py \
 NEWS.rst
