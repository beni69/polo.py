#!/bin/sh
python -m venv VENV
source VENV/bin/activate
whereis python
pip install -r requirements.txt
