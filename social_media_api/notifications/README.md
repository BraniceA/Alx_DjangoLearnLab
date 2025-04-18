POST /posts/<id>/like/

    Like a post

    Request: Empty

    Response:

{ "detail": "Post liked" }

POST /posts/<id>/unlike/

    Unlike a post

    Response:

{ "detail": "Post unliked" }

📘 Notifications API
GET /notifications/

    List notifications for the authenticated user.

    Response:

[
  {
    "id": 1,
    "actor_username": "john_doe",
    "verb": "liked your post",
    "timestamp": "2025-04-10T18:32:21Z",
    "read": false
  }
]