from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class BeastSecurelogin(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import beast.securelogin
        xmlconfig.file('configure.zcml',
                       beast.securelogin,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'beast.securelogin:default')

BEAST_SECURELOGIN_FIXTURE = BeastSecurelogin()
BEAST_SECURELOGIN_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(BEAST_SECURELOGIN_FIXTURE, ),
                       name="BeastSecurelogin:Integration")