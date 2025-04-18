1. Follow User

    POST /api/follow/<user_id>/

    Auth: Required

    Response:

{
  "message": "You are now following johndoe."
}

2. Unfollow User

    POST /api/unfollow/<user_id>/

    Auth: Required

    Response:

{
  "message": "You have unfollowed johndoe."
}

3. User Feed

    GET /api/feed/

    Auth: Required

    Response:

[
  {
    "id": 2,
    "author": "johndoe",
    "title": "My Second Post",
    "content": "More updates.",
    "created_at": "2025-04-10T15:00:00Z",
    ...
  }
]

🧾 Model Changes

CustomUser now includes:

following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

