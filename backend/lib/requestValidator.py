from marshmallow import fields, Schema

class ReqValidator(Schema):
    url = fields.URL(required=True)



if __name__ == "__main__":
    i = {
        "url": "https://github.com/beazt123/GovtechTechAsmt/blob/main/projectLib/request_validation.py"
    }
    i2 = {
        "url": "www.facebook.com"
    }
    i3 = {
        "url": "wfcrevfom"
    }
    v = ReqValidator()
    print(v.load(i))
    print(v.load(i2))
    print(v.load(i3))