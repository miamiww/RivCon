## import google api modules
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

def api_setup(PRESENTATION_ID):
    ## Setup the Slides API
    SCOPES = 'https://www.googleapis.com/auth/presentations'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('slides', 'v1', http=creds.authorize(Http()))
    return service
    # login to google slides and call the Slides API
    # PRESENTATION_ID = project_id

#functions for calling on the api
def deck_populate(slide_ID, iteration,PRESENTATION_ID,service,slide_urls):
    requests = [
        {
            'createSlide': {
                'objectId': slide_ID,
                'insertionIndex': '1'
            }
        }
    ]

    body = {
        'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
    create_slide_response = response.get('replies')[0].get('createSlide')
    print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))

    requests = [
        {
            "updatePageProperties": {
                "objectId": slide_ID,
                "pageProperties": {
                    "pageBackgroundFill": {
                        "stretchedPictureFill": {
                        "contentUrl": slide_urls[len(slide_urls)-1-iteration]
                        }
                    }
                },
                "fields": "pageBackgroundFill"
            }
        }
    ]

    body = {
        'requests': requests
    }


    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

def change_title(PRESENTATION_ID,service):
    presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
    slides = presentation.get('slides')
    title_id = slides[0].get('pageElements')[0]['objectId']
    subtitle_id = slides[0].get('pageElements')[1]['objectId']

    requests = [
        {
            "insertText": {
                "objectId": title_id,
                "text": "WELCOME TO",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

    time.sleep(4)
    requests = [
        {
            "insertText": {
                "objectId": subtitle_id,
                "text": "GOOD CONFERENCE TALK",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

def notes_update(the_slides, iteration,PRESENTATION_ID,service,speaker_notes):
    notes_id = the_slides[iteration].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId']
    print(notes_id)
    requests = [
        {
            "insertText": {
                "objectId": notes_id,
                "text": speaker_notes[iteration-1]}
        }
     ]

    body = {
            'requests': requests
    }
    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

def last_slide(slide_ID,PRESENTATION_ID,service,n_slides):
    numslides = str(n_slides+1)
    requests = [
        {
            'createSlide': {
                'objectId': slide_ID,
                'insertionIndex': numslides,
                "slideLayoutReference": {
                    "predefinedLayout": "SECTION_TITLE_AND_DESCRIPTION"
        }
            }
        }
    ]

    body = {
        'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
    create_slide_response = response.get('replies')[0].get('createSlide')
    print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))



def change_final_slide(PRESENTATION_ID,service,n_slides):
    presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
    slides = presentation.get('slides')
    last_title_id = slides[n_slides+1].get('pageElements')[0]['objectId']
    last_subtitle_id = slides[n_slides+1].get('pageElements')[1]['objectId']
    last_details_id = slides[n_slides+1].get('pageElements')[2]['objectId']
    requests = [
        {
            "insertText": {
                "objectId": last_title_id,
                "text": "THANK YOU",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
    requests = [
        {
            "insertText": {
                "objectId": last_details_id,
                "text": "Twitter: @miamiworldwide\nGithub: miamiww\nEmail: rivendalejones@gmail.com\nwww.alden.website",
                "insertionIndex": 0
            }
        }
     ]
    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
