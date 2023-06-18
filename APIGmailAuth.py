from google_auth_oauthlib.flow import Flow

SCFILE="client_secret_199415634341-1i3p36rgi5atq2vf2u645p1kd9ku39fl.apps.googleusercontent.com.json"

flowSession = Flow.from_client_secrets_file(SCFILE, ["https://www.googleapis.com/auth/gmail.send"], redirect_uri = "https://dylanmroe-obscure-goldfish-w6pp65xpq7jc9wjq.github.dev/")

auth_Url,y = flowSession.authorization_url()

print("Please go to this URL: {}".format(auth_Url))
print(y)

#flowSession.fetch_token(authorization_response = y)

#session = flowSession.authorized_session()
