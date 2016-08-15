import json
import sys
import datetime
import platform as _platform

try:
    import httplib as http_client
except ImportError:
    import http.client as http_client


def submit(successes_list, failures_list, HOST):
    """
    This function sends the details of failures and successes to server.
    """

    endpoint = "/installation_data/"

    try:
        with open('.swc_submission_id', 'r') as f:
            first_line = f.readline()
            unique_id = first_line.split("[key:]")[1]
            date = first_line.split("[key:]")[0]
            if date != str(datetime.date.today()):
                unique_id = None
    except:
        unique_id = None

    successful_installs = []
    failed_installs = failures_list
    for checker, version in successes_list:
        successful_installs.append(
            {
                "name": checker.full_name(),
                "version": version
            }
        )

    user_system_info = {
        "distribution_name": _platform.linux_distribution()[0],
        "distribution_version": _platform.linux_distribution()[1],
        "system": _platform.system(),
        "system_version": _platform.version(),
        "machine": _platform.machine(),
        "system_platform": _platform.platform(),
        "python_version": _platform.python_version()
    }

    headers = {"Content-Type": "application/json"}
    data = {
        "successful_installs": successful_installs,
        "failed_installs": failed_installs,
        "user_system_info": user_system_info,
        "unique_user_id": unique_id
    }

    def senddata():
        final_data = json.dumps(data)
        conn = http_client.HTTPConnection(HOST)
        print("\nPushing the data to server....\n")
        try:
            conn.request("POST", endpoint, final_data, headers=headers)
            response = conn.getresponse()
            response_string = response.read()
            if response.status == 200:
                print("\nSuccessfully Pushed to Server!")
                response = json.loads(response_string.decode('utf-8'))
                unique_id = response.get("key")
                file = open('.swc_submission_id', 'w+')
                file.write(str(datetime.date.today()) + "[key:]" + unique_id)
            else:
                print("\nSomething bad happened at Server!")
        except:
            print("\nConnection could not be established with server!")
        conn.close()

    global input
    try:
        input = raw_input  # making it compatible for Python 3.x and 2.x
    except NameError:
        pass
    choice = input("\nTo improve our lessons, we gather anonymous data about failed package installations."
                    "  Can we send anonymous list of your packages? (y/N): ")
    if choice == 'y' or choice == 'Y':
        workshop_id = input("Please enter your workshop name (similar to '2016-08-13-place', ask your instructor for details) (none by default): ")
        if not workshop_id:
            workshop_id = "No workshop name provided"
        email = input("What is your email address (none by default): ")
        if not email:
            email = None
        data['user_system_info']['email_id'] = email
        data['user_system_info']['workshop_id'] = workshop_id
        senddata()
    else:
        sys.exit(0)
