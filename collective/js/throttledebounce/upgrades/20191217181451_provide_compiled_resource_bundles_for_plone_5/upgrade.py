from ftw.upgrade import UpgradeStep
from Products.CMFPlone.utils import getFSVersionTuple


IS_PLONE_5 = getFSVersionTuple() > (5, )


class ProvideCompiledResourceBundlesForPlone5(UpgradeStep):
    """Provide compiled resource bundles for Plone 5.
    """

    def __call__(self):
        if IS_PLONE_5:
            self.install_upgrade_profile()
