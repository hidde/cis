# CIS API

The CIS API is a REST interface returning JSON documents. It provides visibility into user data to consumers.
There is a specific intent to make endpoints similar to [OpenID Connect](http://openid.net/developers/specs/) or identical 
where possible. It is possible that names differ for compatibility.
Endpoints utilize [OAuth2](http://openid.net/developers/specs/) for access authorization.

## Use cases for the CIS API

## Implementation

- The endpoints only support HTTPS.
- The endpoints require OAuth authorization.
- The authorizations are controlled by short-lived access-tokens that are generated by Auth0's API feature (until Mozilla 
IAM supports this natively)

**TODO**

## Typical endpoint query

1. Service owner (person) manually request a `client_id` and `client_secret` that can request access tokens.
2. Service utilizes `client_id` and `client_secret` in order to request a time-limited access token from the access 
provider, including which scopes it desires. The token is renewed as needed by the service.
3. The access provider authenticate the service, and verifies that it is allowed to access these scopes. 
This access control is currently set in Auth0 (the access provider) directly.
3. Service queries the CIS API endpoint by providing the access token in the headers, as such:
   ```
   GET /userinfo HTTP/1.1
   Host: server.example.com
   Authorization: Bearer AkdsWz...
   ```
4. The CIS API verifies the access token is valid with the access provider, and if valid, returns the JSON-formatted data
from the endpoint.

## `/userinfo` 'Profile' endpoint

This endpoint is also more tightly [defined by OIDC](http://openid.net/specs/openid-connect-core-1_0.html#UserInfo).
This endpoint does **NOT** follow the OIDC specifications to the letter as it is not part of an OIDC flow, however, it is 
as close as possible to the original specifications so that it can be easily ported and utilized as a real OIDC endpoint 
in the future.

### Key features

- The endpoint OAuth validation is performed by Auth0 API feature (until Mozilla IAM supports this natively).
- The endpoint provides the [CIS User profile](Profiles.md).
- All endpoints are currently **read-only**.

### Key use-cases
- I want to be able to query full profile information so that my RP has up to date user information, without having the 
user logging in. I need to be able to perform search queries.
- I want to be able to query, from the API: director name, manager name, developer name, developer bugmail for all user profiles, where directory name is one from a list of directors.
The resulting data is used to run bugzilla queries on needinfos and review requests.
- I want to create an org chart from querying the API, similar to phonebook's org chart.

### Supported Scopes

- The endpoint require the `profile` scope in the OAuth request.
- The endpoint requires additional scopes to specific part of the profile:
  - `profile:staff_confidential` for profile data that is limited to staff and NDA (see 
  [Mozilla Data Classification](https://wiki.mozilla.org/Security/Data_Classification)).
  - `profile:workgroup_confidential` for profile data that is limited to certain groups only, such as employment data.
  - `profile:individual_confidential` for profile data that the user who's profile it is has decided that this data may 
  not be available without it's consent. This is not currently used.

### JSON structure

The structure returned by the `/userinfo` endpoint is the [CIS User profile](Profiles.md).
The profile may be truncated depending on the scopes that are requested.
