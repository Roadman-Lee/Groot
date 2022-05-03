from tabom.models import Like


def do_like(user_id: int, artist_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=artist_id)
