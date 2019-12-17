from ftw.upgrade import UpgradeStep
from Products.CMFPlone.utils import getFSVersionTuple


IS_PLONE_4 = getFSVersionTuple() < (5, )


class MoveJsToResourceFolderForPlone4(UpgradeStep):
    """Move js to resource folder for Plone 4.
    """

    def __call__(self):
        if IS_PLONE_4:
            self.install_upgrade_profile()
