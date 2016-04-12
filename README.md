MusiCon for MAS 8803


APIs

1. User Create API

  HTTP POST,data needs to be sent as form-data
  endpoint - http://52.37.58.111/v1/user/create
  compulsory fields = username,email,first_name,last_name
  optional = phone



2.  User fetch
  
  endpoint - http://52.37.58.111/v1/user/get/ < username >

  HTTP GET,
  Sample APIs
  http://52.37.58.111/v1/user/get/sbhati3


  
3.  User State update(Currently only has PAM updates)
  
  endpoint - http://52.37.58.111/v1/user/update_state
  HTTP POST,data needs to be sent as form-data
  sample fields and data =>
  username:bverma
  feature_id:5
  feature:"mood_feature"
