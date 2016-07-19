#server = "192.168.40.22:8080"
#server = "192.168.245.161:8081"
#server = "127.0.0.1:8000"
server = "symportalsymstream.ddns.net"
URL_UPDATE_CERT="http://" + server + "/symportal/updatecert/"
URL_AUTHENTICATE="http://" + server + "/symportal/authenticate"

CERT_FETCH_SUCCESS_MSG = "Successfully fetched certificate from modem #"
CERT_FETCH_FAILURE_MSG = "Failed to fetch certificate or connect to the target.\
\n\n1) Check if the modem is connected properly to your machine.\
\n\n2) Have you selected the right ethernet configuration?"
CERT_UPDATE_SUCCESS_MSG = "Successfully updated certificate in the Database."
CERT_UPDATE_FAILURE_MSG = "Failed to update certificate in the Database."
CERT_INVALID_MSG = "Invalid format of Certificate."
CERT_UPDATE_IN_PROGESS = "Updating Certificate in the Database..."
CERT_START = "-----BEGIN CERTIFICATE-----"
CERT_END = "-----END CERTIFICATE-----"
FAILURE_MSG_FROM_FETCH = "Failed to connect to target!"
GENERAL_ERROR_MSG = "Something went wrong. Please try again."
