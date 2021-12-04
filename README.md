# TREX-Starter
This script will check if a trex.service is running, if it is not it will prompt the user if they are currently logged in otherwise it will auto start silently.

#Prerequisites:
* A TREX Service

#How to use:

You will want to change/check the session ID variable to match your current session ID, you can find this via the command: 

```loginctl```

Then run this script, either in its own service, or a background screen, etc.
