import imapy
from imapy.query_builder import Q

box = imapy.connect(
    host='server',
    username=input('Username: '),
    password=input('Password: '),
    ssl=True)

folders = box.folders()

def get_attachments():
    # select unseen mail
    q = Q()
    emails = box.folder('INBOX').emails(q.unseen())

    # get attachment from newest
    if len(emails):
        email = emails[-1]
        for attachment in email['attachments']:
            data = attachment['data']

            # Mark as seen
            email.mark('seen')
            return data


get_attachments()

# logout
box.logout()