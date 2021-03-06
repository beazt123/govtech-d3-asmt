import os
import hashlib
from flask import Blueprint, request, redirect
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError


from ..lib.requestValidator import ReqValidator
from ..lib.utils import serverResponse
from ..database import db
from ..models import URL

BACKEND_SERVER_BASE_URL = os.environ.get("BACKEND_SERVER_BASE_URL")

bp = Blueprint('/', __name__)



@bp.route('/shortener', methods=['POST'])
def shorten():
    if request.method == 'POST':
        jn = request.get_json()
        try:
            cleanedJson = ReqValidator().load(jn)
        except ValidationError:
            return serverResponse(
                None,
                400,
                "Invalid URL. Check if you have http or https in your URL"
                )
        
        url = cleanedJson["url"]
        hasher = hashlib.md5()
        hasher.update(url.encode('utf-8'))
        hashedURL = hasher.hexdigest()

        urlData = URL(
            id=hashedURL, 
            originalUrl=url
        )
        try:
            db.session.add(urlData)
            db.session.commit()
        except IntegrityError:
            pass
            # url = URL.query.filter_by(id=id)
        # except InvalidRequestError:
        #     return serverResponse(
        #         None,
        #         400,
        #         "URL rejected by database"
        #     )
        data = {
            "url": url,
            "url-short": f"{BACKEND_SERVER_BASE_URL}/{hashedURL}"
        }
        return serverResponse(
            data, 
            200, 
            "URL has been shortened"
        )

        

        # except Exception as e:
        #     print(e)
        #     return serverResponse(
        #         None,
        #         500,
        #         "Unexplained exception"
        #     )

@bp.route('/<string:id>', methods=['GET'])
def goTo(id):
    if request.method == 'GET':
        # try:
        url = URL.query.filter_by(id=id).first()
        print(url)
        print(url.originalUrl)
        # except Exception as e:
        #     return serverResponse(
        #         None,
        #         500,
        #         "Unexplained exception"
        #     )
        return redirect(url.originalUrl)

