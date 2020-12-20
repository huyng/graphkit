# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
import os.path as osp
import subprocess
import sys


def test_README_as_PyPi_landing_page(monkeypatch):
    from docutils import core as dcore

    proj_path = osp.join(osp.dirname(__file__), "..")
    long_desc = subprocess.check_output(
        "python setup.py --long-description".split(), cwd=proj_path
    )
    assert long_desc

    monkeypatch.setattr(sys, "exit", lambda *args: None)
    dcore.publish_string(
        long_desc,
        enable_exit_status=False,
        settings_overrides={  # see `docutils.frontend` for more.
            "halt_level": 2  # 2=WARN, 1=INFO
        },
    )
