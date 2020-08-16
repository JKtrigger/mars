
import yaml

from flask import Flask
from flask_cors import CORS

from base.application import root
from sub_application_stripe.init_stripe import stripe_balance

app = Flask(__name__)

# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
CORS(app)  # , resources=r'/api/*'


def main_config():
    with open("config.yml", "r") as yml_file:
        return yaml.load(yml_file, Loader=yaml.FullLoader)


@app.route('/')
def _root():
    return root()


@app.route('/stripe')
def _stripe():
    return stripe_balance(main_config()['stripe']['secret'])


if __name__ == '__main__':
    app.run()
