json_criterion = (
    "id",
    "province",
    "property",
    "city",
    "district",
    "maximumPrice",
    "minimumPrice",
    "bedroom",
    "bathroom",
    "additionalFilters",
    "dwelling",
    "equipment",
    "allowPet",
    "otherPreferences"
)
core_api_response_headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU2NyYXBwZXIiLCJuYmYiOjE1NDE2NjcwNTgsImV4cCI6MTU3MzIwMzA1OCwiaWF0IjoxNTQxNjY3MDU4fQ.n7EUS311Mg85WAOW1v4gkQPBBVePMJmsjSPFKMhQOW1TngpuBvo1YKscZ_tbu1JYpF0ru0ABeiR1HzbtTo6oTg'
}
core_api_url = "http://35.204.84.172:5000/api/v1/searchResults"