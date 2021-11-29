import json
import boto3
import base64
from botocore.exceptions import ClientError
# from app.core.loggin import MyLogger
from configparser import ConfigParser

# logger = MyLogger().get_logger("knit_services")


class SecretManager:

    def __init__(self):
        self.secret_name = "knit_secret_manager"
        self.region_name = "us-east-1"
        self.session = boto3.session.Session()
        self.service_name = "secretsmanager"

    def get_secret_manager_details(self):
        """
        This function is used to get secret manager details.
        :return:
        """
        secret = {}
        client = self.session.client(
            service_name=self.service_name,
            region_name=self.region_name
        )

        # try:
        get_secret_value_response = client.get_secret_value(
            SecretId=self.secret_name
        )
        # except ClientError as e:
        #
        #     if e.response['Error']['Code'] == 'DecryptionFailureException':
        #         # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
        #         # Deal with the exception here, and/or rethrow at your discretion.
        #         raise e
        #     elif e.response['Error']['Code'] == 'InternalServiceErrorException':
        #         # An error occurred on the server side.
        #         # Deal with the exception here, and/or rethrow at your discretion.
        #         logger.error("Found error : {}".format(e.__str__()))
        #         # raise e
        #     elif e.response['Error']['Code'] == 'InvalidParameterException':
        #         # You provided an invalid value for a parameter.
        #         # Deal with the exception here, and/or rethrow at your discretion.
        #         logger.error("Found error : {}".format(e.__str__()))
        #
        #     elif e.response['Error']['Code'] == 'InvalidRequestException':
        #         # You provided a parameter value that is not valid for the current state of the resource.
        #         # Deal with the exception here, and/or rethrow at your discretion.
        #         logger.error("Found error : {}".format(e.__str__()))
        #
        #     elif e.response['Error']['Code'] == 'ResourceNotFoundException':
        #         # We can't find the resource that you asked for.
        #         # Deal with the exception here, and/or rethrow at your discretion.
        #         logger.error("Found error : {}".format(e.__str__()))
        #
        # else:
        #     # Decrypts secret using the associated KMS CMK.
        #     # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            secret = json.loads(secret)
        # else:
        #     decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        #     logger.info("decoded_binary_secret : {}".format(decoded_binary_secret))

        return secret


class AppServices:

    @staticmethod
    def app_response(status_code: int, message: str, data: any = None) -> dict:
        response = {
            "status_code": status_code,
            "message": message,
            "data": data
        }
        return response

    @staticmethod
    def get_config():
        configure = ConfigParser()
        configure.read('config.ini')
        return configure
