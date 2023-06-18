from google_auth_oauthlib.flow import Flow

secFile = "C:\\Users\\dylan\\Downloads\\client_secret_199415634341-1i3p36rgi5atq2vf2u645p1kd9ku39fl.apps.googleusercontent.com.json"

flowSession = Flow.from_client_secrets_file(secFile, ["email"])

(x,y) = flowSession.authorization_url()

print(x)
