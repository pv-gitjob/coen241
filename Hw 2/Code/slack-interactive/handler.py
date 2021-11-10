import json
import urllib

def handle(req):
    # Get the input value
    urlstring = urllib.unquote(req).decode('utf8').strip('payload=')
    # Convert the JSON object input into a Python Dictionary
    response = json.loads(urlstring)
    # Different values can be returned based on the response value
    # Declare the output value
    data = {
        "attachments": [
            {
                "replace_original": True,
                "response_type": "ephemeral",
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                "pretext": "Ahh yeah! Great choice, COEN 241 is absolutely amazing!",
                "author_name": "Praveen Vandeyar",
                "author_link": "https://github.com/pv-gitjob",
                "author_icon": "https://avatars.githubusercontent.com/u/58917968?v=4",
                "title": "COEN 241",
                "title_link": "https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "text": "Head over to COEN 241",
                "image_url": "https://www.scu.edu/media/offices/umc/scu-brand-guidelines/visual-identity-amp-photography/visual-identity-toolkit/logos-amp-seals/Mission-Dont3.png",
                "thumb_url": "https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "footer": "Slack Apps built on OpenFaas",
                "footer_icon": "https://a.slack-edge.com/45901/marketing/img/_rebrand/meta/slack_hash_256.png",
                "ts": 123456789
            }
        ]
    }
    # Return the output value to the requester as a JSON object
    return json.dumps(data)
