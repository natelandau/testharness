# Development

Valentina Noir is a REST API for building World of Darkness tabletop gaming applications. This guide covers the essential concepts for integrating with the API.

## Getting Started

1. [Create an account](https://valentina.dev/signup)
2. [Generate API credentials](https://valentina.dev/settings/api)
3. Authenticate your application using your API key
4. Start making requests

## Quick Reference

### Making Requests

All requests require the `X-API-KEY` header:

```shell
GET /api/v1/companies HTTP/1.1
Host: api.valentina-noir.com
X-API-KEY: your-api-key-here
```

For `POST`, `PUT`, and `PATCH` requests, include an `Idempotency-Key` header to enable safe retries:

```shell
POST /api/v1/companies/{company_id}/users HTTP/1.1
Host: api.valentina-noir.com
X-API-KEY: your-api-key-here
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json
```

## Documentation Topics

| Topic                                  | Description                                            |
| -------------------------------------- | ------------------------------------------------------ |
| [Companies](companies.md)              | Understanding the company model and data isolation     |
| [Authentication](authentication.md)    | API key usage, developer permissions, and security     |
| [User Authorization](authorization.md) | User roles and your responsibility for user management |
| [Error Handling](errors.md)            | RFC 9457 Problem Details error format                  |
| [Pagination](pagination.md)            | Offset-based pagination for list endpoints             |
| [Rate Limiting](rate-limiting.md)      | Token bucket algorithm and retry strategies            |
| [Idempotency](idempotency.md)          | Safe request retries with idempotency keys             |

## Base URL

All API endpoints use the following base URL:

```
https://api.valentina-noir.com/api/v1
```

## Response Format

All responses are returned as JSON. Successful responses return the requested data directly. Error responses follow the [RFC 9457 Problem Details](errors.md) format.

## Need Help?

-   Review the API documentation for endpoint-specific details
-   Check the [Error Handling](errors.md) guide for troubleshooting
-   Contact support for additional assistance
