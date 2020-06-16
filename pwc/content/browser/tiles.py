from plone import api
from plone.app.standardtiles import _PMF as _
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.supermodel.model import Schema
from plone.tiles import Tile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.component import getUtility
from zope.schema.vocabulary import SimpleVocabulary


class IStyledText(Schema):
    title = schema.TextLine(
        title=_(u"Text Block Title"),
        required=True,
    )
    body = RichText(
        title=_(u"Text Block body"),
        description=_(u"Text to appear within the block"),
        required=True,
    )
    image = schema.Choice(
        title=_(u"Select image to be used as the title background"),
        required=False,
        vocabulary='plone.app.vocabularies.Catalog',
    )
    form.widget(
        'image',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            'recentlyUsed': True,
            'selectableTypes': ['Image'],
        }
    )
    bgcolor = schema.Choice(
        title=_(u"Background Color"),
        required=False,
        vocabulary=SimpleVocabulary.fromItems([
            ("White", "white"),
            ("Blue", "blue"),
            ("Red", "red"),
            ("Purple", "purple"),
        ]),
    )


class StyledText(Tile):
    template = ViewPageTemplateFile('templates/styledtext.pt')

    def __call__(self):
        self.update()
        return self.template()

    def update(self):
        self.title = self.data.get('title', '')
        self.body = self.data.get('body', '')
        self.tile_id = getUtility(IIDNormalizer).normalize(self.title)
        self.bgcolor = self.data.get('bgcolor', '')
        img_uid = self.data.get('image', None)
        if img_uid is None:
            self.image_url = None
        else:
            self.image_url = api.content.get(UID=img_uid).absolute_url()
