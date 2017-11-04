"""import json
import unirest

response = unirest.post("https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/vtupage", headers={ "Accept": "application/json" },
  params=json.dumps({
    "courseId": "ahJzfnVwbG9hZG5vdGVzLTIwMTZyEwsSBkNvdXJzZRiAgIDAxteOCQw"
  })
)

print response.body"""

import requests
import json
r = requests.post('https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/vtupage', json={"courseId": "ahJzfnVwbG9hZG5vdGVzLTIwMTZyEwsSBkNvdXJzZRiAgIDAxteOCQw"})

print(r.status_code)