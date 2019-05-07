# bigbattle


API to post information about Daily bigbang status.

EndPoint: http:///api/v1/postmeta

payload (Example)

{ "Developer_Issues" : 3, "Issues_Resolved": 5, "Issues_Pending" : 1, "Component_Issues": 2, "Component_Failures": ["Util","Ndb-Client", "FOO","BAR"], "Jiras": ["ENG-1000", "ENG-1101010"], "Total_Tickets" : 5, "Faq_Updated" : 0 }
