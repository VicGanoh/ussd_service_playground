from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from cachetools import Cache
import logging


# maxsize is the size of data the Cache can hold
cache_data = Cache(maxsize=50000)

logger = logging.getLogger(__name__)

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    return Response(
        data={"message": "Hello, World!"},
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def handle_ussd(request):

    ussd_request: dict = request.data
    print("Ussd Request ", ussd_request)

    ussd_response: dict = {
        "sessionID": ussd_request.get("sessionID"),
        "userID": ussd_request.get("userID"),
        "msisdn": ussd_request.get("msisdn")
    }

    session_id = ussd_request.get("sessionID")

    print("Received USSD request with sessionID:", session_id)

    user_response_tracker = cache_data.get(session_id, [])

    print("User response tracker (before update):", user_response_tracker)

    if ussd_request.get("newSession") and ussd_request.get("userData") == "*928*93＃":
        message = (
            "Welcome to THE Poll Portal. Please select one of the following options"
            +"\n1. View Poll Options"
            +"\n2. Vote"
            +"\n3. Poll Result"
        )
        ussd_response["message"] = message

        ussd_response["continueSession"] = True

        # Keep track of the USSD state of the user and their session

        current_state: dict = {
            "sessionID": ussd_request.get("sessionID"),
            "msisdn": ussd_request.get("msisdn"),
            "userData": ussd_request.get("userData"),
            "network": ussd_request.get("network"),
            "message": ussd_response.get("message"),
            "level": 1,
            "part": 1,
            "newSession": True,
        }

        user_response_tracker.append(current_state)

        cache_data[session_id] = user_response_tracker

        print("Stored initial state in cache:", current_state)
    else:
        last_response = user_response_tracker[-1] if user_response_tracker else {}

        print("Last response from cache:", last_response)

        if last_response.get("level") == 1:
            user_data = ussd_request.get("userData")

            if user_data == "1":
                message = (
                    "Poll Options"
                    +"\n1. Victor Ganoh"
                    +"\n2. James Ofori"
                    +"\n3. Nana Agyemang"
                    +"\n*. Back"
                )
                ussd_response["message"] = message
                ussd_response["continueSession"] = True

                # Keep track of the USSD state of the user and their session
                current_state = {
                    "sessionID": ussd_request.get("sessionID"),
                    "msisdn": ussd_request.get("msisdn"),
                    "userData": ussd_request.get("userData"),
                    "network": ussd_request.get("network"),
                    "message": ussd_response.get("message"),
                    "level": 1,
                    "part": 2,
                    "newSession": ussd_request.get("sessionID"),
                }

                user_response_tracker.append(current_state)

                cache_data[session_id] = user_response_tracker
            if last_response.get("part") == 2:
                user_data = ussd_request.get("userData")
                if user_data == "*":
                    ussd_response["message"] = (
                        "Please select one of the following options"
                        + "\n1. View Poll Options"
                        + "\n2. Vote"
                        + "\n3. Poll Result"
                    )
                    ussd_response["continueSession"] = True

                    # Keep track of the USSD state of the user and their session
                    current_state = {
                        "session_id": ussd_request.get("sessionID"),
                        "msisdn": ussd_request.get("msisdn"),
                        "userData": ussd_request.get("userData"),
                        "network": ussd_request.get("network"),
                        "message": ussd_response.get("message"),
                        "level": 1,
                        "part": 1,
                        "newSession": ussd_request.get("sessionID"),
                    }

                    user_response_tracker.append(current_state)
                    cache_data[session_id] = user_response_tracker

                    print("Updated state to level 1:", current_state)  # Debugging        
            elif user_data == "2":
                ussd_response["message"] = (
                    "Select your candidate"
                    +"\n1. Victor Ganoh"
                    +"\n2. James Ofori"
                    +"\n3. Nana Agyemang"
                )

                ussd_response["continueSession"] = True

                # Keep track of the USSD state of the user and their session
                current_state = {
                    "sessionID": ussd_request.get("sessionID"),
                    "msisdn": ussd_request.get("msisdn"),
                    "userData": ussd_request.get("userData"),
                    "network": ussd_request.get("network"),
                    "message": ussd_response.get("message"),
                    "level": 2, # voting level
                    "part": 1,
                    "newSession": ussd_request.get("sessionID"),
                }
                
                user_response_tracker.append(current_state)
                cache_data[session_id] = user_response_tracker

                print("Updated state to level 2:", current_state)  # Debugging
            elif user_data == "3":
                ussd_response["message"] = (
                    "Poll Result"
                    + "\n1. Victor Ganoh - 20 votes"
                    + "\n2. James Ofori - 15 votes"
                    + "\n3. Nana Agyemang - 10 votes"
                )
                ussd_response["continueSession"] = False
            else:
                ussd_response["message"] = "Invalid input."
                ussd_response["continueSession"] = False
        elif last_response.get("level") == 2:
            user_data = ussd_request.get("userData")
            print("=====================================")
            print("user_data: ", user_data)
            if user_data in ["1", "2", "3"] and last_response.get("part") == 1:
                ussd_response["message"] = "Thank you for voting."
                ussd_response["continueSession"] = False
            else:
                ussd_response["message"] = "Invalid input."
                ussd_response["continueSession"] = False

    return Response(ussd_response)
   