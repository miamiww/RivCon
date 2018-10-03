"""
Shows basic usage of the Slides API. Prints the number of slides and elments in
a presentation.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import random
# Setup the Slides API
SCOPES = 'https://www.googleapis.com/auth/presentations'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('slides', 'v1', http=creds.authorize(Http()))

# Call the Slides API
PRESENTATION_ID = '1kNgshD1_dMxGEdN-V_sakNEKJaJhbVbWjqwRc7EROIc'
presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
slides = presentation.get('slides')
title_id = slides[0].get('pageElements')[0]['objectId']
subtitle_id = slides[0].get('pageElements')[1]['objectId']
print(slides[1].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId'])
# ['speakerNotesObjectId']
print(title_id)
print(subtitle_id)

def change_title():
    requests = [
        {
            "insertText": {
                "objectId": title_id,
                "text": "Good Talk",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
# change_title()

notes_id = slides[1].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId']

def notes_update(the_slides, iteration):
    notes_id = the_slides[i].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId']
    requests = [
        {
            "insertText": {
                "objectId": notes_id,
                "text": "hi"}
        }
     ]

    body = {
            'requests': requests
    }
    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

slides = presentation.get('slides')
# for i in range(len(slides)):
#     notes_update(slides, i)


def last_slide(slide_ID):
    requests = [
        {
            'createSlide': {
                'objectId': slide_ID,
                'insertionIndex': '12',
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


unique_id = random.randint(1000,10000000000000000000000)
unique_id = str(unique_id)
deck_populate(unique_id,0)
presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
slides = presentation.get('slides')
last_title_id = slides[12].get('pageElements')[0]['objectId']
last_subtitle_id = slides[12].get('pageElements')[1]['objectId']
last_details_id = slides[12].get('pageElements')[2]['objectId']
# final_slide_text(unique_id)


def change_final():
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
                "text": "Twitter: @miamiworldwide\nGithub: miamiww\nwww.alden.website",
                "insertionIndex": 0
            }
        }
     ]
    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()


change_final()

print ('The presentation contains {} slides:'.format(len(slides)))
# for i, slide in enumerate(slides):
#     print('- Slide #{} contains {} elements.'.format(i + 1,
#                                                      len(slide.get('pageElements'))))
#
# requests = [
#     {
#         'createSlide': {
#             'objectId': '3424234234230904317031275981435-4841-',
#             'insertionIndex': '1'
#         }
#     }
# ]
#
# body = {
#     'requests': requests
# }
#
# response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
#                                                       body=body).execute()
# create_slide_response = response.get('replies')[0].get('createSlide')
# print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))
#
# requests = [
#     {
#         "updatePageProperties": {
#             "objectId": '3424234234230904317031275981435-4841-',
#             "pageProperties": {
#                 "pageBackgroundFill": {
#                     "stretchedPictureFill": {
#                     "contentUrl": 'https://image.slidesharecdn.com/webinarhowtoscaleadreamsalesteam-160210174334/95/webinar-how-to-scale-a-dream-sales-team-4-1024.jpg?cb=1455214873'
#                     }
#                 }
#             },
#             "fields": "pageBackgroundFill"
#         }
#     }
# ]
#
# body = {
#     'requests': requests
# }
#
#
# response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
#                                                       body=body).execute()
