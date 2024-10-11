from .. import base

class Issue69Test(base.TestCase):
    def setUp(self):
        self.table = self.models.Table.objects.create()
        self.owner = self.models.Owner.objects.create()

        self.models.OwnerAsset.objects.create(owner=self.owner, asset=self.table)

    def test_table_get_queryset(self):
        # just check that no exception is raised when calling migrate
        list(self.table.owners.all())
