# --
# File: zendesk/zendesk_consts.py
#
# Copyright (c) Phantom Cyber Corporation, 2016
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

MXTOOLBOX_BASE_URL = "https://mxtoolbox.com/api/v1/"
MXTOOLBOX_BASE_ENDPOINT_URL = "lookup/{type}/{domain}"

MXTOOLBOX_ERR_API_UNSUPPORTED_METHOD = "Unsupported method"
MXTOOLBOX_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
MXTOOLBOX_ERR_FROM_SERVER = "API failed, Status code: {status}, Detail: {detail}"
MXTOOLBOX_ERR_JSON_PARSE = "Unable to parse reply as a Json from URL {url}. raw string reply: '{raw_text}'"
MXTOOLBOX_ERR_SERVER_CONNECTION = "Connection failed"
MXTOOLBOX_ERR_INVALID_TYPE = "Invalid type for lookup."
MXTOOLBOX_JSON_RESP_KEY = "Information"
MXTOOLBOX_JSON_API_TOKEN = "api_token"
MXTOOLBOX_JSON_COMMAND = "type"
MXTOOLBOX_JSON_DOMAIN = "domain"
MXTOOLBOX_JSON_IP = "ip"
MXTOOLBOX_JSON_PER_PAGE = "max_results_per_page"
MXTOOLBOX_JSON_PAGE = "page_number"
MXTOOLBOX_JSON_PORT = "port"

MXTOOLBOX_MSG_GET_INCIDENT_TEST = "Querying google.com. . ."

MXTOOLBOX_SUCC_LOOKUP = "Successfully received {type} of {domain}."
MXTOOLBOX_SUCC_CONNECTIVITY_TEST = "Successfully queried google.com and received a JSON reply."

MXTOOLBOX_TEST_CONNECTION_ENDPOINT = "lookup/dns/google.com"
MXTOOLBOX_TEST_FAILURE = "Invalid API key."

MXTOOLBOX_USING_BASE_URL = "Using url: {base_url}"
MXTOOLBOX_USING_PORT = "?port={port}"