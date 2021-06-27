import os
from flask import Blueprint, request, redirect
# from flask_sqlalchemy.exc import InvalidRequestError
from ..lib.utils import serverResponse
from ..database import db
from ..models import URL

BACKEND_SERVER_BASE_URL = os.environ.get("BACKEND_SERVER_BASE_URL")

bp = Blueprint('/', __name__)


@bp.route('/shortener', methods=['POST'])
def shorten():
    if request.method == 'POST':
        json = request.json
        url = json.get("url", None)

        if not url:
            return serverResponse(
                None,
                400,
                "No URL submitted"
                )
        hashedURL = hash(url)

        urlData = URL(
            id=hashedURL, 
            originalUrl=url
        )
        # try:
        db.session.add(urlData)
        db.session.commit()
        data = {
            "url": url,
            "url-short": "{BACKEND_SERVER_BASE_URL}/{hashedURL}"
        }
        return serverResponse(
            data, 
            200, 
            "URL has been added to the database"
        )

        # except InvalidRequestError:
        #     return serverResponse(
        #         None,
        #         400,
        #         "URL rejected by database"
        #     )

        # except Exception as e:
        #     print(e)
        #     return serverResponse(
        #         None,
        #         500,
        #         "Unexplained exception"
        #     )

@bp.route('/<int:id>', methods=['GET'])
def goTo(id):
    if request.method == 'GET':
        try:
            url = URL.query.filter_by(id=id)
        except Exception as e:
            return serverResponse(
                None,
                500,
                "Unexplained exception"
            )
        return redirect(url["originalUrl"])

