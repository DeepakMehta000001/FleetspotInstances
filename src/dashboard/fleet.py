import boto3

class FleetSpotInstance(object):
    def __init__(self,aws_access_key,aws_secret_access_key,aws_session_token):
        self.aws_access_key= aws_access_key
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
    def requestSpotFleet(self):
        pass
