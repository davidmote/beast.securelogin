import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from beast.securelogin.testing import\
    BEAST_SECURELOGIN_INTEGRATION_TESTING

#                        site_properties context/portal_properties/site_properties;

class TestInstalled(unittest.TestCase):

    layer = BEAST_SECURELOGIN_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.resource_path = "++theme++beast.securelogin"

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'beast.securelogin'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_css_registry_configured(self):
        cssRegistry = getToolByName(self.portal, 'portal_css')
        css_files = ['login.css',
                    ]
        for file in css_files:
            self.assertTrue("%s/%s" % (self.resource_path, file)
                        in cssRegistry.getResourceIds()
                    )

    def test_properties_configured(self):
        propertiesTool = getToolByName(self.portal, 'portal_properties')
        siteProperties = propertiesTool['site_properties']

        self.assertTrue(hasattr(siteProperties, 'external_login_iframe'), 
            'external_login_iframe not in site properties')

        self.assertTrue(siteProperties.external_login_iframe, 
            'external_login_iframe not set to True')

        self.assertTrue(hasattr(siteProperties, 'external_login_https'),
             'external_login_https not in site properties')

        self.assertTrue(siteProperties.external_login_https, 
            'external_login_https not set to True')

    # def test_skins_configured(self):
        
