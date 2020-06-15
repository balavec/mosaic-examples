from sixfeetup.utils import helpers as sfutils


def importVariousInitial(context):
    """Run the setup handlers for the initial profile"""
    if context.readDataFile('pwc_policy-initial.txt') is None:
        return
    members = [
        {'id': 'staff',
         'password': '$staff_password',
         'roles': ['Manager', 'Member'],
         'properties': {
             'email': 'changeme@example.com',
             'fullname': 'pwc Staff',
             'username': 'staff'
         }
        }
    ]
    sfutils.addUserAccounts(members)


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('pwc_policy-default.txt') is None:
        return
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'pwc.policy:default')
    
