from django.db import migrations


def add_ids(apps, schema_editor):
    """
    Adds back user ids that were removed in a previous erroneous migration.
    This will not cover all users; just the ones that we had matches for in the
    database.
    """
    User = apps.get_model("fuauth", "User")
    i = 1
    for user in User.objects.order_by("date_joined"):
        if i in (3, 105, 116):
            i += 1
        user.id = i
        user.save()
        i += 1


class Migration(migrations.Migration):

    dependencies = [("fuauth", "0022_user_id")]

    operations = [migrations.RunPython(add_ids)]
