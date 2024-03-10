# Import required modules
import requests
import boto3
import json  
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "prod/te-app/oauth_token"  # AWS Secret Name
    # Secret ARN: arn:aws:secretsmanager:us-east-2:149674702839:secret:prod/te-app/oauth_token-oNfKo8
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e
    else:
        # Parse the secret value as JSON and return the oauth_token value
        secret_dict = json.loads(get_secret_value_response['SecretString'])
        return secret_dict['oauth_token']

# Retrieve Test Data via API Call to ThousandEyes APIv6
def fetch_thousandeyes_tests():
    oauth_token = get_secret()  # Retrieve the OAuth2 token from AWS Secrets Manager
    api_url = "https://api.thousandeyes.com/v6/tests.json"
    headers = {"Authorization": f"Bearer {oauth_token}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print("successful api call")
        return response.json()
    else:
        print("failed api call")
        return {}

if __name__ == "__main__":
    tests = fetch_thousandeyes_tests()
    print(tests)

#####################################################################################################################
# In order to interact with the ThousandEyes API, obtain an API token.
# Obtaining the API token: https://developer.cisco.com/docs/thousandeyes/v6/#!authentication/obtaining-your-api-token