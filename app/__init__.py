import os
from flask import Flask, render_template

app = Flask(__name__)
print("→ URL map:", app.url_map)
print("importing app")
from app import interview