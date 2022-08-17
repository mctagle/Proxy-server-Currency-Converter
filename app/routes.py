
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

currency_key = os.environ.get("CURRENCY_KEY")

@proxy_bp.route("/convert", methods=["GET"])
def get_exch_rate():
    curr_query = request.args.get("q")
    if not curr_query:
        return {"message": "must provide q parameter (currency)"}

    response = requests.get(
        "https://free.currconv.com/api/v7/convert",
        params={"q": curr_query, "compact": "ultra", "apiKey": currency_key}
    )

    return jsonify(response.json())

