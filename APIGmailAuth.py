from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests as GglRequest

SCFILE = "client_secret_199415634341-v2q2jj5e8fp44b6q40pbh6dd2n0jvaff.apps.googleusercontent.com.json"

flowSession = Flow.from_client_secrets_file(SCFILE, ["https://www.googleapis.com/auth/gmail.send"], redirect_uri = "https://github.com/DylanMRoe/mail-bulk-sender")

auth_Url,y = flowSession.authorization_url()

print("Please go to this URL: {}".format(auth_Url))


code = input("Enter the code: ")
flowSession.fetch_token(code=code)

creds = flowSession.credentials

