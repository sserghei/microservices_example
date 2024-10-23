require 'sinatra'
require 'net/http'

set :port, 5000
set :bind, '0.0.0.0'

get '/auth/:user_id' do
  user_id = params['user_id']
  uri = URI("http://user_service:5001/user/#{user_id}")
  res = Net::HTTP.get(uri)

  user_data = JSON.parse(res)
  
  if user_data["username"]
    "User authenticated: #{user_data['username']}"
  else
    "Authentication failed"
  end
end