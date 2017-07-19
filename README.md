MusiCon for MAS 8803


APIs

1. User Create API

  HTTP POST,data needs to be sent as form-data
  endpoint - http://localhost:port/v1/user/create
  compulsory fields = username,email,first_name,last_name
  optional = phone



2.  User fetch
  
  endpoint - http://localhost:port/v1/user/get/ < username >

  HTTP GET,
  Sample APIs
  http://localhost:port/v1/user/get/sbhati3


  
3.  User State update(Currently only has PAM updates)
  
  endpoint - http://localhost:port/v1/user/update_state
  HTTP POST,data needs to be sent as form-data
  sample fields and data =>
  username:bverma
  feature_id:5
  feature:"mood_feature"


4.  Fetch Recommendation API

  endpoint - http://localhost:port/v1/user/fetch_rec/username where username can be anything say bverma
  HTTP POST, data needs to be sent as form-data
  Compulsory Arguments - 
  lat - latitude 
  lon - longitude
  
  Additional Arguments(activity recognition) - 
  bmp - integer that has the BMP of the user. If not available, donot send this field
